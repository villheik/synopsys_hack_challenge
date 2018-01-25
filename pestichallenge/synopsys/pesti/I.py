# Cipher via character set mirroring. Translate A->Z -> Z->A and 0-9 -> 9-0
#
# Example: "ABCXYZ012" -> "ZYXCBA987"
def transform(n):
    n = list(n)
    newString = []
    for c in n:
        c = ord(c)
        if (c <= 57 and c >= 48):
            c = 48 + 57 - c
        elif (c <= 90 and c >= 65):
            c = 65 + 90 - c
        elif (c <= 122 and c >= 97):
            c = 97 + 122 - c
        newString.append(chr(c))
                    
    return ''.join(newString)
