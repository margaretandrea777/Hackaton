from flask import Flask, render_template, request 
import sqlite3 as sql
app=Flask(__name__)


nombre_db="basedatos2.db"
@app.route("/")
def render_html():
    return render_template("bienvenida.html")

def lista():
    return []

@app.route("/index")
def render1():
    return render_template("index.html")


@app.route("/registro2", methods=['POST'])
def registrohtml2():
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
                print("Hola")
                cur.execute('''CREATE TABLE IF NOT EXISTS usuario (
                                        ci integer ,
                                        nombre text,
                                        numeroT integer,                                        
                                        profesion text,
                                        ciudad text,
                                        celular integer,
                                        gastosd integer,
                                        ingd integer,
                                        fecha text,
                                        monto integer,
                                        tipo text
                                    );'''
                       )
                print("FSdaf")
                cur.execute('''INSERT INTO usuario (ci) VALUES (?);''', datos )
            
                con.commit()   
             
        except sql.DatabaseError as e:
            con.rollback()
            print(e)

        finally:
            con.close()# cerramos la conexion de la base de datos 
            #js=lista()   #retornamos datos de la db para el form del lado del cliente
            return render_template('3ra.html')
            


@app.route('/registro2', methods=['POST','GET'])      # aca es para registrar al animal
def registro2():
    if request.method=='POST':   
        try:
            nombre=request.form['nombre'] 
            profesion=request.form['profesion']
            ciudad=request.form['ciudad']
            telefono=request.form['telefono']
                                        #identificativo del animal
            datos=[nombre,profesion,ciudad,telefono]  # esto es para meter en la db luego
            print(datos)
            with sql.connect(nombre_db) as con:        
                cur = con.cursor()
                print("Hola")
                cur.execute('''CREATE TABLE IF NOT EXISTS usuario (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        ci integer ,
                                        nombre text,
                                        numeroT integer,                                        
                                        profesion text,
                                        ciudad text,
                                        celular integer,
                                        gastosd integer,
                                        ingd integer,
                                        fecha text,
                                        monto integer,
                                        tipo text
                                    );'''
                       )
                print("FSdaf")
                cur.execute('''INSERT INTO usuario (ci) VALUES (?);''', datos )
            
                con.commit()   
             
        except sql.DatabaseError as e:
            con.rollback()
            print(e)

        finally:
            con.close()# cerramos la conexion de la base de datos 
            #js=lista()   #retornamos datos de la db para el form del lado del cliente
            return render_template('3ra.html')
            






@app.route("/2da.html")
def render_index1():
    return render_template("2da.html")

@app.route("/3ra.html")
def render_inde():
    return render_template("3ra.html")
