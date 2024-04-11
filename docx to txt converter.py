import os
from docx import Document

def list_folders():
    folders = [folder for folder in os.listdir('.') if os.path.isdir(folder) and folder != '.git']
    for i, folder in enumerate(folders):
        print(f'{i+1}. {folder}')
    return folders

def select_folder():
    attempts = 0
    while attempts < 5:
        folder_num = input('Bitte geben Sie die Nummer des Ordners ein, den Sie auswählen möchten (oder "n" zum Beenden): ')
        if folder_num.lower() == 'n':
            print('Beende denn konverter...')
            return None
        try:
            folder_num = int(folder_num)
            folders = list_folders() 
            if folder_num >= 1 and folder_num <= len(folders):
                selected_folder = folders[folder_num - 1]
                print(f'Ausgewählter Ordner: {selected_folder}')
                return selected_folder
            else:
                print('Ungültige Ordner-Nummer. Bitte versuchen Sie es erneut.')
                attempts += 1
        except ValueError:
            print('Ungültige Eingabe. Bitte geben Sie eine Zahl oder "n" zum Abbruch ein.')
            attempts += 1

    print('Zu viele ungültige Versuche. Beende denn Konverter...')
    return None

def list_word_documents(folder):
    word_documents = [file for file in os.listdir(folder) if file.endswith('.docx')]
    for i, document in enumerate(word_documents):
        print(f'{i+1}. {document}')

def create_output_folder(folder):
    output_folder = os.path.join(folder, "Konvertiert zu txt-Dokumente")
    os.makedirs(output_folder, exist_ok=True)
    print('\n\n'+f'Erstelle Ausgabeordner: {output_folder}')
    return output_folder

def convert_word_documents(folder):
    word_documents = [file for file in os.listdir(folder) if file.endswith('.docx')]
    if len(word_documents) == 0:
        print('Der Ordner ist leer.')
        return
    output_folder = create_output_folder(folder)
    print('\nStarte Konvertierung von Word-Dokumenten in Textdateien... \n')  
    counter = 0  # Zähler für konvertierte Dokumente
    for document in word_documents:
        docx_path = os.path.join(folder, document)
        txt_path = os.path.join(output_folder, f"{os.path.splitext(document)[0]}.txt")  # Save txt files in output folder
        try:
            doc = Document(docx_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            counter += 1  # Zähler erhöhen
            print(f"Converted {document} to {os.path.basename(txt_path)}")
        except Exception as e:
            print(f"Failed to convert {document}: {str(e)}")
    print(f"\nAnzahl der konvertierten Dokumente: {counter}")

def main():
    list_folders()
    selected_folder = select_folder()

    if selected_folder is not None:
        list_word_documents(selected_folder)
        convert_word_documents(selected_folder)
        

if __name__ == '__main__':
    main()