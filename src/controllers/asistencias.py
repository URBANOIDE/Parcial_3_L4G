from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.asistencias import AsistenciasModel


ATTENDANCESMODEL = AsistenciasModel()

@app.route('/asistencias/sesion/<int:sesion_id>', methods=['GET', 'POST'])
def asistencias(sesion_id):
    if request.method == 'GET':
        found = ATTENDANCESMODEL.traerTodos(sesion_id)
        arrAttendances = []
        for element in found:
            data = {
                'id': element[0],
                'sesion': element[1],
                'identificacion': element[2],
                'estudiante': element[3],
                'presente': element[4],
            }
            arrAttendances.append(data)
        return jsonify({'Asistencia': arrAttendances})
    ###############
    data = {
        'sesion_id': sesion_id,
        'student_id': request.json['student_id'],
        'present': request.json['present'],
    }
    ATTENDANCESMODEL.crear(data)
    found = ATTENDANCESMODEL.traerTodos(sesion_id)
    arrAttendances = []
    for element in found:
        data = {
            'id': element[0],
            'sesion': element[1],
            'identificacion': element[2],
            'estudiante': element[3],
            'presente': element[4],
        }
        arrAttendances.append(data)
    return jsonify({
        'message': 'Sesion agregada correctamente',
        'Subjects': arrAttendances})


