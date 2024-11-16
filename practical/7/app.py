from flask import Flask, render_template, request

app = Flask(__name__)

def hash_and_salt(password, shift=3, salt="python"):
    hashed = ''.join(chr((ord(char) + shift - 97) % 26 + 97) if char.isalpha() else char for char in password.lower())
    salted = ''.join(hashed[i:i+3]+salt if i%3 == 0 else hashed[i:i+3] for i in range(0, len(password), 3))
    return salted

db = {
    "chetan": {
        "username": "chetan",
        "password": hash_and_salt("chetan")
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    username = request.form["username"]
    user = db.get(username)

    password = request.form["password"]
    cipher = hash_and_salt(password)

    if user and cipher == user["password"]:
        return f"welcome {username}"
    return "invalid details"

if __name__=="__main__":
    app.run(debug=True)