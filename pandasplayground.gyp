import pandas as pd

import ctypes 
from tqdm import tqdm
class DynamicArray(object): 
    ''' 
    DYNAMIC ARRAY CLASS (Similar to Python List) 
    '''
      
    def __init__(self): 
        self.n = 0 # Count actual elements (Default is 0) 
        self.capacity = 1 # Default Capacity 
        self.A = self.make_array(self.capacity) 
          
    def __len__(self): 
        """ 
        Return number of elements sorted in array 
        """
        return self.n 
      
    def __getitem__(self, k): 
        """ 
        Return element at index k 
        """
        if not 0 <= k <self.n: 
            # Check it k index is in bounds of array 
            return IndexError('K is out of bounds !')  
          
        return self.A[k] # Retrieve from the array at index k 
          
    def append(self, ele): 
        """ 
        Add element to end of the array 
        """
        if self.n == self.capacity: 
            # Double capacity if not enough room 
            self._resize(2 * self.capacity)  
          
        self.A[self.n] = ele # Set self.n index to element 
        self.n += 1
  
    def insertAt(self,item,index): 
        """ 
         This function inserts the item at any specified index. 
        """
  
          
        if index<0 or index>self.n: 
            print("please enter appropriate index..") 
            return
          
        if self.n==self.capacity: 
            self._resize(2*self.capacity) 
              
          
        for i in range(self.n-1,index-1,-1): 
            self.A[i+1]=self.A[i] 
              
          
        self.A[index]=item 
        self.n+=1
  
  
          
    def delete(self): 
        """ 
        This function deletes item from the end of array 
        """
  
        if self.n==0: 
            print("Array is empty deletion not Possible") 
            return
          
        self.A[self.n-1]=0
        self.n-=1
          
          
          
      
    def removeAt(self,index): 
        """ 
        This function deletes item from a specified index.. 
        """        
  
        if self.n==0: 
            print("Array is empty deletion not Possible") 
            return
                  
        if index<0 or index>=self.n: 
            return IndexError("Index out of bound....deletion not possible")         
          
        if index==self.n-1: 
            self.A[index]=0
            self.n-=1
            return        
          
        for i in range(index,self.n-1): 
            self.A[i]=self.A[i+1]             
              
          
        self.A[self.n-1]=0
        self.n-=1
  
          
    def _resize(self, new_cap): 
        """ 
        Resize internal array to capacity new_cap 
        """
          
        B = self.make_array(new_cap) # New bigger array 
          
        for k in range(self.n): # Reference all existing values 
            B[k] = self.A[k] 
              
        self.A = B # Call A the new bigger array 
        self.capacity = new_cap # Reset the capacity 
          
    def make_array(self, new_cap): 
        """ 
        Returns a new array with new_cap capacity 
        """
        return (new_cap * ctypes.py_object)() 


























my_series = pd.Series([4.6, 2.1, -4.0, 3.0])
print(my_series)


# Names (keys) mapped to a tuple (the value) containing the height, lat and longitude.
scottish_hills = {'Ben Nevis': (1345, 56.79685, -5.003508),
                  'Ben Macdui': (1309, 57.070453, -3.668262),
                  'Braeriach': (1296, 57.078628, -3.728024),
                  'Cairn Toul': (1291, 57.054611, -3.71042),
                  'Sgòr an Lochain Uaine': (1258, 57.057999, -3.725416)}

'''
dicts = {}
keys = range(4)
values = ["Hi", "I", "am", "John"]
for i in keys:
    for x in values:
        dicts[i] = x
print(dicts)
'''

tofile1 = open("pandas.txt", "w")
fromfile1 = open("patterns.txt", "r")
match_pattern = fromfile1
iterationvar = 0
match_pattern = fromfile1.read().lower()
fromfile = fromfile1.read().lower()
#tofile = tofile.read().lower()
fromfile = fromfile.split()
match_pattern = match_pattern.split()
dicts = {}
keys = range(len(fromfile))
values=[len(fromfile)]


t = 0 #iterator
for word in match_pattern:
    values[t]=word
    #t+=1

for i in tqdm(keys):
    for x in values:
        dicts[i] = x
print(dicts)

new_dictionary = dict.fromkeys(match_pattern)                        
#print(new_dictionary)

# Creating an empty dictionary 
myDict = {} 
  

  
print(myDict) 

i = 0 
wilson = 0
match_pattern = str(match_pattern)
for i in tqdm(range (0,len(match_pattern))):
    '''
    if i % 10000 == 0:
        print("|",end="")
    '''
    #go through and save the values in the string to array. What will 
    #denote the terms is this... None,#,#,#,#_space_letters

    #samurai holder

    samurai = DynamicArray()
    castle = "" #holds word 
    comma = 0 # this counts the commas so that when new line is hit commas go back to zero and signal new word
    ronin =(match_pattern[i])
    if ronin.isalpha() == True:
        #its a letter
        
        castle = castle + ronin

        
       
        #print('letter')
    if ronin == ',':
        if comma < 1:
            #it's the first comma
            sleepingbeauty = castle #holds on to the castle word, it will be used to subscript the dict. 
            
        #its a letter
        comma+=1
        #print('comma')
    if ronin == '\n':
        wilson = 0
        comma = 0
        castle = ""

        myDict[sleepingbeauty] = samurai #save samurai (the row) to sleeping beauty (the word)



        samurai.clear()
        #print('new line')
    
    if ronin.isdigit() == True:
        samurai.append(ronin)
        wilson += 1
    i+=1

print(myDict)

tofile1.close()
fromfile1.close()




'''

tofile.write("book_data = {") #matching first part of dictionary convention

#if new line then put parenthesis and comma
i = 0
while i < 1000:
    
    for word in match_pattern:
        tofile.write(" '{0}' : (".format(word)) #perfect
        tofile.write("{0},".format(word))
        #this is the original below
        """ text_file.write("{0},".format(word))
        text_file.write("{0}\n".format(iterationvar)) """
        iterationvar+=1
        #y +=1
                                    #I am working in the above function. Goal: get a dictionary that is full of arrays. One array for each word with every position where it occured 
                                    #in the book. This gives an idea of sentiment over time. Copy the syntax for the above frequency dictionary but implement an array instead of the 0 on the right

tofile.write("}") #matching first part of dictionary convention'''


