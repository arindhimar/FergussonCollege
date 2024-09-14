def isPalindrome(tempString):
    newStr = tempString[::-1]
    return tempString == newStr

print(isPalindrome("madam"))