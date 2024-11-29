# https://flask-ptbr.readthedocs.io/en/latest/quickstart.html
# Importiere die Flask-Klasse und Jinja-Templates aus dem Flask-Modul
from flask import Flask, render_template

# Erstelle eine Instanz der Flask-Klasse, die die Webanwendung repräsentiert
app = Flask(__name__)

# Dekoriere die Funktion `home` mit der Route `/`, die die Startseite der Anwendung definiert
@app.route("/")
def index():
    # Diese Funktion wird ausgeführt, wenn jemand die Startseite besucht
    return render_template("index.html", title="Startseite")

@app.route("/registrierung")
def registrierung():
    return render_template("registrierung.html", title="Registrieren")

@app.route("/anmeldung")
def anmeldung():
    return render_template("anmeldung.html", title="Anmelden")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", title="Kontakt")

@app.route("/impressum")
def impressum():
    return render_template("impressum.html", title="Impressum")

@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html", title="Datenschutz")

# Prüfe, ob das Skript direkt ausgeführt wird (nicht importiert) 
if __name__ == "__main__":
    # Starte die Flask-Anwendung im Debug-Modus, damit Änderungen ohne Neustart übernommen werden
    app.run(debug=True)
