## HW 10
## Chhaya Arora
## I worked on this assignment alone using only this course's materials

import urllib.request
from tkinter import *
import datetime
from datetime import timedelta


import xml.etree.ElementTree as etree 

class GUI:
    def __init__(self, window): 
        self.window = window
        button = Button(self.window, text = "Download File", command = self.clicked)
        button.pack()

    def clicked(self):
        try: 
##            data = urllib.request.urlopen('http://www.ibm.com/software/support/lifecycle/rss/PLCWeeklyXMLDownload.xml')
            data = urllib.request.urlopen('http://www-01.ibm.com/software/support/lifecycleapp/data/PLCXMLDownload.wss?days=3&event=ALL&rss=sp&ca=rssplc&ibm-submit=Download')

            tree = etree.parse(data)
            self.root = tree.getroot()
            self.download()
        except:
            messagebox.showerror("Error", "There was an error downloading the file")
            raise

    def download(self):
        #create one master list which will have everything you need
        ## the for loops basically go through each indentation of a tree
        self.masterList = []
        #go through root of the tree which records
        for SWBranches in self.root.findall("SWTitleRecord"):
            #go through all of the title in titles
            for title in SWBranches.findall("SWTitle"):
                softwareTitle = title.text
                #print (title.text)
            for versions in SWBranches.findall("Versions"):
                #go through all of the versions
                for version in versions.findall("Version"):
                    versionNum = version.find("versionNumber")
                    #print(versionNum.text)
                    softwareVersionNum = versionNum.text
                    #for relase modules in versions
                    for releaseMods in version.findall("Release_Mods"):
                            # For all of the information in release mod
                        for releaseMod in releaseMods.findall("Release_Mod"):
                            miniList = [softwareTitle, softwareVersionNum]
                            releaseNum = releaseMod.find("releaseNumber")
                            #print(releaseNum.text)
                            miniList.append(releaseNum.text)
                            modLevel = releaseMod.find("modLevelNumber")
                            #print(modLevel.text)
                            miniList.append(modLevel.text)
                            for item in releaseMod:
                                if item.tag == "PLCInfo":
                                   self.eosDate = item.attrib["eosDate"]
                            miniList.append(self.eosDate)
                            #print(self.eosDate)
                            self.masterList.append(miniList)
                            #eos = releaseMod.attrib["eosDate"]

    
        messagebox.showinfo("Downloaded Succeeded", "Downloaded succeeded. Press okay to save your file!")
        
        self.filter()

        #print(self.masterList)
        
    def filter(self):
        monthDict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun": 6, "Jul":7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        dateToday = datetime.datetime.today ()
        
        delta365 = timedelta(days = 365)
        dateToday365 = dateToday + delta365
        counter = 0
       
        self.filteredList = []
              
        while counter < len(self.masterList):
            try:

               junkyEosDate = self.masterList[counter][4]
               eosDate = junkyEosDate[0:2]
               eosStringMonth = junkyEosDate[3:6]     #3 letter month
               #print('month', eosStringMonth)
               eosMonth = monthDict[eosStringMonth]    #numerical month
               #print("numerical month", eosMonth)
               eosYear = junkyEosDate[9:11]

               eosStringDate = str(eosDate)+ " "+ str(eosMonth)+ " "+ str(eosYear)    ## numerical
               eosOldTime = datetime.datetime.strptime(eosStringDate, "%d %m %y")
               
               delta = timedelta(days = 365)

                           
               #comparisionTime = eosOldTime -  delta
               #print("OLD TIME", eosOldTime, "COMPARISION TIME", comparisionTime)
               
               if dateToday < eosOldTime and eosOldTime < dateToday365:
                   self.filteredList.append(self.masterList[counter])
                   ## keep it
               else:
                   del self.masterList[counter]
               #if compparisionTime > eosOldTime and oldTime > dateToday:
                   #del self.masterList[counter]

                #check if old time is between comparision date and today date
        
               ## get the difference between the two days
##               difference = dateToday - oldTime
##               if difference[0] > 365 or  difference[0] < 0 :
##                   del self.masterList[counter]
                   
                    
            except:
               
                del self.masterList[counter]


            counter = counter + 1
            

        
            

        
        self.writeXML(self.filteredList)
                          
    def writeXML (self,filteredList):
        answer = messagebox.askyesno ("Save", "Do you want to save this file as an XML?")
        print(answer)
        if answer == True:

        
            t = filedialog.asksaveasfilename()
            
           
            filteredListroot = etree.Element ('packages')
            

            for each in filteredList:
                SWtitle = each[0]
                VersionNumber = each[1]
                ReleaseNumber = each[2]
                ModLevelNumber = each [3]
                EOSText = each[4]
                node = etree.Element("package", eosDate = str(EOSText), modLevelNum = str(ModLevelNumber), releaseNum = str(ReleaseNumber), versionNum = str(VersionNumber))
                node.text = SWtitle

                filteredListroot.append(node)

            tree = etree.ElementTree(filteredListroot)
            tree.write(t, 'UTF-8')
            
        else:
            self.clicked()
        
      
        ## create a dictionary with a month and 
            
                        
            

window = Tk ()
app = GUI (window)
window.mainloop ()

