# Python program for (Knuth Morris Prat) KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)  # what we need to find
    N = len(txt)  # sample

    lps = [0]*M
    # create an array based on the pat size

    FindLPS(pat, M, lps)  # Get the longest LPS in the array
    j = 0
    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:  # if its match then check the next character
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index", str(i-j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:

            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def FindLPS(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[len] == pat[i]:
            len += 1
            lps[i] = len
            i += 1
        else:

            if len != 0:
                len = lps[len-1]

            else:
                lps[i] = 0
                i += 1


txt = "algorisfunalgoisgreat"
pat1 = "fun"
pat2 = "algo"
KMPSearch(pat1, txt)
KMPSearch(pat2, txt)
