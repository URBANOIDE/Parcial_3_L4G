import src.config.globals as globals



class EstudiantesModel():
    #crud estudiantes
    def traerTodos(self):
        cursor = globals.DB.cursor()
        cursor.execute(""" 
        SELECT * FROM students 
        """)
        found = []
        for element in cursor:
            found.append(element)
        cursor.close()
        return found

    def crear(self, data):
        cursor = globals.DB.cursor()
        cursor.execute(""" 
        INSERT INTO students(identity,names,surname,email,phone,semester) VALUES(?,?,?,?,?,?)
        """,(data['identity'],data['name'],data['surname'],data['email'],data['phone'],data['semester']))
        cursor.close()

    def editar(self, data, id):
        cursor = globals.DB.cursor()

        cursor.execute(""" 
        UPDATE students SET identity = ?, names = ?, surname = ?, email = ?, phone = ?, semester = ? WHERE id = ?
        """,(data['identity'],data['name'],data['surname'],data['email'],data['phone'],data['semester'],id))
        cursor.execute(""" 
        SELECT * FROM students WHERE id = ?
        """,(id,))
        found = cursor.fetchone()
        cursor.close()
        return found
    def eliminar(self, id):
        cursor = globals.DB.cursor()

        cursor.execute("""
        delete from students  WHERE id = ?
        """,(id,))
        
        cursor.close()
        