from flask import Flask, render_template

app = Flask(__name__)

# Criar a 1º pagina do site
# como criar a pagina -> Toda pagina tem:
# route -> qual link vai ficar a pagina, após o dominio fernandesadv.com/ , se tiver somente até a barra,
# será sua home page
#função ->  O que você quer exibir naquela página
#DECORATOR -> é uma linha de codigo que o objetivo é atribuir uma funcionalidade a função que vem logo abaixo dela

@app.route("/") #assim que se cria  a route do site
def homepage(): # isso é a função do site
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)




if __name__ == "__main__":
    app.run(debug=True) # isso é pra colocar o site no ar