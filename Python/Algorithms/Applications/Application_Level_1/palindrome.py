from builtins import range, len


def is_palindrome(word):
    result = True
    for index in range(int(len(word) / 2)):
        if word[index] != word[-(index + 1)]:
            result = False
    return result


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))