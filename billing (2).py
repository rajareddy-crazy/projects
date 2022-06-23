
from tkinter import *
import random

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Billing Software")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.Gobi_Manchureian= IntVar()
        self.Chilli_Chicken = IntVar()
        self.Chicken_Lolipop = IntVar()
        self.Paneer_Tikkas = IntVar()
        self.Chicken_Curry_Rice = IntVar()
        self.Mutton_Curry_Rice = IntVar()
        self.Prawn_Curry_Rice = IntVar()
        self.Egg_Curry_Rice = IntVar()
        self.Butter_Naan = IntVar()
        self.Butter_Roti = IntVar()
        self.Cheese_Garlic_Naan = IntVar()
        self.Keema_Naan = IntVar()
        self.Channa_Masala = IntVar()
        self.Kadhai_Paneer = IntVar()
        self.Mushroom_Curry = IntVar()
        self.Mutton_Chicken = IntVar()
        self.Mutton_Biryani = IntVar()
        self.Chicken_Biryani = IntVar()
        self.EggVeg_Biryani = IntVar()
        self.JeeraSteamed_Rice = IntVar()
        self.Water_Bottle = IntVar()
        self.SaltSweet_Lassi = IntVar()
        self.Juices = IntVar()
        self.Lemon_SodaWater = IntVar()
        self.total_bill= StringVar()
       


        #===================================
        bg_color = "#8B7D6B"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "RESTAURANT BILLING SYSTEM ",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)

        #==================Straters=====================#
        F2 = LabelFrame(self.root,text = 'Straters',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 220)

        gobi_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Gobi Manchureian")
        gobi_lbl.grid(row = 0,column = 0,padx = 5,pady = 10)
        gobi_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Gobi_Manchureian)
        gobi_en.grid(row = 0,column = 1,ipady = 2,ipadx = 1)
        face_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Chilli Chicken")
        face_lbl.grid(row = 1,column = 0,padx = 5,pady = 10)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Chilli_Chicken)
        face_en.grid(row = 1,column = 1,ipady = 2,ipadx = 1)      
        wash_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Chicken Lolipop")
        wash_lbl.grid(row = 2,column = 0,padx = 5,pady = 10)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Chicken_Lolipop)
        wash_en.grid(row = 2,column = 1,ipady = 2,ipadx = 1)
        hair_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Paneer Tikkas")
        hair_lbl.grid(row = 3,column = 0,padx = 5,pady = 10)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Paneer_Tikkas)
        hair_en.grid(row = 3,column = 1,ipady = 2,ipadx = 1)

        
        F2 = LabelFrame(self.root,text = 'Specials',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 400,width = 325,height = 380)

        gobi_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Chicken Curry Rice")
        gobi_lbl.grid(row = 0,column = 0,padx = 5,pady = 10)
        gobi_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Chicken_Curry_Rice)
        gobi_en.grid(row = 0,column = 1,ipady = 2,ipadx = 1)
        face_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Mutton Curry Rice")
        face_lbl.grid(row = 1,column = 0,padx = 5,pady = 10)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Mutton_Curry_Rice)
        face_en.grid(row = 1,column = 1,ipady = 2,ipadx = 1)      
        wash_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Prawn Curry Rice")
        wash_lbl.grid(row = 2,column = 0,padx = 5,pady = 10)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Prawn_Curry_Rice)
        wash_en.grid(row = 2,column = 1,ipady = 2,ipadx = 1)
        hair_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Egg Curry Rice")
        hair_lbl.grid(row = 3,column = 0,padx = 5,pady = 10)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Egg_Curry_Rice)
        hair_en.grid(row = 3,column = 1,ipady = 2,ipadx = 1)

        

        F2 = LabelFrame(self.root,text = 'Main Course-INDIAN BREADS',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 220)

        gobi_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Butter Naan")
        gobi_lbl.grid(row = 0,column = 0,padx = 5,pady = 10)
        gobi_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Butter_Naan)
        gobi_en.grid(row = 0,column = 1,ipady = 2,ipadx = 1)
        face_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Butter Roti")
        face_lbl.grid(row = 1,column = 0,padx = 5,pady = 10)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Butter_Roti)
        face_en.grid(row = 1,column = 1,ipady = 2,ipadx = 1)      
        wash_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Cheese Garlic Naan")
        wash_lbl.grid(row = 2,column = 0,padx = 5,pady = 10)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Cheese_Garlic_Naan)
        wash_en.grid(row = 2,column = 1,ipady = 2,ipadx = 1)
        hair_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Keema Naan")
        hair_lbl.grid(row = 3,column = 0,padx = 5,pady = 10)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Keema_Naan)
        hair_en.grid(row = 3,column = 1,ipady = 2,ipadx = 1)

        

        F2 = LabelFrame(self.root,text = 'MAIN COURSE - VEG& NON VEG',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 400,width = 325,height = 380)

        gobi_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Channa Masala")
        gobi_lbl.grid(row = 0,column = 0,padx = 5,pady = 10)
        gobi_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Channa_Masala)
        gobi_en.grid(row = 0,column = 1,ipady = 2,ipadx = 1)
        face_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Kadhai Paneer")
        face_lbl.grid(row = 1,column = 0,padx = 5,pady = 10)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Kadhai_Paneer)
        face_en.grid(row = 1,column = 1,ipady = 2,ipadx = 1)      
        wash_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Mushroom Curry")
        wash_lbl.grid(row = 2,column = 0,padx = 5,pady = 8)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Mushroom_Curry)
        wash_en.grid(row = 2,column = 1,ipady = 2,ipadx = 0)
        hair_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Mutton/Chicken")
        hair_lbl.grid(row = 3,column = 0,padx = 5,pady = 8)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Mutton_Chicken)
        hair_en.grid(row = 3,column = 1,ipady = 2,ipadx = 0)


        F2 = LabelFrame(self.root,text = 'INDIAN RICE & BIRYANI',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 220)

        gobi_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Mutton Biryani")
        gobi_lbl.grid(row = 0,column = 0,padx = 5,pady = 10)
        gobi_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Mutton_Biryani)
        gobi_en.grid(row = 0,column = 1,ipady = 2,ipadx = 1)
        face_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Chicken Biryani")
        face_lbl.grid(row = 1,column = 0,padx = 5,pady = 10)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Chicken_Biryani)
        face_en.grid(row = 1,column = 1,ipady = 2,ipadx = 1)      
        wash_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Egg/Veg Biryani")
        wash_lbl.grid(row = 2,column = 0,padx = 5,pady = 10)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.EggVeg_Biryani)
        wash_en.grid(row = 2,column = 1,ipady = 2,ipadx = 1)
        hair_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Jeera/Steamed Rice")
        hair_lbl.grid(row = 3,column = 0,padx = 5,pady = 10)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.JeeraSteamed_Rice)
        hair_en.grid(row = 3,column = 1,ipady = 2,ipadx = 1)
      
        F2 = LabelFrame(self.root,text = 'Cold Beverages',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 400,width = 325,height = 380)

        gobi_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Water Bottle")
        gobi_lbl.grid(row = 0,column = 0,padx = 5,pady = 10)
        gobi_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Water_Bottle)
        gobi_en.grid(row = 0,column = 1,ipady = 2,ipadx = 1)
        face_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Salt/Sweet Lassi")
        face_lbl.grid(row = 1,column = 0,padx = 5,pady = 10)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.SaltSweet_Lassi)
        face_en.grid(row = 1,column = 1,ipady = 2,ipadx = 1)      
        wash_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Juices")
        wash_lbl.grid(row = 2,column = 0,padx = 5,pady = 8)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Juices)
        wash_en.grid(row = 2,column = 1,ipady = 2,ipadx = 0)
        hair_lbl = Label(F2,font = ("times new roman",12,"bold"),fg = lbl_color,bg = bg_color,text = "Lemon Soda/Water")
        hair_lbl.grid(row = 3,column = 0,padx = 5,pady = 8)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Lemon_SodaWater)
        hair_en.grid(row = 3,column = 1,ipady = 2,ipadx = 0)
      

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 325,height = 450)
        #===========
        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 600,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_bill)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 0,column = 2,ipadx = 20,padx = 30)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 0,column = 3,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 0,column = 4,ipadx = 20,padx = 30)

#Function to get total prices
    def total(self):
        #=================Total
        sm=0
        sm = (sm+
            (self.Gobi_Manchureian.get() * 189)+
            (self.Chilli_Chicken.get() * 240)+
            (self.Chicken_Lolipop.get() * 240)+
            (self.Paneer_Tikkas.get() * 200)+
            (self.Chicken_Curry_Rice.get() * 300)+
            (self.Mutton_Curry_Rice.get()*350)+
            (self.Prawn_Curry_Rice.get() * 300)+
            (self.Egg_Curry_Rice.get() * 400)+
            (self.Butter_Naan.get() *45)+
            (self.Butter_Roti.get() * 35)+
            (self.Cheese_Garlic_Naan.get() * 80)+
            (self.Keema_Naan.get() * 50)+
            (self.Channa_Masala.get() * 160)+
            (self.Kadhai_Paneer.get() * 240)+
            (self.Mutton_Chicken.get() * 280)+
            (self.Mutton_Biryani.get() *320)+
            (self.Chicken_Biryani.get() * 270)+
            (self.EggVeg_Biryani.get() * 200)+
            (self.JeeraSteamed_Rice.get() * 150)+
            (self.Water_Bottle.get() * 20)+
            (self.SaltSweet_Lassi.get() * 40)+
            (self.Juices.get() * 80)+
            (self.Lemon_SodaWater.get() * 45)
        )
        self.total_bill.set("Rs. "+str(sm))
        return sm


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Restaurant \n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct            Qty       Price")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def bill_area(self):
    
        self.welcome_soft()
        if self.Gobi_Manchureian.get() != 0:
            self.txt.insert(END,f"\nGobiManchureian     {self.Gobi_Manchureian.get()}        {self.Gobi_Manchureian.get() * 189}")
        if self.Chilli_Chicken.get() != 0:
            self.txt.insert(END,f"\nChilliChicken       {self.Chilli_Chicken.get()}        {self.Chilli_Chicken.get() * 240}")
        if self.Chicken_Lolipop.get() != 0:
            self.txt.insert(END,f"\nChickenLolipop      {self.Chicken_Lolipop.get()}        {self.Chicken_Lolipop.get() * 240}")
        if self.Paneer_Tikkas.get() != 0:
            self.txt.insert(END,f"\nPaneerTikkas        {self.Paneer_Tikkas.get()}        {self.Paneer_Tikkas.get() * 200}")
        if self.Chicken_Curry_Rice.get() != 0 :
            self.txt.insert(END,f"\nChickenCurryRice    {self.Chicken_Curry_Rice.get()}        {self.Chicken_Curry_Rice.get() * 300}")
        if self.Mutton_Curry_Rice.get() != 0:
            self.txt.insert(END,f"\nMuttonCurryRice     {self.Mutton_Curry_Rice.get()}        {self.Mutton_Curry_Rice.get()*350}")
        if self.Prawn_Curry_Rice.get() != 0:
            self.txt.insert(END,f"\nPrawnCurryRice      {self.Prawn_Curry_Rice.get()}        {self.Prawn_Curry_Rice.get() * 300}")
        if self.Egg_Curry_Rice.get() != 0:
            self.txt.insert(END,f"\nEggCurryRice        {self.Egg_Curry_Rice.get()}        {self.Egg_Curry_Rice.get() * 400}")
        if self.Butter_Naan.get() != 0:
            self.txt.insert(END,f"\nButterNaan          {self.Butter_Naan.get()}        {self.Butter_Naan.get() *45}")
        if self.Butter_Roti.get() != 0:
            self.txt.insert(END,f"\nButterRoti          {self.Butter_Roti.get()}        {self.Butter_Roti.get() * 35}")
        if self.Cheese_Garlic_Naan.get() != 0:
            self.txt.insert(END,f"\nCheeseGarlicNaan    {self.Cheese_Garlic_Naan.get()}        {self.Cheese_Garlic_Naan.get() * 80}")
        if self.Keema_Naan.get() != 0:
            self.txt.insert(END,f"\nKeemaNaan           {self.Keema_Naan.get()}        {self.Keema_Naan.get() * 50}")
        if self.Channa_Masala.get() != 0:
            self.txt.insert(END,f"\nChannaMasala        {self.Channa_Masala.get()}        {self.Channa_Masala.get() * 160}")
        if self.Kadhai_Paneer.get() != 0:
            self.txt.insert(END,f"\nKadhaiPaneer        {self.Kadhai_Paneer.get()}        {self.Kadhai_Paneer.get() * 240}")
        if self.Mutton_Chicken.get() != 0:
            self.txt.insert(END,f"\nMuttonChicken       {self.Mutton_Chicken.get()}        {self.Mutton_Chicken.get() * 280}")
        if self.Mutton_Biryani.get() != 0:
            self.txt.insert(END,f"\nMuttonBiryani       {self.Mutton_Biryani.get()}        {self.Mutton_Biryani.get() *320}")
        if self.Chicken_Biryani.get() != 0:
            self.txt.insert(END,f"\nChickenBiryani      {self.Chicken_Biryani.get()}        {self.Chicken_Biryani.get() * 270}")
        if self.EggVeg_Biryani.get() != 0:
            self.txt.insert(END,f"\nEgg/VegBiryani      {self.EggVeg_Biryani.get()}        {self.EggVeg_Biryani.get() * 200}")
        if self.JeeraSteamed_Rice.get() != 0:
            self.txt.insert(END,f"\nJeera/SteamedRice   {self.JeeraSteamed_Rice.get()}        {self.JeeraSteamed_Rice.get() * 150}")
        if self.Water_Bottle.get() != 0:
            self.txt.insert(END,f"\nWaterBottle         {self.Water_Bottle.get()}        {self.Water_Bottle.get() * 20}")
        if self.SaltSweet_Lassi.get() != 0:
            self.txt.insert(END,f"\nSaltSweetLassi      {self.SaltSweet_Lassi.get()}        {self.SaltSweet_Lassi.get() * 40}")
        if self.Juices.get() != 0:
            self.txt.insert(END,f"\nJuices              {self.Juices.get()}        {self.Juices.get() * 80}")
        if self.Lemon_SodaWater.get() != 0:
            self.txt.insert(END,f"\nLemonSoda/Water     {self.Lemon_SodaWater.get()}        {self.Lemon_SodaWater.get() * 45}")
        
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                    Total : {self.total()}")


    #Function to exit
    def exit(self):
        self.root.destroy()

    #Function To Clear All Fields


        


root = Tk()
object = Bill_App(root)
root.mainloop()



