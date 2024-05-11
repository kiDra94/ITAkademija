def palindrom(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]: #if s[i] != s[-1-i]
            return False
    return True

def palindrom1(s):
    return s == s[::-1]

if __name__ == "__main__":
    assert palindrom1("anavolimilovana") == True
    assert palindrom1("123456789") == False
    assert palindrom1("melem") == True