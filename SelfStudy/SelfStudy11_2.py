inFp = None
inStr = ""

inFp = open("C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\FileTest\\파이썬 10주차 실습.txt", "r", encoding='utf8')

for i in range(1, 4):
    inStr = inFp.readline()
    if not inStr:
        break
    print("%d : %s" % (i, inStr), end = "")

inFp.close()