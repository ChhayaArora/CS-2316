#Chhaya Arora
#902970578
#carora3@gatech.edu
#I worked on this assignment with Marcos Valdez using only this course's materials

from tkinter import *
import csv

class TSwift:
    def __init__ (self,root):
        self.root = root
        self.root.title ("Who won the Grammy?")
        
        ##create the welcome  
        self.label1 = Label (self.root, text = "Welcome to the 2015 Grammys!", font = ("Helvetica", int(20))) 
        self.label1.grid(row = 0, columnspan = 3)
        
       ## create frames that you'll use later
                # for the nomination category
        self.frame1 = Frame (self.root, borderwidth = 1, relief = SOLID)
        self.frame1.grid(row = 3, column = 0)
                # for the labels
        self.frame2 = Frame (self.root, borderwidth = 1, relief = SOLID)
        self.frame2.grid(row = 3, column = 1)
                # for the winner
        self.frame3 = Frame (self.root, borderwidth = 1, relief = SOLID)
        self.frame3.grid(row = 3, column = 2)
        self.count = 0 

       ## create the entries and buttons 
        
        self.entry1 = Entry(self.root, width = 30, state = NORMAL)
        self.entry1.grid(row = 1, column = 0)
              
        self.button1 = Button(self.root, text = "Select File", font = ("Helvetica", int(12)), command=self.loadFile)
        self.button1.grid(row = 1, column = 1 )
        self.button2 = Button(self.root, text = "Get the Nominees", font = ("Helvetica", int(12)), command = self.getNominees)
        self.button2.grid(row = 1, column = 2)
## READ ONLY FILE PATH 
        
    def loadFile (self):
        self.root.fileName = filedialog.askopenfilename(filetypes = (("CSV Files", "*.csv"), ("All files", "*.*")))
        self.entry1.delete(0,END)
        self.entry1.insert(0, self.root.fileName)
        self.entry1.config(state="readonly")

    def getNominees (self):
        try:
            self.file = open(self.root.fileName)
            reader = csv.reader(self.file)

            ## so many empty lists; forgive me :(
            data = []
            categories = []
            artistSong = []
            smallArtistSongList = []
            bigArtistSongList = []
            newArtistList = []
            artists = []
            self.aDict = {}

            ## puts all the categories into a list 
            for i in reader:      
                data.append (i)
            newData = data[1:]      #gets rid of the heading

          
            ## gives you just the categories
            for nestedList in newData:
                categories.append(nestedList[0])
            
            ## give you the song-artist list without the categories 
            for nestedList in newData:
                smallArtistSongList.append(nestedList[1:])


            ## splits everything by commas to make a nested individual song-artist list 
            for aList in smallArtistSongList:
                for song in aList:
                    y = song.strip().split(",")
                    bigArtistSongList.append(y)
            
            
            ## gives you all of the artists in one big list
            for aList in bigArtistSongList:
                try:          #get the artists and not the songs
                    artists.append(aList[1])
                except:       #get just the artists for the best artist case
                    if len(aList) == 1:
                        artists.append(aList[0])
        
            for artist in artists:
                newArtist = artist.lstrip(). strip(' " ')
                newArtistList.append(newArtist)
                
            ##make everything into a dictionary                       
            start = 0
            end = 5
            for each in categories:
                self.aDict[each] = newArtistList[start:end]
                start += 6
                end += 6

          
            self.showNominees ()
        except: 
            messagebox.showerror("Error", "There was an error with your file!")
        
    def showNominees (self):
        self.label2 = Label(self.frame1, text = "Nomination Categories", font = ("Helvetica", int(18)))
        self.label2.pack(side = TOP)

        #create a radiobutton and loop over it
        
        self.v = StringVar ()
        self.v.set("Random")
        for key in self.aDict.keys():
            Radiobutton (self.frame1, text = key, variable = self.v, value = key, command = self.saveValue).pack(anchor = NW)
            

    def saveValue (self):
        global v
        categoryName = self.v.get()
        # get all of the values from the dictionary given the category in a list format
        self.nominees = list(self.aDict[categoryName])
        

        #allows the user to go through and choose different radibuttons by previously destroying and creating a new one
        if self.count != 0:
            self.frame2.destroy ()
            self.frame2 = Frame(self.root,borderwidth = 1, relief = SOLID).grid(row = 3, column = 1)
        self.frame2 = Frame(self.root,borderwidth = 1, relief = SOLID)
        self.frame2.grid(row = 3, column = 1)

        #displays the nominees 
        for each in self.nominees:
            Label (self.frame2, text = each, state = NORMAL).pack(anchor = W)
        self.count += 1

        #creates the winner and entry boxes
        self.nominee = StringVar()
        Label (self.frame3, text = "Winnner:", state = NORMAL).grid(row = 0, column = 0)
        Entry (self.frame3, width = 20, textvariable = self.nominee).grid (row = 0, column = 1)
        Button (self.frame3, text = "Give them an award!", command = self.kanyeFactor).grid (row = 0, column =2)

            
    def kanyeFactor (self):
        for each in self.nominees:
            counter = 0
            if self.nominee.get() in each:
                self.root.withdraw()
                self.message = Toplevel ()
                self.message.title("Who won the grammy?")
                CongratsText = "Congratulation {0} for winning a grammy for {1}".format(self.nominee.get(), self.v.get())
                self.labelCongrat = Label(self.message, text = CongratsText, font = ("Verdana", int(15)))
                self.labelCongrat.pack()
                self.close1 = Button(self.message, text = "Close", command = self.closeWindow)
                self.close1.pack()
                if "Beyonce" in self.nominees and "Beyonce" != self.nominee.get():
                    self.message.withdraw()
                    kanyeText = "{0} I'mma let you finish, but Beyonce had the {1} of all time!".format(self.nominee.get(),self.v.get())
                    self.kanyeMessage = Toplevel()
                    self.kanyeMessage.title("Who won the grammy?")
                    self.labelKanye = Label(self.kanyeMessage, text=kanyeText, fg = "red", font = ("Comic Sans MS", int(30)))
                    self.labelKanye.pack()
                    self.close2 = Button(self.kanyeMessage, text = "Close", command = self.closeWindow2)
                    self.close2.pack()
                   
            else:
                counter = counter + 1
                if counter == 5: 
                    messagebox.showerror ("Error", "He/She is not a nominee")
            
    def closeWindow (self):
        self.message.destroy()
        self.root.deiconify ()
        
    def closeWindow2(self):
        self.kanyeMessage.destroy()
        self.root.deiconify()
                


root = Tk ()
app = TSwift(root)   
root.mainloop ()
