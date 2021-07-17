from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "why are you here"


@app.route('/convert=<string:word>')
def convert(word):
    output = ''.join(format(ord(i), '08b') for i in word)
    return output


if __name__ == '__main__':
    app.run()
