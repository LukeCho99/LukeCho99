import mysql.connector
import datetime
op=input("1-	Truncate table\n2-	Erase data from ref\n3-	Drop table\n4-	Exit\n")
try:
	op=int(op)
	table=input("Specify table name: ")
	conexion1=mysql.connector.connect(host="localhost", user="root", passwd="password", database= "bdfiuna_2022" )
	cursor1=conexion1.cursor()
	if op==1:
		cursor1.execute("TRUNCATE TABLE "+table)
		conexion1.commit()
		print("Done, table "+table+" was successfully truncated")
	elif op==2:
		ref1=int(datetime.datetime.strptime(input("Specify time reference start (Y-m-d M:H:S): "),"%Y-%m-%d %H:%M:%S").timestamp())
		ref2=int(datetime.datetime.strptime(input("Specify time reference end (Y-m-d M:H:S): "),"%Y-%m-%d %H:%M:%S").timestamp())
		cursor1.execute("DELETE FROM "+table+" WHERE timestamp>="+str(ref1)+" AND timestamp<="+str(ref2))
		conexion1.commit()
		print("Data points were sucessfully erased")
	elif op==3:
		cursor1.execute("DROP TABLE "+table)
		print("Done, table "+table+" was deleted")
	else:
		print("Exiting...")
	conexion1.close()
except Exception as e:
	print(e)
	print("Nothing happened...")
print("Program terminated")
