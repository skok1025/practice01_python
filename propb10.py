#문제10
#숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
num = int(input("숫자를 입력하세요:"))
sum = 0
while True:
    sum += num
    num -= 2
    if num <0 : break

print(sum)