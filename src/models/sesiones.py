import src.config.globals as globals



class SesionesModel():

    #sesiones
    def traerSesion(self):
        cursor = globals.DB.cursor()

        cursor.execute('SELECT sesions.id, subjects.`names`, sesions.date, sesions.time_start, sesions.time_end FROM sesions INNER JOIN subjects ON sesions.subject_id = subjects.id')

        found = []
        for element in cursor:
            found.append(element)
        cursor.close()
        return found

    def crear(self, data):
        cursor = globals.DB.cursor()

        cursor.execute('insert into sesions(subject_id, date, time_start, time_end) values(?,?,?,?)', (data['subject_id'], data['date'], data['time_start'], data['time_end'],))
        
        cursor.close()

        
        