def decToRoman(num):
    coding = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    )
    if num <= 0 or num >= 4000 or int(num) != num:
        raise ValueError('Число должно быть не более 3999')
    result = []
    for d, r in coding:
        while num >= d:
            result.append(r)
            num -= d
    return ''.join(result)

def RomanToDec(strng):
    dec = 0
    strng = strng.upper()
    coding = dict(M=1000, D=500, C=100, L=50, X=10 ,V=5, I=1)
    if not ("I" == strng[-1] or "X" == strng[-1] or "L" == strng[-1] or "C" == strng[-1] or "D" == strng[-1] or "M" == strng[-1]):
        raise ValueError("Не верный формат римского числа")
    for i in range(0, len(strng)-1):
        if not ("I" == strng[i] or "X" == strng[i] or "L" == strng[i] or "C" == strng[i] or "D" == strng[i] or "M" == strng[i]):
            raise ValueError("Не верный формат римского числа")
        if coding[strng[i]] < coding[strng[ i +1]]:
            dec -= coding[strng[i]]
        else:
            dec += coding[strng[i]]
    dec += coding[strng[-1]]
    return dec

print(RomanToDec("MCMXCIXe"))
print(decToRoman(1999))
