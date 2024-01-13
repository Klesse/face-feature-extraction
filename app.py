import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import flet as ft
from FaceRecognition import *
import cv2


def main(page: ft.Page):
    # face = FaceRecognition()

    page.title = "Face Recognition"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    title = ft.Text(value = 'Face Recognition', 
                    size=22,
                    width=300,
                    weight=ft.FontWeight.BOLD,
                    text_align = ft.TextAlign.CENTER)
    
    text_field = ft.TextField(value="Name", width=300, text_align=ft.TextAlign.CENTER)
    button_add = ft.FilledButton(text="Add", width=300, icon="add")
    #page.controls.append(title)

    page.add(
        ft.Column([title, text_field, button_add])
    )
    
    page.update()


if __name__=="__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER) # , view=ft.AppView.WEB_BROWSER
    #ft.app(port=8550, target=main)