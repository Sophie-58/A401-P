words = {}
words_num = 0

def build_menu():
    print('功能=>')
    print('1.建立字彙表')
    print('2.列出全部單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習成果')
    print('6.離開系統')

while True:
    build_menu()
    
    sel = input('請輸入欲執行的選項:')
    
    if sel == '1':
        words_num = int(input('請輸入總共要輸入幾個單字：')) 
        print('您要輸入',words_num,'個單字')
        for i in range(words_num):
            key = input('請輸入單字：')
            value = input('請輸入此單字的中文：')
            words [key] = value
        print('目前的字彙表是：',words)
    elif sel == '2':
        print('目前的字彙表是：',words)
    elif sel == '3':
        kw = input('請輸入要查詢的單字：')
        if kw in words:
            print('它的中文是：',words[kw])
        else:
            print('錯誤輸入')
    elif sel == '4':
        booling = True
        vw = input('請輸入要查詢的中文：')
        for keys,values in words.items():
            if vw == values:
                print('它的英文是：',keys)
                booling = False
        if booling == True:
            print('查不到')
    elif sel == '5':
        print('總共有',len(words),'題')
        score = 0
        for keys,values in words.items():
            print(values,':')
            ans = input()
            if ans == keys:
                print("答對了！")
                score = score + 1
            else:
                print('答錯囉！')
        print('你得了',score,'分')
    elif sel == '6':
        break
    else:
        print('錯誤輸入')