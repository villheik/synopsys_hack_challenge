# Return a substring with every fourth character of the input string dropped.
#
# Example: "0123456789" -> "01245689"
def transform(n):
    n = list(n)
    del n[3::4]
    return ''.join(n)


