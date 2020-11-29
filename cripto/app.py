from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
fernet = Fernet(key)


@app.route('/encrypt')
def encrypt():
    result = "Encrypt result: "
    param = request.args.get('param') #получаем значение из адрессной строки
    string = (fernet.encrypt(param.encode())).decode() #кодируем значение и приводим в вид строки

    return render_template('index.html', string=string, result=result)
"""Эта функция отвечает за страницу кодировки, вводим после param=слово которое нам нужно закодировать и получаем результат, """

@app.route('/decrypt')
def decrypt():
    result = "Decrypt result: "
    param = request.args.get('param') #получаем значение из адрессной строки
    string = (fernet.decrypt(param.encode())).decode() #декодируем значение и приводим в вид строки

    return render_template('index.html', string=string, result=result)

"""Эта функция отвечает за страницу декодировки, после param= в адрессной строке вводим что нужно розшифровать и получаем результат"""

app.run(debug=True)