
#! THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTERS OF FaizeenHoque
#* IT IS RECOMMENDED TO INSTALL THESE PYTHON MODULES :
#? 1. PyTube -> pip install pytube
#? 2. Custom Tkinter -> pip install customtkinter

# ---------------------------------------------------------------- Terms of Service

#! 1. Please do not use this YouTube video downloaded for un-ethical purposes.
#! 2. Please do not Download someones YouTube video without explicit permission.
#! 3. Please do not Harras someone by using their video against them.

#* If you follow these rules, You have all rights to use this video downloader :

#@ ---------------😊 ENJOY -------------------------- @#

import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

#! IMPORTANT FUNCTIONS  ----------------------------------------------------------------

def DownloadVideo():
    try:
        YouTube_LINK = link.get() #@  Gets the youtube link
        YouTube_Object = YouTube(YouTube_LINK) #@ makes a youtube object to get data form
        video = YouTube_Object.streams.get_highest_resolution() #@ Sets the video to be high resolution
        
        title.configure(text=YouTube_Object.title, text_color='white')  #@ Changes the title
        finish_lable.configure(text='') #@ Resets the finish_lable
        
        video.download() #@ downloads the video
    except Exception:
        finish_lable.configure(text='INVALID LINK GIVEN', text_color='red')
    finish_lable.configure(text='Downloaded video',text_color='green')


#* SYSTEM SETTINGS *--------------------------------------------------------------------------------

ctk.set_appearance_mode('System') #@ Appearance Mode
ctk.set_default_color_theme('blue') #@ Default Color Theme

#* APP FRAME *--------------------------------------------------------------------------------

app = ctk.CTk() #@ INITALIZATION
app.geometry('720x480') #@ Geometry of the window
app.title('Youtube downloader') #@ Title of the window


#* ADDING UI ELEMENTS *----------------------------------------------------------------

title = ctk.CTkLabel(app, text='INSERT YOUTUBE LINK')   #@ Text box title for the video link
title.pack(padx=10, pady=10) #@ Pack the Lable (reffering to title for the video link)

#% LINK INPUT  ⬇

url_var = tk.StringVar() #@ The url var
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var) #@ Entry box for the video link
link.pack()

#% LINK INPUT  ⬇

finish_lable = ctk.CTkLabel(app, text='')
finish_lable.pack()

#% DOWNLOAD BUTTON  ⬇

download = ctk.CTkButton(app, text='DOWNLOAD BUTTON', command=DownloadVideo) #@ Button to download the video
download.pack(padx=20, pady=10)


#* RUN APP *--------------------------------------------------------------------------------

app.mainloop() #! MAIN LOOP