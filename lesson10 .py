import os.path
content = ''
dwc = {}

def Menu ():
    print('1.輸入檔案')
    print('2.單字統計表')
    print('3.查詢檔案中單字')
    print('4.更換檔案中單字')
    print('5.離開系統')
    
    
while True:
    print('Word Counter')
    Menu()
    sel = input('請輸入欲執行的選項：')

    if sel == '1':
        fn = input('請輸入檔名(含副檔名)：')
        if os.path.isfile(fn):
            fo = open(fn,'r')
            content = fo.read()
            print('檔案內容如下:\n', content)
        else:
            print('沒有這個檔案！')
        fo.close()
    
    elif sel == '2':
        if content:
            words = content.split()
            for word in words:
                if word in dwc:
                    dwc[word] = dwc[word]+1
                else:
                    dwc[word] = 1
            print(dwc)
            print('There are', len(words), 'words in the file.')
        else:
            print('No content!!!')

    elif sel == '3':
        word = input('請輸入要查詢的單字：')
        if word in dwc:
            print(word, '在檔案中出現', dwc[word], '次')
        else:
            print('檔案中沒有這個字！')

    elif sel == '4':
        old = input('請輸入要被換掉的單字：')
        new = input('請輸入替代的文字：')
        if old in dwc:
            content = content.replace(old, new)
        print(content)
        fo = open(fn, "w")
        fo.write(content)
        fo.close()

    elif sel == '5':
        break

    else:
        print('錯誤輸入！！！！')