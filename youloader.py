import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

# App Frame
app = customtkinter.CTk()
app.geometry('1920x1080')
app.title('YouLoader')

# Download
def download_mp4():
    try:
        yt_link = link.get()
        yt_func = YouTube(yt_link)
        video = yt_func.streams.get_highest_resolution()
        title.configure(text=yt_func.title)
        finish_download.configure(text='')
        video.download()
        finish_download.configure(text='Download complete', text_color='green')
    except:
        finish_download.configure(text='Download unsuccessful', text_color='red')

def download_sound():
    try:
        yt_link = link.get()
        yt_func = YouTube(yt_link)
        audio = yt_func.streams.get_audio_only()
        title.configure(text=yt_func.title)
        finish_download.configure(text='')
        audio.download()
        finish_download.configure(text='Download complete', text_color='green')
    except:
        finish_download.configure(text='Download unsuccessful', text_color='red')
        
# UI Elements
title = customtkinter.CTkLabel(app, text='YouLoader\nInsert a YouXXXX link to download')
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=720, height=60, textvariable=url_var)
link.pack()

download_video = customtkinter.CTkButton(app, text='Download as video', command=download_mp4)
download_video.pack(padx=10, pady=10)
download_audio = customtkinter.CTkButton(app, text='Download as audio', command=download_sound)
download_audio.pack(padx=10, pady=10)
finish_download = customtkinter.CTkLabel(app, text='')
finish_download.pack()

# Run App
app.mainloop()
