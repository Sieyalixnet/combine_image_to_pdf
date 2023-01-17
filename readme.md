# README说明书

**THIS README FILE IS IN CHINESE IF YOU WANT TO READ ENGLISH VERSION PLEASE TRANSLATE IT OR WAIT THE readme_en.md**

## 目的说明

本小程序可以直接把图片转换后，按文件名顺序合成为pdf。期间可对图片格式进行转换/压缩。至少支持`jpg`(`jpeg`)、`png`和`avif`。
为了简单易用，配有相应的bat，可以直接运行。
使用的是MIT证书。

## 使用流程

1. 下载并安装python。

2. 打开`install.bat`进行依赖安装(请打开管理员模式)。您也可以使用`pip install -r ./requirement.txt`进行安装(请确保安装python后重新打开命令行工具，并使用`cd`命令到达本文件夹内)。**这个步骤可能会遇到问题，请最好用`pip install...`方法来安装，请参考文末的处理方法。**

3. (可选)直接打开`run.bat`，您可以看到其自动把本文件夹下的`combine_image_to_pdf/test/test_jpg_book`合成为`combine_image_to_pdf/test_jpg_book.pdf`。

4. 如果您要把`jpg`合并成`pdf`，请直接把文件复制到本文件夹下，路径为`"combine_image_to_pdf/pdf书名/01.jpg", "combine_image_to_pdf/pdf书名/02.jpg"`(书名可以为任意字符，但务必保证在系统文件顺序读取时，书页号是正确的)。并运行`run.bat`。请参考`test`内的文件路径。若已完成您需要的目标，请忽略下列步骤。

5. 如果您要把其他图片格式，比如`avif`合成为`pdf`，请使用`Visual Studio Code`(等文本编辑软件，请勿使用微软的notepad即记事本)打开`avif_to_png.py`文件，对配置进行定制，主要修改`#####CONFIG`内的内容：

```python
#### GLOBAL_VAR
##### CONFIG
PATH = r"./"
FROM = "jpg"#please make sure the format you want to convert
TO = "JPEG"#JPEG,PNG
SPLIT= "\\"#"\\" is for Windows. if you are in UNIX system, you should use "/"
JPEGQUALITY = 100#0~100
#####
####
```

- `PATH`是需要转换的地址，会遍历所有子文件夹及其文件。默认在本文件夹下。您可以修改为需要的文件夹内，比如`PATH=r"F:/temp/"`。请参考本文件夹下的`test`内的文件路径。
- `FROM`是需要转换的文件格式，若文件不是本文件格式，则不会被读取。请注意，`jpg`、`jpeg`是不同的格式，并请注意大小写。这里至少支持`png`、`jpg`和`avif`。具体支持格式可以到`pillow`查看。若要修改，则应当为`FROM = "avif"`。
- `TO`是转换到目标的图片文件格式，为了多端都能看到该pdf文件的图片，请优先选择`JPEG`或`PNG`。
- `SPLIT`是文件分割符，如果是`Windows`，则无需理会该项。如果是UNIX(比如`MacOS`或`Linux`)，则应当使用`SPLIT = "/"`，但暂未测试。
- `JPEGQUALITY`是如果是`TO`(目标图片文件格式)为`JPEG`情况下有效。可填写`0`至`100`的整数值，`100`是最高的图片质量，但相应的合成后的`pdf`会非常大。

    定制完成后，请**保存**该文件。

6. 运行`run.bat`，或使用`python ./avif_to_png.py`进行运行(请确保安装python后重新打开命令行工具，并使用`cd`命令到达本文件夹内)。

## 文件说明

您可以自己定制相应的文件。

- `test` 测试的图片，用`jpg`和`png`两种图片
- `utils.py`本文件只有一个函数，遍历对应格式的子文件夹和文件。
- `png_to_pdf.py`本文件函数主要是把图片文件转换为`pdf`文件。
- `avif_to_png.py`主文件，有全局变量。`open_save_img`把图片打开并保存为目标图片格式。`main`则是主要的流程。其先会遍历获取符合条件的图片文件，转换到对应的目标图片格式，等全部转换图片完成后，会合成为`pdf`，最后把途中自动生成的过度图片进行删除。

## 某些步骤可能遇到的问题

### 步骤2可能遇到的问题及解决方法

这一个步骤可能会出现问题(因为打开管理员模式下,cmd当前会直接会直接到系统目录下)，以下两种解决方法:

方法1.按下win键弹出的应用搜索中，搜索`命令提示符`，右键，点击`以管理者员身份运行`。然后逐行输入并以回车键确认:

```shell
pip install Pillow==9.4.0
pip install pillow-avif-plugin==1.3.1
pip install img2pdf==0.4.4
pip install PyPDF2[full]
```

方法2.假设该文件夹在`F:/download/combine_image_to_pdf-master/`。按下win键弹出的应用搜索中，搜索`命令提示符`，右键，点击`以管理者员身份运行`，在逐行输入并回车确认

```shell
cd F:/download/combine_image_to_pdf-master/
install.bat
```

假如下载/安装速度异常缓慢，您可能需要一些方法让上外网速度更快一些。

## 未来可能更新

- 原本打算做成命令行CLI，未来会添加。
- 测试更多的图片。
- 会制作前端软件进行更好使用。