li = list(range(1,101)) # 1~100 리스트 생성
sum3 = 0 # 3의 배수의 합
sum7 = 0 # 7의 배수의 합

for i in li:
    if i%3 == 0:
        sum3 = sum3 + i
    if i%7 == 0:
        sum7 = sum7 + i

print('3의 배수의 합 : {}'.format(sum3))
print('7의 배수의 합 : {}'.format(sum7))
