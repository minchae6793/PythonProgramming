outFp = None
outStr = ""

outFp = open("C:\Users\minch\OneDrive\Desktop\Python실습\FileTest\파이썬 10주차 실습.txt", "w")

while True:
    outStr = input("내용입력:")
    if outStr !="":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("---정상적으로 파일에 씀---")