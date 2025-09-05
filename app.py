from flask import Flask, render_template, request
import base64
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

app = Flask(__name__)

# ===== AES Helpers =====
def pad(message):
    return message + ' ' * (16 - len(message) % 16)

def aes_encrypt(plaintext):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(pad(plaintext).encode())
    # Store nonce, tag, and key with ciphertext for decryption
    package = cipher.nonce + tag + key + ciphertext
    return base64.b64encode(package).decode()

def aes_decrypt(encrypted_text):
    try:
        data = base64.b64decode(encrypted_text)
        nonce, tag, key, ciphertext = data[:16], data[16:32], data[32:48], data[48:]
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag).decode().rstrip()
        return plaintext
    except Exception as e:
        return f"❌ AES Decryption Failed: {str(e)}"


# ===== RSA Helpers =====
def rsa_generate_keys():
    key = RSA.generate(2048)
    return key, key.publickey()

rsa_key, rsa_public_key = rsa_generate_keys()

def rsa_encrypt(plaintext):
    cipher = PKCS1_OAEP.new(rsa_public_key)
    encrypted = cipher.encrypt(plaintext.encode())
    return base64.b64encode(encrypted).decode()

def rsa_decrypt(encrypted_text):
    try:
        encrypted_bytes = base64.b64decode(encrypted_text)
        cipher = PKCS1_OAEP.new(rsa_key)
        return cipher.decrypt(encrypted_bytes).decode()
    except Exception as e:
        return f"❌ RSA Decryption Failed: {str(e)}"


# ===== Routes =====
@app.route("/", methods=["GET", "POST"])
def index():
    result = {"encrypted": "", "decrypted": ""}
    
    if request.method == "POST":
        text = request.form.get("text")
        method = request.form.get("method")
        action = request.form.get("action")

        if action == "Encrypt":
            if method == "AES":
                result["encrypted"] = aes_encrypt(text)
            elif method == "RSA":
                result["encrypted"] = rsa_encrypt(text)

        elif action == "Decrypt":
            encrypted_text = request.form.get("encrypted_text")
            if method == "AES":
                result["decrypted"] = aes_decrypt(encrypted_text)
            elif method == "RSA":
                result["decrypted"] = rsa_decrypt(encrypted_text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5050)
