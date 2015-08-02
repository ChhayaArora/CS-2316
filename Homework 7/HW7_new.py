#Chhaya Arora
#902970578
#I worked on this assignment alone using this course's materials

import urllib.request
from tkinter import*
from re import findall


    
class GUI:
    def __init__(self,root):
        self.root = root
        self.root.title("GUESS WHAT I'M GONNA SHOW YOU")
        mainButton = Button (self.root, text = "GET SUPER COOL SUPER SECRET INFO", command = self.getInfo)
        mainButton.pack ()
        
    def getInfo(self):
        
        #get all this information from your website 
        webpage = urllib.request.urlopen ("http://www.nytimes.com/best-sellers-books/young-adult/list.html")
        data= webpage.read()
        webpage.close ()
        text = data.decode ()

        
        #create a bunch of empty lists
        self.bigList = []
        self.authorName = []
        self.descriptions = []

        #dictionary of everything
        self.aDict = {}    #for keys as being author names
        self.bDict = {}    #for keys as being book titles

        #use of some really awesome regex

        self.bookTitles = findall ("""bookName">(.+), <""", text)   #list of all the book names 
        self.everythingElse = findall (""" </span>(.+)             </td>""", text)


        #create a big list of all the descriptions, authors, and more 
        for each in self.everythingElse:
            newEach = each.split(".")
            self.bigList.append(newEach)

        #create a list of all of the author names 
        for each in self.bigList:   
            self.authorName.append(each[0])

        #create a list of all of the descriptions 
        for each in self.bigList:
            newEach = each[2]
            newEach2 = newEach.strip(")")
            self.descriptions.append(newEach2)

        #deiconify root window
        self.root.withdraw()

       
        #main top level window with the option to pick author, name
        self.mainToplevel = Toplevel ()
        self.mainToplevel.title("New York Times Best-Selling Books for YA")

    
        label1 = Label (self.mainToplevel, text = "Best-Selling Books for Young Adults", font = ("Helvetica", int(19)))
        label1.pack (side = TOP)
        label2 = Label (self.mainToplevel, text = "Pick a category through which you want to see the books",font = ("Helvetica", int(12)))
        label2.pack (side = LEFT)

        button1 = Button (self.mainToplevel, text = "Author", font = ("Helvetica", int(14)), command = self.author)
        button1.pack (side = TOP)
        button2 = Button (self.mainToplevel, text = "Title", font = ("Helvetica", int(14)), command = self.title)
        button2.pack(side = TOP)

    def author (self):
        self.cleanAuthorName = []
        self.authorList = []
        self.mainToplevel.withdraw()
        self.authorWindow = Toplevel ()
        self.authorWindow.title ("Pick by an author")
        self.sv1 = StringVar ()
        self.sv1.set ("WHATEVER") #so nothing is clicked

        
        
        for each in self.authorName:
            self.cleanAuthorName = each.strip("by ")
            self.authorList.append(self.cleanAuthorName)
        
        
        #self.singleAuthorName = list(set(self.cleanAuthorName))

    
        self.setList = list(set(self.authorList))
        
        for self.author in self.setList:  #self.authorList
            
                Radiobutton (self.authorWindow, text = self.author, variable = self.sv1, value = self.author, font = ("Helvetica", int(12)), command = self.infoBox).pack(side=TOP, anchor = W)   #creates all the buttons for all the authors 
                
        #first dictionary with all of the keys as being the names of the author (with by attached) and the book titles 
        for each in range(len(self.authorList)):
            ## check with the if statement the item is already in the dictionary, if it is then add to the list. If it isn't, then create a new key/value pair. 
            if self.authorList[each] in self.aDict:
                self.aDict[self.authorList[each]].append(self.bookTitles[each])
                self.aDict[self.authorList[each]].append(self.descriptions[each])
            else:
                self.aDict[self.authorList[each]] = [self.bookTitles[each], self.descriptions[each]]  #notice that the value is a single item list

        
    def infoBox (self):
            name = self.sv1.get()
           
            everything = self.aDict[name]
            
            self.authorVarWindow = Toplevel ()    #create a top level window to display descriptions for whatever author is picked
            #create a name label
            for each in range(len(everything)):
                if each%2 == 0:
                    descriptionLabel = Label(self.authorVarWindow, text = everything[each], font = ("Helvetica", int(18)))
                    descriptionLabel.pack(side = TOP)
                    authorLabel = Label (self.authorVarWindow, text = name, font = ("Helvetica", int(12)))
                    authorLabel.pack(side = TOP)
                else:
                    titleLabel = Label(self.authorVarWindow, text = everything[each], font = ("Helvetica", int(12)))
                    titleLabel.pack (side = TOP)     
            
            
        

### ENTRY BOXES: textvariables
### EVERYTHING ELSE (BUTTONS, RADIOBUTTONS, LABELS) = variable 
   




    def title (self):
        self.sv2 = StringVar ()
        self.sv2.set ("UGH")
        self.TitleWindow = Toplevel ()
        for each in self.bookTitles:
            Radiobutton(self.TitleWindow, text = each, value = each, variable = self.sv2, font = ("Helvetica", int(12)), command = self.infobox2).pack(side = TOP, anchor = W)
            
    def infobox2 (self):
        self.TitleWindow.withdraw()
        name = self.sv2.get ()
        self.infoboxWindow = Toplevel ()

        self.authorList = []


        for each in self.authorName:
            self.cleanAuthorName = each.strip("by ")
            self.authorList.append(self.cleanAuthorName)
    

        self.upperbookTitles = []
        for each in self.bookTitles:
            newEach = each.upper()
            self.upperbookTitles.append(newEach)

        for each in range(len(self.bookTitles)):
            self.bDict[self.upperbookTitles[each]] = [self.authorList[each],self.descriptions[each]]
    
        
        everything = self.bDict[name]
        
        nameLabel = Label(self.infoboxWindow, text = name, font = ("Helvetica", int(18)))
        nameLabel.pack(side = TOP)
        for each in range(len(everything)):
            if each%2 == 0:
                descriptionLabel = Label (self.infoboxWindow, text = everything[each], font = ("Helvetica", int(12)))
                descriptionLabel.pack(side = TOP)
            else:             
                authorLabel = Label (self.infoboxWindow, text = everything[each], font = ("Helvetica", int(12)))
                authorLabel.pack(side = TOP)
        
        




root = Tk ()
app = GUI(root)
root.mainloop ()
