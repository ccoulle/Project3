import os, sys
import Tkinter as tk
import controller

GEOMETRY = '640x480+0+100'

class NotAController(object):
   def getMoney(self): print "Get money"
   def addMoney(self): print "Adding money"

class View(object):
  
   def __init__(self, controller):
      self.controller = controller
      self.root = tk.Tk()
      self.root.geometry(GEOMETRY)
      #self.root.title('File Management')
      self.moneyVar = tk.IntVar()
      self.root.bind('<Escape>', lambda event: self.root.quit())
      self.initScreen()
      self.makeMenu()
      self.makeFileList()
      self.Entry()
      
      '''button = tk.Button(root, text="Add Money", width=20) 
         button.configure(command=self.controller.addMoney)
         button.pack(side=tk.TOP)
         button = tk.Button(root, text="Remove Money", width=20) 
         button.configure(command=self.controller.removeMoney)
         button.pack(side=tk.TOP)'''
   def initScreen(self):
      labelFont = ('symbol', 12, 'bold')
      label = tk.Label(self.root, text = "File Management")
      label.pack(expand=tk.NO, fill=tk.BOTH)
   def makeMenu(self): 
      menubar = tk.Menu(self.root)
      menubar.config(bg='#a2a2a2')
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
        
     
      for item in range(100):
         listbox.insert("File Name #:", item)
    
      label = tk.Label(view, text="Money Available").pack(side=tk.LEFT)
      self.entry = tk.Entry(view, textvariable=self.moneyVar)
      self.entry.pack(side=tk.LEFT)
      self.moneyVar.set(self.controller.getMoney)

   def Entry(self):
      labelFont = 'Symbol', 12
      label = tk.Label(self.root, text = "File Name:")
      label.config(font = labelFont, bd=2, relief=tk.SUNKEN)
      label.config(height=1)
      label.pack(side=tk.LEFT)
      
      button = tk.Button(self.root, text="Search", width=20) 
      button.config(command=self.controller.addMoney)
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

if __name__ == "__main__":
   view = View(NotAController())
