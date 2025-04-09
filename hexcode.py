from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

def valid_hex_chars(hex_code):
    # Check if the hex_code has exactly 6 characters
    if len(hex_code) != 6:
        return False
    
    # Loop through each character and check if it's valid (0-9, A-F, case insensitive)
    for char in hex_code:
        if not (char.isdigit() or char.lower() in 'abcdef'):
            return False
    return True

@app.route('/hex_form', methods=["GET", "POST"])
def hex_form():
    if request.method == 'POST':
        hex = request.form['hex']
        # Check if the hex code is valid
        if not valid_hex_chars(hex):
            feedback = "Invalid hex code. Please enter a valid 6-character hex code (0-9, A-F)."
        else:
            feedback = "Successful submission!"
    else:
        hex = 'FF0000'  # Default hex code
        feedback = ''

    return render_template('hex_form.html', hex=hex, feedback=feedback)

if __name__ == '__main__':
    app.run()

# Find the exercise instructions here:
# https://education.launchcode.org/lchs/chapters/flask-intro/exercises.html
