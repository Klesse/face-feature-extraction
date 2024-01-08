from tkinter import *
from FaceRecognition import *


CANVAS_HEIGTH = 600
CANVAS_WIDTH = 800


def main():
    m = Tk()

    m.title('Face Recognition')



    w = Canvas(m, width=800, height=600)
    w.pack()


    m.mainloop()

if __name__=="__main__":
    main()