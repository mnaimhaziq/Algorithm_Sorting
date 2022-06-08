def Rabin_Karp(pattern, text, q):
    pattern_len = len(pattern)
    text_len = len(text)
    d = 256  # number of characters in input alphabet
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1
    i = 0
    j = 0

    #calculate the value of d^(pattern_len-1) % q
    for i in range(pattern_len-1):
        h = (h*d) % q

    # Calculate hash value of pattern and first window of text
    for i in range(pattern_len):
        p = (d*p + ord(pattern[i])) % q  # store hash of pattern

        t = (d*t + ord(text[i])) % q  # store text of substring


    # slide the pattern over text one by one
    for i in range(text_len-pattern_len+1):

        # check the hash values of current window of text and pattern.
        if p == t:

            # If the hash values match, then only check for characters one by one
            for j in range(pattern_len):
                if text[i+j] != pattern[j]:
                    break

            j += 1

            # if the loop before does not break, j = (pattern_len - 1) + 1
            if j == pattern_len:
                print("Pattern '"+pattern+"' is found at position: " + str(i+1))

        #calculate hash value for next window of text: remove leading digits, add trailing digit
        if i < text_len-pattern_len:
            t = (d*(t-ord(text[i])*h) + ord(text[i+pattern_len])) % q

            # we might get negative value of t, converting it to positive
            if t < 0:
                t = t+q


text = "algorisfunalgoisgreat"
pattern1 = "fun"
pattern2 = "algo"
q = 13  # select a prime number
Rabin_Karp(pattern1, text, q)
Rabin_Karp(pattern2, text, q)
