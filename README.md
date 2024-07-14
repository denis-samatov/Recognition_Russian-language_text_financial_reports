# Recognition of Russian-language Text in Financial Reports Using Neural Networks

## PDF to CSV Converter

This Python script is designed to convert PDF and PNG files containing tables into CSV format. The process involves the following steps:

1. **Convert PDF to PNG:**
   - If the input file is a PDF, the script converts each page of the PDF into a PNG image.
   - If the input file is a PNG, the script directly uses the provided PNG file.

2. **Recognize Tables and Convert to CSV:**
   - The converted PNG files are processed to extract tabular data using image processing techniques.
   - The extracted data is then written to a CSV file.

## Implementation Details

The primary idea behind reading data from a table is to determine the coordinates of its cells. This allows for isolating each cell from the entire image, reading the information from it, and recording the data in a file. For implementation, OpenCV-Python and the Python-Tesseract (PyTesseract) library, a wrapper for the Google Tesseract-OCR Engine, are mainly used. Additionally, libraries such as Matplotlib and CSV are used. Matplotlib is for data visualization, and CSV is for writing recognized information to an Excel file.

### Workflow:

1. **Loading the Table:**
   - Input data can be in PDF or PNG format.
   - The program processes only files with PDF and PNG extensions. If the format is not supported, it displays the message: "File format not supported. Please use PNG or PDF."

2. **Loading and Filtering the Image:**
   - PyMuPDF is used to convert PDF files to PNG.
   - The `cv2.imread()` function from OpenCV is used to read PNG files.
   - Preprocessing the image includes converting it to grayscale and applying adaptive binarization using OpenCV.

   ```python
   gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
   binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)
   ```

   - These steps ensure the accuracy of contour and text recognition.

   <div align="center">
       <img src="https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports/blob/main/image_1.png" alt="Table Image">
   </div>

3. **Defining Table Contours:**
   - The result of filtering is a binary image that allows applying morphological operations.
   - A structuring element is created for morphological operations, including erosion and dilation.
   - Horizontal and vertical lines of the table are defined using these operations.
   - Intersections of lines are determined using bitwise AND operations.

   ```python
   scale = 40
   mask = cv2.getStructuringElement(cv2.MORPH_RECT, (cols // scale, 1))
   eroded = cv2.erode(binary, mask, iterations=1)
   dilated_col = cv2.dilate(eroded, mask, iterations=1) 
   ```

   ```python
   scale = 20
   mask = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows // scale))
   eroded = cv2.erode(binary, mask, iterations=1) 
   dilated_row = cv2.dilate(eroded, mask, iterations=1)
   ```

   - Results are shown in the figures below:

   <div align="center">
       <img src="https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports/blob/main/image_2.png" alt="Horizontal Table Lines">
       <img src="https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports/blob/main/image_3.png" alt="Vertical Table Lines">
   </div>

   - The coordinates of the intersections are determined and sorted.

4. **Identifying Cell Coordinates:**
   - After defining the table contours, binary operations are used to find intersections of vertical and horizontal lines.
   - The bitwise AND operation using the `cv2.bitwise_and()` function determines the white intersections on the black-and-white image.
   - The coordinates of the intersections are determined using the NumPy library.

   ```python
   bitwise_and = cv2.bitwise_and(dilated_col, dilated_row)
   y_point, x_point = np.where(bitwise_and > 0)
   ```

   - The coordinates are sorted to determine the intersection points.

   ```python
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
   ```

   - The transition parameter (10 in this case) may need adjustment based on table characteristics.

<div align="center">
    <img src="https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports/blob/main/image_4.png" alt="Accuracy Measurements">
</div>

## Accuracy Evaluation

The accuracy of the program is evaluated by comparing the results obtained by the program with manual data entry. The accuracy is assessed based on the following parameters:

1. **Determine the total number of characters in the table (n_total) and the number of errors (n_errors):**
   - Calculate the total number of characters in the table and the number of recognition errors.

2. **Calculate recognition accuracy using the formula:**

$$
\eta = \left( \frac{n_{total} - n_{errors}}{n_{total}} \right) \times 100\%
$$


### Conducting the Accuracy Study

The accuracy study is conducted on data collected from the methodological material "Analysis of Financial and Economic Activities." Several recognition attempts were made with an increasing number of pages. In addition to recognition accuracy, the recognition time for one page with a table (\(t_page\)) is calculated using the formula:

$$
t_{page} = \frac{t_{total}}{N}
$$


where \(N\) is the number of recognized pages with a table, and \(t_total\) is the total recognition time for all pages.

<div align="center">
    <img src="https://github.com/denis-samatov/Recognition_Russian-language_text_financial_reports/blob/main/image_5.png" alt="Accuracy Measurements">
</div>

### Additional Notes:

- It is important to adjust the image preprocessing parameters according to the characteristics of your tables.

## Disclaimer

This script is provided "as is." The results may vary depending on the nature and complexity of the tables in the input files. It is recommended to carefully review the generated CSV files for accuracy before using them.
