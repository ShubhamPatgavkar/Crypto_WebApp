from flask import Flask, render_template, request, send_file, jsonify
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import io, struct

app = Flask(__name__)

# ===== AES Helpers with Password =====
def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=1000000)  # AES-256


def encrypt_file(file_data, filename, password):
    salt = get_random_bytes(16)
    key = derive_key(password.encode(), salt)

    cipher = AES.new(key, AES.MODE_EAX)
    filename_bytes = filename.encode()
    packed_data = struct.pack("I", len(filename_bytes)) + filename_bytes + file_data

    ciphertext, tag = cipher.encrypt_and_digest(packed_data)

    encrypted_data = salt + cipher.nonce + tag + ciphertext
    return io.BytesIO(encrypted_data)


def decrypt_file(file_data, password):
    salt, nonce, tag, ciphertext = file_data[:16], file_data[16:32], file_data[32:48], file_data[48:]
    key = derive_key(password.encode(), salt)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_packed = cipher.decrypt_and_verify(ciphertext, tag)

    filename_len = struct.unpack("I", decrypted_packed[:4])[0]
    filename = decrypted_packed[4:4+filename_len].decode()
    file_content = decrypted_packed[4+filename_len:]

    return filename, file_content


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mode = request.form.get("mode")
        password = request.form.get("password")

        if not password:
            return jsonify({"error": "❌ Please provide a password."}), 400

        uploaded_file = request.files["file"]
        if not uploaded_file:
            return jsonify({"error": "❌ No file uploaded."}), 400

        if mode == "encrypt":
            filename = uploaded_file.filename
            file_data = uploaded_file.read()
            encrypted_file = encrypt_file(file_data, filename, password)

            return send_file(
                encrypted_file,
                as_attachment=True,
                download_name=f"{filename}.enc"
            )

        elif mode == "decrypt":
            file_data = uploaded_file.read()
            try:
                filename, decrypted_data = decrypt_file(file_data, password)
                return send_file(
                    io.BytesIO(decrypted_data),
                    as_attachment=True,
                    download_name=filename
                )
            except Exception:
                return jsonify({"error": "❌ Decryption failed. Wrong password or corrupted file."}), 400

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5050)
