# Convert the ASCII input to hex representation in upper case.
#
# Example: "FOo123" -> "464F6F313233"
def transform(n):
    hexn = []
    for c in n:
        value = hex(ord(c).replace('0x', ''))
        if len(value) == 1:
            value = '0' + value.upper()
        hexn.append(hv)
    return reduce(lambda x,y:x+y, hexn)
