from flask import Flask #Importamos la libreria Flask

app = Flask(__name__) #Crear la aplicación Flask

@app.route('/') #Definir una ruta
def  home():
        
        #Creación de la estructura html de la calculadora
        #Su funcionamiento será hecho con javascript
    return """
    <center>

        <h1>Calculadora</h1>
        <label for ='n1'> Número 1: </label>
        <input type = 'number' id = 'n1' name = 'n1'>
        <br><br>
        <label for ='n2'> Núumero 2: </label>
        <input type = 'number' id = 'n2' name = 'n2'>
        <br><br>
        <label> Elige la operación: </label>
        <select id="op">
        <option value="+">Sumar</option>
        <option value="-">Restar</option>
        <option value="*">Multiplicar</option>
        <option value="/">Dividir</option>
        </select>
        <br><br>
        <button onclick="operar()">Realizar operación</button></center>

   
        <script>

        function operar(){
        
            const numero1 = document.getElementById('n1').value;
            const numero2 = document.getElementById('n2').value;

            const select = document.getElementById("op");
            const operacion = select.value;

            if (operacion=="+"){
            
                const suma=Number(numero1)+Number(numero2);
                alert(suma)

            }
            
        }

        </script>
    """    

if __name__ == "__main__":
    app.run(debug=True) #Iniciar el servidor

