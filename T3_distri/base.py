import sqlite3

# Función de parseo
def parse_line(line):
    words = line.split()
    group_a = words[0]
    numbers = []
    for word in words[1:]:
        parts = [part.strip(',') for part in word.strip('()').split(',')]
        numbers.extend([int(part) for part in parts if part])

    return group_a, numbers

# Conexión a la base de datos SQLite.
conn = sqlite3.connect('./T3_distri/base.db')
cursor = conn.cursor()

# Crear la tabla si no exist.e
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tabla (
        nombre TEXT,
        grupo TEXT,
        frecuencia INTEGER,
        url TEXT
    )
''')

# Leer el archivo y agregar datos a la base de datos
with open('./T3_distri/part-00000.txt', 'r') as file:
    lines = file.readlines()

    for line in lines[1:]:
        result = parse_line(line)
        if result:
            group_a, groups_numbers = result
            for i in range(0, len(groups_numbers), 2):
                key = (group_a, groups_numbers[i])
                value = groups_numbers[i+1]

                # Insertar datos en la base de datos.
                cursor.execute('INSERT INTO tabla (nombre, grupo, frecuencia, url) VALUES (?, ?, ?, ?)', (key[0],key[1], value,"https://es.wikipedia.org/wiki/"+str(key[1])))

conn.commit()
conn.close()
