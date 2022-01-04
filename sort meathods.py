import random
import time
import copy
import sys
sys.setrecursionlimit(10000)

def cal_time(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    print('function {} runs for {:.7f}'.format(func.__name__, end_time - start_time))
  return wrapper

class sort_methods():
  def __init__(self, li):
    self.li = li
    self.len = len(self.li)
    
  @cal_time
  def bubble_sort(self):
    for i in range(self.len - 1):
      for j in range(self.len - i - 1):
        if self.li[j] > self.li[j + 1]:
          self.li[j], self.li[j + 1] = self.li[j + 1], self.li[j]
     
    return self.li
  
  
  @cal_time
  def select_sort(self):
    for i in range(self.len - 1):
      selected_val = self.li[i]
      for j in range(i + 1, self.len): #!
        if self.li[j] < selected_val:
          self.li[i], self.li[j] = self.li[j], self.li[i]
          selected_val = self.li[i] #!
    
    return self.li
  
  
  @cal_time
  def insert_sort(self):
    for i in range(1, self.len):
      tmp = self.li[i]
      j = i - 1
      while j >= 0 and self.li[j] > tmp:
        self.li[j + 1] = self.li[j]
        j -= 1
      self.li[j + 1] = tmp
    
    return self.li
  
  def partition(self, left, right):
    tmp = self.li[left]
    while left < right:#!
      while right > left and self.li[right] >= tmp:#!
        right -= 1
      self.li[left] = self.li[right]
      while right > left and self.li[left] <= tmp:
        left += 1
      self.li[right] = self.li[left]
    self.li[left] = tmp
    return left
  
  def _quick_sort(self, left, right):
    if left < right:
      mid = self.partition(left, right)
      self._quick_sort(left, mid - 1)#!
      self._quick_sort(mid + 1, right)
  
  @cal_time
  def quick_sort(self):
    self._quick_sort(0, self.len - 1)
  

length = int(2e3)
li = [random.randint(0, 899) for i in range(length)]
li_1 = copy.deepcopy(li)
li_2 = copy.deepcopy(li)
li_3 = copy.deepcopy(li)
li_4 = copy.deepcopy(li)

sort = sort_methods(li_1)
sort.quick_sort()
print(sort.li)

sort = sort_methods(li_2)
sort.bubble_sort()
print(sort.li)

sort = sort_methods(li_3)
sort.select_sort()
print(sort.li)

sort = sort_methods(li_4)
sort.insert_sort()
print(sort.li)
