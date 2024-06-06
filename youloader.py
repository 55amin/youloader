import tkinter
import customtkinter
from pytube import youtube

# System Settings
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

# App Frame
app = customtkinter.CTk()
app.geometry('1920x1080')
app.title('YouLoader')

# UI Elements
title = customtkinter.CTkLabel(app, text='YouLoader\nInsert a YouXXXX link to download')
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=720, height=60, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text='Download', command=start_download)
download.pack(padx=10, pady=10)
finish_download = customtkinter.CTkLabel(app, text='')
finish_download.pack()

