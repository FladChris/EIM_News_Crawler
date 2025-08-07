
# EIM_News_Crawler

A web crawler that extracts news articles from the website of the Faculty of Electrical Engineering, Computer Science and Mathematics at Paderborn University and saves each article as a separate DOCX file.

[![Release](https://img.shields.io/github/v/release/FladChris/EIM_News_Crawler)](https://github.com/FladChris/EIM_News_Crawler/releases)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Table of Contents

- [EIM_News_Crawler](#eim_news_crawler)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Dependencies](#dependencies)
  - [Known Issues and Notes](#known-issues-and-notes)
  - [License](#license)

## Overview

The **EIM_News_Crawler** automatically scans the faculty’s news page and saves articles published in a user-defined year as structured DOCX documents.

## Features

- **Year filter:** Extracts only articles from a year specified by the user.
- **DOCX creation:** Converts HTML content to DOCX, including images and contact information.
- **Simple CLI interface:** Prompts for the target year via the command line.
- **Modular code:** Easily extensible structure through helper functions.

## Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/FladChris/EIM_News_Crawler.git
   cd EIM_News_Crawler
  

2. **Virtual environment (optional):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   

3. **Install dependencies:**
   Create or adjust `requirements.txt` and install:

   ```text
   requests==2.28.2
   beautifulsoup4==4.11.1
   python-docx==0.8.11
   htmldocx==0.1.7
   ```

   ```bash
   pip install -r requirements.txt
   

## Usage

1. **Run the script:**

   ```bash
   python EIM_News_Crawler_docx.py
   ```

2. **Enter the year:**
   Follow the prompt and enter the desired year (e.g., `2024`).

3. **Results:**
   A directory is created for the entered year, and all found articles are saved inside it as `YYYY-MM-DD_slug.docx`.

## Dependencies

The script uses the following external libraries:

* `requests` (HTTP requests)
* `beautifulsoup4` (HTML parsing)
* `python-docx` (DOCX file creation)
* `htmldocx` (HTML → DOCX conversion)

## Known Issues and Notes

* **Timeout & network access:**
  Accessing from outside the university network can lead to timeouts. Using a VPN connection to the university network may help.
* **Missing content:**
  Articles without text, images or contact information are flagged accordingly.

## License

This project is licensed under the MIT License.


