inFp = None
inList, inStr = [], ""

inFp=open("C:\\Users\\minch\\OneDrive\\Desktop\\Python실습\\FileTest\\파이썬 10주차 실습.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    print(inStr,end="")

inFp.close()