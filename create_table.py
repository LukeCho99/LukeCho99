import mysql.connector
import pandas as pd
table_name="clase1"
var=['cedula','nombre','apellido']
line=""
for a in var: line+=", "+a+" FLOAT"
line="CREATE TABLE "+table_name+" (id INT AUTO_INCREMENT PRIMARY KEY"+line+");"
print(line)

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="password", database= "bdfiuna_2022" )
cursor1=conexion1.cursor()	
try:	
	cursor1.execute(line)    
	conexion1.commit()
	print("The SQL table was created successfully...")
except Exception as e: print(e)
conexion1.close()
