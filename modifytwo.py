from email import errors
from jinja2 import Environment, FileSystemLoader
import pdfkit 

env = Environment(loader=FileSystemLoader("temp"))
template = env.get_template("una.html")

usuario = {
    "Name"      : "Joel Samorant",
    "CC"        : "1102569874",

}

#usuario["total"] = usuario["valor1"] + usuario["valor2"], usuario["valor3"] + usuario["valor4"]
#usuario['total'] = sum(usuario['total'])
html = template.render(usuario)
pdfkit.from_string(html, "saves/nuevaPd.pdf")
