# filePath = '../data/readme.txt'
filePath = '../data/readme.txt'

try:
    f = open(filePath, mode='r', encoding='utf-8')
    f2 = open('../data/writeme.txt', mode='w', encoding='utf-8')
    line = f.read()
    while line:
        print(line)
        f2.write(line)
        line = f.read()
    f2.write('추가　내용입니다')
    print('파일　작성　완료')
    f.close()
    f2.close()
    

except Exception as e:
    print('Exception Occured : {0}'.format(e))

