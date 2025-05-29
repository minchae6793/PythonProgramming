inFp, outFp = None, None
inStr = ""

inFp = open(input("소스 파일명을 입력하세요: "),"r")
outFp = open(input("타깃 파일명을 입력하세요: "),"w")

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("---%s 파일이 %s 파일로 정상적으로 복사되었음---" %(inFp.name, outFp.name))