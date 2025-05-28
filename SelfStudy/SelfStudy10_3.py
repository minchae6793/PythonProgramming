from tkinter import *
from time import *

#전역 변수 선언 부분
fnameList = [
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\bear.gif",
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\bee.gif",
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\cupid.gif",
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\dog.gif",
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\dog2.gif",  
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\sun.gif",
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\sun2.gif",  
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\tractor.gif",
    "C:\\Users\\minch\\OneDrive\\Desktop\\PythonPractice\\WindowProgramming\\unicorn.gif"
]
photoList = [None]*9
num=0

#함수 선언 부분
def clickNext():
    global num
    num +=1
    if num >8:
        num = 0
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    filename = fnameList[num].split("\\")[-1]
    nameLabel.config(text=filename)

def clickPrev():
    global num
    num-=1
    if num < 0:
        num = 8
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    filename = fnameList[num].split("\\")[-1]
    nameLabel.config(text=filename)

#메인 코드 부분
window=Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<<이전", command=clickPrev)
btnFname = Button(window, text = "")
btnNext = Button(window, text = "다음>>", command=clickNext)

photo = PhotoImage(file=fnameList[0])
pLabel = Label(window, image=photo)

nameLabel = Label(window, text=fnameList[0].split("\\")[-1])

btnPrev.place(x=250, y=10)
nameLabel.place(x=320, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()