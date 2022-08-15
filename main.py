"""
Name: Love Meter
Author: Kai Simpson
Lisence: MIT Lisence
Language: English


Copying of this file has to be credited as 'Kai Simpson' or it is illegal to publicly use this file when uncredited.


Have A Good Day!

"""


import PySimpleGUI as sg
import os
import tkinter
from tkinter import messagebox
import random

layout = [
    [sg.Text("LOVE METER")],
    [sg.Text("                                                                             ")],
    [sg.Text("Name 1"), sg.InputText()],
    [sg.Text("Name 2"), sg.InputText()],
    [sg.Button("Submit")],
    [sg.Text("                                                                             ")],
    [sg.Button("Close")]
]

with open(r"theme.txt", encoding='UTF8') as f:
    theme1 = f.read()
    theme = sg.theme(theme1)

window = sg.Window('Window Title', layout, element_justification='c')

while True:
    event, values = window.read()

    Name1 = [values[0]]
    Name2 = [values[1]]

    ResultName = Name1 + Name2

    Chance = random.randint(1, 100)

    if event == 'Close' or event == sg.WINDOW_CLOSED:
        break

    if event == 'Submit':
        messagebox.showinfo("Results", Chance)