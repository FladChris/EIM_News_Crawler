# EIM_News_Crawler
Webcrawler, der dazu dient, Nachrichtenartikel von der Website der Fakultät für Elektrotechnik, Informatik und Mathematik der Universität Paderborn) zu extrahieren und als DOCX-Dateien zu speichern.

#Abhängigkeiten
Das Skript verwendet die folgenden Python-Bibliotheken:

os: Zur Verwaltung von Dateien und Verzeichnissen.
requests: Zum Senden von HTTP-Anfragen und Empfangen von HTTP-Antworten.
BeautifulSoup: Zur Extraktion von Daten aus HTML- oder XML-Dokumenten.
datetime: Zur Arbeit mit Datums- und Zeitinformationen.
htmldocx: Zum Konvertieren von HTML zu DOCX.
docx: Zur Erstellung und Bearbeitung von DOCX-Dateien.

#Verwendung
Das Skript startet und fragt den Benutzer nach dem gewünschten Jahr für die News-Berichte.
Es erstellt ein Verzeichnis für das angegebene Jahr, falls es nicht existiert.
Der Crawler durchsucht die News-Seite der Fakultät für das angegebene Jahr.
Gefundene Artikel werden extrahiert und als DOCX-Dateien im entsprechenden Verzeichnis gespeichert.

#Anmerkungen
Der Crawler berücksichtigt das angegebene Jahr und extrahiert nur Artikel, die im angegebenen Zeitraum veröffentlicht wurden.
Wenn kein Artikeltext vorhanden ist, wird eine entsprechende Meldung ausgegeben.
