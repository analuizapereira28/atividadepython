from flask import Flask,render_template, request  # Importa a classe Flask do módulo Flask

app = Flask(__name__)  # Cria uma instância da aplicação Flask

@app.route('/')
def index():
    return render_template('index.html', resultado='')
@app.route('/verificar', methods=['POST'])
def verificar():
    mensagem = ''
    idade = int(request.form['idade'])
    if 0 <= idade <= 5:
        mensagem = 'resultado: bebê'

    elif 6 <= idade <= 15:
         mensagem = "Criança"

    elif 16 <= idade <= 18:
        mensagem = "Marmanjos, hora de trabalhar"

    elif 19 <= idade <= 60:
        mensagem ="Acorda pra vida, que você tem boleto pra pagar"

    else:
        mensagem= "Daqui pra frente é só pra trás"
    return render_template('index.html', resultado=mensagem)

if __name__ == '__main__':  # Verifica se este arquivo está sendo executado diretamente
       app.run(debug=True)  # Inicia o servidor de desenvolvimento do Flask com

