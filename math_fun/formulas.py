
def convert(number,base):
    s = str(number)
    print(len(s))
    for i in range(0,len(s)):
        j = s[i] * base**((len(s)-1) -i)
        print(str(j) + " ")





convert(10,2)