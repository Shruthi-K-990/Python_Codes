from reportlab.platypus import SimpleDocTemplate,Table,Paragraph,TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
    ["Date" , "Name" , "Subscription" , "Prices (Rs.)"],
    ["01/01/2024" , "JioFiber" , "Anually" , "11786/-" ],
    ["01/05/2024" , "Amazon" , "Anually" , "2599/-"],
    ["12/12/2023" , "Netflix" , "Monthly" , "250/-"],
    ["04/05/2024" , "MCAFFE" , "Quaterly" , "2019/-"]
]

pdf = SimpleDocTemplate("data.pdf",pagesize = A4)
styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = 1
title = Paragraph("Subscription information",title_style)

style = TableStyle(
    [
    ("BOX" , (0,0),(-1,-1),1,colors.black),
    ("GRID",(0,0),(4,4),1,colors.blueviolet),
    ("BACKGROUND",(0,0),(3,0),colors.beige),
    ("TEXTCOLOR",(0,0),(-1,0),colors.darkblue),
    ("ALIGN",(0,0),(-1,-1),"CENTER"),
    ("BACKGROUND",(0,1),(-1,-1),colors.yellow)
    ]
)

table = Table(DATA,style=style)
pdf.build([title,table])