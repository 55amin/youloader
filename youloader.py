import tkinter as tk
import customtkinter as ctk
from pytubefix import YouTube
from PIL import Image, ImageTk
import requests
import threading
from io import BytesIO

# App Frame
app = ctk.CTk()
app.geometry("1920x1080")
app.title("YouLoader")
app.resizable(True, True)
app.state('zoomed')
# System Settings
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# UI Elements
title = ctk.CTkLabel(app, text="YouLoader", font=("Arial", 20), text_color="white")
title.pack(padx=10, pady=(10, 0))
subtitle = ctk.CTkLabel(app, text="\nInsert the URL of the video you want to download")
subtitle.pack(after=title, padx=2, pady=(0, 15))
url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=720, height=60, textvariable=url_var)
link.pack()
vid_title = ctk.CTkLabel(app, text="")

def display_video_info():
    yt_link = link.get()
    try:
        yt = YouTube(yt_link)
        vid_title.configure(text=yt.title)
        vid_title.pack(after=link, padx=2, pady=2)
        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)
        img = Image.open(BytesIO(response.content))
        img.thumbnail((1000, 1000))
        thumbnail = ImageTk.PhotoImage(img)
        thumbnail_label.configure(image=thumbnail)
        thumbnail_label.image = thumbnail
    except:
        vid_title.configure(text="")
        thumbnail_label.configure(image="")

thumbnail_label = ctk.CTkLabel(app, text="")
thumbnail_label.pack(padx=10, pady=(10, 20))

def update_video_info():
    display_video_info()
    app.after(1000, update_video_info) 

progress_bar = tk.ttk.Progressbar(app, orient="horizontal", length=200, mode="determinate")
progress_label = ctk.CTkLabel(app, text="0%")

def on_progress(stream, chunk, bytes_remaining):
    progress_bar.pack(pady=10)
    progress_label.pack()
    bytes_downloaded = stream.filesize - bytes_remaining
    percentage = int((bytes_downloaded / stream.filesize) * 100)
    progress_bar['value'] = percentage
    progress_label.configure(text=f"{percentage}%")
    app.update_idletasks()
    
# Download
def download(func):
    download_thread = threading.Thread(target=func)
    download_thread.start()

def download_mp4():
    try:
        yt_link = link.get()
        yt_func = YouTube(yt_link, on_progress_callback=lambda stream, chunk, bytes_remaining: on_progress(stream, chunk, bytes_remaining))
        video = yt_func.streams.get_highest_resolution()
        title.configure(text=yt_func.title)
        finish_download.configure(text="")
        video.download()
        finish_download.configure(text="Download complete", text_color="green")
    except:
        finish_download.configure(text="Download unsuccessful", text_color="red")

def download_mp3():
    try:
        yt_link = link.get()
        yt_func = YouTube(yt_link, on_progress_callback=on_progress)
        audio = yt_func.streams.get_audio_only()
        title.configure(text=yt_func.title)
        finish_download.configure(text="")
        audio.download(mp3=True)
        finish_download.configure(text="Download complete", text_color="green")
    except:
        finish_download.configure(text="Download unsuccessful", text_color="red")

button_frame = ctk.CTkFrame(app)
button_frame.pack(padx=10, pady=(0, 10))
download_video = ctk.CTkButton(button_frame, text='Download as video (mp4)', command=lambda: download(download_mp4))
download_video.grid(row=0, column=0, padx=5)
download_audio = ctk.CTkButton(button_frame, text='Download as audio (mp3)', command=lambda: download(download_mp3))
download_audio.grid(row=0, column=1, padx=5)
finish_download = ctk.CTkLabel(app, text="")
finish_download.pack()

update_video_info()

# Run App
app.mainloop()
