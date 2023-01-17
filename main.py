import tkinter
import customtkinter
from pytube import YouTube

def linkDownload():
    try:
        ytLink = txt_link.get()
        ytObj = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObj.streams.get_highest_resolution()
        lbl_title.configure(text=ytObj.title, text_color='white')
        lbl_done.configure(text='')
        video.download()
        lbl_done.configure(text="Downloaded", text_color='green')
    except:
        lbl_done.configure(text="Invalid YouTube link", text_color='red')
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = (bytes_downloaded/total_size)*100

    percent = str(int(percent_completed))
    lbl_percent.configure(text=percent+'%')
    lbl_percent.update()

    # now update progress bar
    progress_bar.set(float(percent_completed)/100)

# do some system settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


# Our app frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title("YouTube downloader")

# Add UI elements
lbl_title = customtkinter.CTkLabel(app, text="Paste a YouTube link")
lbl_title.pack(padx=10, pady=10)

# get the URL through tkinter string
url_you = tkinter.StringVar()
txt_link = customtkinter.CTkEntry(app, width=350, height=45, textvariable=url_you)
txt_link.pack()

# updated frame on finish
lbl_done = customtkinter.CTkLabel(app, text='')
lbl_done.pack()


# Add a download buttone
btn_download = customtkinter.CTkButton(app,text='Download', command=linkDownload)
btn_download.pack(padx=10, pady=10)



# Add progress bar
lbl_percent = customtkinter.CTkLabel(app, text='0%')
lbl_percent.pack(padx=10, pady=110)

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=0)


# Run the app
app.mainloop()