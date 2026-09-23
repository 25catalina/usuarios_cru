from mysqlconnection import connectToMySQL

class Usuario: #moldeo plantilla
    def __init__(self, datos): #todo proyectos tienes clases
        self.id = datos ["id"]
        self.nombre = datos ["nombre"]
        self.apellido = datos ["apellido"]
        self.gmail = datos ["gmail"]
        self.created_at = datos ["created_at"]
        self.updated_at = datos ["updated_at"]

    #metodo para obtener todos los usuarios de la base de datos
    @classmethod
    def obtener_todos (cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL("usuarios_crum").query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append( cls(usuario) )
        return usuarios  #si no es un objeto, es una lista de objetos, por eso se usa cls para crear una instancia de la clase Usuario con los datos obtenidos de la base de datos

 #metodo para guardar un usuario en la base de datos
    @classmethod
    def guardar (cls, datos): #SENTENCIAS preparadas para evitar inyecciones SQL, datos es un diccionario 
        query = "INSERT INTO usuarios (nombre, apellido, gmail, created_at, updated_at ) VALUES (%(nombre)s, %(apellido)s, %(gmail)s, NOW(), NOW());"
        resultado = connectToMySQL("usuarios_crum").query_db(query, datos)
        return resultado
    
    @classmethod
    def actualizar(cls, datos):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, gmail = %(gmail)s, updated_at = NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL("usuarios_crum").query_db(query, datos)
        return resultado
