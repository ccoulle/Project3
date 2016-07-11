import os, sys
import Tkinter as tk
import controller

GEOMETRY = '740x480+0+100'

class View(object):
  
   def __init__(self, controller):
      self.controller = controller
      self.root = tk.Tk()
      self.root.geometry(GEOMETRY)
      self.moneyVar = tk.IntVar()
      self.root.bind('<Escape>', lambda event: self.root.quit())
      self.initScreen()
      self.makeMenu()
      self.makeFileList()
      self.Entry()

   def initScreen(self):
      labelFont = ('symbol', 12, 'bold')
      label = tk.Label(self.root, text = "File Management Application")
      label.config(bg='#fff500')
      label.pack(expand=tk.NO, fill=tk.BOTH)
   def makeMenu(self): 
      menubar = tk.Menu(self.root)
      menubar.config(bg='#15ff00')
      filemenu = tk.Menu(menubar, tearoff=1)
      menubar.add_cascade(menu=filemenu, label='File')
      filemenu.add_command(label="Exit", command=self.root.quit)
      
      helpmenu = tk.Menu(menubar)
      helpmenu.add_command(label='Get Help', command=self.showWarning)
      menubar.add_cascade(menu=helpmenu, label='Help')
      self.root.config(menu=menubar)
      
      
   def makeFileList(self):      
      scrollbar = tk.Scrollbar(self.root)
      scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    
      view = tk.Toplevel()
      listbox = tk.Listbox(self.root, yscrollcommand = scrollbar.set)
      listbox.pack(side="top", fill="both", expand=True)    
      scrollbar.config(command = listbox.yview)
        
     
      listbox.insert(tk.END, self.controller.populateFiles())
    
      label = tk.Label(view, text="Current Directory: ").pack(side=tk.LEFT)
      self.entry = tk.Entry(view, textvariable=self.controller.getMoney(), width=40)
      self.entry.pack(side=tk.LEFT )
      self.entry.insert(0, self.controller.getMoney())
      #self.moneyVar.set(self.controller.getMoney)

   def Entry(self):
      labelFont = 'Symbol', 12
      label = tk.Label(self.root, text = "File Name:")
      label.config(font = labelFont, bd=2, relief=tk.SUNKEN)
      label.config(height=1)
      label.pack(side=tk.LEFT)
      
      button = tk.Button(self.root, text="Remove", width=15) 
      button.config(command=self.controller.remove)
      button.pack(side=tk.RIGHT)
      
      button = tk.Button(self.root, text="Remove All", width=15) 
      button.config(command=self.controller.removeAll)
      button.pack(side=tk.RIGHT)
      
      button = tk.Button(self.root, text="Search", width=20) 
      button.config(command=self.controller.walk)
      button.pack(side=tk.RIGHT)

      self.entry = tk.Entry(self.root)
      self.entry.bind('<Return>', lambda event: self.displayEntryInfo())   
      self.entry.config(font = labelFont)
      self.entry.pack(fill = tk.BOTH, side=tk.BOTTOM)
      self.entry.focus()
  
   def displayEntryInfo(self):
      print self.entry.get()  
   
   def notify(self, m):
      self.moneyVar.set(m)

   def showWarning(self):
      tkMessageBox.showwarning('How can I help you?')

