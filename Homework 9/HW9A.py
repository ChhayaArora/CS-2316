#902970578
#Chhaya Arora
#carora3@gatech.edu
#I worked on this assignment alone using only this course's material

import pymysql
from tkinter import *
import urllib.request
import base64
import os


##QUESTIONS
##### WITHDRAW V. DESTROY

class HW9:
    ## initialize and create the root window
    def __init__(self, root):
        self.root = root
        self.root.title ("GTMarketPlace Login Page")
        #self.root.configure (background = "gold")
        self.login()

    #function which creates the login window 
    def login (self):

        self.connect()

        self.sv1 = StringVar()
        
        #create the 2 frames
        self.frame1 = Frame(self.root, bg = "gold")
        self.frame1.pack(side = TOP)
        self.frame2 = Frame (self.root)
        self.frame2.pack(side = TOP, fill = X)

        #the labels
        self.userLabel = Label(self.frame1, text = "Username:",bg = "gold")
        self.userLabel.grid(row = 1, column = 0, sticky = E)
        self.passwdLabel = Label(self.frame1, text = "Password:", bg = "gold")
        self.passwdLabel.grid(row = 2, column = 0, sticky = E)
    

        #the entries 
        self.userEntry = Entry(self.frame1, width = 30, textvariable = self.sv1)
        self.userEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.passwdEntry = Entry(self.frame1, width = 30)
        self.passwdEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

        #the buttons
        self.loginButton = Button (self.frame2, text = "Login", command = self.loginCheck)
        self.loginButton.pack(fill = X, anchor = E, side = RIGHT)
        self.registerButton = Button(self.frame2, text= "Register", command = self.register)
        self.registerButton.pack(fill = X, anchor = E, side = RIGHT)


        ## call the image function 
        self.imagefunction()

        self.disconnect()

    def imagefunction(self):

        url = "http://www.cc.gatech.edu/classes/AY2015/cs2316_fall/codesamples/techlogo.gif"
        u = urllib.request.urlopen(url)
        raw_data = u.read()
        u.close()

        
        self.b64 = base64.encodebytes(raw_data)
        self.image = PhotoImage(data=self.b64)
        
        self.img = Label(self.frame1, image=self.image)
        self.img.image = self.image
        self.img.grid(row = 0, column = 0, columnspan = 2)

        

    #function that gets called upon once you hit cancel that pulls up the login window again
    def login2 (self):
        
       self.register.withdraw()
       self.root.deiconify()
       
    def register (self):

        self.connect()
        
        #show only the register
        self.root.withdraw ()
        self.register = Toplevel()
        self.register.title("GTMarketPlace Register Page")

        #create the 2 frames
        self.frame1 = Frame(self.register, bg = "gold")
        self.frame1.pack(side = TOP)
        self.frame2 = Frame (self.register)
        self.frame2.pack(side = TOP, fill = X)

        #all of the labels 
        self.nameLabel2 = Label(self.frame1, text = "Full Name:",bg = "gold")
        self.nameLabel2.grid(row = 1, column = 0, sticky = E)
        self.userLabel2 = Label(self.frame1, text = "Username:", bg = "gold")
        self.userLabel2.grid(row = 2,  column = 0, sticky = E)
        self.passwdLabel2 = Label(self.frame1, text = "Password:",bg = "gold")
        self.passwdLabel2.grid(row = 3, column = 0, sticky = E)
        self.passwdLabel22 = Label(self.frame1, text = "Confirm Password:", bg = "gold")
        self.passwdLabel22.grid(row = 4, column = 0, sticky = E)

        #all of the entries
        self.nameEntry2 = Entry(self.frame1, width = 30)
        self.nameEntry2.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.userEntry2 = Entry(self.frame1, width = 30)
        self.userEntry2.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.passwdEntry2 = Entry(self.frame1, width = 30)
        self.passwdEntry2.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.passwdEntry22 = Entry(self.frame1, width = 30)
        self.passwdEntry22.grid(row = 4, column = 1, padx = 5, pady = 5)

        #all the buttons
        self.cancelButton2 = Button (self.frame2, text = "Cancel", command = self.login2)
        self.cancelButton2.pack(fill = X, anchor = E, side = RIGHT)
        self.registerButton2 = Button(self.frame2, text= "Register", command = self.registerCheck)
        self.registerButton2.pack(fill = X, anchor = E, side = RIGHT)

        self.imagefunction()

        self.disconnect()

    def connect (self):
        try:
            self.db = pymysql.connect(user = "carora3",
                                 passwd = "BssKpZPm",
                                 host = "academic-mysql.cc.gatech.edu",
                                 db = "cs2316db")
            self.c = self.db.cursor()
            
            
        except:
            messagebox.showerror("Error", "There was an error connecting with the database.")
    def disconnect (self):
        
        self.c.close()
        self.db.close()

    def loginCheck(self):
        #try to match the given user name and password

        self.connect()
        self.userEntry = self.userEntry.get()
        self.passwordEntry = self.passwdEntry.get()
        sql = """SELECT * FROM MarketPlaceUsers WHERE Username = %s AND Password = %s;"""
        num = self.c.execute(sql,(self.userEntry,self.passwordEntry))  # number of rows it grabs
        if num != 0:
            self.db.commit ()
            messagebox.showinfo("Success!","You have logged in to GTMarketPlace.")
            self.root.withdraw ()
            ## create another top level window which displays the gt market place
            self.marketPlace = Toplevel ()
            self.marketPlace.title ("GTMarketPlace")

            ## frames
            self.marketFrame1 = Frame (self.marketPlace, bg = "gold", relief = SUNKEN)
            self.marketFrame1.pack(side = TOP, fill = BOTH)
            self.marketFrame2 = Frame (self.marketPlace, bg = "gold", relief = SUNKEN)
            self.marketFrame2.pack (side = TOP, fill = BOTH)
            self.marketFrame3 = Frame(self.marketPlace, bg = 'gold', relief = SUNKEN)
            self.marketFrame3.pack(side = TOP, fill = BOTH)
            self.marketFrame4 = Frame(self.marketPlace, relief = SUNKEN)
            self.marketFrame4.pack(side = TOP)

            
            ## logout and statistics button in the main frame
            self.logoutButton = Button(self.marketFrame4, text = "Logout", command = self.logout)
            self.logoutButton.grid(row = 0, column = 0, sticky= EW)
            self.statisticsButton = Button(self.marketFrame4, text = "Statistics", command = self.statistics)
            self.statisticsButton.grid (row = 0, column = 1, sticky = EW)

            
            ##for the name label
            sql = """SELECT FullName FROM MarketPlaceUsers WHERE Username = %s AND Password = %s"""
            num = self.c.execute (sql, (self.userEntry, self.passwordEntry))
            ## gets the name of the person using fetch one, BUT IT'S A TUPLE OMG
            self.tupleName = self.c.fetchone ()
            for each in self.tupleName: 
                self.name = str(each)  ## yay now it's a string we can use
            if self.name != "None": 
                self.marketLabel1 = Label(self.marketFrame1, text = "Welcome, "+self.name, bg = "gold")
                self.marketLabel1.grid(row = 0, columnspan = 2)
            else:
                self.marketLabel1 = Label(self.marketFrame1, text = "Welcome!", bg = "gold")
                self.marketLabel1.grid(row = 0, columnspan = 2)


            ## balance and transaction amount 
            self.balanceLabel = Label(self.marketFrame1, bg = "gold", text = "Current Balance:")
            self.balanceLabel.grid(row = 1, column = 0)
            self.balanceEntry = Entry(self.marketFrame1, width = 15)
            self.balanceEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
            
            sql = """SELECT Balance FROM MarketPlaceUsers WHERE Username = %s AND Password = %s"""
            num = self.c.execute(sql, (self.userEntry, self.passwordEntry))
            #converting it from a tuple to a string
            self.tupleBalance = self.c.fetchone()
            for each in self.tupleBalance:
                self.balance = str(each)
            self.balanceEntry.insert(0, self.balance)
            self.balanceEntry.config(state = "readonly")

            self.transactionLabel = Label(self.marketFrame1, bg = "gold", text = "Trans. Amount")
            self.transactionLabel.grid(row = 2, column = 0)
            self.transactionEntry = Entry(self.marketFrame1, width = 15)
            self.transactionEntry.grid(row = 2, column = 1)
            self.transactionEntry.insert(0,"0.00")

        
            self.sv1.set ('random')
            
            ## radiobuttons
            self.withdraw = Radiobutton(self.marketFrame1, bg = 'gold', text = "Withdraw", variable = self.sv1, value = "withdraw")
            self.withdraw.grid(row = 3, column = 0)
            self.deposit = Radiobutton(self.marketFrame1, bg = 'gold', text = "Deposit",variable = self.sv1,  value = "deposit")
            self.deposit.grid(row = 3, column = 1)

            ##submit button
            self.submitButton = Button(self.marketFrame1, text = "Submit",width = 30, command = self.submit)
            self.submitButton.grid(row = 4, columnspan = 2)

            ##buy; 2nd frame
            self.buyLabel = Label(self.marketFrame2, bg = 'gold', text = "What would you like to buy?")
            self.buyLabel.grid(row = 0, columnspan = 2)

            self.itemNameLabel = Label(self.marketFrame2, bg = 'gold',  text = "Item name:")
            self.itemNameLabel.grid(row = 1, column = 0)
            self.itemNameEntry = Entry (self.marketFrame2, width = 22)
            self.itemNameEntry.grid(row = 1, column = 1, padx = 5, pady = 5)

            self.buyButton = Button (self.marketFrame2, text = "Buy", width = 30, command = self.buy)
            self.buyButton.grid(row = 2, columnspan = 2)

            ## sell; 3rd frame 
            self.sellLabel = Label(self.marketFrame3, bg = 'gold', text = "What would you like to sell?")
            self.sellLabel.grid(row = 0, columnspan = 2)

            self.itemLabel = Label(self.marketFrame3, bg = 'gold',  text = "Item name:")
            self.itemLabel.grid(row = 1, column = 0)
            self.itemEntry = Entry (self.marketFrame3, width = 22)
            self.itemEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
            self.priceLabel = Label(self.marketFrame3, bg = 'gold', text = "Price")
            self.priceLabel.grid(row = 2, column = 0)
            self.priceEntry = Entry (self.marketFrame3, width = 22)
            self.priceEntry.grid(row = 2, column = 1)
            self.priceEntry.insert(0, "0.00")

            self.sellButton = Button (self.marketFrame3, text = "Sell", width = 30, command = self.sell)
            self.sellButton.grid(row = 3, columnspan = 2)            
            
            
        #if you can't match it, then display this error
        else:
            messagebox.showerror("Error", "There was an error connecting with the database.")

        self.disconnect()
       
    def registerCheck(self):
        self.connect ()
        self.c = self.db.cursor ()
        fullName = self.nameEntry2.get()
        userEntry = self.userEntry2.get()
        password = self.passwdEntry2.get()
        confirm = self.passwdEntry22.get()

        try: 
            #find out if the username already exists
            sql = """SELECT * FROM MarketPlaceUsers WHERE Username = %s"""
            num = self.c.execute(sql,userEntry)
            self.db.commit()
            ## if the username doesn't exist
            if num == 0:
                ## if the password contains 5 characters
                if len(password) >= 5:
                    ## if there is an integer in the password
                    for each in password:
                        try:
                            if each in '1234567890':
                        #if password matches confirm password
                                if password == confirm:
                                ## insert the entry into the database
                                    ## if the fullname isn't given
                                    if fullName == "":
                                        sql = """INSERT INTO MarketPlaceUsers (Username,Password, Balance) VALUES (%s, %s, %s)"""
                                        row = self.c.execute(sql,(userEntry,password, "50.00"))
                                        self.db.commit()
                                        messagebox.showinfo("Success!", "You have successfully registered")
                                        self.login2()
                                    else: 
                                        sql = """INSERT INTO MarketPlaceUsers (Fullname, Username,Password, Balance) VALUES (%s, %s, %s, %s)"""
                                        row = self.c.execute(sql,(fullName, userEntry, password, "50.00"))
                                        self.db.commit()
                                        messagebox.showinfo("Success!", "You have successfully registered")
                                        self.login2()
                        except:
                            messagebox.showerror("Error", "Something went wrong during registration. Please try again.")
                            return
                            
        except:
            messagebox.showerror("Error", "Something went wrong during registration. Please try again.")
            raise  

        self.disconnect()                  
    def submit (self):
        self.connect()
        ## if you're withdrawing the money
        if self.sv1.get() == "withdraw":
            sql = """SELECT Balance FROM MarketPlaceUsers WHERE Username = %s AND Password = %s"""
            num = self.c.execute (sql, (self.userEntry, self.passwordEntry))
            self.tupleBalance = self.c.fetchone()
            for each in self.tupleBalance:
                self.balance = int(each)
            ## create an updated balance 
            self.updatedBalance = self.balance - int(self.transactionEntry.get())

            # show the updated entry on the entry box and reset the transaction entry
            ## the if statement checks to see if you have enough money
            if self.updatedBalance >= 0:
                sql = """UPDATE MarketPlaceUsers SET Balance = %s WHERE Username = %s and Password = %s"""
                num = self.c.execute(sql,(self.updatedBalance, self.userEntry, self.passwordEntry))
                self.balanceEntry.config(state = NORMAL)
                self.balanceEntry.delete(0, END)
                self.balanceEntry.insert(0, self.updatedBalance)
                self.balanceEntry.config(state = "readonly")
                self.transactionEntry.delete(0,END)
                self.transactionEntry.insert(0, "0.00")
                self.db.commit()
            else:
                messagebox.showerror("Error", "You do not have enough money to withdraw. Please enter a different amount.")
                self.transactionEntry.delete(0,END)
                self.transactionEntry.insert(0, "0.00")

                
        ## if you're depositing the money
        else:
            sql = """SELECT Balance FROM MarketPlaceUsers WHERE Username = %s AND Password = %s"""
            num = self.c.execute (sql, (self.userEntry, self.passwordEntry))
            self.tupleBalance = self.c.fetchone()
            for each in self.tupleBalance:
                self.balance = int(each)
            ## create an updated balance 
            self.updatedBalance = self.balance + int(self.transactionEntry.get())
            sql = """UPDATE MarketPlaceUsers SET Balance = %s WHERE Username = %s and Password = %s"""
            num = self.c.execute(sql,(self.updatedBalance, self.userEntry, self.passwordEntry))
            self.db.commit()
            
            # show the updated entry on the entry box and reset the transaction entry
            self.balanceEntry.config(state = NORMAL)
            self.balanceEntry.delete(0, END)
            self.balanceEntry.insert(0, self.updatedBalance)
            self.balanceEntry.config(state = "readonly")
            self.transactionEntry.delete(0,END)
            self.transactionEntry.insert(0, "0.00")

        self.disconnect()
    def buy(self):
        self.connect()
        #print('connected')
        ## find out if the value is 1 or 0
        sql = """SELECT Sold FROM MarketPlaceListings WHERE Itemname = %s"""
        row = self.c.execute(sql,(self.itemNameEntry.get()))
        tupleBooleanValue = self.c.fetchall()
        for each in tupleBooleanValue:
            for thing in each:
                self.booleanValue = thing
        ## check to see if this particular is even being sold!
        sql = """SELECT Itemname FROM MarketPlaceListings"""
        row = self.c.execute(sql)
        items = self.c.fetchall()
        itemList = []
        for each in items:
            for thing in each:
                itemList.append(thing)
        if self.itemNameEntry.get () in itemList:   ## it's in the list so someone is selling it
            ## but we gotta check if it's been bought already
            #print("it's in the list")            
        ## if the number is 0, then you know it's in stock and you can buy it 
                
                ## check to see if the user has enough money
                # get the balance from the user
            sql = """SELECT Balance FROM MarketPlaceUsers WHERE Username = %s AND Password = %s"""
            row = self.c.execute (sql, (self.userEntry, self.passwordEntry))
            self.junkyBalance = self.c.fetchone()
            #get the price of the item
            sql = """SELECT ListingUser, Price FROM MarketPlaceListings WHERE Sold = 0 AND Itemname = %s ORDER BY Price ASC"""
            row = self.c.execute (sql, (self.itemNameEntry.get()))
            tupleUserandPrice = self.c.fetchone()
            #print("TupleUser", tupleUserandPrice)
            userSelling = tupleUserandPrice
            #print('user selling', userSelling)
            priceSelling = tupleUserandPrice[1]
            #print('price selling', priceSelling)
            self.customerBalance = self.junkyBalance[0]
            #print("Balance of the user buying the item", self.customerBalance)
            ##compare the two pieces of infomation andd see if the user has enough money
            if self.customerBalance >= priceSelling:
                #compare
                if userSelling != self.userEntry:
                    ## get the lowest price and the lowest listing id of 
                    sql = """SELECT listing_id, Price FROM MarketPlaceListings WHERE Itemname = %s AND Sold = 0 ORDER BY Price ASC"""
                    row = self.c.execute(sql, (self.itemNameEntry.get()))
                    tuplerow = self.c.fetchone()
                    #print(tuplerow)

                    ### OMG LOOK THIS JUST GETS YOU THE PRICE DIRECTLY NO FOR LOOP
                    self.lowestPrice = tuplerow[1]
                    self.id = tuplerow[0]
                    #print(self.lowestPrice)
                    ## get the listing user from market place listings 
                    sql = """SELECT ListingUser FROM MarketPlaceListings WHERE listing_id = %s"""
                    row = self.c.execute(sql,(self.id))
                    userFromListing = self.c.fetchone()[0]
                    #print("user selling", userFromListing)
                    ## get the full name from the market place users 
                    sql = """SELECT Fullname FROM MarketPlaceUsers WHERE Username = %s"""
                    row = self.c.execute(sql,(userFromListing))
                    self.fullName = self.c.fetchone ()[0]
                    #print(self.fullName)
                    ## if the full name is null in the market place users 
                    if self.fullName == "NULL": 
                        answer = messagebox.askyesno("Item Found", "Somebody is selling {} for ${}. Would you like to buy it?".format(self.itemNameEntry.get(), self.lowestPrice))
                    else:
                        answer = messagebox.askyesno("Item Found", "{}is selling {} for ${}. Would you like to buy it?".format(self.fullName, self.itemNameEntry.get(), self.lowestPrice))
                    ## if the user wants to buy the item
        
                    if answer == True:
                        ## set the item to being sold 
                        sql = """UPDATE MarketPlaceListings SET Sold = 1 WHERE listing_id = %s"""
                        row = self.c.execute(sql,(self.id))
                        self.db.commit()
                        boughtUserBalance = self.customerBalance - priceSelling
                        #print("leftover money", boughtUserBalance)
                        #print("price of the item", priceSelling)
                        ## update the balance of the user that bought it
                        sql = """UPDATE MarketPlaceUsers SET Balance = %s WHERE Username = %s"""
                        row = self.c.execute(sql,(boughtUserBalance, self.userEntry))
                        self.db.commit()
                        ## update the balance of the user that sold it
                        sql = """SELECT Balance FROM MarketPlaceUsers WHERE Username = %s"""
                        row = self.c.execute(sql,(userFromListing))
                        sellingUserMoneyBefore = self.c.fetchone()[0]
                        #print("money that the person had before selling the item", sellingUserMoneyBefore)
                        soldUserBalance = sellingUserMoneyBefore + priceSelling
                        #print("made money", soldUserBalance)
                        sql = """UPDATE MarketPlaceUsers SET Balance = %s WHERE Username = %s"""
                        row = self.c.execute(sql,(soldUserBalance, userFromListing))
                        self.db.commit()

                        ## update the entry box
                        self.balanceEntry.config(state = NORMAL)
                        self.balanceEntry.delete(0, END)
                        self.balanceEntry.insert(0, boughtUserBalance)
                        self.balanceEntry.config(state = "readonly")
                        
                    else:
                        pass
            ##if the buyer doens't have enough money
                else:
                    messagebox.showerror("Error", "You do not have sufficient funds to purchase this item")
             ## if the item isn't being sold aka sold boolean value = 1
            else:
                messagebox.showerror("Error", "This item is not being sold at this moment")
        self.disconnect()
    def sell(self):
        self.connect()
        #print("user selling in SELL Function", self.userEntry)
        #print("name of the item", self.itemEntry.get())
        #print("price", self.priceEntry.get())
        
        sql = """INSERT INTO MarketPlaceListings (ListingUser, Itemname, Price) VALUES (%s, %s, %s)"""
        row = self.c.execute(sql, (self.userEntry, self.itemEntry.get(), self.priceEntry.get()))
        messagebox.showinfo("Congratulations!", "Your item is now on sale!")
        self.db.commit()
        self.disconnect()

    def logout(self):
        self.marketPlace.withdraw()
        self.root.deiconify()

    def statistics (self):
        self.connect()
        stats = Toplevel()
        stats.title("GTMarketPlace Statistics Page")
        statsFrame1 = Frame(stats, bg = "gold")
        statsFrame1.grid(row = 0, column = 0)
        statsFrame2 = Frame(stats, bg = "gold")
        statsFrame2.grid(row = 1, column = 0)
        
        sql = """SELECT Itemname FROM MarketPlaceListings ORDER BY Price DESC"""
        row = self.c.execute(sql)
        highestPriced = self.c.fetchone()[0]
        #print(highestPriced)
        sql = """SELECT Itemname FROM MarketPlaceListings ORDER BY Price ASC"""
        row = self.c.execute(sql)
        lowestPriced = self.c.fetchone()[0]
        #print(lowestPriced)
        highestprice = Label(statsFrame1, text = "Highest Priced Item: {}".format(highestPriced),bg = "gold")
        highestprice.grid(row = 0, column = 0)
        lowestprice = Label(statsFrame1, text = "Lowest Priced Item: {}".format(lowestPriced), bg = "gold")
        lowestprice.grid(row = 1, column = 0)
        
        userStatLabel = Label(statsFrame1, text = "Enter a username:", bg = "gold")
        userStatLabel.grid(row = 2, column = 0)
        self.userStatEntry = Entry(statsFrame1)
        self.userStatEntry.grid(row = 2, column = 1)
        userStatButton = Button (statsFrame1, text = "Get info!", command = self.userStat)
        userStatButton.grid(row = 2, column = 2)

        ## number of distinct users
        sql = """SELECT COUNT(DISTINCT ListingUser) AS DistinctUsers FROM MarketPlaceListings"""
        row = self.c.execute(sql)
        countNum = self.c.fetchall()
        for each in countNum:
            for thing in each:
                countNumber = thing
        distinctUsers = Label(statsFrame1, text = "Number of distinct users: {}".format(countNumber),bg = "gold")
        distinctUsers.grid(row = 3, column = 0)
        self.disconnect()

    def userStat(self):
        self.connect ()
        try: 
            userStatWin = Toplevel()
            userStatWin.title("UserInfo")
            userStatWinFrame = Frame(userStatWin, bg = "gold")
            userStatWinFrame.pack()

            userInfoLabel = Label(userStatWinFrame, text = "User information")
            userInfoLabel.pack(side = TOP, anchor = CENTER)

            sql = """SELECT COUNT(DISTINCT Itemname) FROM MarketPlaceListings WHERE ListingUser = %s AND Sold = 0"""
            row = self.c.execute(sql,(self.userStatEntry.get()))
            onsale = self.c.fetchall()
            for each in onsale:
                for thing in each:
                    onSale = thing
            #print("ON SALE", onSale)

            userStatOn = Label(userStatWinFrame, text = "Number of items on sale by the user: {}".format(onSale),  bg = "gold")
            userStatOn.pack(side = TOP)

            sql = """SELECT COUNT(DISTINCT Itemname) FROM MarketPlaceListings WHERE ListingUser = %s AND Sold = 1"""
            row = self.c.execute(sql,(self.userStatEntry.get()))
            alreadysold = self.c.fetchall()
            for each in alreadysold:
                for thing in each:
                    alreadySold = thing
            #print("ALReADY", alreadySold)
                                 
            userStatSold = Label(userStatWinFrame, text = "Number of items sold by the user: {}".format(alreadySold), bg = "gold")
            userStatSold.pack(side = TOP)

            buyLabel = Label(userStatWinFrame, text = "Distinct Items being sold right now by this user! Buy them!:", bg = "gold")
            buyLabel.pack()
            sql = """SELECT DISTINCT Itemname FROM MarketPlaceListings WHERE ListingUser = %s AND Sold = 0"""
            row = self.c.execute(sql,(self.userStatEntry.get()))
            onSaleTup = self.c.fetchall()
            #print("onsaleTup", onSaleTup)
            OnSaleList= []
            num = 1
            for each in onSaleTup:
                Label(userStatWinFrame, text = each, bg = "gold").pack(side = TOP)
                num = num + 1

            sql = """SELECT AVG(Price) FROM MarketPlaceListings WHERE ListingUser = %s """
            row = self.c.execute(sql,(self.userStatEntry.get()))
            avgPrice = self.c.fetchall()
            for each in avgPrice:
                for thing in each: 
                   averagePrice = thing

            averageLabel = Label(userStatWinFrame, text = "Average Price of Items being sold by this user: ${}".format(averagePrice), bg = "gold")
            averageLabel.pack()

        except:
            messagebox.showerror("Error!", "There was an error. Please try a different user.")
            
        
    

        self.disconnect ()
        
        
        
        
        
        
root = Tk ()
app = HW9(root)
root.mainloop ()


