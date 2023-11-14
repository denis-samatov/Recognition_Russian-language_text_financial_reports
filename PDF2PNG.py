import fitz
import os


def convert_pdf2png(input_file: str):
    '''Преобразует PDF в изображение и создает файл за страницей'''
    
    output_files = []
    # Открытие документа
    with fitz.open(input_file) as doc:  
        # Полистаем страницы
        for pg in range(doc.page_count):
            # Выберем страницу
            page = doc[pg]
            # PDF Страница конвертируется в целое изображение 1056 * 816, а затем для каждого изображения делается снимок экрана.
            # zoom = 1.33333333 -----> Размер изображения = 1056 * 816
            # zoom = 2 ---> 2 * Разрешение по умолчанию (текст четкий, текст изображения плохо читается) = маленький размер файла/размер изображения = 1584 * 1224
            # zoom = 4 ---> 4 * Разрешение по умолчанию (текст четкий, текст изображения плохо читается) = большой размер файла
            # zoom = 8 ---> 8 * Разрешение по умолчанию (текст четкий, текст изображения читается) = большой размер файла
            zoom_x = 2
            zoom_y = 2
            # Pre-rotate - это вращеие при необходимости.
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
    # Краткое описание печати
    print("########################### Файл создан ###########################")
    print("\n".join("{}: {}".format(key, value) for key, value in report.items()))
    print("##################################################################")

    os.chdir("table in PNG") 

    return output_files