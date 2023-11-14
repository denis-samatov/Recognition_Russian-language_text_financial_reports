
import os
import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np



page = [['December', '76,870', '953', '556', '53,353', '24', '38,871', '20,729', '304', '4,369', '-557', '50', '195,521'], ['Year 2018', '', '', '', '', '', '', '', '', '', '', '', ''], ['January', '88,647', '2,359', '', '55,197', '', '39,366', '23,664', '', '4,417', '', '', '214,299'], 
['February,', '61,029', '609', '575', '46,841', '', '33,941', '23,504', '335', '3,931', '-226', '40', '170,598'], ['March', '58,552', '585', '491', '50,592', '', '35,262', '23,793', '453', '4,181', '-408', '49', '173,565'], ['', '55,319', '', '', '48,319', '', '30,580', '25,150', '', '3,869', '', '', '164,609'],
['May', '64,011', '730', '336', '58,571', '', '34,479', '28,051', '490', '3,350', '-309', '47', '189,767'], ['June', '77,886', '747', '670', '65,945', '', '36,437', '25,826', '565', '3,510', '-339', '52', '211,313'], 
['', '88,147', '', '', '82,694', '', '38,293', '21,964', '', '2,721', '', '', '235,250'], ['August', '87,383', '700', '686', '78,287', '24', '38,885', '19,240', '521', '2,972', '-626', '58', '228,131'], ['Sept', '73,136', '763', '639', '68,926', '', '34,377', '16,649', '496', '3,052', '-500', '50', '197,592'],
['October]', '65,038', '', '', '59,631', '', '31,364', '16,703', '', '3,411', '', '', '177,349'], ['November', '69,011', '673', '477', '50,518', '', '33,043', '19,806', '342', '3,552', '-254', '52', '177,220'], ['December', '72,165', '633', '601', '48,783', '', '38,223', '21,130', '300', '4,059', '-426', '51', '185,519']]


# for index,  element in enumerate(page):
#     print(len(element))
#     print(element)
#     print('|||||||||||||||||||||||||||||')
    
def write_csv(path, data):
    os.chdir("table in PNG")
    file_path = str(os.getcwd())+"\\"+str(path)
    print(file_path)

    with open(file_path, "w", newline='', encoding ='cp1251') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        for index, item in enumerate(data):
            writer.writerows([item])
    print("Запись в csv файл завершена!")

'''# write_csv("E:\\Studies\\NN\\project\\table in PNG\\Dec2018-019_page1.csv", page)
# path = 'table_page1.csv'

# png = r"E:\\Studies\\NN\\project\\table in PNG\\fin-analysis-ai-018_page1.png"
png = r"E:\\Studies\\NN\\project\\table in PNG\\fin_page1.png"
raw = cv.imread(png, 1)
gray = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)
binary = cv.adaptiveThreshold(~gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, -5)
# plt.imshow(binary,'gray')
# plt.show()
rows, cols = binary.shape

# Определение горизонтальных линий
scale = 40 # можно поставить значение от 20-60
kernel = cv.getStructuringElement(cv.MORPH_RECT, (cols // scale, 1))
eroded = cv.erode(binary, kernel, iterations=1)
dilated_col = cv.dilate(eroded, kernel, iterations=1)
# plt.imshow(dilated_col,'gray')
# plt.show()

# Определение вертикальных линий
scale = 20 # можно поставить значение от 10-30
kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, rows // scale))
eroded = cv.erode(binary, kernel, iterations=1) 
dilated_row = cv.dilate(eroded, kernel, iterations=1)
# plt.imshow(dilated_row,'gray')
# plt.show()

# Определение пересечений
bitwise_and = cv.bitwise_and(dilated_col, dilated_row) # побитовое И истинно тогда и только тогда, когда оба пикселя больше нуля
# plt.imshow(bitwise_and,'gray')
# plt.show()
print(bitwise_and)

# Идентификационная форма таблицы
merge = cv.add(dilated_col, dilated_row)
# plt.imshow(merge,'gray')
# plt.show()

#  Удаление рамок таблицы
merge2 = cv.subtract(binary, merge)
# plt.imshow(merge2,'gray')
# plt.show()

new_kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
# plt.imshow(new_kernel,'gray')
# plt.show()
erode_image = cv.morphologyEx(merge2, cv.MORPH_OPEN, new_kernel)
# plt.imshow(erode_image,'gray')
# plt.show()
ys, xs= np.where(bitwise_and > 0)
print(ys)
print("///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print(xs)
ys, xs = np.where(bitwise_and > 0)
# Ордината
y_point_arr = []
# Абсцисса
x_point_arr = []

# Путем сортировки получаем значения x и y перехода, указывающие, что это точка пересечения,
# в противном случае в точке пересечения будет много значений пикселей с аналогичными значениями.
# Я беру только последнюю точку аналогичного значения.
# Переход этого 10 не фиксирован. Он будет точно настроен в соответствии с различными изображениями.
# В основном это высота (переход по координате y) и длина (переход по координате x) таблицы ячеек.
i = 0
sort_x_point = np.sort(xs)
for i in range(len(sort_x_point) - 1):
    if sort_x_point[i + 1] - sort_x_point[i] > 10:
        x_point_arr.append(sort_x_point[i])
    i = i + 1
x_point_arr.append(sort_x_point[i])  # Чтобы добавить последнюю точку

i = 0
sort_y_point = np.sort(ys)
for i in range(len(sort_y_point) - 1):
    if (sort_y_point[i + 1] - sort_y_point[i] > 10):
        y_point_arr.append(sort_y_point[i])
    i = i + 1
y_point_arr.append(sort_y_point[i]) # Чтобы добавить последнюю точку

print('Список координат x', x_point_arr)
print('Список координат y', y_point_arr)

# Циклическая таблица разделения координат y координат x
data = [[] for i in range(len(y_point_arr))]
print(data)
# import pytesseract
# def ocr_core(filename): 
#     pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#     text = pytesseract.image_to_string(filename, lang="rus")
#     return text

# info = ocr_core(binary)

# write_csv("fin-analysis-ai-002_page1.csv", info)
'''

# Сравнение методов бинаризации

# png = r"E:\\Project python\\OpenCV\\1.jfif"
# raw = cv.imread(png, 1)
# gray = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)
# binary = cv.adaptiveThreshold(~gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, -5)
# plt.imshow(binary,'gray')
# plt.show()

# ret1,thresh1 = cv.threshold(~gray, 127, 255, cv.THRESH_BINARY)  
# print(ret1)
# plt.imshow(thresh1,'gray')
# plt.show()

# ret2,thresh2 = cv.threshold(~gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# print(ret2)
# plt.imshow(thresh2,'gray')
# plt.show()

# Расчет точности работы алгоритма
a = {'1': 1234, '2': 512, '3': 1200,'4': 933,'5': 401,'6': 388,'7': 714,'8': 1458,'9': 443,'10': 675,'11': 885,'12': 150,'13': 679,'14': 542,'15': 308,'16': 425,'17': 1091,'18': 2028,'19': 678,'20': 702}
b = {'1': 1161,'2': 496,'3': 1111,'4': 867,'5': 390,'6': 273,'7': 706,'8': 1148,'9': 443,'10': 622,'11': 828,'12': 126,'13': 670,'14': 541,'15': 108,'16': 346,'17': 1008,'18': 2028,'19': 663,'20': 686}
c =[]

# for i, j in zip(a, b):
#     c.append(i-j)
# print(c)

# a1 = sum(a)
# c1 = sum(c)

# print(a1)
# print(c1)
# print((a1-c1)/a1*100)


# a = [34.48, 66.02, 98.35, 131.12]
# b = [5 ,10, 15, 20]
# c =[]

# for i, j in zip(a, b):
#     c.append(i/j)
# print(c)
print((92.3+93.5+90.2+92.1)/4)




import fitz
import os


def convert_pdf2png(input_file: str):
    '''Преобразует PDF в изображение и создает файлы для кажной страницы'''
    
    output_files = []
    with fitz.open(input_file) as doc:  
        for pg in range(doc.page_count):
            page = doc[pg]
            zoom_x = 2
            zoom_y = 2
            rotate = int(0)
            mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pix = page.get_pixmap(matrix = mat, alpha = False)

            if not os.path.isdir("table in PNG"):
                os.mkdir("table in PNG")

            output_file = f"{os.path.splitext(os.path.basename(input_file))[0]}_page_{pg+1}.png"
            pix.save(output_file)
            os.replace(output_file, f"{os.getcwd()}\\table in PNG\\{output_file}")
            output_files.append(output_file)

        report = {
            "Исходный файл": os.path.basename(input_file),
            "Количество страниц": str(doc.page_count),
            "Выходной файл(-ы)": str(output_files)
        }

    print("########################### Файл создан ###########################")
    print("\n".join("{}: {}".format(key, value) for key, value in report.items()))
    print("##################################################################")

    os.chdir("table in PNG") 

    return output_files


    import matplotlib.pyplot as plt
import cv2
import numpy as np
import pytesseract
import re


def parse_img_to_csv_data(src):   

    raw = cv.imread(src, 1)
    
    # Изображение в оттенках серого
    gray = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)

    # Бинаризация
    binary = cv.adaptiveThreshold(~gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, -5) # выбрать пятый параметр 21
    # plt.imshow(binary,'gray')
    # plt.show()
    rows, cols = binary.shape
    
    # Определение горизонтальных линий
    scale = 40 # можно поставить значение от 20-60
    mask = cv.getStructuringElement(cv.MORPH_RECT, (cols // scale, 1))
    eroded = cv.erode(binary, mask, iterations=1)
    dilated_col = cv.dilate(eroded, mask, iterations=1)
    # plt.imshow(dilated_col,'gray')
    # plt.show()

    # Определение вертикальных линий
    scale = 20 # можно поставить значение от 10-30
    mask = cv.getStructuringElement(cv.MORPH_RECT, (1, rows // scale))
    eroded = cv.erode(binary, mask, iterations=1) 
    dilated_row = cv.dilate(eroded, mask, iterations=1)
    # plt.imshow(dilated_row,'gray')
    # plt.show()

    # Определение пересечений
    bitwise_and = cv.bitwise_and(dilated_col, dilated_row) # побитовое И истинно тогда и только тогда, когда оба пикселя больше нуля
    # plt.imshow(bitwise_and,'gray')
    # plt.show()

    # # Идентификационная форма таблицы
    # merge = cv.add(dilated_col, dilated_row) # по факту ненужная вещь
    # # plt.imshow(merge,'gray')
    # # plt.show()

    # # Удаление рамок таблицы
    # merge2 = cv.subtract(binary, merge) # по факту ненужная вещь
    # # plt.imshow(merge2,'gray')
    # # plt.show()

    # new_kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2)) # по факту ненужная вещь
    # erode_image = cv.morphologyEx(merge2, cv.MORPH_OPEN, new_kernel)
    # # plt.imshow(erode_image,'gray')
    # # plt.show()

    # merge3 = cv.add(erode_image, bitwise_and) # по факту ненужная вещь
    # # plt.imshow(merge3,'gray')
    # # plt.show()

    # Определение белых пересечений на черно-белом изображении и выведение горизонтальных и вертикальных координат
    y_point, x_point = np.where(bitwise_and > 0)
    # Ордината
    y_point_arr = []
    # Абсцисса
    x_point_arr = []

    # Путем сортировки получаем значения x и y перехода, указывающие, что это точка пересечения, в противном случае в точке пересечения будет много значений пикселей с аналогичными значениями. Я беру только последнюю точку аналогичного значения.
    # Переход этого 10 не фиксирован. Он будет точно настроен в соответствии с различными изображениями. В основном это высота (переход по координате y) и длина (переход по координате x) таблицы ячеек.
    i = 0
    sort_x_point = np.sort(x_point)
    for i in range(len(sort_x_point) - 1):
        if sort_x_point[i + 1] - sort_x_point[i] > 10:
            x_point_arr.append(sort_x_point[i])
        i = i + 1
    x_point_arr.append(sort_x_point[i])  # Чтобы добавить последнюю точку

    i = 0
    sort_y_point = np.sort(y_point)
    for i in range(len(sort_y_point) - 1):
        if (sort_y_point[i + 1] - sort_y_point[i] > 10):
            y_point_arr.append(sort_y_point[i])
        i = i + 1
    y_point_arr.append(sort_y_point[i]) # Чтобы добавить последнюю точку
    
    # print("Список координат x", x_point_arr)
    # print("Список координат y", y_point_arr)
    
    # Циклическая таблица разделения координат y и координат x
    data = [[] for i in range(len(y_point_arr))]
    for i in range(len(y_point_arr) - 1):
        for j in range(len(x_point_arr) - 1):

            # При делении первым параметром является координата y, а вторым параметром - координата x
            cell = raw[y_point_arr[i]:y_point_arr[i + 1], x_point_arr[j]:x_point_arr[j + 1]]
            # plt.imshow(cell)
            # plt.show()

            # Считывает информацию с ячейки
            pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
            text = pytesseract.image_to_string(cell, lang="rus")

            # Удалить специальные символы
            text = re.findall(r'[^\*"$@&/?\\|<>~`″′‖{}!#〈\n]', text, re.S)
            text = "".join(text)
            # print("Информация о изображении ячейки：" + text)
            data[i].append(text)
            j = j + 1
        i = i + 1

    return data


import cv2 as cv
import numpy as np
import pytesseract
import re


def parse_img_to_csv_data(src):   

    raw = cv.imread(src, 1)
    
    gray = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(~gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, -5)
    
    rows, cols = binary.shape
    
    scale = 40 
    mask = cv.getStructuringElement(cv.MORPH_RECT, (cols // scale, 1))
    eroded = cv.erode(binary, mask, iterations=1)
    dilated_col = cv.dilate(eroded, mask, iterations=1)

    scale = 20 
    mask = cv.getStructuringElement(cv.MORPH_RECT, (1, rows // scale))
    eroded = cv.erode(binary, mask, iterations=1) 
    dilated_row = cv.dilate(eroded, mask, iterations=1)

    bitwise_and = cv.bitwise_and(dilated_col, dilated_row) 

    y_point, x_point = np.where(bitwise_and > 0)
    y_point_arr = []
    x_point_arr = []
    
    i = 0
    sort_x_point = np.sort(x_point)
    for i in range(len(sort_x_point) - 1):
        if sort_x_point[i + 1] - sort_x_point[i] > 10:
            x_point_arr.append(sort_x_point[i])
        i = i + 1
    x_point_arr.append(sort_x_point[i]) 

    i = 0
    sort_y_point = np.sort(y_point)
    for i in range(len(sort_y_point) - 1):
        if (sort_y_point[i + 1] - sort_y_point[i] > 10):
            y_point_arr.append(sort_y_point[i])
        i = i + 1
    y_point_arr.append(sort_y_point[i]) 

    data = [[] for i in range(len(y_point_arr))]
    for i in range(len(y_point_arr) - 1):
        for j in range(len(x_point_arr) - 1):

            cell = raw[y_point_arr[i]:y_point_arr[i + 1], x_point_arr[j]:x_point_arr[j + 1]]
            
            pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
            text = pytesseract.image_to_string(cell, lang="rus")

            text = re.findall(r'[^\*"$@&/?\\|<>~`″′‖{}!#〈\n]', text, re.S)
            text = "".join(text)
            data[i].append(text)
            j = j + 1
        i = i + 1

    return data

