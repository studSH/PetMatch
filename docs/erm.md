# ERM PetMatch

```mermaid
erDiagram
    BENUTZER {
        TEXT Email PK
        TEXT Benutzername
        TEXT Passwort
    }
    HALTER {
        INTEGER Halter_id PK
        TEXT Email FK
        TEXT Name
        TEXT Strasse
        INTEGER Hausnummer
        TEXT Stadt
        INTEGER PLZ
        REAL Breitengrad
        REAL Laengengrad
        INTEGER Radius
    }
    TIER {
        INTEGER Tier_id PK
        INTEGER Halter_id FK
        TEXT Tier_name
        TEXT Rasse
        DATE Geburtsdatum
        TEXT Das_mag_ich
        TEXT Das_mag_ich_nicht
    }
    FEEDBEITRAG {
        INTEGER Feed_id PK
        INTEGER Tier_id FK
        INTEGER Halter_id FK
        TEXT Titel
        TEXT Inhalt
        DATE Erstellt_am
        TIME Erstellt_um
    }
    BILD {
        INTEGER Bild_id PK
        INTEGER Feed_id FK
        BLOB Bild
        TEXT Beschreibung
    }

    BENUTZER ||--|| HALTER : "ist registriert als"
    HALTER ||--o| TIER : "besitzt"
    HALTER ||--o| FEEDBEITRAG : "hat gepostet"
    TIER ||--o| FEEDBEITRAG : "ist enthalten"
    FEEDBEITRAG ||--o| BILD : "gehört zu"
