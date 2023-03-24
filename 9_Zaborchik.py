def zaborchik(s):
    result = ""
    last = False  

    for i in range(len(s)):
        if s[i].isalpha():
            if last:
                result += s[i].lower()
            else:
                result += s[i].upper()
            last = not last
        else:
            result += s[i]

    return result

s = input("Введите строку: ")
result = zaborchik(s)
print(result)