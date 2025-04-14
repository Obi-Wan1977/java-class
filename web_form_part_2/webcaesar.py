from flask import Flask, render_template, request
from encrypt import encrypt_with_shift

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/user_message', methods=['GET', 'POST'])
def user_message():
    user_msg = ''
    coded_msg = ''
    error = ''

    if request.method == 'POST':
        user_msg = request.form.get('message', '')
        shift = request.form.get('shift', '')
        action = request.form.get('action', '')

        try:
            shift = int(shift)

            # ✅ Validations
            if not user_msg or not any(c.isalpha() for c in user_msg):
                error = "Message must include at least one letter."
            elif shift < 1 or shift > 25:
                error = "Shift must be between 1 and 25."
            else:
                if action == 'Decrypt':
                    shift = -shift
                coded_msg = encrypt_with_shift(user_msg, shift)
        except ValueError:
            error = "Shift must be a number."

    return render_template(
        'user_message.html',
        user_message=user_msg,
        result_message=coded_msg,
        error_message=error
    )

if __name__ == '__main__':
    app.run()
