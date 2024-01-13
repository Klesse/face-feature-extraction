import flet
from FaceRecognition import *

def main():
    face = FaceRecognition()

    # End of program
    face.conn.close()
    face.cur.close()

if __name__=="__main__":
    main()