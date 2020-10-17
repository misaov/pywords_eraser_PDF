from pdf2image import convert_from_path
from pytesseract import Output
import cv2, pytesseract, argparse, numpy, os


def file_path(filepath):
    '''
    This function checks if a pdf document exists.
    returns: if filepath does exists, it returns the full path of the file.
    '''
    if filepath[-3:] not in 'pdf':
        raise argparse.ArgumentTypeError(
            f"Extension:{filepath[-3:]} is not a valid pdf file")
    if os.path.isfile(filepath):
        return filepath
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{filepath} is not a valid path")


def folder_path(folderpath):
    '''
    This function checks if a folder path is valid.
    returns: if folder_path is valid, it returns the full path.
    '''
    if os.path.isdir(folderpath):
        return folderpath
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{folderpath} is not a valid path")


def draw_rectangle(img, pos):
    '''
    This function takes an image, and draws a rectangle on the given coordinates.
    returns: an image file with censored words.
    '''
    (x, y, w, h) = pos
    return cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)


def data_ret(pdf_page):
    '''
    This function takes a pdf page.
    returns: a tuple of a PIL image Object and the text extraction for the given pdf.
    '''
    open_cv_image = numpy.array(pdf_page)
    return (img := open_cv_image[:, :, ::-1].copy(), pytesseract.image_to_data(img, output_type=Output.DICT))


def word_coords(ocr, index):
    '''
    returns: a coordinate tuple for the given index word.
    '''
    return (ocr['left'][index], ocr['top'][index], ocr['width'][index], ocr['height'][index])


def logic(path, names, makedir, DPI, matchsensitivity):
    pages = convert_from_path(path, DPI)
    # path & filename formating
    dir = path.split('\\')
    filename = dir[-1]
    mkdir = '\\'.join(dir[:-1])+f'\\{filename[:-4]}_results'
    dir = '\\'.join(dir[:-1])

    for n, page in enumerate(pages):
        img, ocr = data_ret(page)
        word_groups, text, reliability = len(
            ocr['text']), ocr['text'], ocr['conf']

        for i in range(word_groups):
            for name in names:
                if name.lower() in text[i].lower() and int(reliability[i]) > matchsensitivity:
                    coords = word_coords(ocr, i)
                    img = draw_rectangle(img, coords)
        if makedir:
            if not os.path.isdir(mkdir):
                os.makedirs(mkdir)
            cv2.imwrite(
                f'{mkdir}\\{filename[:-4]}_Sheet{n+1}_processed.png', img)
            print(
                f'{filename[:-4]}_Sheet{n+1}_processed.png, has been created at {mkdir}')
        else:
            cv2.imwrite(
                f'{dir}\\{filename[:-4]}_Sheet{n+1}_processed.png', img)
            print(
                f'{filename[:-4]}_Sheet{n+1}_processed.png, has been created at {dir}')


def Main(path, names, makedir, folderpath, DPI=30, matchsensitivity=50):
    # If user chose the folderpath argument it will iterate over all pdf files within the folder.
    if folderpath:
        for pdf in os.listdir(folderpath):
            if pdf[-3:] in 'pdf':
                logic(folderpath+'\\'+pdf, names,
                      makedir, DPI, matchsensitivity)
    else:
        logic(path, names, makedir, DPI, matchsensitivity)


if __name__ == "__main__":
    # Command Line arguments:
    parser = argparse.ArgumentParser(description='Command line arguments.')
    group = parser.add_mutually_exclusive_group()
    # name is the default argument, this arg takes one or more names, ej. John Doe / John / John Snow Second
    parser.add_argument(
        'name', nargs='+', help='Type multiple names separated by spaces, these are to be removed from the pdf.')
    # The document path argument takes a full path including the pdf document itself.
    group.add_argument('-d', '--documentpath',
                       help='This option allows the user to directly point to a pdf document.', type=file_path)
    # The folder path argument takes a full path for a folder containing one or multiple pdf documents.
    group.add_argument('-f', '--folderpath',
                       help='This option allows the user to set a path folder to multiple pdf files at once.', type=folder_path)
    # makedir is an argument which takes no value, if this argument is casted then the script will create a folder for each file to place the results into.
    parser.add_argument(
        '-mk', '--makedir', help='This option creates a subfolder (results) under the current file path.', action="store_true")
    args = parser.parse_args()

    # Initializating Main function
    Main(args.documentpath, args.name, args.makedir, args.folderpath)
