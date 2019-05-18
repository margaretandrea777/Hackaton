from flask import Flask, render_template, request 
app=Flask(__name__)

@app.route("/")
def render_html():
    return render_template("bienvenida.html")

@app.route("/index")
def render1():
    return render_template("index.html")


@app.route("/registro", methods=['POST'])
def reg():
    return render_template("index.html")

@app.route('/registro1', methods=['POST','GET'])      # aca es para registrar al animal
def registro1():
    if request.method=='POST':   
        try:
            ci=request.form['ci']                             #identificativo del animal
            datos=[ci]  # esto es para meter en la db luego
            print(datos)
            with sql.connect(nombre_db) as con:        
                cur = con.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS usuario (
                                        ci integer ,
                                        nombre text,
                                        numeroT interger,                                        
                                        profesion text,
                                        ciudad text,
                                        celular interger,
                                        gastosd interger,
                                        ingd interger,
                                        fecha text,
                                        monto interger,
                                        tipo text,
                                    );'''
                       )
                cur.execute('''INSERT INTO usuario (ci) VALUES (?,);''', datos )
            
                con.commit()   
             
        except:
            con.rollback()

        finally:
            con.close()# cerramos la conexion de la base de datos 
            js=lista()   #retornamos datos de la db para el form del lado del cliente
            return render_template('registro.html',dato=js)
            

@app.route("/2da.html")
def render_index1():
    return render_template("2da.html")

@app.route("/3ra.html")
def render_inde():
    return render_template("3ra.html")
