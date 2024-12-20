import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

# Character groups
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = string.punctuation

def generate_password(length):
    if length < 12:  # Enforce minimum length
        return "Password must be at least 12 characters long."
    
    # Ensure the password contains at least one character from each group
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with a mix of all character types
    remaining_length = length - 4
    all_characters = uppercase + lowercase + digits + special
    password += random.choices(all_characters, k=remaining_length)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

@app.route('/', methods=['GET'])
def index():
    return render_template('password.html')

@app.route('/password', methods=['POST'])
def password():
    try:
        length = int(request.form['length'])
        password = generate_password(length)
    except ValueError:
        password = "Invalid input. Please enter a valid number for password length."
    return render_template('password.html', password=password)

if __name__ == "__main__":
    app.run(debug=True)
