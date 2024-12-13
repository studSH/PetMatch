
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# aktuelles Verzeichnis (app.py oder db.py)
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite-Datenbank (Datenbank wird im gleichen Verzeichnis wie db.py erstellt)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "petmatch.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Vermeidet unnötige Warnungen

# SQLAlchemy-Instanz initialisieren
db = SQLAlchemy(app)

# Definition der Tabelle 'Benutzer'
class Benutzer(db.Model):
    email = db.Column(db.String, primary_key=True)
    benutzername = db.Column(db.String, nullable=False)
    passwort = db.Column(db.String, nullable=False)

# Startseite
@app.route("/")
def index():
    return render_template("index.html", title="Startseite")

# Registrierung
@app.route("/registrierung", methods=['GET', 'POST'])
def registrierung():
    if request.method == 'POST':
        # Daten aus dem Formular erhalten
        email = request.form['email']
        email_wiederholen = request.form['email_wiederholen']
        benutzername = request.form['benutzername']
        passwort = request.form['passwort']

        # Überprüfen, ob die E-Mails übereinstimmen
        if email != email_wiederholen:
            return "Die E-Mail-Adressen stimmen nicht überein. Bitte versuche es erneut."

        # Benutzer in die Datenbank einfügen
        neuer_benutzer = Benutzer(email=email, benutzername=benutzername, passwort=passwort)
        try:
            db.session.add(neuer_benutzer)
            db.session.commit()
            return redirect(url_for('index'))  # Weiterleitung nach erfolgreicher Registrierung
        except Exception as e:
            db.session.rollback()
            return f"Fehler bei der Registrierung: {e}"

    return render_template("registrierung.html", title="Registrieren")

# Anmeldung
@app.route("/anmeldung", methods=['GET', 'POST'])
def anmeldung():
    if request.method == 'POST':
        email = request.form['email']
        passwort = request.form['passwort']

        # Überprüfung der Benutzeranmeldedaten
        benutzer = Benutzer.query.filter_by(email=email, passwort=passwort).first()

        if benutzer:
            return redirect(url_for('feed'))  # Weiterleitung bei erfolgreicher Anmeldung
        else:
            return "Ungültige Anmeldedaten. Bitte versuche es erneut."

    return render_template("anmeldung.html", title="Anmelden")

# Kontakt
@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", title="Kontakt")

@app.route('/feed', methods=['GET', 'POST'])
def feed():
    menu_open = False
    if request.method == 'POST':
        # Wenn der Benutzer auf das Bild klickt, Menü öffnen
        if 'open_menu' in request.form:
            menu_open = True
        # Wenn der Benutzer "Menü schließen" klickt, Menü schließen
        elif 'close_menu' in request.form:
            menu_open = False
    return render_template('feed.html', menu_open=menu_open)


# Route für 'Profil anzeigen'
@app.route("/profil_anzeigen")
def profil_anzeigen():
    # Hier kannst du Logik hinzufügen, um Benutzerdaten zu laden
    return render_template("profil_anzeigen.html", title="Profil anzeigen")

# Route für 'Profil bearbeiten'
@app.route("/profil_bearbeiten")
def profil_bearbeiten():
    # Hier kannst du Logik hinzufügen, um Benutzerdaten zum Bearbeiten zu laden
    return render_template("profil_bearbeiten.html", title="Profil bearbeiten")

# Route für 'Beitrag erstellen'
@app.route("/beitraege_erstellen")
def beitraege_erstellen():
    # Hier kannst du Logik hinzufügen, um die Beitragsseite zu rendern
    return render_template("beitraege_erstellen.html", title="Beitrag erstellen")

# Impressum
@app.route("/impressum")
def impressum():
    return render_template("impressum.html", title="Impressum")

# Datenschutz
@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html", title="Datenschutz")

# Prüfe, ob das Skript direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":
    # Erstellt alle Tabellen (falls sie noch nicht existieren)
    with app.app_context():
        db.create_all()

    # Start Flask-Anwendung im Debug-Modus, damit Änderungen ohne Neustart übernommen werden
    app.run(debug=True)
