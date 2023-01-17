import os
def getFileName(path,suffix,current=False):#False including the children files, while True only search the recent file of "path"
    input_template_All=[]
    input_template_All_Path=[]
    if current == False:
        for root, dirs, files in os.walk(path, topdown=True):
            for name in files:
                if os.path.splitext(name)[1] == suffix:
                    input_template_All.append(name)
                    input_template_All_Path.append(os.path.join(root, name))
        return input_template_All,input_template_All_Path
    elif current == True:
        fileList = os.listdir(path)
        for name in fileList:
            if os.path.splitext(name)[1] == suffix:
                input_template_All.append(name)
                input_template_All_Path.append(os.path.join(path, name))
        return (input_template_All,input_template_All_Path)