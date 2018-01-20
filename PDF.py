
#ReportLab#
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib.enums import TA_CENTER

PDFDir = "/home/lars/MeldungLYCC/V2/Meldungen/"

### Create PDF to Download ### 	
def createPDF(logo, Event, Width, Height, Meld):
	global Meldung
	style = getSampleStyleSheet()
	normal = style["Normal"]
	normal.alignment = TA_CENTER
	normal.fontName = "Helvetica"
	normal.fontSize = 20
	normal.leading = 25
	normal.spaceAfter = 5

	elements = []

	if 'Seascape' in Event:
		data = [['Steuermann','Segelnummer','Club','Bootsklasse','Bootsname','Land']]
		for Mel in Meld:
			liste = []
			liste.append(Mel["Vorname"] + " " + Mel["Name"])
			liste.append(Mel["Segelnummer"])
			liste.append(Mel["Club"])
			liste.append(Mel["Bootstyp"])
			liste.append(Mel["Bootsname"])
			liste.append(Mel["Land"])
			data.append(liste)
	else:
		data = [['Steuermann','Segelnummer','Club','Bootsklasse','Yardstick','Bootsname']]
		for Mel in Meld:
			liste = []
			liste.append(Mel["Vorname"] + " " + Mel["Name"])
			liste.append(Mel["Segelnummer"])
			liste.append(Mel["Club"])
			liste.append(Mel["Bootstyp"])
			liste.append(Mel["Yardstick"])
			liste.append(Mel["Bootsname"])
			data.append(liste)

	print ("Data: " + str(data))
	#Anlegen des PDF Dokuments, Seitengröße DIN A4 Hochformat)
	pdf = SimpleDocTemplate(str(PDFDir + Event + '.pdf'),pagesize=A4)
	t=Table(data)
	t.setStyle(TableStyle([('TEXTCOLOR',(0,1),(5,-1),colors.gray),
							('INNERGRID', (0,0), (-1,-1), 0.25, colors.gray)]))
	elements.append(Image(logo, width=Width*cm, height=Height*cm))
	elements.append(Paragraph(Event, normal))
	elements.append(Paragraph("MELDELISTE", normal))
	elements.append(t)
	pdf.build(elements)
