from flask import Flask , request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def create_article():
        
    return """
    <center><form method ='POST' action = "/">
        <label for ='n1'> Número 1: </label>
        <input type = 'number' id = 'n1' name = 'n1'>
        <br><br>
        <label for ='n2'> Núumero 2: </label>
        <input type = 'number' id = 'n2' name = 'n2'>
        <br><br>
        <label for ='op'> Elige la operación: </label>
        <select>
        <option value="+">Sumar</option>
        <option value="-">Restar</option>
        <option value="*">Multiplicar</option>
        <option value="/">Dividir</option>
        </select>
        <br><br>
        <input type = 'submit' value = 'Crear articulo'>
    </form></center>
"""    

if __name__ == "__main__":
    app.run(debug=True)

