from PDF2PNG import convert_pdf2png
from recognition import parse_img_to_csv_data
from writeToCSV import write_csv


if __name__ == "__main__":

    input_file = str(input("Введите путь файла: "))
    if ".pdf" in input_file:
        new_input_file = input_file.replace("\\", "\\\\")
        files = convert_pdf2png(new_input_file)
        for file in files:
            data = parse_img_to_csv_data(file)
            # print(data)
            write_csv(file.replace(".png", ".csv"), data)
            
    elif ".png" in input_file:
        new_input_file = input_file.replace("\\", "\\\\")
        data = parse_img_to_csv_data(new_input_file)
        # print(data)
        write_csv(new_input_file.replace(".png", ".csv"), data)
    else:
        print("Файл с данным форматом не поддерживается. Используйте PNG или PDF.")  


