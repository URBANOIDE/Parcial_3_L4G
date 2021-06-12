import src.config.globals as globals



class MateriasModel():

    #sesiones
    def traerMateria(self):
        cursor = globals.DB.cursor()

        cursor.execute('select * from subjects ')

        found = []
        for element in cursor:
            found.append(element)
        cursor.close()
        return found

    def crear(self, data):
        cursor = globals.DB.cursor()

        cursor.execute(""" 
        INSERT INTO subjects(names,semester) VALUES(?,?)
        """,(data['name'],data['semester']))
        cursor.close()
        
        