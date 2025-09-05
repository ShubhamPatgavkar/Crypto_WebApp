# 🔐 Crypto WebApp – AES & RSA Encryption/Decryption

This project is a **Flask-based web application** that allows users to encrypt and decrypt text using two popular cryptographic techniques:

- **AES (Advanced Encryption Standard)** – Symmetric key encryption for fast and secure bulk data protection.  
- **RSA (Rivest–Shamir–Adleman)** – Asymmetric key encryption using public/private key pairs for secure communication.

---

## 🚀 Features
- Encrypt and decrypt **custom text** using AES or RSA.
- Auto-generation and **persistent storage of keys**:
  - AES key is stored in `aes_key.bin`.
  - RSA private/public keys are stored in `rsa_private.pem` and `rsa_public.pem`.
- Interactive **web-based UI** built with Flask.
- Secure handling of cryptographic operations with PyCryptodome.

---

## 🖼️ Screenshots

### 🔑 Home Page
![Home Page](https://via.placeholder.com/800x400.png?text=Home+Page)

### 🔒 AES Encryption Example
![AES Encryption](https://via.placeholder.com/800x400.png?text=AES+Encryption)

### 🔓 AES Decryption Example
![AES Decryption](https://via.placeholder.com/800x400.png?text=AES+Decryption)

### 🔒 RSA Encryption Example
![RSA Encryption](https://via.placeholder.com/800x400.png?text=RSA+Encryption)

### 🔓 RSA Decryption Example
![RSA Decryption](https://via.placeholder.com/800x400.png?text=RSA+Decryption)

*(Replace the above placeholder links with actual screenshot URLs, e.g., hosted in your GitHub repo or Imgur.)*

---

## 📂 Project Structure
Crypto_WebApp/
│── app.py # Flask backend
│── templates/
│ └── index.html # Web UI template
│── aes_key.bin # Stored AES key
│── rsa_private.pem # Stored RSA private key
│── rsa_public.pem # Stored RSA public key
│── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Crypto_WebApp.git
   cd Crypto_WebApp
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install dependencies:

bash
Copy code
pip install flask pycryptodome
▶️ Running the App
Start the Flask server:

bash
Copy code
python app.py
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
🔐 How It Works
AES
A secret AES key is generated once and stored in aes_key.bin.

User text is padded, encrypted, and Base64-encoded.

On decryption, the ciphertext is decoded and restored using the stored AES key.

RSA
RSA private and public keys are generated once and stored in .pem files.

User text is encrypted using the public key.

Decryption uses the private key.

🛡️ Security Notes
Never share your private key (rsa_private.pem) or AES key file.

For production, consider storing keys securely (e.g., using a key vault).

This demo is for educational purposes.
