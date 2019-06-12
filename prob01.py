#문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
import sys

num = input('수를 입력하세요:')

num = int(num)

# print(type(num))
num % 3 ==0 and print(num,'은 3의 배수입니다.')
sys.exit(0)