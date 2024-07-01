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
    'user': 'DrKRazieL',
    'password': '@Jacaranda',
    'host': 'DrKRazieL.mysql.pythonanywhere-services.com',
    'database': 'DrKRazieL$jacaranda'
    }

conexion = mysql.connector.connect(**config_dev)