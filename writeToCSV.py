import csv
import os


def write_csv(path, data):
    file_path = str(os.getcwd())+"\\"+str(path) 
   
    with open(file_path, "w", newline='', encoding ='cp1251') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        for index, item in enumerate(data):
            writer.writerows([item])
    print(f"Запись файла: {os.path.basename(file_path)} - завершена!\n")
    print("#"*66)
