txt = input('문자열 txt: ')  
ptn = input('문자열 ptn: ')   

c = txt.count(ptn)

if c == 0:                                                  
    print('ptn은 txt에 포함되어 있지 않습니다.')
elif c == 1:                                               
    print('ptn이 txt에 포함되어 있는 인덱스: ', txt.find(ptn))
else:                                                      
    print('ptn이 txt에 포함되어 있는 맨 앞 인덱스: ', txt.find(ptn))
    print('ptn이 txt에 포함되어 있는 맨 끝 인덱스: ', txt.rfind(ptn))