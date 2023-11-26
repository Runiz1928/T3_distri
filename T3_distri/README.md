ESTE README ESTA DISEÑADO PARA EXPLICAR CADA PARTE DE LA CARPETA T3_DISTRI PARA MÁS DETALLES APARTE DEL VIDEO.

Archivos:
base.db -> base de datos de part-00000.txt, contiene todas las palabras de las paginas de la wiki con su respectivo n° de documento


base.py -> codigo que se utiliza para crear la base.db

buscador.py -> se usa para buscar dentro de la base.db la palabra clave que queramos, nos retorna los 5 mejores resultados segun frecuencia en las paginas

documentos.py -> se usa wrapper de wiki para buscar las 30 paginas de wiki y guardarlas en carpeta1 y carpeta2.

mapper.py y reducer.py -> MapReducer normal sin index inverso

mapper1.py y reducer1.py -> MapReducer con index inverso, es lo mismo que se utiliza en la carpeta de hadoop.

part-00000.txt -> archivo con todos los datos de frecuencia y n° de documento de documentos.py (es lo que retorna hadoop al terminar).



Comandos:
python3 buscador.py "palabra" -> busca palabra en base.db
cat carpeta1/*.txt | mapper.py | sort | reducer.py -> MapReducer en carpeta1
cat carpeta2/*.txt | mapper.py | sort | reducer.py

----- Hadoop -----
docker compose up --build
docker exec -it hadoop bash
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input
sudo chown -R hduser .

cd examples/
hdfs dfs -put carpeta1/*.txt input
hdfs dfs -put carpeta2/*.txt input

hdfs dfs -ls input

mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output hduser/outhadoop/ -mapper ./mapper.py -reducer ./reducer.py

hdfs dfs -get /user/hduser/hduser/outhadoop/ /home/hduser/examples
