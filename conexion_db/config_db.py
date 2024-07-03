import mysql.connector
from mysql.connector import Error
error = Error
# Produccion
config_dev = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'jacarandaclienteuser'
}

# Despliegue
config_prod = {
    'user': '',
    'password': '',
    'host': '',
    'database': ''
    }

conexion = mysql.connector.connect(**config_dev)
