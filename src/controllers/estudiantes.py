from flask import render_template, request, redirect, url_for, jsonify
from src import app
from src.models.estudiantes import EstudiantesModel

STUDENTMODEL = EstudiantesModel()


def convert():
    found = STUDENTMODEL.traerTodos()
    arrStudents = []
    for element in found:
        data = {
            'id': element[0],
            'identificacion': element[1],
            'nombre': element[2],
            'Apellido': element[3],
            'Email': element[4],
            'Telefono': element[5],
            'Semestre': element[6],
        }
        arrStudents.append(data)
    return arrStudents
# obtener y agregrar alumnos


@app.route('/estudiantes', methods=['GET', 'POST'])
def estudiantes():
    if request.method == 'GET':
        return jsonify({'students': convert()})
    data = {
        'identity': request.json['identity'],
        'name': request.json['name'],
        'surname': request.json['surname'],
        'email': request.json['email'],
        'phone': request.json['phone'],
        'semester': request.json['semester'],
    }
    try:
        STUDENTMODEL.crear(data)
        return jsonify({
            'message': 'Estudiante agregado correctamente',
            'Estudiantes': convert()})
    except:
        return jsonify({
            'ERROR': 'El estudiante no se puede agregar, ¡las datos INDETIDAD, E-MAIL Y TELEFONO son unicos, puede que ya se halla guardado otro estudiante con estos datos!'})
    

# actualizar y/o eliminar


@app.route('/estudiantes/<int:id>', methods=['PUT', 'DELETE'])
def editar_estudiante(id):
    if request.method == 'PUT':
        data = {
            'identity': request.json['identity'],
            'name': request.json['name'],
            'surname': request.json['surname'],
            'email': request.json['email'],
            'phone': request.json['phone'],
            'semester': request.json['semester'],
        }
        try:
            if STUDENTMODEL.editar(data, id) == None:
                return jsonify({
                    'ERROR': 'El estudiante no se encuentra en la DB'})
            return jsonify({
                'message': 'Estudiante editado correctamente',
                'Estudiantes': convert()})
        except:
            return jsonify({
                'ERROR': 'El estudiante no se puede editar, puede que la identificacion, email o telefono sean las mismas que la de otro estudiante ya registrado'})
    #validacion si es posible eliminar o no
    try:
        if STUDENTMODEL.eliminar(id) == None:
            return jsonify({
                'ERROR': 'El estudiante que desea eliminar no se encuentra en la DB'})
        return jsonify({
            'message': 'Estudiante eliminado correctamente',
            'Estudiantes': convert()})

    except:
        return jsonify({
            'ERROR': 'El estudiante no se puede borrar, debido a que ya esta asociado a una asistencia de alguna materia'})
    