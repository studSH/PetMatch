# Datenmodell PetMatch

## Tier

| Spalte         | Typ     | Beschreibung              |
|----------------|---------|---------------------------|
| Tier_id        | INTEGER | PK                        |
| Halter_id      | INTEGER | FK                        |
| Tier_name      | TEXT    | Name des Tieres           |
| Rasse          | TEXT    | Rasse des Tieres          |
| Geburtsdatum   | DATE    | Geburtsdatum              |
| Das_mag_ich    | TEXT    | Vorlieben des Tieres      |
| Das_mag_ich_nicht | TEXT | Abneigungen des Tieres    |

## Halter

| Spalte       | Typ     | Beschreibung            |
|--------------|---------|-------------------------|
| Halter_id    | INTEGER | PK                      |
| Name         | TEXT    | Name des Halters        |
| Strasse      | TEXT    | Straßennamen            |
| Hausnummer   | INTEGER | Hausnummer              |
| Stadt        | TEXT    | Stadtname               |
| PLZ          | INTEGER | Postleitzahl            |
| Breitengrad  | REAL    | Breitengrad als Dezimalzahl |
| Längengrad   | REAL    | Längengrad als Dezimalzahl |
| Radius       | INTEGER | Gewählter Radius des Nutzers (nur Deutschland, daher Ländercode raus) |

## Feedbeitrag

| Spalte      | Typ     | Beschreibung             |
|-------------|---------|--------------------------|
| Feed_id     | INTEGER | PK                       |
| Tier_id     | INTEGER | FK                       |
| Halter_id   | INTEGER | FK                       |
| Inhalt      | TEXT    | Der Inhalt des Beitrages |
| Erstellt_am | DATE    | Erstellungsdatum         |
| Erstellt_um | TIME    | Zeit der Erstellung      |