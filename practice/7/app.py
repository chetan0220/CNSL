from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def hash_and_salt(plaintext, shift = 3, salt = "python"):
    hashed = "".join(chr((ord(char) + shift - 97) % 26) if char.isalpha() else char for char in plaintext.lower())
    salted = "".join(hashed[i:i+3] + salt if i%3 == 0 else hashed[i:i+3] for i in range(0, len(plaintext), 3))
    return salted

db = {
    "chetan": {
        "username": "chetan",
        "password": hash_and_salt("chetan")
    }
}

@app.route('/login', methods = ["POST"])
def login():
    username = request.form["username"]
    user = db.get(username)
    
    password = request.form["password"]
    cipher = hash_and_salt(password)

    if user and cipher == user["password"]:
        return f"Welcome {username}"
    return "invalid :("

if __name__ == "__main__":
    app.run(debug = True)