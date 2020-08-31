import re
import string
import time
import numpy as nmp
import nltk
import pandas
#nltk.download()
#import matplotlib.pyplot as plt
#import pandas as pd
from nltk.corpus import wordnet as wn
from datetime import datetime
from tqdm import tqdm
from tqdm import tqdm_gui
import pdfminer
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
'''
#goals: 

Further functions should be able to check if a word is a noun, verb, adjective
that should be a column 

another function should be designed to test the emotion of words and put that in a column

possibly the program could ask for certain words of interest which could recieve their own column and be combined with the other functions to find correlations. 


#to change book remove it in def removenumerics and normal main


'''

#pdf conversion section

def pdfconvert():
    #include pdfminer here
    print("converting pdf now...")
   

    output_string = StringIO()
    with open('textfromfile.pdf', 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in tqdm(PDFPage.create_pages(doc)):
            interpreter.process_page(page)

    #print(output_string.getvalue())

    pdftext = output_string.getvalue()

    return pdftext

def searchforthis(text,intext):
    #searches for this text in the pdf 
    # cases
    # 1 - week
    # 2 - Assignment
    # 3 - Discussion

    for i in tqdm(intext):

        if i == text:
            print('.',end="")

""" def changeformatforpandas():
    text_file_old = open("patterns.txt", "rw")
    text_file_new = open("patterns_pandas.txt", "w")
    text_file_new.truncate(0)#clearing the previous contents
    travolta = text_file_old.read().lower()
    text_file_new.write("Word;Frequency;Occurances")
    i = 0
    comma = ','
    newline = '\n'
    for word in travolta:
        if word == comma:
            text_file_new.write("{0}".format(';') """
        
    
        
def arrayofarrays(array):
    #create array1 = [1 2 3]
    # create array2 = [4 5 6]
    #create array3 = [array1, array2]
    return 0
       



def heatmap(var):
    # importing pandas as pd 
    import pandas as pd 
    
    # import the StrinIO function 
    # from io module 
    from io import StringIO 
    
    # wrap the string data in StringIO function 




    StringData = StringIO(var) 
    
    # let's read the data using the Pandas 
    # read_csv() function 
    df = pd.read_csv(StringData, sep =";") 
    
    # Print the dataframe 
    print(df) 

def progressbar(fulltext,iterator):
    total = len(fulltext)
    t = int(iterator)
    result =(total)/2
    result = int(result)
    percentage = total % 10
    



    if t == result:
        print("50 percent complete")
    result =(total)/3
    if t == result:
        print("30 percent complete")
    result =2*(total)/3
    if t == result:
        print("60 percent complete")
    result =3*(total)/4
    if t == result:
        print("75 percent complete")
    result =(total)/4
    if t == result:
        print("25 percent complete")
    result =(total)/1
    if t == result:
        print("10 percent complete")

def removenumerics(nothing):
    print("removenumerics")
    
    document_text = open('textfileforparse.txt', 'r')
    document_nonum = open('denumbered.txt', 'w')
    document_nonum.truncate(0)#clearing the previous contents
    print("opened documents")
    text_string = document_text.read().lower()
    fulltext = text_string
    avoids = [1,2,3,4,5,6,7,8,9,0]
    avoids_c = ['1','2','3','4','5','6','7','8','9','0']

    #specific cases
    #case1 = ".'"
    # #,#
    # '#
    # .'



    i = 0
    processed = 0
    warning = 0
    case1 = 0
    period = 0
    paren = 0
    commas = 0
    string_length = len(text_string)



    fulltext = text_string

        
    reffound = 0 #when it senses (p.#) or (name,date) IN PROGRESS

    for character in tqdm(fulltext):
        i+=1
        #progress bar shows the percentage complete
        progressbar(fulltext,i)
            #this first loop is checking the arrays for numbers that match current character. 
        x = 0
        while x < 10:
            if character == avoids[x] or character == avoids_c[x]:
                commas = 0 #reset if it is a number
                paren = 0
                warning = 1 #trip the warning to be caught by next if statement below
                    #means that there was a number found.
                    #print(character,end="")
            x+=1
        x = 0 #reset iterator for this while loop
        if character == ',':
            commas+=1
        if character == '.':
            period+=1
        if character == "'":
            paren+=1
        if commas >= 3 and paren >= 2:
            warning = 1
        if period >= 1 and paren >= 1:
            warning = 1
            period = 0
            paren = 0
        if warning < 1 and character != ',': #indicates the character is not a number
                
            document_nonum.write("{0}".format(character))
            processed+=1 #add one processed element. 
            warning = 0 #reset trip wire
        
                
        warning = 0
    i+=1







    '''
    while i<string_length:
        fulltext = text_string

        #progress bar shows the percentage complete
        progressbar(text_string,i)

        for character in fulltext:
            
            #this first loop is checking the arrays for numbers that match current character. 
            x = 0
            while x < 10:
                if character == avoids[x] or character == avoids_c[x]:
                    commas = 0 #reset if it is a number
                    paren = 0
                    warning = 1 #trip the warning to be caught by next if statement below
                    #means that there was a number found.
                    #print(character,end="")
                x+=1
            x = 0 #reset iterator for this while loop
            if character == ',':
                commas+=1
            if character == '.':
                period+=1
            if character == "'":
                paren+=1
            if commas >= 3 and paren >= 2:
                warning = 1
            if period >= 1 and paren >= 1:
                warning = 1
                period = 0
                paren = 0
            if warning < 1 and character != ',': #indicates the character is not a number
                
                document_nonum.write("{0}".format(character))
                processed+=1 #add one processed element. 
                warning = 0 #reset trip wire
                
                
            warning = 0
        i+=1

        

    document_nonum.close()
    document_text.close()
    print("successfully processed: ",processed, "replacements")
'''   
def checkfornumerics(nothing):
    print("checkfornumerics")
    document_text = open('textfileforparse.txt', 'r')
    text_string = document_text.read().lower()
    fulltext = text_string
    contains_digit = False
    
    for character in fulltext:
        if character.isdigit():
            contains_digit = True


    return contains_digit

def partone(word,typew):
    print("partone")
    lines = str(word)
    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == typew
    # do the nlp stuff
    tokenized = nltk.word_tokenize(lines)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    if nouns.__contains__(word) == True:
        return typew
    
def occurances(word,fulltext):
    #print("occurances",end = " ")
    
    #this function receives a word and returns an array of all of the occurances of the word
    #will not be efficient, but will work
    locations = []#will hold the locations found where matching words are within the kjvbible.txt
    #fulltextfile = open('1984.txt', 'r')
    #fulltext = fulltextfile.read().lower() #make lowercase to parse correctly 
    #for speed this could be done globally and save a new file with the lowercase already done 

    #check for word in index and append to index with position
    #position = re.search(word, index)

    fulltext = fulltext.split() # to seperate the sentence into its word for analysis. now the item below 
    #refers to a word not letter
    position = 0 # this is an initilization for the iterator
    count = 0 # this iterates through the array that will be returned, it will equal number of 
    #occurances of the word in the string
    #print("*",end = "")
    for item in fulltext:
        
        position+=1
        if item == word:
            #print(position,end = ",")
            #word has been found
            #append the location to array
            #print(item," @ ",position)
            
            # -----//// these two are options of methods for saving these things. 
        
            locations.append(position) # save position in locations at index = count
            #locations[count] = position # save position in locations at index = count
            
            count += 1 #found one occurance


    
    
    #fulltextfile.close()
    #print("")
    return locations

def matrixize(array,rows,colms):
    #rows is number of words in the corpus
    #colms is the number of terms in 
    #rows,columns
    shape = (rows,colms)

""" def graphingpandas(var):
    
    plt.close('all')
    ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts = ts.plot()

    df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
    df['b'] = df['b'] + np.arange(1000)
    df.plot.hexbin(x='a', y='b', gridsize=25)

 """
    
def typeofword(word):
    #check what kind of word word is 
    from nltk.tokenize import word_tokenize

    #option 2

    text = word_tokenize(word)
    nltk.pos_tag(text)
    #text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
    #text.similar('woman')
    sent = str(word)
    sent2 = [nltk.tag.str2tuple(t) for t in sent.split()]
    #print(sent2[0]) 

    #from stack overflow https://stackoverflow.com/questions/33587667/extracting-all-nouns-from-a-text-file-using-nltk 
    
    partone(word,"NN")
    partone(word,"JJ")
    partone(word,"RB")
    partone(word,"CC")
    partone(word,"IN")

    
 
#cc = coordinating conjunction
#RB adverbs
#IN - preposition
#NN - a noun
#JJ - adjective.
#using the nltk is exactly what I need to do... lots of processing power. 
choice1 = 'n'

print("Entering the program -- ")
print("          MENU             ")
print("1 - pdf convert saved to file")
print("2 - frequency analysis")
print("3 - other")
menu1 = input("which program would you like to use? - ")
multarrays = []
if menu1 == 1 or menu1 == '1':
    #pdf convert 
    pdftext = pdfconvert()
    text_file_frompdf = open("textfileforparse.txt", "w")
    text_file_frompdf.truncate(0)#clearing the previous contents
    
    for word in tqdm(pdftext):   
        text_file_frompdf.write("{0}".format(word))
       

#save this to the text file textfileforparse.txt
prechoice1 = input("compute simple frequency of words or complete word analysis? f/a ")
choice4 = input("check for and remove numerical values? y/n ")
choice5 = input("web automation? y/n")

if prechoice1 == 'f':
    choice3 = True #just frequency
    choice1 = 'n'
    choice2 = 'n'
if prechoice1 == 'a':  
    choice1 = input("include the frequency as a column? y/n ")
    choice2 = input("include the type of word as column? y/n ")
#typeofword("mountain")
nothing = 1 #this is literally nothing dont bother with it.

if choice4 == 'y' or choice4 == 'Y': #if selected it will remove numbers
    contains_number = checkfornumerics(nothing)
else:
    contains_number = False
if contains_number == True:
    print("removing numerical values...")
    removenumerics(nothing)
frequency = {}
document_text = open('textfileforparse.txt', 'r')
text_string = document_text.read().lower()
fulltext = text_string
match_pattern = re.findall(r'\b[a-z]{2,15}\b', text_string)
position = {}
y = 0

text_file = open("positions.txt", "w")
text_file.truncate(0)#clearing the previous contents



iterationvar = 0
for word in tqdm(match_pattern):
    count = frequency.get(word,0)#working here
    #here = position.get(word,)
    frequency[word] = count + 1
    #position[word].append(y)

    text_file.write("{0}".format(word))
    text_file.write("[{0}]".format(iterationvar))
    #this is the original below
    """ text_file.write("{0},".format(word))
    text_file.write("{0}\n".format(iterationvar)) """
    iterationvar+=1
    #y +=1
                                #I am working in the above function. Goal: get a dictionary that is full of arrays. One array for each word with every position where it occured 
                                #in the book. This gives an idea of sentiment over time. Copy the syntax for the above frequency dictionary but implement an array instead of the 0 on the right

#also add in a word length dictionary to be able to graph that... but first position. 
#then sentiment analysis will be easier to do when we are able to assign sentiment to words. 
text_file.close()

#typeofword("Africa")


frequency_list = frequency.keys()
 
text_file = open("patterns.txt", "w")
text_file.truncate(0)#clearing the previous contents

#uncomment this section down to end of for loop for displaying the freq in the commandline
#for words in frequency_list:
    #print(words, frequency[words])

print("sorting now")

sort_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
t = 0
total = len(sort_words)

#math declarations
from datetime import date
print("processing word: ",word, "in ",total," lines...")


text_file.write("{0},".format("File_generated_"))
now = datetime.now()

text_file.write("{0}-->".format(now))
for i in tqdm(sort_words):
	#print(i[0], i[1])
    var1 = i[0]
    var2 = i[1]
    var3 = occurances(i[0],fulltext) #this is highly inefficient and is taking a long time. 
    
    text_file.write("{0},".format(var1))
    
    if choice1 == 'y' or choice1 == 'Y':
        text_file.write("{0},".format(var2))
        
        if choice2 == 'y' or choice2 == 'Y':
            var4 = typeofword(i[0]) #what kind of word is it?
            text_file.write("{0},".format(var4))
    multarrays.append(var3)#TESTING 7/30/20
    text_file.write("{0}\n".format(var3))
    if t % len(sort_words)/10 == 0:
        print(".",end="")
    
    """ result =(total)/2
    if t == result:
        print("50 percent complete")
    result =(total)/3
    if t == result:
        print("30 percent complete")
    result =2*(total)/3
    if t == result:
        print("60 percent complete")
    result =3*(total)/4
    if t == result:
        print("75 percent complete")
    result =(total)/4
    if t == result:
        print("25 percent complete")
    result =(total)/1
    if t == result:
        print("10 percent complete") """

    t+=1
   

    
    

#include a position in the book


#print("starting occurances")
#occurancesarray = occurances("just")
#print(occurancesarray)
#print(wordsarray)

#successfully implemented the occurances function. Now iterate across the index and create arrays for each of these saved to
# a matrix. 



text_file.close()










if choice5 =='y':




    # this is testing

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys


    driver = webdriver.Chrome()
    #driver.get("https://www.biblegateway.com/quicksearch/?quicksearch=summer&qs_version=KJV")
    #driver.get("https://biblehub.com/str/greek/1.htm")
    #driver.get("http://www.newjerusalem.org/Strongs/h2017?from=Strongs(h2019).Search(h2017)")
    #driver.get("https://www.eliyah.com/lexicon.html")
    #assert "Google" in driver.title
    #elem = driver.find_element_by_name("quicksearch")
    #elem = driver.find_element_by_name("quicksearch")
    #elem = driver.find_element_by_xpath("/html/body/nav[2]/div[4]/form/div[1]/div[1]/input")



    #elem = driver.find_element_by_id("yui-gen55")


    import numpy as np 
    #arr = np.stringarray((5,1))
    arr = ["heaven","hell","summer","winter","return"]

    #phrase = "Strongs H"
    i = 0
    #max = input("enter max")
    driver.get("https://biblehub.com/text/genesis/1-1.htm")
    """ for element in self.driver.find_elements_by_tag_name('txt'):
        print(element.text) """
        
    firstfield = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/table/tbody/tr/td/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[1]").getText()
    #this is the field with the results


    hubpage = open('textholder.txt', 'w')
    text_string = document_text.read().lower()
    fulltext = text_string
    hubpage.write(firstfield)
    driver.close()

    """ while i<1500:
        
        #print(arr[i])
        a = i+1
        a = str(a)
        firstfield = driver.find_element_by_xpath("/html/body/center/table/tbody/tr[3]/td[2]/form/p/input[3]")
        #firstfield.clear()
        
            
        
    
        
        firstfield.send_keys(a)#could error
        firstbutton = driver.find_element_by_xpath("/html/body/center/table/tbody/tr[3]/td[2]/form/p/input[4]")
        #/html/body/center/table/tbody/tr[2]/td[2]/form/p/submit/input
        #/html/body/center/table/tbody/tr[9]/td[2]/form/input[1]
        #firstfield.clear()
        firstbutton.click()
    
        if i<1:
            #clicking the cookies button
            cookiesbutton = driver.find_element_by_xpath("/html/body/div[18]/a")
            cookiesbutton.click()
        
        
        
        if i<=5:
            times = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[4]/div[2]/div/div/div/div[2]")
        if i>5:
            times = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/strong")
        #print("...  ")
        #print(times)
        #print("...  ")

        #driver.get_attribute(times)
        textlen = times.get_property("text_length")
        #textcontent = times.text()
        textone = times.get_property('innerText')
    # print(textone)
        #print("...  ")
        print(textone)
        #print("...  ")
        #print(textlen)
        #times.clear()
        
        #selenium.webdriver.remote.command.Command

        #textlen.clear_element


        #elem.clear()
        #firstfield.clear()
        #firstbutton.clear()
        #phrase.clear()
        #print("back")
        #driver.back()

        driver.get("https://www.eliyah.com/lexicon.html")

        #phrase = "Strongs H"
        #times.clear()
        
        i += 1 
        

    #print(arr)



    '''


    '''









    #phrase = phrase + a
        #wordholder = arr[i] #holds the string to pass to the finder function
        #elem.clear()
        #elem.send_keys(wordholder)
        #print("elem.sendkeys wordholder")
        #elem.send_keys(Keys.RETURN)
        #print("send keys")
        #assert "No results found." not in driver.page_source
        #print("finding by xpath number")
        #number = driver.find_element_by_xpath("/html/body/section[4]/form/div/div/div[1]/div[2]/div[1]/div[2]/p")
        #number = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/table/thead/tr[2]/th/span[2]")
        #print("found by xpath number")
        #print(number)
        #button clicking
        #elem = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[2]/table/tbody/tr/td/div[2]/div/p[4]/b/a[2]")
        #elem = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[1]/table/tbody/tr/td/div/a[2]")
        #saving that value
        #elem = driver.find_element_by_name("q")
        
        #elem.send_keys(phrase)
        #print("elem.sendkeys wordholder")
        #elem.send_keys(Keys.RETURN)
        #print("send keys")
        #desktopbutton = driver.find_element_by_xpath("/html/body/div[6]/form/div[2]/div[1]/div[2]/button/div/span/svg")
        #desktopbutton = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/div[1]/table/tbody/tr/td/div/a[2]")# this value changes every time you load the website to keep you from using automation.
        #desktopbutton.click()#push button for desktop view
        #assert "No results found." not in driver.page_source

        #website = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3")
        #website.click()
        #driver.find_element(By.XPATH, '(//h3)[1]/a').click()
    """

    
#print("searching for assignment")
#searchforthis("Assignment",pdftext)

# Instructor: Name Name \n 
# Required Texts
# Respond to 
# Post ... each week
#
#changeformatforpandas()
#textpandas = open("patternspandas.txt", "r")
#heatmap(text_file)
textMATCH = open("patterns.txt", "r")
#array creation

arr1 = []
arr2 = []
johncena = 0 #iteration in dynamic array matrix below
for word in tqdm(textMATCH):
    if word == '\n':
        multarrays[johncena] = arr1
        arr1.clear()
    else:
        arr1.append(word)#  TESTING DYNAMIC ARRAY 7/30/20




""" text_file = open("multpatterns.txt", "w")
text_file.truncate(0)#clearing the previous contents

print(multarrays[5])


#plotting
i = 5 # test value
import plotly.graph_objects as go
import numpy as np
top = len(multarrays[i])
x = np.arange(top)
z = multarrays
e = z[i]
y = np.array(e)
fig = go.Figure(x=x,data=y)
fig.show() """