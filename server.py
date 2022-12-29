from flask import Flask, render_template, request

app = Flask(__name__)

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def convert_text(text_string):
    morse_code = []
    for char in text_string:
        for key, value in MORSE_CODE_DICT.items():
            if char == key:
                morse_code.append(value)
    final_code = ' '.join(morse_code)
    return final_code


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def results():
    user_input = str(request.form['user-string'])
    morse_code = convert_text(user_input.upper())
    return render_template('index.html', input=user_input, output=morse_code)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
