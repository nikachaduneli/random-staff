from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_name = ''


def open_location():

  global Folder_name
  Folder_name = filedialog.askdirectory()

  if len(Folder_name) > 1:
    location_error.config(text=Folder_name, fg='green')
  else:
    location_error.config(text="Please Select Folder", fg='red')

def download_video():
  choice = ytd_choises.get()
  url = ytd_entry.get()
  try:
    if len(url) > 1:
      ytd_error.config(text='')
      ytd = YouTube(url)

      if choice == choices[0]:
        select = ytd.streams.filter(progressive=True).first()
      elif choice == choices[1]:
        select = ytd.streams.filter(progressive=True).last()
      elif choice == choices[2]:
          select = ytd.streams.filter(only_audio=True).first()
      else: ytd_error.config(text='Paste link Again', fg='red')
      
      select.download(Folder_name)
      ytd_error.config(text='Download Completed.', fg='green')
  except:
    ytd_error.config(text='Something Went Wrong...')  




root = Tk()
root.title('Youtube Downloader')
root.geometry('350x400')
root.columnconfigure(0, weight=1)

ytd_label = Label(root, text='Enter URL Here...', font=('jost', 15))
ytd_label.grid()


ytd_entry_var = StringVar()

ytd_entry = Entry(root, width=50, textvariable=ytd_entry_var)
ytd_entry.grid()

ytd_error = Label(root, text='', fg='red', font=('jost',10))
ytd_error.grid()

save_label = Label(root, text='Save The Video File', font=('jost', 15, 'bold'))
save_label.grid()

save_enrty_btn = Button(root, width=10, bg='red', fg='white', text='Choose Path', command=open_location)
save_enrty_btn.grid()

location_error = Label(root,text='', font=('jost',10))
location_error.grid()

ytd_quality = Label(root, text='Select Quality', font=('jost',15))
ytd_quality.grid()

choices = ['720p','144p','Only Audio']

ytd_choises=ttk.Combobox(root, values=choices)
ytd_choises.grid()

download_btn = Button(root, text="Download",width=10, bg='red', fg='white', command=download_video)
download_btn.grid()



root.mainloop()

