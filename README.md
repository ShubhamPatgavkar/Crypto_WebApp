🔐 Crypto Web – File Encryption & Decryption App

A simple yet powerful Flask-based web application that lets you encrypt and decrypt files securely using AES-256 encryption. Built with a clean UI using Material UI and SweetAlert for interactive feedback.

🚀 Features

✅ AES-256 Encryption (PBKDF2 + EAX Mode) – Industry standard security

✅ File Upload & Download – Supports any file type

✅ Password Protected – Your files are encrypted with your secret key

✅ Toggle Functionality – Switch between Encrypt 🔒 and Decrypt 🔓 modes

✅ Beautiful UI – Modern design with square card layout

✅ SweetAlert Integration – Instant feedback for success/error

✅ Lightweight & Fast – Runs locally with Flask

🏗️ Project Workflow

User Uploads File – Choose any file to encrypt or decrypt

Enter Password – Set password (for encryption) / Enter password (for decryption)

Encryption Flow

File + filename packed → Encrypted with AES-256 (PBKDF2 key derivation)

Output file: yourfile.enc

Decryption Flow

Encrypted file + password → Original file retrieved

Handles wrong password with SweetAlert error

Download Result – User downloads secure/encrypted/decrypted file

🖥️ Tech Stack

Backend: Flask

Encryption: PyCryptodome
 (AES, PBKDF2)

Frontend: HTML, CSS, Material UI

UI Enhancements: SweetAlert

📸 Screenshots

🔒 Encrypt Mode
<img src="static/encrypt.png" alt="Encrypt UI" width="800"/>

🔓 Decrypt Mode
<img src="static/decrypt.png" alt="Decrypt UI" width="800"/>

⚙️ Installation & Setup

Clone the repository:

git clone https://github.com/your-username/crypto_web.git
cd crypto_web


Create a virtual environment & install dependencies:

python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate
pip install -r requirements.txt


Run the Flask app:

python app.py


Open in your browser:

http://127.0.0.1:5050

📂 Project Structure
crypto_web/
│── app.py               # Flask backend with AES encryption/decryption logic
│── templates/
│    └── index.html      # Frontend UI (Material UI + SweetAlert)
│── static/
│    ├── encrypt.png     # Screenshot of Encrypt Mode
│    ├── decrypt.png     # Screenshot of Decrypt Mode
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation

🔮 Future Enhancements

📦 Multi-file & folder encryption (ZIP support)

☁️ Cloud integration (AWS S3 / Google Drive)

👥 User authentication & session management

📊 File activity logs & analytics

🙌 Author

👨‍💻 Shubham Patgavkar
