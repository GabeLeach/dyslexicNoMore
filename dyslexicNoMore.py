import markdown
import PyPDF2
#A small app to enable the parsing of text into a more dyslexic friendly format.
#Concept is to allow user to drop in file and then we parse that and embolden the first couple of letters of each word.


#Create  markdown
#parse input into markdown
#Format in text file
#output back to the user
#once functionality is complete, create a nice UI

#for i in text:
    #if i.length <=2 bold first char
    #if i.length == 3 bold first 2 char
    #else bold 3 chars

#boilerplate 
def dyslexicNoMore(text):
    splitted = text.split(" ")
    friendly = []
    print (splitted)
    for word in splitted:
        if (len(word) <= 2):
            print("1")
            friendly.append(("**" + word[0:1] + "**" + word[1:]))
        if (len(word) == 3):
            friendly.append(("**" + word[0:2] + "**" + word[2:]))
            print("2")
        if (len(word) >= 4):
            friendly.append(("**" + word[0:4] + "**" + word[4:]))
            print("3")
    new = (" ").join(friendly)
    print (new)    

dyslexicNoMore("Hi I eat sausages every day")

#def getFile():
