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

# Prüfe, ob das Skript direkt ausgeführt wird (nicht importiert) 
if __name__ == "__main__":
    # Starte die Flask-Anwendung im Debug-Modus, damit Änderungen ohne Neustart übernommen werden
    app.run(debug=True)
