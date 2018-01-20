import sqlite3
import os



##Initiate SQLite Database
def INITSQLite(DBpath):
	if os.path.isfile(DBpath):
		print ("File vorhanden")
		connection = sqlite3.connect(DBpath)
		cursor = connection.cursor()

	else:
		print ("File nicht vorhanden")
		connection = sqlite3.connect(DBpath)
		cursor = connection.cursor()
		createSQLite(cursor, connection)
		connection = sqlite3.connect(DBpath)
		cursor = connection.cursor()
	return cursor, connection
	
#Create Database 
def createSQLite(cursor, connection):
	
	sql_command = """
	CREATE TABLE Meldungen ( 
		number INTEGER PRIMARY KEY, 
		Veranstaltung VARCHAR(100),
        Name VARCHAR(50),
        Vorname VARCHAR(50),
        Bday VARCHAR(30),
        Street VARCHAR(100),
        Ort VARCHAR(100),
        Land VARCHAR(100),
        Email VARCHAR(50),
        Tel VARCHAR(30),
        Mobil VARCHAR(30),
        Club VARCHAR(100),
        Abendprogramm_Ja_Nein VARCHAR(5),
        Abendprogramm_TicketNum VARCHAR(5),
        Bootstyp VARCHAR(30),
        Bootsname VARCHAR(50),
        Segelnummer VARCHAR(30),
        Yardstick VARCHAR(10),
        Spinacker_Ja_Nein VARCHAR(5),
        Crew_Name1 VARCHAR(50),
        Abendprogramm_Crew1_Ja_Nein VARCHAR(5),
        Crew1_Bday VARCHAR(30),
        Crew1_Club VARCHAR(50),
        Crew_Name2 VARCHAR(50),
        Abendprogramm_Crew2_Ja_Nein VARCHAR(5),
        Crew2_Bday VARCHAR(30),
        Crew2_Club VARCHAR(50),
        Crew_Name3 VARCHAR(50),
        Abendprogramm_Crew3_Ja_Nein VARCHAR(5),
        Crew3_Bday VARCHAR(30),
        Crew3_Club VARCHAR(50),
        Crew_Name4 VARCHAR(50),
        Abendprogramm_Crew4_Ja_Nein VARCHAR(5),
        Crew4_Bday VARCHAR(30),
        Crew4_Club VARCHAR(50),
        Crew_Name5 VARCHAR(50),
        Abendprogramm_Crew5_Ja_Nein VARCHAR(5),
        Crew5_Bday VARCHAR(30),
        Crew5_Club VARCHAR(50),
        Crew_Name6 VARCHAR(50),
        Abendprogramm_Crew6_Ja_Nein VARCHAR(5),
        Crew6_Bday VARCHAR(30),
        Crew6_Club VARCHAR(50),
        Crew_Name7 VARCHAR(50),
        Abendprogramm_Crew7_Ja_Nein VARCHAR(5),
        Crew7_Bday VARCHAR(30),
        Crew7_Club VARCHAR(50),
        Crew_Name8 VARCHAR(50),
        Abendprogramm_Crew8_Ja_Nein VARCHAR(5),
        Crew8_Bday VARCHAR(30),
        Crew8_Club VARCHAR(50)
    );"""
	cursor.execute(sql_command)
	connection.commit()
	connection.close()

#insert Meldung into SQL
def insertSQLite(Meldung, DBpath):
	cursor, connection = INITSQLite(DBpath)
	
#Check for duplicates
	SQLcom = ("SELECT 1 from Meldungen WHERE "
				"Veranstaltung='" + Meldung["Veranstaltung"] + "' AND "
				"Name='" + Meldung["Name"] + "' AND "
				"Vorname='" + Meldung["Vorname"] + "' AND "
				"Street='" + Meldung["Street"] + "' AND "
				"Ort='" + Meldung["Ort"] + "' AND "
				"Email='" + Meldung["Email"] + "' AND "
				"Tel='" + Meldung["Tel"] + "' AND "
				"Club='" + Meldung["Club"] + "' AND "
				"Abendprogramm_Ja_Nein='" + Meldung["Abendprogramm_Ja_Nein"] + "' AND "
				"Abendprogramm_TicketNum='" + Meldung["Abendprogramm_TicketNum"] + "' AND "
				"Bootstyp='" + Meldung["Bootstyp"] + "' AND "
				"Bootsname='" + Meldung["Bootsname"] + "' AND "
				"Segelnummer='" + Meldung["Segelnummer"] + "' AND "
				"Yardstick='" + Meldung["Yardstick"] + "' AND "
				"Spinacker_Ja_Nein='" + Meldung["Spinacker_Ja_Nein"] + "' AND "
				"Crew_Name1='" + Meldung["Crew_Name1"] + "' AND "
				"Abendprogramm_Crew1_Ja_Nein='" + Meldung["Abendprogramm_Crew1_Ja_Nein"] + "' AND "
				"Crew_Name2='" + Meldung["Crew_Name2"] + "' AND "
				"Abendprogramm_Crew2_Ja_Nein='" + Meldung["Abendprogramm_Crew2_Ja_Nein"] + "' AND "
				"Crew_Name3='" + Meldung["Crew_Name3"] + "' AND "
				"Abendprogramm_Crew3_Ja_Nein='" + Meldung["Abendprogramm_Crew3_Ja_Nein"] + "' AND "
				"Crew_Name4='" + Meldung["Crew_Name4"] + "' AND "
				"Abendprogramm_Crew4_Ja_Nein='" + Meldung["Abendprogramm_Crew4_Ja_Nein"] + "' AND "
				"Crew_Name5='" + Meldung["Crew_Name5"] + "' AND "
				"Abendprogramm_Crew5_Ja_Nein='" + Meldung["Abendprogramm_Crew5_Ja_Nein"] + "' AND "
				"Crew_Name6='" + Meldung["Crew_Name6"] + "' AND "
				"Abendprogramm_Crew6_Ja_Nein='" + Meldung["Abendprogramm_Crew6_Ja_Nein"] + "' AND "
				"Crew_Name7='" + Meldung["Crew_Name7"] + "' AND "
				"Abendprogramm_Crew7_Ja_Nein='" + Meldung["Abendprogramm_Crew7_Ja_Nein"] + "' AND "
				"Crew_Name8='" + Meldung["Crew_Name8"] + "' AND "
				"Abendprogramm_Crew8_Ja_Nein='" + Meldung["Abendprogramm_Crew8_Ja_Nein"] + "'")
								
	cursor.execute(str(SQLcom))
	if (str(cursor.fetchall()) != "[]"):
		print("duplicat meldung")
		return 
	
#Insert Meldung into DB
	SQLcom = ("INSERT INTO " 
				"Meldungen(number, Veranstaltung, Name, Vorname, "
				"Street, Ort, Email, Tel, Club, "
				"Abendprogramm_Ja_Nein, Abendprogramm_TicketNum, "
				"Bootstyp, Bootsname, Segelnummer, Yardstick, Spinacker_Ja_Nein, "
				"Crew_Name1, Abendprogramm_Crew1_Ja_Nein, "
				"Crew_Name2, Abendprogramm_Crew2_Ja_Nein, "
				"Crew_Name3, Abendprogramm_Crew3_Ja_Nein, "
				"Crew_Name4, Abendprogramm_Crew4_Ja_Nein, "
				"Crew_Name5, Abendprogramm_Crew5_Ja_Nein, "
				"Crew_Name6, Abendprogramm_Crew6_Ja_Nein, "
				"Crew_Name7, Abendprogramm_Crew7_Ja_Nein, "
				"Crew_Name8, Abendprogramm_Crew8_Ja_Nein "
				") VALUES ( "
				"NULL, '" + Meldung["Veranstaltung"] + "','"
				"" + Meldung["Name"] + "','"
				"" + Meldung["Vorname"] + "','"
				"" + Meldung["Street"] + "','"
				"" + Meldung["Ort"] + "','"
				"" + Meldung["Email"] + "','"
				"" + Meldung["Tel"]  +"','"
				"" + Meldung["Club"] + "','"
				"" + Meldung["Abendprogramm_Ja_Nein"] + "','"
				"" + Meldung["Abendprogramm_TicketNum"] + "','"
				"" + Meldung["Bootstyp"] + "','"
				"" + Meldung["Bootsname"] + "','"
				"" + Meldung["Segelnummer"] + "','"
				"" + Meldung["Yardstick"] + "','"
				"" + Meldung["Spinacker_Ja_Nein"] + "','"
				"" + Meldung["Crew_Name1"] + "','"
				"" + Meldung["Abendprogramm_Crew1_Ja_Nein"] + "','"
				"" + Meldung["Crew_Name2"] + "','"
				"" + Meldung["Abendprogramm_Crew2_Ja_Nein"] + "','"
				"" + Meldung["Crew_Name3"] +"','"
				"" + Meldung["Abendprogramm_Crew3_Ja_Nein"] + "','"
				"" + Meldung["Crew_Name4"] + "','"
				"" + Meldung["Abendprogramm_Crew4_Ja_Nein"] + "','"
				"" + Meldung["Crew_Name5"] + "','"
				"" + Meldung["Abendprogramm_Crew5_Ja_Nein"] + "','"
				"" + Meldung["Crew_Name6"] + "','"
				"" + Meldung["Abendprogramm_Crew6_Ja_Nein"] + "','"
				"" + Meldung["Crew_Name7"] + "','"
				"" + Meldung["Abendprogramm_Crew7_Ja_Nein"] + "','"
				"" + Meldung["Crew_Name8"] + "','"
				"" + Meldung["Abendprogramm_Crew8_Ja_Nein"] + "')")
	print (SQLcom)
	cursor.execute(str(SQLcom))
	print ("File Added")

	connection.commit()
	connection.close()

#insert Meldung into SQL
def insertSQLite_Seascape(Meldung, DBpath):
	cursor, connection = INITSQLite(DBpath)
	
#Check for duplicates
	SQLcom = ("SELECT 1 from Meldungen WHERE "
				"Veranstaltung='" + Meldung["Veranstaltung"] + "' AND "
				"Name='" + Meldung["Name"] + "' AND "
				"Vorname='" + Meldung["Vorname"] + "' AND "
				"Street='" + Meldung["Street"] + "' AND "
				"Ort='" + Meldung["Ort"] + "' AND "
				"Land='" + Meldung["Land"] + "' AND "							
				"Email='" + Meldung["Email"] + "' AND "
				"Tel='" + Meldung["Tel"] + "' AND "
				"Mobil='" + Meldung["Mobil"] + "' AND "
				"Club='" + Meldung["Club"] + "' AND "
				"Bootstyp='" + Meldung["Bootstyp"] + "' AND "
				"Bootsname='" + Meldung["Bootsname"] + "' AND "
				"Segelnummer='" + Meldung["Segelnummer"] + "' AND "
				"Crew_Name1='" + Meldung["Crew_Name1"] + "' AND "
				"Crew1_Bday='" + Meldung["Crew1_Bday"] + "' AND "
				"Crew1_Club='" + Meldung["Crew1_Club"] + "' AND "
				"Crew_Name2='" + Meldung["Crew_Name2"] + "' AND "
				"Crew2_Bday='" + Meldung["Crew2_Bday"] + "' AND "
				"Crew2_Club='" + Meldung["Crew2_Club"] + "' AND "
				"Crew_Name3='" + Meldung["Crew_Name3"] + "' AND "
				"Crew3_Bday='" + Meldung["Crew3_Bday"] + "' AND "
				"Crew3_Club='" + Meldung["Crew3_Club"] + "' ")			
	cursor.execute(str(SQLcom))
	if (str(cursor.fetchall()) != "[]"):
		print("duplicat meldung")
		return 

#Insert Meldung into DB
	SQLcom = ("INSERT INTO " 
				"Meldungen(number, Veranstaltung, Name, Vorname, "
				"Bday, Street, Ort, Land, Email, Tel, Mobil, Club, "
				"Bootstyp, Bootsname, Segelnummer, "
				"Crew_Name1, Crew1_Bday, Crew1_Club, "
				"Crew_Name2, Crew2_Bday, Crew2_Club, "
				"Crew_Name3, Crew3_Bday, Crew3_Club "
				") VALUES ( "
				"NULL, '" + Meldung["Veranstaltung"] + "','"
				"" + Meldung["Name"] + "','"
				"" + Meldung["Vorname"] + "','"
				"" + Meldung["Bday"] + "','"				
				"" + Meldung["Street"] + "','"
				"" + Meldung["Ort"] + "','"
				"" + Meldung["Land"] + "','"
				"" + Meldung["Email"] + "','"
				"" + Meldung["Tel"] +"','"
				"" + Meldung["Mobil"]  +"','"
				"" + Meldung["Club"] + "','"
				"" + Meldung["Bootstyp"] + "','"
				"" + Meldung["Bootsname"] + "','"
				"" + Meldung["Segelnummer"] + "','"
				"" + Meldung["Crew_Name1"] + "','"
				"" + Meldung["Crew1_Bday"] + "','"
				"" + Meldung["Crew1_Club"] + "','"
				"" + Meldung["Crew_Name2"] + "','"
				"" + Meldung["Crew2_Bday"] + "','"
				"" + Meldung["Crew2_Club"] + "','"
				"" + Meldung["Crew_Name3"] + "','"
				"" + Meldung["Crew3_Bday"] + "','"
				"" + Meldung["Crew3_Club"] + "')")
						
	print (SQLcom)
	cursor.execute(str(SQLcom))
	print ("File Added")

	connection.commit()
	connection.close()

#Add SQLfiles to Meldel Liste
def refreshLIST(Event, DBpath):
	Liste = []

	cursor, connection = INITSQLite(DBpath)
	
	cursor.execute("SELECT Name, Vorname, Segelnummer, Club, Bootstyp, Yardstick, Bootsname, Land FROM Meldungen WHERE Veranstaltung = '" + Event + "'")

	for r in cursor.fetchall():
		Meldung = {'Name' : str(r[0]), 'Vorname' : str(r[1]), 'Segelnummer' : str(r[2]), 'Club' : str(r[3]), 'Bootstyp' : str(r[4]), 'Yardstick' : str(r[5]), 'Bootsname' : str(r[6]), 'Land' : str(r[7])}
		Liste.append(Meldung)

	print ("Liste:" + str(Liste))
	return Liste

##Delete Item from SQL !!!!!!!!!!!TODO
def DelSQLite(url, name, color, DBpath):

        cursor, connection = INITSQLite(DBpath)

        SQLcom = ["DELETE FROM img WHERE url='", str(url) , "' AND name='", str(name) , "' AND color='", str(color) ,"'"]
        print ("".join(SQLcom))
        cursor.execute("".join(SQLcom))
        print ("File Removed")

        connection.commit()
        connection.close()
