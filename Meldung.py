 # -*- coding: utf-8 -*-
import os

import base64
import smtplib
import logging

from SQLite import *
from Email import *
from PDF import *

from flask import *
app = Flask(__name__,static_url_path ='')

#Variables
DBpath = "/home/lars/MeldungLYCC/V2/Meldungen.db"
#DBpath = "./Meldungen.db"

Meldung = {}


#### Convert PostData to Meldeform ####
def createMeldung(poststream):
	print("analysing data")
	Meldung = {}

	Meldung['Veranstaltung'] = poststream.form['Veranstaltung']
	Meldung['Name'] = poststream.form['Name']
	Meldung['Vorname'] = poststream.form['Vorname']
	Meldung['Street'] = poststream.form['Street']
	Meldung['Ort'] = poststream.form['Ort']
	Meldung['Email'] = poststream.form['Email']
	Meldung['Tel'] = poststream.form['Tel']
	Meldung['Club'] = poststream.form['Club']
	Meldung['Abendprogramm_Ja_Nein'] = poststream.form['Abendprogramm_Ja_Nein']
	Meldung['Abendprogramm_TicketNum'] = poststream.form['Abendprogramm_TicketNum']
	Meldung['Bootstyp'] = poststream.form['Bootstyp']
	Meldung['Bootsname'] = poststream.form['Bootsname']
	Meldung['Segelnummer'] = poststream.form['Segelnummer']
	Meldung['Yardstick'] = poststream.form['Yardstick']
	Meldung['Spinacker_Ja_Nein'] = poststream.form['Spinacker_Ja_Nein']
	Meldung['Crew_Name1'] = poststream.form['Crew_Name1']
	Meldung['Abendprogramm_Crew1_Ja_Nein'] = poststream.form['Abendprogramm_Crew1_Ja_Nein']
	Meldung['Crew_Name2'] = poststream.form['Crew_Name2']	
	Meldung['Abendprogramm_Crew2_Ja_Nein'] = poststream.form['Abendprogramm_Crew2_Ja_Nein']
	Meldung['Crew_Name3'] = poststream.form['Crew_Name3']
	Meldung['Abendprogramm_Crew3_Ja_Nein'] = poststream.form['Abendprogramm_Crew3_Ja_Nein']
	Meldung['Crew_Name4'] = poststream.form['Crew_Name4']
	Meldung['Abendprogramm_Crew4_Ja_Nein'] = poststream.form['Abendprogramm_Crew4_Ja_Nein']
	Meldung['Crew_Name5'] = poststream.form['Crew_Name5']
	Meldung['Abendprogramm_Crew5_Ja_Nein'] = poststream.form['Abendprogramm_Crew5_Ja_Nein']
	Meldung['Crew_Name6'] = poststream.form['Crew_Name6']
	Meldung['Abendprogramm_Crew6_Ja_Nein'] = poststream.form['Abendprogramm_Crew6_Ja_Nein']
	Meldung['Crew_Name7'] = poststream.form['Crew_Name7']
	Meldung['Abendprogramm_Crew7_Ja_Nein'] = poststream.form['Abendprogramm_Crew7_Ja_Nein']
	Meldung['Crew_Name8'] = poststream.form['Crew_Name8']
	Meldung['Abendprogramm_Crew8_Ja_Nein'] = poststream.form['Abendprogramm_Crew8_Ja_Nein']	

	return Meldung

	#if Cookie is not checked it cant be found in poststream => add manual dirty???
	try:
		Meldung['Cookie'] = poststream.form['Cookie']
	except:
		Meldung['Cookie'] = ""

#### Convert PostData to Meldeform  SEASCAPE####
def createMeldungSeascape(poststream):
	print("analysing data")
	Meldung = {}

	Meldung['Veranstaltung'] = poststream.form['Veranstaltung']
	Meldung['Name'] = poststream.form['Name']
	Meldung['Vorname'] = poststream.form['Vorname']
	Meldung['Bday'] = poststream.form['Bday']
	Meldung['Street'] = poststream.form['Street']
	Meldung['Ort'] = poststream.form['Ort']
	Meldung['Land'] = poststream.form['Land']
	Meldung['Email'] = poststream.form['Email']
	Meldung['Tel'] = poststream.form['Tel']
	Meldung['Mobil'] = poststream.form['Mobil']	
	Meldung['Club'] = poststream.form['Club']
	Meldung['Bootstyp'] = poststream.form['Bootstyp']
	Meldung['Bootsname'] = poststream.form['Bootsname']
	Meldung['Segelnummer'] = poststream.form['Segelnummer']
	Meldung['Crew_Name1'] = poststream.form['Crew_Name1']
	Meldung['Crew1_Bday'] = poststream.form['Crew1_Bday']
	Meldung['Crew1_Club'] = poststream.form['Crew1_Club']	
	Meldung['Crew_Name2'] = poststream.form['Crew_Name2']
	Meldung['Crew2_Bday'] = poststream.form['Crew2_Bday']
	Meldung['Crew2_Club'] = poststream.form['Crew2_Club']
	Meldung['Crew_Name3'] = poststream.form['Crew_Name3']
	Meldung['Crew3_Bday'] = poststream.form['Crew3_Bday']
	Meldung['Crew3_Club'] = poststream.form['Crew3_Club']
	
	return Meldung

##################Display Meldeform##################
#Return main HTML
@app.route("/<Event>", methods=['GET', 'POST'])
def MAIN(Event):
	global DBpath
	if request.method == 'POST':
		Meldung = createMeldung(request)
		insertSQLite(Meldung, DBpath)
		print("Meldung eingegangen")
		email(Meldung)
		Mel = refreshLIST(Meldung["Veranstaltung"],DBpath)
		createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png',Meldung["Veranstaltung"], 10, 2, Mel)

		#cookie handling
		resp = make_response(render_template('Meldung_Print.html', Meldung = Meldung))
		
#		if Meldung["Cookie"] == "Ja":
#			resp.set_cookie('CookieMeldung', str(Meldung))
#		else:
#			resp.set_cookie('CookieMeldung', '')
		return resp
	#Get the cookie Dirty version, but should work ....
	try:
		CookieMeldung = request.cookies.get('CookieMeldung')
		CookieMeldung = ast.literal_eval(CookieMeldung)
	except:
		print("No or wrong cookie")
	#return the meldeseite
	return render_template('Meldung.html', Veranstaltung = Event, cookie = CookieMeldung)


@app.route("/Seascape", methods=['GET', 'POST'])
def MAINS():
	global Meldung
	if request.method == 'POST':
		Meldung = createMeldungSeascape(request)
		insertSQLite_Seascape(Meldung, DBpath)
		
		print("Meldung eingegangen")
		email_Seascape(Meldung)
		Mel = refreshLIST(Meldung["Veranstaltung"],DBpath)
		createPDF('http://www.seascape18.de/wp-content/uploads/2015/10/seascape-logo.jpg','Seascape CUP Chiemsee 2018', 8, 4, Mel)
		return render_template('Meldung_Print_Seascape.html', Meldung = Meldung)
	return render_template('Meldung_Seascape.html')
	
#@app.route("/Seascape/list")
#def Seascape_liste():
#	global Meldung
#	return render_template('Meldeliste_Seascape.html', Liste = refreshLIST("Seascape CUP Chiemsee 2018"), Event = "Seascape CUP Chiemsee 2018")


#@app.route("/liste/<Event>")
#def LISTE(Event):
#	global Meldung
#	return render_template('Meldeliste.html', Liste = refreshLIST(Event), Event = Event)

@app.route("/Meldung/<Event>")
def File(Event):
        return send_file('Meldungen/'+ Event)


##########################MAIN RUN #############################
if __name__ == "__main__":

	#create PDFs at startup
	
	createPDF('http://www.seascape18.de/wp-content/uploads/2015/10/seascape-logo.jpg','Seascape CUP Chiemsee 2017', 8, 4, refreshLIST("Seascape CUP Chiemsee 2017",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Ansegeln LYCC & YCU', 10, 2, refreshLIST("Ansegeln LYCC & YCU",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Cruiser Cup 1.Wettfahrt', 10, 2, refreshLIST("Cruiser Cup 1.Wettfahrt",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Gelb-Schwarzes-Band', 10, 2, refreshLIST("Gelb-Schwarzes-Band",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Cruiser Cup 2.Wettfahrt', 10, 2, refreshLIST("Cruiser Cup 2.Wettfahrt",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Chiemsee Classic Cup 2.Wettfahrt', 10, 2, refreshLIST("Chiemsee Classic Cup 2.Wettfahrt",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Herbsttrophy – Känguru LYCC & YCU', 10, 2, refreshLIST("Herbsttrophy – Känguru LYCC & YCU",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Cruiser Cup 3.Wettfahrt', 10, 2, refreshLIST("Cruiser Cup 3.Wettfahrt",DBpath))
	
	#2018
	createPDF('http://www.seascape18.de/wp-content/uploads/2015/10/seascape-logo.jpg','Seascape CUP Chiemsee 2018', 8, 4, refreshLIST("Seascape CUP Chiemsee 2018",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Ansegeln 2018', 10, 2, refreshLIST("Ansegeln 2018",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Cruiser Cup 1. Wettfahrt 2018', 10, 2, refreshLIST("Cruiser Cup 1. Wettfahrt 2018",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Gelb-Schwarzes-Band 2018', 10, 2, refreshLIST("Gelb-Schwarzes-Band 2018",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Cruiser Cup 2. Wettfahrt 2018', 10, 2, refreshLIST("Cruiser Cup 2. Wettfahrt 2018",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Chiemsee Classic Cup 2.Wettfahrt 2018', 10, 2, refreshLIST("Chiemsee Classic Cup 2.Wettfahrt 2018",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Känguru-Regatta 2018', 10, 2, refreshLIST("Känguru-Regatta 2018",DBpath))
	createPDF('http://www.lycc.de/New_Page/wp-content/uploads/2017/01/Logo-LYCC-Original.png','Cruiser Cup 3. Wettfahrt 2018', 10, 2, refreshLIST("Cruiser Cup 3. Wettfahrt 2018",DBpath))
	
	logging.basicConfig(filename='error.log',level=logging.DEBUG)
	
#	app.run(host='0.0.0.0', port=8080)

	app.run(host='79.137.84.240', port=8080, threaded=True)
