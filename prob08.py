# 문제8.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

def reverse(word):
    result = ''
    size = len(str(word))
    for i in range(0,size):
        print(i)
        result += str(word)[size-1-i]
    return result

print(reverse("Python Programming!Python Programming!"))