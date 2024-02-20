# EIM_News_Crawler
Webcrawler, der dazu dient, Nachrichtenartikel von der Website der Fakultät für Elektrotechnik, Informatik und Mathematik der Universität Paderborn) zu extrahieren und je nach Skript als DOCX-Dateien oder *.txt-Datei zu speichern.

# Abhängigkeiten
## in allen Skripten enthalten
Das Skript verwendet die folgenden Python-Bibliotheken:  
os: Zur Verwaltung von Dateien und Verzeichnissen.  
requests: Zum Senden von HTTP-Anfragen und Empfangen von HTTP-Antworten.  
BeautifulSoup: Zur Extraktion von Daten aus HTML- oder XML-Dokumenten.  
datetime: Zur Arbeit mit Datums- und Zeitinformationen.  
## im Docx Skript enthalten
htmldocx: Zum Konvertieren von HTML zu DOCX.  
docx: Zur Erstellung und Bearbeitung von DOCX-Dateien.  
## im *.txt Skript enthalten
codecs: für die Codierung und Decodierung von Zeichenfolgen

# Verwendung
## Abhängikeiten installieren
Per Commandozeile in das Verzeichnis wechseln, in dem das requirements.txt gespeichert ist und mit dem Befehl `pip install -r requirements.txt` ausführen.

Gewisse Abhängigkeiten sind nur in einem der beiden Skripte enthalten. Ebenfalls werden nicht alle Installiert, da z.B. codecs bereits in Python enthalten sind.

## News herunterladen
Das Skript startet und fragt den Benutzer nach dem gewünschten Jahr für die News-Berichte.
Es erstellt ein Verzeichnis für das angegebene Jahr, falls es nicht existiert.
Der Crawler durchsucht die News-Seite der Fakultät für das angegebene Jahr.
Gefundene Artikel werden extrahiert und im entsprechenden Verzeichnis gespeichert.

# Anmerkungen
Der Crawler berücksichtigt das angegebene Jahr und extrahiert nur Artikel, die im angegebenen Zeitraum veröffentlicht wurden.
Wenn kein Artikeltext vorhanden ist, wird eine entsprechende Meldung ausgegeben.

## Wichtig
Unter umständen kommt es zu einem Timeout, wenn man sich ausserhalb des Universitätsnetzwerkes befindet. In diesem Fall hilft es einfach, sich in das Netzwerk per VPN einzuwählen und das Skript erneut auszuführen.


# gitignore
*.zip  
*.docx
