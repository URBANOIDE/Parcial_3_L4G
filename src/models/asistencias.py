import src.config.globals as globals



class AsistenciasModel():
    #crud estudiantes
    def traerTodos(self, sesion_id):
        cursor = globals.DB.cursor()

        cursor.execute('SELECT attendances.id, subjects.`names`, students.identity, students.`names`, attendances.present FROM attendances INNER JOIN sesions ON attendances.sesion_id = sesions.id INNER JOIN subjects ON sesions.subject_id = subjects.id INNER JOIN students ON attendances.student_id = students.id where sesion_id=?',(sesion_id,))

        found = []
        for element in cursor:
            found.append(element)
        cursor.close()
        return found

        return asistencias
    def crear(self, data):
        cursor = globals.DB.cursor()

        cursor.execute("""
        insert into attendances(sesion_id, student_id, present) values(?,?,?)
        """, (data['sesion_id'], data['student_id'], data['present'],))
        
        cursor.close()