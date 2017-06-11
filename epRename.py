import urllib2
import json
import os
import re
from Tkinter import *
import tkMessageBox
import tkFileDialog
parent = Tk()
parent.minsize(width=500, height=300)
parent.resizable(width=False, height=False)
currentDir="C:/Users/"
list = Listbox(parent,selectmode=BROWSE,width=70,height=20,yscrollcommand=Scrollbar(parent, orient=VERTICAL).set)
list.grid(row=1, column=0, columnspan=5, rowspan=3,padx=2, pady=2)
dirText=Entry(parent,width=50)
dirText.grid(row=0, column=1,columnspan=2,padx=5, pady=10)
def populateList(dir):
  list.delete(0, END)
  for name in os.listdir(dir):
    if not name.startswith('.'):
      list.insert(END,name)
populateList(currentDir)  
def browse():
  currentDir=tkFileDialog.askdirectory()
  if not dir==NONE:
    populateList(currentDir)
  dirText.delete(0,END)  
  dirText.insert(0,currentDir)
browse=Button(parent, text ="Browse",command=browse,width=7)
browse.grid(row=0, column=4,columnspan=2,padx=5, pady=10)
dirText.insert(0,"C:/Users/Sanidhya")
info=Label(parent, text="Current directory:",justify="right")
info.grid(row=0, column=0,padx=3, pady=10)
def renameFiles(showName):
  epQueryJSON=json.loads(urllib2.urlopen('http://api.tvmaze.com/singlesearch/shows?q='+showName).read())
  epJSON=json.loads(urllib2.urlopen(epQueryJSON['_links']['self']['href']+'/episodes').read())
  for seasonFolder in os.listdir(dirText.get() + '/' + showName):
    if not seasonFolder.startswith('.'):
      currentSeason=int(re.search(r'\d+', seasonFolder).group())
      for epNames in os.listdir(dirText.get() + '/' + showName + '/' + seasonFolder):
        if not (epNames.startswith('.') or epNames.startswith('~') or epNames.endswith('.db')):
          temp= map(int, re.findall(r'\d+', os.path.splitext(epNames)[0]))
          fileFormat=os.path.splitext(epNames)[1]
          print 'Renaming '+epNames
          if len(temp) != 1:
            temp.remove(currentSeason)
          currentEp=temp[0]
          for episode in range(0,len(epJSON)-1):
            if epJSON[episode]['season']==currentSeason and epJSON[episode]['number']==currentEp:
              epNewName=epJSON[episode]['name'].encode('utf-8').replace(':','-').replace('?', '').replace('\"','').replace('*','.')
              if currentEp < 10:
                os.rename(dirText.get() + '/' + showName + '/' + seasonFolder+'/'+epNames,dirText.get() + '/' + showName + '/' + seasonFolder+'/'+str(currentSeason) +'x0'+ str(currentEp) + '-' + epNewName.decode('utf-8') + str(fileFormat))
              else:
                os.rename(dirText.get() + '/' + showName + '/' + seasonFolder+'/'+epNames,dirText.get() + '/' + showName + '/' + seasonFolder+'/'+str(currentSeason) +'x'+ str(currentEp) + '-' + epNewName.decode('utf-8') + str(fileFormat))
rename=Button(parent, text ="Rename",command=lambda : renameFiles(list.get(list.curselection())),width=7)
rename.grid(row=2, column=5,columnspan=2,padx=5, pady=10)
mainloop()
