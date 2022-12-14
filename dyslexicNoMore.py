from PyPDF2 import PdfReader
#A small app to enable the parsing of text into a more dyslexic friendly format.
#Concept is to allow user to drop in file and then we parse that and embolden the first couple of letters of each word.


#Create  markdown
#parse input into markdown
#Format in text file
#output back to the user
#once functionality is complete, create a nice UI


#====================================================THE TEXT APPENDER===============================================================#
#for i in text:
    #if i.length <=2 bold first char
    #if i.length == 3 bold first 2 char
    #else bold 3 chars

#boilerplate 
def appendText(file):
    splitted = file.split(" ")
    friendly = []
    print (splitted)
    for word in splitted:
        if word == ('\n'):
            break
        if (len(word) <= 2):
            #print("1")
            friendly.append(("**" + word[0:1] + "**" + word[1:]))
        if (len(word) == 3):
            friendly.append(("**" + word[0:2] + "**" + word[2:]))
           #print("2")
        if (len(word) >= 4):
            friendly.append(("**" + word[0:4] + "**" + word[4:]))
            #print("3")
    new = (" ").join(friendly)
    return (new)

#appendText("Hi I eat sausages every day")


#====================================================THE FILE HANDLER ===============================================================#
#====================THE GET FILE HANDLER =============================#
#take user file
#convert to markdown
#send raw text to text appender
#get back text and output as a .md file or even pdf if possible
def getFile(userInput):

    reader = PdfReader(userInput)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + '\n'
    #send the parse to append function for formatting
    done = appendText(text)
    print (done)
getFile("example.pdf")
#====================THE MAKE MD FILE HANDLER =============================#
#Now that the PDF has been read and formatted we wanna output it to MarkDown.
def newFormat():
    return 0