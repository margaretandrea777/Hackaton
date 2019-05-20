from flask import Flask, render_template, request 
import sqlite3 as sql

app=Flask(__name__,static_url_path='')


nombre_db="basedatos4.db"
@app.route("/")
def render_html():
    return render_template("bienvenida.html")


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
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        ci integer ,
                                        nombre text,
                                        numeroT integer,                                        
                                        profesion text,
                                        ciudad text,
                                        cantper integer,
                                        gastosm integer,
                                        gastosd integer,
                                        ingresosm interger,
                                        ingresosd integer,
                                        zona text,
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


            
@app.route('/registro3', methods=['POST','GET'])      # aca es para registrar al animal
def registro3():
    if request.method=='POST':   
        try:
            cantidad=request.form['cantidad'] 
            ingresos=request.form['ingresos']                          #identificativo del animal
            zona=request.form['zona']
              # suma=alimentacion + servicios+otros
            datos=[cantidad,ingresos,zona]  # esto es para meter en la db luego
         
            print(datos)
            with sql.connect(nombre_db) as con:        
                cur = con.cursor()
                print("Hola")
                cur.execute('''CREATE TABLE IF NOT EXISTS usuario (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        ci integer,
                                        nombre text,
                                        numeroT integer,                                        
                                        profesion text,
                                        ciudad text,
                                        cantper integer,
                                        gastosm integer,
                                        gastosd integer,
                                        ingresosm interger,
                                        ingresosd integer,
                                        zona text,
                                        fecha text,
                                        monto integer,
                                        tipo text
                                    );'''
                       )
                print("FSdaf")
                #cur.execute('''INSERT INTO usuario (ci) VALUES (?);''', datos )
                cedulas=lista()
                ultimoelemento=len(cedulas) -1 #obtenemos el tamaño de las cedulas
                #debemos elegir el ultimo 
                ultimo=cedulas[ultimoelemento]  
                sentencia=''' UPDATE usuario SET     cantper='{1}',
                                                     ingresosm= '{2}',
                                                     zona= '{3}' 
                                                     where ci='{0}' '''.format(str(ultimo),str(cantidad),str(ingresos),str(zona))
                print(sentencia)
                cur.execute(sentencia)
                con.commit()   
                
        except sql.DatabaseError as e:
            con.rollback()
            print(e)

        finally:
            con.close()# cerramos la conexion de la base de datos 
            #js=lista()   #retornamos datos de la db para el form del lado del cliente
            total=int(ingresos)/int(cantidad)

            totalUrbano = int(cantidad) * 664297
            totalRural = int(cantidad) * 256881

            estado = "bien"

            if zona == "urbana":
                if total < totalUrbano:
                    estado = "mal"
            elif zona == "rural":
                if total < totalRural:
                    estado = "mal"

            print("total1",total)
            print("total2",totalUrbano)
            print(estado)
            return render_template('6ta.html',cantidad=total, estado=estado)
            
@app.route('/registro4', methods=['POST','GET'])      # aca es para registrar al animal
def registro4():
    if request.method=='POST':   
        try:
            mes=request.form['mes']
            alimentacion=request.form['alimentacion']
            servicios=request.form['servicios']
            otros=request.form['otros']
            suma=int(alimentacion)+int(servicios)+int(otros)
            cantidad=request.form['cantidad'] 
            ingresos=request.form['ingresos']                          #identificativo del animal
            zona=request.form['zona']
              # suma=alimentacion + servicios+otros
            datos=[cantidad,ingresos,zona]  # esto es para meter en la db luego
         
            print(datos)
            with sql.connect(nombre_db) as con:        
                cur = con.cursor()
                print("Hola")
                cur.execute('''CREATE TABLE IF NOT EXISTS usuario (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        ci integer,
                                        nombre text,
                                        numeroT integer,                                        
                                        profesion text,
                                        ciudad text,
                                        cantper integer,
                                        gastosm integer,
                                        gastosd integer,
                                        ingresosm interger,
                                        ingresosd integer,
                                        zona text,
                                        fecha text,
                                        monto integer,
                                        tipo text
                                    );'''
                       )
                print("FSdaf")
                #cur.execute('''INSERT INTO usuario (ci) VALUES (?);''', datos )
                cedulas=lista()
                ultimoelemento=len(cedulas) -1 #obtenemos el tamaño de las cedulas
                #debemos elegir el ultimo 
                ultimo=cedulas[ultimoelemento]  
                sentencia=''' UPDATE usuario SET     cantper='{1}',
                                                     ingresosm= '{2}',
                                                     zona= '{3}' 
                                                     where ci='{0}' '''.format(str(ultimo),str(cantidad),str(ingresos),str(zona))
                print(sentencia)
                cur.execute(sentencia)
                con.commit()
        except sql.DatabaseError as e:
            con.rollback()
            print(e)

        finally:
            con.close()# cerramos la conexion de la base de datos 
            #js=lista()   #retornamos datos de la db para el form del lado del cliente
            return render_template('5ta.html')


@app.route ('/registro2', methods=['POST','GET'])
def registro2():
    if request.method=='POST':   
        try:
            nombre=request.form['nombre'] 
            profesion=request.form['profesion']
            ciudad=request.form['ciudad']
            telefono=request.form['telefono']  #identificativo del animal
            datos=[nombre,telefono,profesion,ciudad]  # esto es para meter en la db luego
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
                                        cantper integer,
                                        gastosm integer,
                                        gastosd integer,
                                        ingresosm interger,
                                        ingresosd integer,
                                        zona text,
                                        fecha text,
                                        monto integer,
                                        tipo text
                                    );'''
                       )
                print("FSdaf")
                sent='''INSERT INTO usuario (nombre,numeroT,profesion,ciudad) VALUES (?,?,?,?);''', datos 
                print(sent)
                #cur.execute('''INSERT INTO usuario (nombre,numeroT,profesion,ciudad) VALUES (?,?,?,?);''', datos )
                #pedimos el ultimo ci que agregamos 
                cedulas=lista()
                ultimoelemento=len(cedulas) -1 #obtenemos el tamaño de las cedulas
                #debemos elegir el ultimo 
                ultimo=cedulas[ultimoelemento]  
                print("La ultima cedula es",ultimo)
                dic={'ci': ultimo,
                    'nombre': nombre, 
                     'numeroT': telefono, 
                      'profesion': profesion, 
                      'ciudad': ciudad}
                sentencia=''' UPDATE usuario SET     ci='{0}',
                                                     nombre= '{1}',
                                                    numeroT= '{2}',
                                                    profesion= '{3}',
                                                    ciudad= '{4}' 
                                                    where ci='{0}' '''.format(str(ultimo),str(nombre),str(telefono),str(profesion),str(ciudad))
                datos=[str(ultimo),nombre,telefono,profesion,ciudad]  # esto es para meter en la db luego
               # sentencia1='''UPDATE usuario (ci,nombre,numeroT,profesion,ciudad) VALUES (?,?,?,?,?) where ci='5427222';''', datos 
                print(sentencia)
                cur.execute(sentencia)
                con.commit()   
             
        except sql.DatabaseError as e:
            con.rollback()
            print(e)

        finally:
            con.close()# cerramos la conexion de la base de datos 
            #js=lista()   #retornamos datos de la db para el form del lado del cliente
            return render_template('5ta.html')
            


def lista():
   try:
       con = sql.connect(nombre_db)
       con.row_factory = sql.Row  
       cur = con.cursor()
       cur.execute("select * from usuario")
       dato = cur.fetchall()     #cargamos toda la info de la db en la variable dato
       cedulas=[]                   #lista para almacenar datos de razas 
 
       
       for a in dato:
          cedulas.append(a[1])   #usamos la posicion 1 ya que ahi se encuentran las nombres

       
       return cedulas
   except:            #si tiene problemas puede ser porque no existe la base de datos
       with sql.connect(nombre_db) as con:        
           cur = con.cursor()
           cur.execute('''CREATE TABLE IF NOT EXISTS usuario (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        ci integer,
                                        nombre text,
                                        numeroT integer,                                        
                                        profesion text,
                                        ciudad text,
                                        cantper integer,
                                        gastosm integer,
                                        gastosd integer,
                                        ingresosm interger,
                                        ingresosd integer,
                                        zona text,
                                        fecha text,
                                        monto integer,
                                        tipo text
                                    );'''
                       )
       cedulas=[]
       return  cedulas




@app.route("/2da.html")
def render_index1():
    return render_template("2da.html")

@app.route("/3ra.html")
def render_inde():
    return render_template("3ra.html")

@app.route("/4ta.html")
def render_ind():
    return render_template("4ta.html")

@app.route("/5ta.html")
def render_in():
    return render_template("5ta.html")

@app.route("/6ta.html")
def render_i():
    return render_template("6ta.html")

@app.route("/7ma.html")
def render_():
    return render_template("7ma.html")