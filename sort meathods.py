import random

class sort_methods():
  def __init__(self, li):
    self.li = li
    self.len = len(self.li)
    

  def bubble_sort(self):
    for i in range(self.len - 1):
      for j in range(self.len - i - 1):
        if self.li[j] > self.li[j + 1]:
          self.li[j], self.li[j + 1] = self.li[j + 1], self.li[j]
     
    return self.li
  
  def select_sort(self):
    for i in range(self.len - 1):
      selected_val = self.li[i]
      for j in range(i, self.len):
        if self.li[j] < selected_val:
          self.li[i], self.li[j] = self.li[j], self.li[i]
          selected_val = self.li[j]
    
    return self.li
  
  def insert_sort(self):
    for i in range(1, self.len):
      tmp = self.li[i]
      j = i - 1
      while j >= 0 and self.li[j] > tmp:
        self.li[j + 1] = self.li[j]
        j -= 1
      self.li[j + 1] = tmp
    
    return self.li
  
# li = [3, 2, 1, 6, 3, 2.9, 7, 9, 8]
li = [random.randint(0, 899) for i in range(30)]
print(li)
sort = sort_methods(li)
print(sort.bubble_sort())
print(sort.select_sort())
print(sort.insert_sort())
