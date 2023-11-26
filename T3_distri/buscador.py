import sqlite3
import sys
import argparse

def buscar_top_nombres(nombre_a_buscar):
    # Conexión a la base de datos SQLite
    conn = sqlite3.connect('./base.db')
    cursor = conn.cursor()
    # Consulta SQL para encontrar los 5 nombres y grupos con mayor frecuencia según el nombre_a_buscar
    query = '''
        SELECT nombre, grupo, frecuencia, url
        FROM tabla
        WHERE nombre = ?
        GROUP BY nombre, grupo
        ORDER BY frecuencia DESC
        LIMIT 5
    '''

    # Ejecutar la consulta con el nombre_a_buscar como parámetro
    cursor.execute(query, (nombre_a_buscar,))
    resultados = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    conn.close()

    return resultados

def main():
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Buscar los 5 nombres y grupos con mayor frecuencia para una palabra.')
    parser.add_argument('palabra_a_buscar', type=str, help='Palabra a buscar')

    # Obtener la palabra a buscar desde los argumentos de la línea de comandos
    args = parser.parse_args()
    palabra_a_buscar = args.palabra_a_buscar

    # Ejecutar la función con la palabra a buscar
    resultados = buscar_top_nombres(palabra_a_buscar)

    # Imprimir los resultados
    for resultado in resultados:
        print(f"Nombre: {resultado[0]}, Grupo: {resultado[1]}, Frecuencia: {resultado[2]}, Url: {resultado[3]}")

if __name__ == "__main__":
    main()
