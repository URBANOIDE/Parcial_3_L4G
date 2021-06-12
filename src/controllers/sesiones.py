from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.sesiones import SesionesModel

SESIONSMODEL = SesionesModel()


def convert():
    found = SESIONSMODEL.traerSesion()
    arrSesions = []
    for element in found:
        data = {
            'id': element[0],
            'Materia': element[1],
            'Fecha': element[2],
            'Hora Inicio': element[3],
            'Hora Fin': element[4],
        }
        arrSesions.append(data)
    return arrSesions

@app.route('/sesiones', methods =['GET', 'POST'])
def sesiones():
    if request.method == 'GET':
        return jsonify({'Sesiones': convert()})
    data = {
        'subject_id': request.json['subject_id'],
        'date': request.json['date'],
        'time_start': request.json['time_start'],
        'time_end': request.json['time_end'],
    }
    SESIONSMODEL.crear(data)
    return jsonify({
        'message': 'Sesion agregada correctamente',
        'Subjects': convert()})