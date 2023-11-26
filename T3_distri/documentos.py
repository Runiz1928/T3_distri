import os
import wikipediaapi

###############################################################
# Punto 1.
def obtener_documentos(clave, num_documentos):
    wiki_wiki = wikipediaapi.Wikipedia('Vicente', 'en')

    documentos = []

    # Obtener la página relacionada con la clave
    pagina_principal = wiki_wiki.page(clave)

    if pagina_principal.exists():
        # Obtener los enlaces desde la página
        enlaces = pagina_principal.links

        for i, (titulo, _) in enumerate(enlaces.items()):
            # Obtener la página según el título del enlace
            page = wiki_wiki.page(titulo)

            # Verificar si la página es válida y tiene contenido
            if page.exists() and page.text:
                documentos.append(page.text)

            # Se alcanzan los 30 documentos y se sale de la funcion
            if len(documentos) == num_documentos:
                break

    return documentos

# Obtener 30 documentos relacionados con la palabra "war"
documentos_relacionados = obtener_documentos("war", 30)  # (Se puede cambiar la palabra para obtener distintos resultados)

###############################################################
# Punto 2.
# Directorios para los documentos dentro de T3_distri
directorio_script = os.path.dirname(__file__)
carpeta_1 = os.path.join(directorio_script, "carpeta1")
carpeta_2 = os.path.join(directorio_script, "carpeta2")

# Crear carpetas si no existen
os.makedirs(carpeta_1, exist_ok=True)
os.makedirs(carpeta_2, exist_ok=True)

# Guardar documentos
for i, doc in enumerate(documentos_relacionados, start=1):
    # 1 al 15 carpeta 1, 16 al 30 carpeta 2.
    if i <= 15:
        carpeta_actual = carpeta_1
    else:
        carpeta_actual = carpeta_2

    # Crear el nombre del archivo
    nombre_archivo = f"documento{i}.txt"

    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_actual, nombre_archivo)

    # Eliminar saltos de línea del contenido del documento
    doc_sin_saltos_de_linea = doc.replace('\n', '')

    # Guardar el documento como archivo de texto
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        # Escribir el número de documento con el formato deseado
        archivo.write(f"{i}<splittername>\"{doc_sin_saltos_de_linea}\"")
