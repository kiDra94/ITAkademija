def palindrom1(s):
    if s =="":
        return s
    return s[-1]+palindrom1(s[:-1])

if __name__ == "__main__":
    assert (palindrom1("anavolimilovana") == "anavolimilovana") == True
    assert (palindrom1("1123211") == "11223211") == False
    assert (palindrom1("melem") == "melem") == True