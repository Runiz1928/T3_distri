#!/bin/bash
set -e

# Iniciar el servicio SSH
echo "Starting SSH..."
sudo service ssh start

# Configurar variables de entorno
HDFS_DIR="/tmp/hadoop-hduser/dfs/name"
YARNSTART=${YARNSTART:-0}

# Verificar si el directorio HDFS existe
if [ ! -d "$HDFS_DIR" ]; then
    $HADOOP_HOME/bin/hdfs namenode -format && echo "OK : HDFS namenode format operation finished successfully !"
fi

# Iniciar los servicios de Hadoop
$HADOOP_HOME/sbin/start-dfs.sh

echo "YARNSTART = $YARNSTART"
# Verificar si se debe iniciar YARN
if [[ $YARNSTART -eq 0 ]]; then
    echo "Running start-yarn.sh"
    $HADOOP_HOME/sbin/start-yarn.sh
fi

# Configurar directorios y permisos en HDFS
$HADOOP_HOME/bin/hdfs dfs -mkdir /tmp
$HADOOP_HOME/bin/hdfs dfs -mkdir /users
$HADOOP_HOME/bin/hdfs dfs -mkdir /jars
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /tmp
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /users
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /jars

# Salir del modo seguro en HDFS
$HADOOP_HOME/bin/hdfs dfsadmin -safemode leave

# Mantener el contenedor en ejecución indefinidamente
tail -f $HADOOP_HOME/logs/hadoop-*-namenode-*.log

