def isPalindrome(x):
        if x<0:
            return False
        number=str(x)
        for i in range(0, len(number)):
            if number[i] == number[len(number)-1-i]:
                continue
            else:
                return False
        return True
print(isPalindrome(1211))
