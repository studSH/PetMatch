## Vergleich der Geoapify Geocoding API und Google Geocoding API

| Merkmal                 | Geoapify Geocoding API                                 | Google Geocoding API                              |
|-------------------------|--------------------------------------------------------|---------------------------------------------------|
| **Kosten**              | Kostenlose Nutzung bis 3.000 Anfragen pro Tag; günstige Tarife für Mehrbedarf. | Monatliches Gratis-Guthaben von 200 USD, für bis zu 40.000 Anfragen; Konto mit Abrechnung nötig. |
| **Einrichtung**         | API-Schlüssel ohne Abrechnungsanforderungen.           | API-Schlüssel nur mit aktivierter Abrechnung.     |
| **Datenumfang**         | Basisdaten: Koordinaten, Adressstruktur. Zusätzliche Funktionen gegen Gebühr. | Sehr detaillierte Adressdaten und Geodaten.       |
| **Zusätzliche Funktionen** | Länderspezifische Infos, Zeitzonen (kostenlos nutzbar) | Zusätzliche Standortinformationen (z. B. `location_type`). |
| **Datenschutz**         | Nutzt OpenStreetMap-Daten, speichert keine Nutzerdaten dauerhaft. | Erfordert Google Cloud-Account und speichert Daten auf Google-Servern. |
| **Support und Dokumentation** | Solide Dokumentation, hauptsächlich in Englisch. | Umfangreiche Dokumentation in Deutsch und Englisch. |
| **Einsatzbeispiele**    | Ideal für Prototypen, kleine bis mittlere Anwendungen. | Bewährt für umfangreiche kommerzielle Anwendungen mit hohen Anforderungen. |

## Entscheidungshilfe und Begründung

### Wir haben uns für die **Geoapify Geocoding API** entschieden:
**Begründung**: Die Wahl der Geoapify API liegt in ihrer Einfachheit und Kosteneffizienz, die sich besonders für ein kleines, moderates Projekt wie ein Uni-Projekt anbietet. Geoapify bietet einen unkomplizierten Zugriff ohne Anforderungen an die Abrechnung und eine solide kostenlose Nutzung für bis zu 3.000 Anfragen pro Tag, was für eine solche Anwendung völlig ausreicht. Zudem erfordert Geoapify keine Speicherung sensibler Nutzerdaten auf externen Servern, was den Datenschutz verbessert.

Diese API bietet ausreichende Funktionalität für die Umwandlung von Adressen in Geokoordinaten und ist schnell und einfach integrierbar. Daher eignet sich die Geoapify API für einen ersten Prototyp, bei dem eine moderate Nutzung und einfache Handhabung im Vordergrund stehen.

