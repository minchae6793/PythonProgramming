inFp=None
inStr=""

inFp=open("C:\\Users\\minch\\OneDrive\\Desktop\\Python실습\\FileTest\\파이썬 10주차 실습.txt", "r", encoding="utf-8")

inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inStr=inFp.readline()
print(inStr,end="")

inFp.close()