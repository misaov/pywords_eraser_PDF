from pdf2image import convert_from_path
from pytesseract import Output
import cv2,pytesseract,argparse,numpy,os

def file_path(filepath):
    if filepath[-3:] not in 'pdf':
        raise argparse.ArgumentTypeError(f"Extension:{filepath[-3:]} is not a valid pdf file")
    if os.path.isfile(filepath):
        return filepath
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{filepath} is not a valid path")

def folder_path(folder_path):
    if os.path.isdir(folder_path):
        return folder_path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{folder_path} is not a valid path")


def draw_rectangle(img, pos):
    (x,y,w,h) = pos
    return cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)


def data_ret(pdf_page):
    open_cv_image = numpy.array(pdf_page) 
    return (img := open_cv_image[:, :, ::-1].copy(), pytesseract.image_to_data(img, output_type=Output.DICT))


def word_coords(ocr, index):
    return (ocr['left'][index], ocr['top'][index], ocr['width'][index], ocr['height'][index])


def logic(path, names, makedir, DPI, matchsensitivity):
    pages = convert_from_path(path, DPI)
    dir = path.split('\\')
    filename = dir[-1]
    mkdir = '\\'.join(dir[:-1])+f'\\{filename[:-4]}_results'
    dir = '\\'.join(dir[:-1])

    for n,page in enumerate(pages):
        img, ocr = data_ret(page)
        word_groups, text, reliability = len(ocr['text']), ocr['text'], ocr['conf']

        for i in range(word_groups):
            for name in names:
                if name in text[i] and int(reliability[i]) > matchsensitivity:
                    coords = word_coords(ocr, i)
                    img = draw_rectangle(img, coords)
        if makedir:
            if not os.path.isdir(mkdir):
                os.makedirs(mkdir)
            cv2.imwrite(f'{mkdir}\\{filename[:-4]}_Sheet{n+1}_processed.png', img)
            print(f'{filename[:-4]}_Sheet{n+1}_processed.png, has been created at {mkdir}')
        else:
            cv2.imwrite(f'{dir}\\{filename[:-4]}_Sheet{n+1}_processed.png', img)
            print(f'{filename[:-4]}_Sheet{n+1}_processed.png, has been created at {dir}')
        

def Main(path, names, makedir, folderpath, DPI=30, matchsensitivity = 50):
    if folderpath:
        for pdf in os.listdir(folderpath):
            if pdf[-3:] in 'pdf':
                logic(folderpath+'\\'+pdf, names, makedir, DPI, matchsensitivity)
    else:
        logic(path, names, makedir, DPI, matchsensitivity)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Command line arguments.')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('name', nargs='+', help='Type multiple names separated by spaces, these are to be removed from the pdf.')
    group.add_argument('-d','--documentpath', help='This option allows the user to directly point to a pdf document.', type=file_path)
    group.add_argument('-f','--folderpath', help='This option allows the user to set a path folder to multiple pdf files at once.', type=folder_path)
    parser.add_argument('-mk','--makedir', help='This option creates a subfolder (results) under the current file path.', action="store_true")
    args = parser.parse_args()
    
    
    Main(args.documentpath, args.name, args.makedir, args.folderpath)



