import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import flet as ft
from FaceRecognition import *


def main(page: ft.Page):
    # face = FaceRecognition()

    page.title = "Face Recognition"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    t = ft.Text(value='Hello, world!')
    page.controls.append(t)
    
    page.update()


if __name__=="__main__":
    ft.app(target=main, view=ft.WEB_BROWSER) # , view=ft.AppView.WEB_BROWSER
    #flet.app(port=8550, target=main)