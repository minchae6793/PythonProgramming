inFp=None
inStr=""

inFp=open("C:\\Users\\minch\\OneDrive\\Desktop\\Python실습\\FileTest\\파이썬 10주차 실습.txt", "r", encoding="utf-8")


while True:
    inStr=inFp.readline()
    if inStr=="":
        break;
    print(inStr,end="")

inFp.close()