import os
from PIL import Image
import pillow_avif
import png_to_pdf
from utils import getFileName

#### GLOBAL_VAR
##### CONFIG
PATH = r"./"#DEFAULT: r"./"
FROM = "jpg"#please make sure the format you want to convert. DEFAULT: "jpg"
TO = "JPEG"#JPEG,PNG. DEFAULT: "JPEG"
SPLIT= "\\"#"\\" is for Windows. if you are in UNIX system, you should use "/". DEFAULT: "\\"
JPEGQUALITY = 100#0~100. DEFAULT: 100
#####
(FILESNAMES,FILESPATHS) = getFileName(PATH,"."+FROM)
####

def open_save_img(filepath,filename,newFileDir=""):
    img = Image.open(filepath)
    if os.path.isdir(os.path.join(filepath.replace(filename,""),newFileDir)):
        pass
    else:
        os.mkdir(os.path.join(filepath.replace(filename,""),newFileDir))
    newPath = os.path.join(filepath.replace(filename,""),newFileDir,filename.replace("."+FROM,"__temp."+TO.upper()))
    if TO.upper() in ["JPEG","JPG"]:
        if img.mode in ["RGBA","P"]: 
            img = img.convert('RGB')
        img.save(newPath,quality=JPEGQUALITY)
    else:
        img.save(newPath)
    print("saved temp image: ", newPath)
    return newPath

def take_apply(index):#this is for multiprocessing. here I do not use it because it have some problem in my pc.
    return open_save_img(FILESPATHS[index],FILESNAMES[index],"")
    

def main():
    groups = ([x for x in range(0,len(FILESNAMES))])
    paths = {}
    try:
        for i in groups:
            path = take_apply(i)
            spilited_path = os.path.normpath(path).split(SPLIT)
            PDF_name = spilited_path[-2]#this is the PDF's name. Default: -2. It is the dirname of the image.
            if PDF_name in paths:
                paths[PDF_name].append(path)
            else:
                paths[PDF_name]=[]
                paths[PDF_name].append(path)
        for key in paths:
            png_to_pdf.combine_pdf(paths[key],key)
            print("combine to PDF: ", key)
            for f in paths[key]:
                os.remove(f)
                print("remove temp file: ", f)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
