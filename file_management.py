import shutil
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import sys
 
root = tk.Tk()
 
#Method selection
root.title('Choose what set of files you need')
root.geometry('500x100')
 
#Exit/X button handling
def on_closing():
    root.destroy()
    sys.exit()
 
#Select button handling
def close():
   root.quit()
   root.withdraw()
   if (site.get() == 0 and seismic.get() == 0):
    messagebox.showinfo("Operation Cancelled", "You did not select a file method (GAM Site and/or Seismic)")
    sys.exit()
 
site = tk.IntVar()
seismic = tk.IntVar()
 
tk.Checkbutton(root, text="For GAM Site", variable=site, onvalue=1, offvalue=0).pack()
tk.Checkbutton(root, text="For Sesimic", variable=seismic, onvalue=1, offvalue=0).pack()
btn = tk.Button(root, text='Select', padx=20, pady=5, command=close)
btn.pack()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
 
#Get Desktop path
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
 
def siteAggregation():
 
    #Make new folder and set path if folder does not exist, if folder exists, cancel operation
    if not os.path.exists(desktop + r"\English"):
        os.makedirs(desktop + r"\English")
    else:
        messagebox.showinfo("Operation Cancelled", "Folder named 'English' already exists on Desktop, please rename or remove")
        sys.exit()
 
    if not os.path.exists(desktop + r"\French"):
        os.makedirs(desktop + r"\French")
    else:
        messagebox.showinfo("Operation Cancelled", "Folder named 'French' already exists on Desktop, please rename or remove")
        sys.exit()
 
    if not os.path.exists(desktop + r"\Global - English"):
        os.makedirs(desktop + r"\Global - English")
    else:
        messagebox.showinfo("Operation Cancelled", "Folder named 'Global - English' already exists on Desktop, please rename or remove")
        sys.exit()
 
    eng_dest = desktop + r"\English"
    fr_dest = desktop + r"\French"
    gl_dest = desktop + r"\Global - English"
 
    #English file names
    english_file_names = ["!!\\FILEPATHS!!"]
 
    #French file names
    french_file_names = ["!!\\FILEPATHS!!"]
 
    #Global/Non-ACS file names
    global_file_names = ["!!\\FILEPATHS!!"]
 
    #Manual file names
    m1 = "!!\\FILEPATH!!"
    m2 = "!!\\FILEPATH!!"
    m3 = "!!\\FILEPATH!!"
    m4 = "!!\\FILEPATH!!"
    m5 = "!!\\FILEPATH!!"
    m6 = "!!\\FILEPATH!!"  
   
    #Copy paste English files to English folder
    eng_files = os.listdir(eng_src)
    for x in english_file_names:
        for file in eng_files:
            shutil.copy((eng_src+x),eng_dest)
 
    #Copy paste Global/Non-ACS files to Global-English folder  
    gl_files = os.listdir(gl_src)
    for x in global_file_names:
        for file in gl_files:
            shutil.copy((gl_src+x),gl_dest)
 
    #Copy paste French files to French folder
    fr_files = os.listdir(fr_src)
    for x in french_file_names:
        for file in fr_files:
            shutil.copy((fr_src+x),fr_dest)
 
    #Copy paste Manual files to respective folders
    m_files = os.listdir(m_src)
    for file in m_files:
        shutil.copy((m_src+m1),eng_dest)
        shutil.copy((m_src+m2),eng_dest)
        shutil.copy((m_src+m3),eng_dest)
        shutil.copy((m_src+m4),fr_dest)
        shutil.copy((m_src+m5),fr_dest)
        shutil.copy((m_src+m6),fr_dest)
 
def seismicAggregation():
 
    #Make new folder and set path if folder does not exist, if folder exists, cancel operation
    if not os.path.exists(desktop + r"\Eng Seismic"):
        os.makedirs(desktop + r"\Eng Seismic")
    else:
        messagebox.showinfo("Operation Cancelled", "Folder named 'Eng Seismic' already exists on Desktop, please rename or remove")
        sys.exit()
 
    if not os.path.exists(desktop + r"\Fr Sesimic"):
        os.makedirs(desktop + r"\Fr Sesimic")
    else:
        messagebox.showinfo("Operation Cancelled", "Folder named 'Fr Seismic' already exists on Desktop, please rename or remove")
        sys.exit()
 
    eng_dest = desktop + r"\Eng Seismic"
    fr_dest = desktop + r"\Fr Sesimic"
 
    #English file names
    english_file_names =["!!\\FILEPATHS!!"]
 
    #French
    french_file_names =["!!\\FILEPATHS!!"]
 
    #Global/ACS file names + renaming
    global_file_names =["!!\\FILEPATHS!!"]
    rename_global = ["!!\\FILEPATHS!!"]
 
    #Manual file names
    m1 =  "!!\\FILEPATH!!"
    m2 =  "!!\\FILEPATH!!"
    m3 =  "!!\\FILEPATH!!"
    m4 =  "!!\\FILEPATH!!"
    m5 =  "!!\\FILEPATH!!"
    m6 =  "!!\\FILEPATH!!"
    m7 =  "!!\\FILEPATH!!"
 
    #Copy paste English files to English folder
    eng_files = os.listdir(eng_src)
    for x in english_file_names:
        for file in eng_files:
            shutil.copy((eng_src+x),eng_dest)
   
    #Copy paste Global/ACS files to English folder
    gl_files = os.listdir(gl_src_acs)
    for x in global_file_names:
        for file in gl_files:
            shutil.copy((gl_src_acs+x),eng_dest)
   
    #Copy paste French files to French folder
    fr_files = os.listdir(fr_src)
    for x in french_file_names:
        for file in fr_files:
            shutil.copy((fr_src+x),fr_dest)
 
    #Copy paste manual files to respective folder
    m_files = os.listdir(m_src)
    for file in m_files:
        shutil.copy((m_src+m1),eng_dest)
        shutil.copy((m_src+m2),eng_dest)
        shutil.copy((m_src+m3),eng_dest)
        shutil.copy((m_src+m4),eng_dest)
        shutil.copy((m_src+m5),eng_dest)
        shutil.copy((m_src+m6),fr_dest)
        shutil.copy((m_src+m7),fr_dest)
 
    #Rename Global/ACS files
    for i in range(5):
        os.rename(eng_dest+global_file_names[i], eng_dest+rename_global[i])
 
#GAM Site/V-Drive File Aggregation
if (site.get() == 1 and seismic.get() == 0):
 
    messagebox.showwarning("Please Read", "The following selection windows are for you to select the file locations. Please be sure to select each folder in accordance to the list below.\n\n1. English Files\n2. French Files\n3. Global/Non-ACS Files\n4. Manually Run Files")
 
    #Folder selection
    eng_src = filedialog.askdirectory(title='Select the folder with the English files')
    fr_src = filedialog.askdirectory(title='Select the folder with the French files')
    gl_src = filedialog.askdirectory(title='Select the folder with the Global/Non-ACS files')
    m_src = filedialog.askdirectory(title='Select the folder with the manually run files')
 
    #End script if at least 1 folder is not chosen
    if (len(eng_src) == 0) or (len(fr_src) == 0) or (len(gl_src) == 0) or (len(m_src) == 0):
        messagebox.showinfo("Operation Cancelled", "You did not select a folder for at least one of the prompts, operation has been cancelled")
        sys.exit()
   
    siteAggregation()
   
#Seismic/ACS file aggregation  
elif (site.get() == 0 and seismic.get() == 1):
 
    messagebox.showwarning("Please Read", "The following selection windows are for you to select the file locations. Please be sure to select each folder in accordance to the list below.\n\n1. English Files\n2. French Files\n3. Global/ACS Files\n4. Manually Run Files")
   
    #Folder selection
    eng_src = filedialog.askdirectory(title='Select the folder with the English files')
    fr_src = filedialog.askdirectory(title='Select the folder with the French files')
    gl_src_acs = filedialog.askdirectory(title='Select the folder with the Global/ACS Specific files')
    m_src = filedialog.askdirectory(title='Select the folder with the manually run files')
 
    #End script if at least 1 folder is not chosen
    if (len(eng_src) == 0) or (len(fr_src) == 0) or (len(gl_src_acs) == 0) or (len(m_src) == 0):
        messagebox.showinfo("Operation Cancelled", "You did not select a folder for at least one of the prompts, operation has been cancelled")
        sys.exit()
 
    seismicAggregation()
 
else:
    messagebox.showinfo("Operation Cancelled", "Due to CPU limitations you can only do one set at a time")
    sys.exit()