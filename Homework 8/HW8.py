#Chhaya Arora
#902970578
#I worked on this assignment alone using only this course's materials


##import everything 
import urllib.request
from tkinter import*
from re import findall
import csv

class GUI:
    def __init__(self, root):
        #self referencing window
        self.root = root


    ##EVERYTHING GUI RELATED
        
        #string variables for the entries
        self.sv1 = StringVar ()
        self.sv2 = StringVar ()
        self.sv3 = StringVar ()


        #all the entries 
        self.entry1 = Entry (self.root, textvariable = self.sv1, width = 60)
        self.entry1.grid (row = 3, column = 1)
        self.entry1.config(state = "readonly")
        
        self.entry2 = Entry (self.root, textvariable = self.sv2, width = 60)
        self.entry2.grid(row = 4, column = 1)
        
        self.entry3 = Entry (self.root, textvariable = self.sv3, width = 60)
        self.entry3.grid(row = 5, column = 1)
        self.entry3.config(state = "readonly")

        ## all the buttons 
        self.button1 = Button(self.root, text = "Load Input CSV File", command = self.loadCSVclicked)
        self.button1.grid(row = 1, columnspan = 2, sticky = EW)
        self.button2 = Button (self.root, text = "Process Data", command = self.PDclicked)
        self.button2.grid(row = 6, columnspan = 2, sticky = EW)
        self.button2.config(state = DISABLED)

        #lonely label 
        self.label1 = Label(self.root, text = "File Path")
        self.label1.grid(row = 2, columnspan = 2)

        #more side labels        
        self.label2 = Label(self.root, text = "Input CSV File")
        self.label2.grid(row = 3, column  = 0)
        self.label3 = Label(self.root, text = "Website URL")
        self.label3.grid(row = 4, column = 0)
        self.label4 = Label(self.root, text = "Output CSV File")
        self.label4.grid(row = 5, column = 0)

        ###ALL DEM LABELS
        ## for each of the cities and the dashes 

        self.label5 = Label(self.root, text = "Average Order Per City:")
        self.label5.grid(row = 0, column = 2, sticky = W)
        self.label6 = Label(self.root, text = "London")
        self.label6.grid(row = 1, column = 2, sticky = EW)
        self.label7 = Label(self.root, text = "-")
        self.label7.grid(row = 1, column = 3, sticky = E) 
        self.label8 = Label(self.root, text = "Manchester")
        self.label8.grid(row = 2, column = 2, sticky = EW)
        self.label9 = Label(self.root, text = "-")
        self.label9.grid(row = 2, column = 3, sticky = E)
        self.label10 = Label(self.root, text = "Bimingham")
        self.label10.grid (row = 3, column = 2, sticky = EW)
        self.label11 = Label (self.root, text = "-")
        self.label11.grid(row = 3, column = 3, sticky = E)
        self.label12 = Label(self.root, text = "Leeds")
        self.label12.grid(row = 4, column = 2, sticky = EW)
        self.label13 = Label(self.root, text = "-")
        self.label13.grid(row = 4, column = 3, sticky = E)
        self.label14 = Label(self.root, text = "Liverpool")
        self.label14.grid (row =5, column = 2, sticky = EW)
        self.label15 = Label(self.root, text = "-")
        self.label15.grid(row = 5, column = 3, sticky = E)
        self.label16 = Label(self.root, text = "2013 Total Orders:")
        self.label16.grid(row = 6, column = 2, sticky = EW)
        self.label17 = Label(self.root, text = "2014 Total Orders:")
        self.label17.grid(row = 7, column = 2, sticky = EW)
        self.label18 = Label(self.root, text = "-")
        self.label18.grid(row = 6, column = 3, sticky = E)
        self.label19 = Label(self.root, text = "-")
        self.label19.grid(row = 7, column = 3, sticky = E)

        #i now realize a for loop would have been much easier
        #but i've typed way too much to go back now
        

    def loadCSVclicked(self):

        #open the file dialong
        self.root.fileName = filedialog.askopenfilename()
        #call the CSV file function 
        self.root.newFile = self.loadCSVfile(self.root.fileName)

        #if the file is from newFile is a list then put it in the entry box
        if type(self.root.newFile) == list:
            objVar = self.root.newFile
            self.entry1.config(state=NORMAL)
            self.entry1.delete(0,END)
            self.entry1.insert(0, self.root.fileName)
            self.entry1.config(state="readonly")
            self.button2.config(state=NORMAL)

        #else, show an error
        else:
            messagebox.showerror("Error", "There was an error with your file!")
    

    def loadCSVfile(self,aFile):

        #try opening and reading the csv file, and if you can, make a list of it
        try:
            self.data = []
            f = open(aFile, "r")
            reader = csv.reader(f)
            for each in reader:
                self.data.append(each)
            return self.data
        
        #if you can't, then show an error            
        except:
            if self.messagebox.showerror == True:  
                return None

    def PDclicked(self):

    #try calling all these functions connected to the buttons
        
        #get the entry that the user typed
        self.urlName = self.sv2.get()
        
        #call all these functions
        self.downloadSalaryData(self.urlName)
        self.newData = self.convertHTMLtoCSVFormat(self.text)
        self.mergeData(self.cList)
        self.saveData(self.masterDict)
        self.calculate(self.finalList)
        

        #else, show an error
##        except:
##            messagebox.showerror("Error", "URL or Data Invalid!")
##            return None

    def downloadSalaryData(self,url):
        try: 
            webpage = urllib.request.urlopen(self.urlName)
            data = webpage.read()
            webpage.close()
            self.text = data.decode ()
            return self.text
            
        except:
            messagebox.showerror("Error","There was an error!")
            return None
    def convertHTMLtoCSVFormat(self,aStr):
        self.everything = findall("<td>([A-Za-z].+)</td><td>(.+)</td><td>(.+)</td><td>([^<].+)</td>",self.text)
        self.nestedList = []
        #converts the tuple into a nested list
        for each in self.everything:
            newEach = list(each)
            self.nestedList.append(newEach)
        #print("NEW LIST",self.nestedList)

        #nested list of all of the names in the order: last name, first name
        self.cList = []
        for each in self.nestedList[1:]:
            #create a new list each time to make a nested list 
            bList = []
            #split the names into first and last names
            splittedEach = each[0].split(" ")
            #print(splittedEach)
            lastName = splittedEach[0].replace(splittedEach[0], splittedEach[1])
            firstName = lastName.replace(splittedEach[1],splittedEach[0])
            
            bList.append(lastName)
            bList.append(firstName)

            #append each of the lists into a big list
            self.cList.append(bList)
        

        ## append the cities to the the each of the nestedList
        counter = 1
        for aList in self.cList:
            aList.append(self.nestedList[counter][3])
            counter = counter + 1
       
        ## append the 2013 and 2014 orders 
        counter = 1
        for aList in self.cList:
            aList.append(self.nestedList[counter][1])
            aList.append(self.nestedList[counter][2])
            counter = counter + 1

        ##insert the first line
        self.cList.insert(0,['Last Name', 'First Name', 'City', '2013 Units Ordered', '2014 Units Ordered'])
        return self.cList
        #print("finalList", self.cList)
    
    def mergeData(self, data):
        #self.cList = list from the web
        #self.data = list from the csv file
    
        csvDict = {}
        for each in self.data[1:]:
            csvDict[(each[0],each[1])] = each[2:]
        #print("CSV",csvDict)

        htmlDict = {}
        for each in self.cList[1:]:
            htmlDict[(each[0],each[1])] = each[2:]
        #print("HTML",htmlDict)

        #compare the two dictionaries to see what names are in what

        #list of names that are only in the html and not in csv file 
        notinCSVList = []
        notinhtmlList = []
        shared =[]
        self.masterDict = {}


        ## find out which names are both in the html and csv file 
        for each in htmlDict:
            csvkeyList = list(csvDict.keys())
            if each in csvkeyList:
                shared.append(each)
        #print ("SHARED",shared)

        ## find out which ones are only in the html and not in the CSV file 
        for each in htmlDict:
            csvkeyList = list(csvDict.keys())
            if each not in csvkeyList:
                 notinCSVList.append(each)
        #print("NOT IN CSV", notinCSVList)

        ## find out which ones are only in the csv and not in the html file 
        for each in csvDict:
            htmlkeyList = list(htmlDict.keys ())
            if each not in htmlkeyList:
                notinhtmlList.append(each)
        #print("NOT IN HTML", notinhtmlList)


        ## put them into a master dictionary 
        for each in notinCSVList:
            self.masterDict[each] = htmlDict[each]
        for each in notinhtmlList:
            self.masterDict[each] = csvDict[each]

     
        
        ## account for the ones where the information is split into two

        for each in shared:

            ## im sorry i couldn't think of a smarter way :(
            csvValue1 = csvDict[each][1]
            csvValue2 = csvDict[each][2]
            htmlValue1 = htmlDict[each][1]
            htmlValue2 = htmlDict[each][2]

            #print("EACH", each)
        #everything dealing with the first value
            
            #if the value is a dash then keep it a dash 
            if csvValue1 == "-" and htmlValue1 == "-":
                self.masterDict[each][1] == "-"

                
            #if the html has something
            if csvValue1 == "-" and htmlValue1 != "-":
                #aList = for people who have csv1 as a dash
                aList = []
                aList.append(csvDict[each][0])
                aList.append(htmlValue1)
                self.masterDict[each] = aList

                
            #if the csv has something
            if htmlValue1 == "-" and csvValue1 != "-":
                #bList = for people who have html1 as a dash
                bList = []
                bList.append(csvDict[each][0])
                bList.append(csvValue1)
                self.masterDict[each] = bList
                
            
            if csvValue1 != "-" and htmlValue1 != "-":
                fList = []
                fList.append(csvDict[each][0])
                fList.append(csvValue1)
                self.masterDict[each] = fList
                
                
        #everything dealing with the second value

            #if both of the values are dashes 
            if csvValue2 == "-" and htmlValue2 == "-" :
                self.masterDict[each][2] == "-"
                
            #if the html has something
            if csvValue2 == "-" and htmlValue2 != "-":
                ## create and append lists in order to make sure every value is being added in the order that it needs to be in
                cList = []
                cList.append(csvDict[each][0])
                if csvValue1 != "-": 
                    cList.append(csvDict[each][1])
                elif htmlValue1 != "-":
                    cList.append(htmlDict[each][1])
                else:
                    cList.append("-")
                cList.append(htmlValue2)
                self.masterDict[each] = cList
                
            if csvValue2 != "-" and htmlValue2 == "-":
                dList = []
                dList.append(csvDict[each][0])
                if csvValue1 != "-": 
                    dList.append(csvDict[each][1])
                elif htmlValue1 != "-":
                    dList.append(htmlDict[each][1])
                else:
                    dList.append("-")
                dList.append(csvValue2)
                self.masterDict[each] = dList
                
            
            if csvValue2 != "-" and htmlValue2 != "-":
                eList = []
                eList.append(csvDict[each][0])
                if csvValue1 != "-":
                    eList.append(csvDict[each][1])
                elif htmlValue1 != "-":
                    eList.append(htmlDict[each][1])
                else:
                    eList.append("-")
                eList.append(csvValue2)
                self.masterDict[each] = eList
                
        
        #print("MASTER I AM YOUR MASTER", self.masterDict)
             
            

    def saveData(self, aDict):
        finalList = []
        finalList2 = []
        
        for each in self.masterDict:
            #make the names into a strin
            names = each[0]+ "," + each[1]
            #get the values
            valueList = self.masterDict.get(each)
            valueList.insert(0,names)
            finalList.append(valueList)
        
        listOne = []
        listTwo = []
        listThree = []
        #create three separate lists so you can sort it accordingly 
        for each in finalList:
            if each[2] == "-":
                listTwo.append(each)
            elif each[3] == "-":
                listThree.append(each)
            else:
                listOne.append(each)
        #sort the list 
        listOne.sort ()
        listTwo.sort()
        listThree.sort()

        #append it to a big list
        finalList2.append(listOne)
        finalList2.append(listTwo)
        finalList2.append(listThree)

        #print("FINAL LIST", finalList2)

        self.finalList = finalList2
                
        saveFile = filedialog.asksaveasfilename()
        self.sv3.set(saveFile)
        f = open (saveFile, "w")
        writer = csv.writer(f, lineterminator = "\n")
        writer.writerows(valueList)
        f.close()
         
    def calculate(self,arg):
        #create all these counters and orders
        #print('got here')
        Manchcounter = 0
        Livercounter = 0
        Leedscounter = 0
        Londoncounter = 0
        Bircounter = 0
        Manchorder = 0
        Liverorder = 0
        Leedsorder = 0
        Londonorder = 0
        Birmorder = 0
        total2013 = 0
        total2014 = 0
        for each in self.finalList:
            for each2 in each:
                if each2[1] == "Manchester":
                    if each2[2] != "-":
                        Manchcounter += int(each2[2])
                        Manchorder += 1
                    if each2[3] != "-":
                        Manchcounter += int(each2[3])
                        Manchorder +=1
                    try: 
                        Manchaverage = Manchcounter/Manchorder
                        self.label9.config(text = Manchaverage)
                    except:
                        pass
                if each2[1] == "Liverpool":
                    if each2[2] != "-":
                        Livercounter += int(each2[2])
                        Liverorder += 1
                    if each2[3] != "-":
                        Livercounter= int(each2[3])
                        Liverorder +=1
                    try: 
                        Liveraverage = Livercounter/Liverorder
                        self.label15.config(text = Liveraverage)
                    except:
                        pass
                    
                if each2[1] == "Leeds":
                    if each2[2] != "-":
                        Leedscounter += int(each2[2])
                        Leedsorder += 1
                    if each2[3] != "-":
                        Leedscounter += int(each2[3])
                        Leedsorder +=1
                    try:
                        Leedsaverage = Leedscounter/Leedsorder
                        self.label13.config(text = Leedsaverage)
                        #print(Leedsaverage)
                    except:
                        pass
                    
                if each2[1] == "London":
                    if each2[2] != "-":
                        Londoncounter += int(each2[2])
                        Londonorder += 1
                    if each2[3] != "-":
                        Londoncounter += int(each2[3])
                        Londonorder +=1
                    try:
                        Londonaverage = Londoncounter/Londonorder
                        self.label7.config(text=Londonaverage)
                        #print(Londonaverage)
                    except:
                        pass
                    
                if each2[1] == "Birmingham": 
                    if each2[2] != "-":
                        Bircounter += int(each2[2])
                        Birmorder += 1
                    if each2[3] != "-":
                        Bircounter += int(each2[3])
                        Birmorder +=1
                    try:
                        Birminghamaverage = Bircounter/Birmorder
                        self.label11.config(text=Birminghamaverage)
                        #print(Birminghamaverage)
                    except:
                        pass
                    
            
        for each in self.finalList:
            for each2 in each:            
                if each2[2] != "-":
                    total2013 += int(each2[2])
                if each2[3] != "-":
                    total2014 += int(each2[3])
        self.label18.config(text = total2013)
        self.label19.config(text = total2014)
            

## two different dictionaries
##two different lists - stuff that was in the csv file, but not the html
        #stuff that was in the html, but not the file
        #stuff that's both in the html and file
    ## first two lists in the master dict

    ## 





root = Tk ()
app = GUI(root)
root.mainloop ()
