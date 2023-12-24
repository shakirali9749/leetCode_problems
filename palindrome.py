def isPalindrome(x):
    if x < 0:
        return False
    digits = list(str(x))
    return digits == digits[::-1]

user_input = int(input('enter digits: '))


print(isPalindrome(user_input))

print("Shakir")
