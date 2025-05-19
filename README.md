# EIM_News_Crawler

Ein Webcrawler, der Nachrichtenartikel von der Website der Fakultät für Elektrotechnik, Informatik und Mathematik der Universität Paderborn extrahiert und jeden Artikel als separate DOCX-Datei speichert.

[![Release](https://img.shields.io/github/v/release/FladChris/EIM_News_Crawler)](https://github.com/FladChris/EIM_News_Crawler/releases)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Inhaltsverzeichnis

- [EIM\_News\_Crawler](#eim_news_crawler)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Überblick](#überblick)
  - [Features](#features)
  - [Installation](#installation)
  - [Verwendung](#verwendung)
  - [Abhängigkeiten](#abhängigkeiten)
  - [Bekannte Probleme und Hinweise](#bekannte-probleme-und-hinweise)
  - [Lizenz](#lizenz)

## Überblick

Der **EIM_News_Crawler** durchsucht automatisiert die News-Seite der Fakultät und speichert Artikel, die in einem benutzerdefinierten Jahr veröffentlicht wurden, als strukturierte DOCX-Dokumente.

## Features

- **Jahresfilter:** Extrahiert nur Artikel eines vom Benutzer eingegebenen Jahres.
- **DOCX-Erstellung:** Konvertierung von HTML-Inhalten in DOCX mit Bildern und Kontaktinfos.
- **Einfaches CLI-Interface:** Fragt über die Kommandozeile nach dem Zieljahr.
- **Modularer Code:** Leicht erweiterbare Struktur durch Helper-Funktionen.

## Installation

1. **Repository klonen:**  
   ```bash
   git clone https://github.com/FladChris/EIM_News_Crawler.git
   cd EIM_News_Crawler
   ```

2. **Virtuelle Umgebung (optional):**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

3. **Abhängigkeiten installieren:**  
   Erstelle oder passe die `requirements.txt` an und installiere:
   ```text
   requests==2.28.2
   beautifulsoup4==4.11.1
   python-docx==0.8.11
   htmldocx==0.1.7
   ```
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

1. **Skript ausführen:**  
   ```bash
   python EIM_News_Crawler_docx.py
   ```

2. **Jahr eingeben:**  
   Folge der Aufforderung und gib das gewünschte Jahr (z. B. `2024`) ein.

3. **Ergebnisse:**  
   Für das eingegebene Jahr wird ein Verzeichnis angelegt, und alle gefundenen Artikel werden darin als `YYYY-MM-DD_slug.docx` abgespeichert.

## Abhängigkeiten

Das Skript nutzt folgende externe Bibliotheken:

- `requests` (HTTP-Anfragen)
- `beautifulsoup4` (HTML-Parsing)
- `python-docx` (Erstellung von DOCX-Dateien)
- `htmldocx` (Konvertierung HTML → DOCX)

## Bekannte Probleme und Hinweise

- **Timeout & Netzwerkzugriff:**  
  Außerhalb des Universitätsnetzwerks kann es zu Timeouts kommen. VPN-Zugriff auf das Uni-Netz kann helfen.
- **Fehlende Inhalte:**  
  Artikel ohne Text, Bilder oder Kontaktinfos werden entsprechend markiert.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.
