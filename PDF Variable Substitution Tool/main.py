import sys
import os
import PyPDF2
import json
import re 

menus = {
    1: "generate a file",
    2: "Exit"
}

def generate_file_franchise(filename, data):
    pdf_text = extract_pdf_to_text(filename)

    someVariables = re.findall(r'\[(.*?)\]', pdf_text)
    #fix all variabels no space with regex
    fixedVariables = [x.replace(" ", "") for x in someVariables]
    # replace the old variabels with new variabels
    for i in range(len(someVariables)):
        pdf_text = pdf_text.replace(someVariables[i], fixedVariables[i])
    # print(pdf_text)

    for key, value in data.items():
        pdf_text = pdf_text.replace("["+key+"]", str(value))
    # print(pdf_text)

    with open("FILENAME_generated.txt", 'w') as file:
        file.write(pdf_text)
    

def extract_pdf_to_text(filename, void=False):
    pdf_text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(open(filename, 'rb'))

        for page in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page].extract_text()
    except Exception as e:
        print(e)
        return e
    
    return pdf_text


def main():
    folder_path = os.path.dirname(os.path.abspath(__file__)) + "./"
    switcher = {
        1: generate_file_franchise,
        2: exit
    }
    sys.stdout.flush()
    for key, value in menus.items():
        print(key, value)
    choice = int(sys.stdin.readline().strip())
    if choice == 2:
        sys.exit(0)
    else:
        filename = folder_path+sys.stdin.readline().strip()
        # Input filename as an example => FILENAME.pdf
        data_input = sys.stdin.readline().strip()
        # The format data_input is JSON
        data = json.loads(data_input)
        result = switcher[choice](filename, data)

        sys.stdout.write(str(result) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()