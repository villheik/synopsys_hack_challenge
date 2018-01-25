# Convert the ASCII input to hex representation in upper case.
#
# Example: "FOo123" -> "464F6F313233"
def transform(n):
    newstring = ''
    n = list(n)
    for c in n:
        newstring += hex(ord(c))[2:].upper()
    return newstring
