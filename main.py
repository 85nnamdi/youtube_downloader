import tkinter
import customtkinter
from pytube import YouTube

# do some system settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


# Our app frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title("YouTube downloader")


# Run the app
app.mainloop()