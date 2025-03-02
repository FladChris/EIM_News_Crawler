# EIM_News_Crawler

Ein Webcrawler, der Nachrichtenartikel von der Website der Fakultät für Elektrotechnik, Informatik und Mathematik der Universität Paderborn extrahiert und jeden Artikel als separate DOCX-Datei speichert.

[![Release](https://img.shields.io/github/v/release/FladChris/EIM_News_Crawler)](https://github.com/FladChris/EIM_News_Crawler/releases)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Features](#features)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Abhängigkeiten](#abhängigkeiten)
- [Bekannte Probleme und Hinweise](#bekannte-probleme-und-hinweise)
- [Lizenz](#lizenz)

## Überblick

Der **EIM_News_Crawler** wurde entwickelt, um automatisiert Nachrichtenartikel von der Webseite der Fakultät zu extrahieren und sie in einem strukturierten Format (DOCX) zu speichern. Der Crawler filtert dabei Artikel basierend auf einem benutzerdefinierten Jahr und speichert jeden Artikel in einem entsprechenden Jahresverzeichnis.

## Features

- **Automatische Extraktion:** Sucht und extrahiert Artikel, die innerhalb eines vom Benutzer definierten Jahres veröffentlicht wurden.
- **Dokumentenerstellung:** Speichert jeden gefundenen Artikel als DOCX-Datei.
- **Medien und Kontakte:** Unterstützt das Einbinden von Bild-URLs und Kontaktinformationen in die Dokumente.
- **Benutzerfreundlich:** Einfaches Interface über die Kommandozeile, das nach dem gewünschten Jahr fragt.

## Installation

1. **Repository klonen:**  
   ```bash
   git clone https://github.com/FladChris/EIM_News_Crawler.git
   cd EIM_News_Crawler
   ```

2. **Abhängigkeiten installieren:**  
   Stelle sicher, dass Python (Version 3.6 oder höher) installiert ist. Installiere dann die benötigten Pakete über:
   ```bash
   pip install -r requirements.txt
   ```  

## Verwendung

1. **Skript starten:**  
   Führe das Skript über die Kommandozeile aus:
   ```bash
   python EIM_News_Crawler_docx.py
   ```

2. **Jahr eingeben:**  
   Das Programm fordert dich auf, das Jahr der gewünschten Artikel einzugeben. Es wird ein Verzeichnis für dieses Jahr erstellt, falls nicht bereits vorhanden.

3. **Artikel-Crawling:**  
   Der Crawler durchsucht die News-Seite und extrahiert Artikel, die in das eingegebene Jahr fallen. Jeder gefundene Artikel wird mit Datum, Überschrift, Inhalt, Bild-URLs und Kontaktinformationen in eine separate DOCX-Datei gespeichert.

## Abhängigkeiten

Das Skript verwendet folgende Python-Bibliotheken:
- **os:** Verwaltung von Dateien und Verzeichnissen.
- **requests:** HTTP-Anfragen senden und Antworten empfangen.
- **BeautifulSoup (beautifulsoup4):** Extraktion von Daten aus HTML/XML-Dokumenten.
- **htmldocx:** Konvertierung von HTML in DOCX.
- **python-docx:** Erstellung und Bearbeitung von DOCX-Dateien.
- **datetime:** Verarbeitung von Datums- und Zeitangaben.

## Bekannte Probleme und Hinweise

- **Timeout-Probleme:**  
  Unter Umständen kann es zu einem Timeout kommen, wenn das Skript außerhalb des Universitätsnetzwerks ausgeführt wird. In diesem Fall wird empfohlen, per VPN auf das Netzwerk zuzugreifen und das Skript erneut zu starten.
  
- **Fehlende Inhalte:**  
  Falls ein Artikel keinen Text, keine Bilder oder keine Kontaktinformationen enthält, wird eine entsprechende Meldung ausgegeben.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. 