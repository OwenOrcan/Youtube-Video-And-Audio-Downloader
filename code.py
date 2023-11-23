import tkinter as tk
import customtkinter
from pytube import YouTube

def download_video():
    print("Download Started")
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        finish_label.configure(text="")

        video.download() 
        finish_label.configure(text="Downloaded")
    except:
        finish_label.configure(text="Youtube Link is Invalid", text_color="red")


def download_audio():
    print("Download Started")
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()
        
        title.configure(text=ytObject.title, text_color="white")
        finish_label.configure(text="")

        video.download() 
        finish_label.configure(text="Downloaded")
    except:
        finish_label.configure(text="Youtube Link is Invalid", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    totalsize = stream.filesize
    bytes_downloaded = totalsize - bytes_remaining
    percentage_of_completion = bytes_downloaded / totalsize * 100
    per = str(int(percentage_of_completion))
    p_percentage.configure(text=per + "%")
    p_percentage.update()

    #Update progress bar
    progressbar.set(float(percentage_of_completion/100))
# System Settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

#Link Input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

#Progress Percentage
p_percentage = customtkinter.CTkLabel(app, text="0%")
p_percentage.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)


#Download Button
download = customtkinter.CTkButton(app, text="Download Video", command=download_video)
download.pack(padx=10, pady=10)
#Audio Download Button
downloadAudio = customtkinter.CTkButton(app, text="Download Audio", command=download_audio)
downloadAudio.pack()



#Run App
app.mainloop()
