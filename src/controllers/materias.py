from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.materias import MateriasModel

SUBJECTSMODEL = MateriasModel()


def convert():
    found = SUBJECTSMODEL.traerMateria()
    arrSubjects = []
    for element in found:
        data = {
            'id': element[0],
            'materia': element[1],
            'semestre': element[2],
        }
        arrSubjects.append(data)
    return arrSubjects

@app.route('/asignaturas', methods =['GET', 'POST'])
def asignaturas():
    if request.method == 'GET':
        return jsonify({'Subjects': convert()})
    data = {
        'name': request.json['name'],
        'semester': request.json['semester'],
    }
    SUBJECTSMODEL.crear(data)
    return jsonify({
        'message': 'Asignatura agregada correctamente',
        'Subjects': convert()})