# pywords_eraser_PDF

## Español:

### Descripción:
Este pequeño proyecto fue creado con la finalidad de borrar o censurar palabras dentro de uno o varios documentos escaneados de formato PDF,
utilizando tesseract OCR para la deteccion de palabras y CV2 para marcarlas en el documento.

### Funcionalidad:
La funcionalidad de este script es mediante el CMD, donde se corre el script, con los siguientes argumentos:
* Nombre: Son las palabras o nombres los cuales se busca borrar del documento, cuando se ingresa mas de una palabra, se debera separar por medio de espacios. **Nota**  para correr el script se debera utilizar almenos 1 argumento.
* Ruta de archivo: Al utilizar el argumento ***-d*** se debera especificar la ruta del archivo completa ej. 'C:\user\desktop\carpeta\documento.pdf', este debera contener la extension pdf.
**Nota**  si se utiliza este argumento, no se podra utilizar el argumento de la ruta de carpeta "-f".
* Ruta de carpeta: Al utilizar el argumento ***-f*** se debera especificar la ruta de la carpeta donde se encuentren el o los archivos pdf a procesar, ej. 'C:\user\desktop\carpeta\'.
**Nota** si se utiliza este argumento, no se podra utilizar el argumento de  la ruta de archivo "-d".
* Crear directorio: Al utilizar el argumento ***-mk*** se crearan los documentos dentro de una carpeta dentro de la ruta que fue especificada, la carpeta llevara el nombre de los documentos distinguiendose con la terminación _results.
**Nota** de omitir este argumento, los resultados se crearan dentro de la ruta que fue especificada.

### Instalación:
Para la instalación de este script, se debera contar con las siguientes librerias:
* Pytesseract   /       pip install pytesseract
* Numpy         /       pip install numpy
* OpenCV        /       pip install opencv-python
* pdf2image     /       pip install pdf2image
en el caso de esta ultima libreria se debera de instalar poppler para su funcionamiento, el cual se puede encontrar en el siguiente link: https://github.com/oschwartz10612/poppler-windows/releases/

* **Nota** Hay que asegurarse de agregar a PATH el folder de poppler, como el de tesseract:   
**C:\Program Files\Tesseract-OCR  
**C:\poppler-20.09.0\bin
