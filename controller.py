import sys
import Tkinter as tk
import model
import view
import os, sys
import fnmatch
import stack
'''
class Stack(object):
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         del self.items[-1]
     def top(self):
         return self.items[-1]
     def size(self):
         return len(self.items)'''


class Controller(object):
  
  def __init__(self, dir, file_pat):
    # model must be instantiated before view 'cuz of tk.mainloop()
    self.model = model.Model()
    self.view = view.View(self)
    self.view.notify(0)
    self.dir = dir
    self.dirStack = stack.Stack()
    self.dirStack.push(self.dir)
    self.file_pat = self.view.displayEntryInfo()
    self.want_files = []
    self.files = []
    self.dirs = []

  def getMoney(self):
    return dir

  def addMoney(self):
    self.model.addMoney(10)
    self.view.notify(self.model.getMoney())

  def removeAll(self):
    for x in self.want_files:
       print x
       self.model.os.remove(x)
    
  def remove(self):  
       x = 0
       while x == 0:
         n = int(raw_input("Which File do you want to delete? "))
         self.model.os.remove(self.want_files[n])
         x = int(raw_input("Do you want to keep going? O for yes, 1 for No. "))

  def walk(self):
    if not self.dirStack.empty():
         preDir = os.getcwd()
         return "This is top dir", self.dirStack.top()
         currDir = self.dirStack.top()
         os.chdir(currDir)
         files = os.listdir( os.getcwd() )
         print files
         for x in files:
           if os.path.isdir(x):
             print "dir found:", x
             self.dirs.append(x)
             self.dirStack.push(x)
             print self.dirStack.top()
             self.walk()
           else:
             if fnmatch.fnmatch(x, file_pat):
               print "A PYC:", x
               file_path = os.getcwd()
               file_path +='/'
               file_path += x
               self.want_files.append(file_path)
             self.files.append(x)
         os.chdir(preDir)
         self.dirStack.pop()
         
  def populateFiles(self):
     return os.listdir( os.getcwd() )
         
         
if __name__ == "__main__":

  file_pat = lambda event: self.displayEntryInfo()
  
  dir = os.getcwd()
  print "DIR IS:", dir
  t = Controller(dir, file_pat )
  t.walk()
  
  print t.dirs
  print t.files
  print t.want_files
  
  #controller = Controller(dir, file_pat)
  tk.mainloop() 
