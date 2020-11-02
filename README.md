# pywords_eraser_PDF

## Español:

### Descripción:
Este pequeño proyecto fue creado con la finalidad de borrar o censurar palabras dentro de uno o varios documentos escaneados de formato PDF,
utilizando tesseract OCR para la detección de palabras y CV2 para marcarlas en el documento.

### Funcionalidad:
La funcionalidad de este script es mediante el CMD, donde se corre el script, con los siguientes argumentos:
* Nombre: Son las palabras o nombres los cuales se busca borrar del documento, cuando se ingresa mas de una palabra, se deberá separar por medio de espacios. **Nota**  para correr el script se deberá utilizar al menos 1 argumento.
* Ruta de archivo: Al utilizar el argumento ***-d*** se deberá especificar la ruta del archivo completa ej. 'C:\user\desktop\carpeta\documento.pdf', este deberá contener la extension pdf.
**Nota**  si se utiliza este argumento, no se podrá utilizar el argumento de la ruta de carpeta "-f".
* Ruta de carpeta: Al utilizar el argumento ***-f*** se deberá especificar la ruta de la carpeta donde se encuentren el o los archivos pdf a procesar, ej. 'C:\user\desktop\carpeta\'.
**Nota** si se utiliza este argumento, no se podrá utilizar el argumento de  la ruta de archivo "-d".
* Crear directorio: Al utilizar el argumento ***-mk*** se crearán los documentos dentro de una carpeta dentro de la ruta que fue especificada, la carpeta llevara el nombre de los documentos distinguiéndose con la terminación _results.
**Nota** de omitir este argumento, los resultados se crearán dentro de la ruta que fue especificada.

### Capturas:
![paso1](https://user-images.githubusercontent.com/50644210/96350020-ecce6000-1078-11eb-9abf-26b10fdc7fc9.png)
![paso2](https://user-images.githubusercontent.com/50644210/96350083-5484ab00-1079-11eb-8b62-0f3e2020914e.png)
![paso3](https://user-images.githubusercontent.com/50644210/96350081-5189ba80-1079-11eb-9ecb-bf2f228cd17e.png)
![paso4](https://user-images.githubusercontent.com/50644210/96350082-52225100-1079-11eb-9dd8-d8817ef262e6.png)

### Instalación:
Para la instalación de este script, se deberá contar con las siguientes librerías:
* Pytesseract   /       pip install pytesseract
* Numpy         /       pip install numpy
* OpenCV        /       pip install opencv-python
* pdf2image     /       pip install pdf2image
en el caso de esta última líbreria se deberá de instalar poppler para su funcionamiento, el cual se puede encontrar en el siguiente link: https://github.com/oschwartz10612/poppler-windows/releases/

* **Nota** Hay que asegurarse de agregar a PATH el folder de poppler, como el de tesseract:   
**C:\Program Files\Tesseract-OCR  
**C:\poppler-20.09.0\bin

** Se debe de instalar las librerias indicadas para el idioma español, estas pueden ser encontradas en https://github.com/tesseract-ocr/tessdata/blob/master/spa.traineddata
estas se deberan colocar en la carpeta de C:\Program Files\Tesseract-OCR\tessdata
