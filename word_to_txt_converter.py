"""
Skript in das Verzeichnis legen, wo die Word Datein konvertiert werden sollen
"""

import os
import docx

current_directory = os.getcwd()
new_directory = current_directory + "-txt"  
os.mkdir(new_directory)  # Erstellen eines neuen Ordners mit dem Namen des aktuellen Ordners und der Endung "-txt"

word_files = [f for f in os.listdir(current_directory) if f.endswith(".docx")]

def main(word_files):
    for each_word_file in word_files:
        new_txt_file_name = each_word_file + ".txt"
        with docx.Document(each_word_file) as docx_file:  # Erstellen einer neuen txt-Datei mit dem gleichen Namen wie die Word-Datei