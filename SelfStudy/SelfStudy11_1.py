inFp = None
inStr = ""
count = 1  # 줄 번호 변수 추가

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (count, inStr), end="")
    count += 1  # 줄 번호 1 증가

inFp.close()