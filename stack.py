class Stack(object):
  def __init__(self):
    self.stk = []
  def push(self, x):
    self.stk.append(x)
  def top(self):
    return self.stk[-1]
  def pop(self):
    del self.stk[-1]
  def empty(self):
    return len(self.stk) == 0



  

