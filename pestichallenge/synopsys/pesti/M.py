# Calculate MD5 hash of the input. Return hex digest in lower case.
#
# Example: "31337c0d3r5!!!" -> "a80d21609b0ff93a3848aa9c8c0f1c13"
def transform(n):
    import md5

    m = md5.new(n).hexdigest()
    return m


    
