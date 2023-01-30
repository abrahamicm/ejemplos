import json

# Nombre del archivo JSON donde se guardará la información
filename = 'data.json'

# Función para crear un registro
def create(data):
    # Carga los datos existentes del archivo JSON
    try:
        with open(filename, 'r') as f:
            records = json.load(f)
    except:
        records = []

    # Agrega el nuevo registro a la lista de registros
    records.append(data)

    # Guarda la lista actualizada de registros en el archivo JSON
    with open(filename, 'w') as f:
        json.dump(records, f)

# Función para leer todos los registros
def read():
    try:
        with open(filename, 'r') as f:
            records = json.load(f)
        return records
    except:
        return []

# Función para actualizar un registro
def update(id, data):
    # Carga los datos existentes del archivo JSON
    with open(filename, 'r') as f:
        records = json.load(f)

    # Actualiza el registro con el id especificado
    for record in records:
        if record['id'] == id:
            record.update(data)
            break

    # Guarda la lista actualizada de registros en el archivo JSON
    with open(filename, 'w') as f:
        json.dump(records, f)

# Función para eliminar un registro
def delete(id):
    # Carga los datos existentes del archivo JSON
    with open(filename, 'r') as f:
        records = json.load(f)

    # Elimina el registro con el id especificado
    records = [record for record in records if record['id'] != id]

    # Guarda la lista actualizada de registros en el archivo JSON
    with open(filename, 'w') as f:
        json.dump(records, f)