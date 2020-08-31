#this finds the frequency of words in the txt file that is named in line 6
# to change the txt use the file explorer and replace file with
# new text. 

import re
import string



def removeparenthesis(text_string):
    #i = 0
    text_string.replace('(','ß')
    text_string.replace(')','å')
    """ while i<len(text_string):
        
        if text_string[i] == '(':
            text_string(replace)
            text_string[i].replace(text_string[i],'ß') #denotes a left paren
        if text_string[i] == ')':
            text_string[i].replace(text_string[i],'å') = 'å' #denotes a right paren
        i += 1 """
    
    return text_string

def founduh(text,text_string,iter):
    if text_string[iter] == text:
        return True
    else:
        return False





















frequency = {}
document_text = open('1984.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
#for words in frequency_list:
    #print(words, frequency[words])

# this is a beta section ... reordering dictionary by value
""" largest = {}
biggest = 0
for words in frequency_list:
    current = int(frequency[words])
    if current > biggest:
        #then 
        biggest = current """

# scan text for certain patterns of speech 


#removing the parentheses from the text

oldstring = text_string
text_string = removeparenthesis(oldstring)


print("parentheses removed")





frequency = {}


sent = {} #holds each sentence 
#search finds pattern within () any where in the string 
#patterns 
""" 
#in TITLE, his/her ... of ..., AUTHOR action, ... (AUTHOR LAST NAME, 2000, p.107)
As AUTHOR ... in TITLE, ... 
AUTHOR's ... of ..., TITLE, action...  """

comma = ","
period = "."
semicolon = ';'
colon = ':'
dash = "-"
LASTNAME = "\bWilson\b" #example
boolisyear = True #example for yes is year
pattern1a = "\bin "
pattern1b = ", his\b"
#or
pattern1c = ", her\b"
pattern1d = "\bof\b"
pattern1e = comma
#two words AUTHOR NAME and then Action
pattern1f = comma
pattern1g = "ß"#a left parentheses
pattern1h = LASTNAME
pattern1i = ", "
pattern1j = boolisyear
pattern1k = ", p."
pattern1l = "å"#this is a right parentheses
#just test distance between 1k and 1l to see if reasonably close (within 6) then this will still be true

#PATTERN 2

LASTNAME = "\bSmith\b"
FIRSTNAME = "\bWinston\b"
NAME = FIRSTNAME + LASTNAME # "Laura Wilson"
pattern2a = "\bAs "
#2B OR 2C OR 2D
pattern2b = FIRSTNAME
pattern2c = LASTNAME
pattern2d = NAME
pattern2e = "\bin\b"
pattern2f = True #is italics
pattern2g = comma

#PATTERN 3
#AUTHOR's ... of ..., TITLE, action... 
pattern3a = LASTNAME
#OR
pattern3b = FIRSTNAME
#OR
pattern3c = NAME
pattern3d = "'s\b"
pattern3e = "\bof\b"
pattern3f = comma
pattern3g = comma
#distance between 3f and 3g needs to accommodate average book titles
#next word is an action
pattern1 = [12,pattern1a,pattern1b,pattern1c,pattern1d,pattern1e,pattern1f,pattern1g,pattern1h,pattern1i,pattern1j,pattern1k,pattern1l]
pattern1_b = [11,pattern1a,pattern1b,pattern1d,pattern1e,pattern1f,pattern1g,pattern1h,pattern1i,pattern1j,pattern1k,pattern1l]
pattern1_c = [11,pattern1a,pattern1c,pattern1d,pattern1e,pattern1f,pattern1g,pattern1h,pattern1i,pattern1j,pattern1k,pattern1l]
pattern2 = [7,pattern2a,pattern2b,pattern2c,pattern2d,pattern2e,pattern2f,pattern2g]
pattern3 = [7,pattern3a,pattern3b,pattern3c,pattern3d,pattern3e,pattern3f,pattern3g]

patterns = [pattern1,pattern1_b,pattern1_c,pattern2,pattern3]
#now iterate through these patterns
temp_text_string = text_string
temp_text_string_new = temp_text_string
count = 0
x = 0
originalholder = temp_text_string_new

i = 0
j = 1
pattern1freq = []
pattern2freq = []
pattern3freq = []
pattern1_bfreq = []
pattern1_cfreq = []

count += 1
while(i<5):
    jster = patterns[i]
    jtop = int(jster[0])
    while(j<jtop):
        iters = patterns[i]
        iterpattern = iters[j]
        #print("."),
        found_pattern = re.search(str(iterpattern),temp_text_string,'i')
        #found_pattern = re.findall(iterpattern,temp_text_string).start()
        #found_pattern = re.finditer(iterpattern,temp_text_string)
        
        #pattern frequency saving
        if i == 0:
            pattern1freq.append(str(found_pattern))
            #print("1 -> ",pattern1freq)
        if i == 1:
            pattern1_bfreq.append(str(found_pattern))
            #print("1_b -> ",pattern1_bfreq)
        if i == 2:
            pattern1_cfreq.append(str(found_pattern))
            #print("1_c -> ",pattern1_cfreq)
        if i == 3:
            pattern2freq.append(str(found_pattern))
            #print("2 -> ",pattern2freq)
        if i == 4: 
            pattern3freq.append(str(found_pattern))
            #print("3 -> ",pattern3freq)
        print("saved pattern to patternfreq",i)
        
        #now iterate 


        for word in found_pattern:
            counter = frequency.get(word,0)

            frequency[word] = count + 1
            
        frequency_list = frequency.keys()
        
        #for words in frequency_list:
            #print(words, frequency[words])

        #EXPERIMENTING HERE ABOVE WITH FLAGS ... CONSIDER USING THE FINDALL METHOD OF RE WHICH RETURNS ALL THE OCCURANCES

        
        if found_pattern is not None:
            found_pattern_start = re.search(iterpattern,temp_text_string).start()
            found_pattern_end = re.search(iterpattern,temp_text_string).end()

            j+=1 #if there is a pattern found then move to the next value in the pattern array. else move on. 
            print("-> ",iterpattern," at ",found_pattern_start," count=",count," i=",i," j=",j)
        else:
            
            break
        #print(found_pattern)
                
        #print(iterpattern)
        #found_pattern = " "
        #found_pattern_start = 0
        temp_text_string.replace(temp_text_string,temp_text_string[found_pattern_end:])
        found_pattern_start = 0
        found_pattern_end = 0
                
    temp_text_string.replace(temp_text_string,originalholder)
    i += 1
            
        #returns from end to the end of the string. 

print("finished")


#print(found_pattern)
#print(text_string[found_pattern])

#now shorten the text string to start at the end point and go again. 



