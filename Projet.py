import random 
import time 
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox



def main():
    root=Tk()
    app=windows1(root)
    root.mainloop()
    
    

class windows1:
    def __init__(self,master):
        self.master=master
        self.master.title("Hospital Management system")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()


        self.Username=StringVar()
        self.Password=StringVar()

        self.LabelTitle = Label(self.frame,text="Hospital Managment System",font=("arial",40,"bold"),
            bd = 10,relief ="sunken")
        self.LabelTitle.grid(row=0,column=0 , columnspan= 2 ,pady=20)


        self.Loginframe1 =Frame(self.frame, width=1000 , height= 300 , bd=10 ,relief="groove" )
        self.Loginframe1.grid(row=1 ,column=0)

        self.Loginframe2 = Frame(self.frame,width=1000 , height= 100 ,bd=10,relief="groove" )
        self.Loginframe2.grid(row=2 ,column=0,pady=15)

        self.Loginframe3 = Frame(self.frame,width=1000 , height= 300 ,bd=10 ,relief="groove" )
        self.Loginframe3.grid(row=6 ,column=0 , pady=5)
        
        
        
        
        
        self.button_reg =Button(self.Loginframe3,text="Patien Registration window",state=DISABLED ,font=("arial",15,"bold"),command=self.Registration_window)
        self.button_reg.grid(row=0,column=0 ,padx=10,pady=10)
        
        
        self.button_Hosp =Button(self.Loginframe3,text="Hospital Managment window",state=DISABLED ,font=("arial",15,"bold"),command=self.Hospital_window)
        self.button_Hosp.grid(row=0,column=1 ,padx=10,pady=10)


        self.button_Dr_appt =Button(self.Loginframe3,text="Doctor Managment window",state=DISABLED ,font=("arial",15,"bold"),command=self.Dr_Apoint_window)
        self.button_Dr_appt.grid(row=0,column=2 ,padx=10,pady=10)

        


        # now we will make user name and password frame


        self.LabelUsername=Label(self.Loginframe1,text="User Name",font=("arial",20,"bold"),bd=3)
        self.LabelUsername.grid(row=0,column=0)
        self.textUsername=Entry(self.Loginframe1,font=("arial",20,"bold"),bd=3, textvariable=self.Username)
        self.textUsername.grid(row=0,column=1 ,padx=40,pady=15)
        self.LabePassword=Label(self.Loginframe1,text="Password",font=("arial",20,"bold"),bd=3)
        self.LabePassword.grid(row=1,column=0)
        self.textPassword=Entry(self.Loginframe1,font=("arial",20,"bold"),sho="*",bd=3, textvariable=self.Password)
        self.textPassword.grid(row=1,column=1 ,padx=40,pady=15)
        
        

        self.button_login =Button(self.Loginframe2,text="Login",width=20,font=("arial",18,"bold"),command=self.login_system)
        self.button_login.grid(row=0,column=0 ,padx=10,pady=10)
        self.button_Reset =Button(self.Loginframe2,text="Reset",width=20,command=self.reset_btn,font=("arial",18,"bold"))
        self.button_Reset.grid(row=0,column=3 ,padx=10,pady=10)
        self.button_Exit =Button(self.Loginframe2,text="Exit",width=20,command=self.Exit_btn ,font=("arial",18,"bold"))
        self.button_Exit.grid(row=0,column=6 ,padx=10,pady=10)
        
        
    def login_system(self):
        user =self.Username.get()
        pswd=self.Password.get()



        if(user == str("admin") and (pswd ==str("admin"))):
            
            self.button_reg.config(state=NORMAL)
            self.button_Hosp.config(state=NORMAL)
            self.button_Dr_appt.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)
            

        else:
            tkinter.messagebox.askyesno("pharmacy Managment System ","you have entred an invalid user name or password")
            self.button_reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_appt.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)
                
#if user name or password is incorrect it will be in its disable state 
            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()


    def reset_btn(self):
        self.button_reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_appt.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)
        #because when we will reset still we haven't given correct user id and password
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()
    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("pharmacy Managment System ","Are you sure you want to exit")
        if self.Exit_btn > 0:
            #we will close that master screen
            self.master.destroy()
            return     


    
        


# first we will define our windows
    def Registration_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Registration(self.newWindow)


    def Hospital_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Hospital(self.newWindow)


    def Dr_Apoint_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Doctor(self.newWindow)


    def Medicin_stock(self):
        self.newWindow=Toplevel(self.master)
        self.app=windows5(self.newWindow)
   




class Registration():
    def __init__(self,root):
        self.root=root
        self.root.title("Patient Registration  system")
        self.root.geometry('1350x750+0+0')
        self.root.configure(background="black")
        
        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        
        
        Ref=StringVar()
        Mobile_no=StringVar()
        pincode=StringVar()
        address=StringVar()
        firstname=StringVar()
        lastname=StringVar()
        ######## for combobox
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=IntVar()
        
        
        membreship=StringVar()
        membreship.set('0')
        
        ########### fonction
        
        def exitbtt():
           exitbttt=tkinter.messagebox.askyesno("Membre Registration Form","Are you sure you want to exit ?")
           if exitbttt > 0:
            root.destroy()
           else:
               self.newWindow=Toplevel(self.master)
               self.app=Registration(self.newWindow)
           return
        
        
        
        def resetbtt():
            genrecmb.current(0)
            idcmb.current(0)
            typecmb.current(0)
            paymentcmb.current(0)
            idcmb.current(0)
            Ref.set("")
            firstname.set("")
            lastname.set("")
            Mobile_no.set("")
            pincode.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            membreship.set("0")
            membre_membreshiptxt(state=DISABLED)
            address.set("")
        def reeesetbtt():
            reeesetbtt=tkinter.messagebox.askokcancel("Membre Registration Form","You want to add as new record")
            if reeesetbtt >0:
                resetbtt()
            elif reeesetbtt <= 0 :
                resetbtt()
                Detail_labeltxt.delete("1.0",END)
                return
        def reference_number():
           ranumber=random.randint(10000,999999)
           randomnumber=str(ranumber)
           Ref.set(randomnumber)
        def membership_fees():
            if(var5.get()==1):
                membre_membreshiptxt.configure(state=NORMAL)
                item=float(15000) # it is random price  of membreship plan
                membreship.set(str(item)+"Rs")
            elif(var5.get()==0): #when unchecked
                membre_membreshiptxt.configure(state=DISABLED)
                membreship.set("0")
                
                
        def receeipt():
            reference_number()
            detail_Labeltxt.insert(END,"\t"+Date_of_Registration.get()+"     \t"+ Ref.get() +"\t"+
                        firstname.get() +" \t"+ lastname.get()+"\t" +Mobile_no.get()+"\t"+addresstxt.get()+
                     " \t"+ pincode.get() +"\t"+paymentcmb.get()+" "+idcmb.get()+"\n")
            
            
                
                
                
                
                
            
            
            
        
            
           
            
            
            
            
           
            
        
         
        
        
        
        
        
        
        #################title
        title = Label(self.root,font=("monotype corsiva",30,"bold"),text="Membre Registration Form", bd = 3,relief ="groove",bg="#E6005C",fg="#000000")
        title.pack(side = TOP ,fill= X)
        
        #################membre frame
        Manage_Frame=Frame(self.root,bd=4 ,relief= RIDGE,bg="#001a66")
        Manage_Frame.place(x=30,y=100,width=450 , height= 630)
        
        cus_title= Label(Manage_Frame,text="Customer Details",font=("arial",20,"bold"),bg="#001a66",fg="white")
        cus_title.grid(row=0, columnspan= 2,pady=5)
        
        
        
        date= Label(Manage_Frame,text="Date",font=("arial",15,"bold"),bg="#001a66",fg="white")
        date.grid(row=1, column=0,pady=5,padx=10,sticky="w")
        
        
        membre_datetxt=Entry(Manage_Frame,textvariable=Date_of_Registration,font=("arial",15,"bold"))
        membre_datetxt.grid(row=1, column=1,pady=5,padx=10,sticky='W')
        
        
        ref= Label(Manage_Frame,text="References ID",font=("arial",15,"bold"),bg="#001a66",fg="white")
        ref.grid(row=2, column=0,pady=5,sticky='W',padx=10)
        
        reftxt=Entry(Manage_Frame,textvariable=Ref,state=DISABLED,font=("arial",15,"bold"))
        reftxt.grid(row=2, column=1,pady=5,sticky='W',padx=10)
        
        
        
        
        fname= Label(Manage_Frame,text="First Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        fname.grid(row=3, column=0,pady=5,sticky='W',padx=10)
        fnametxt=Entry(Manage_Frame,textvariable=firstname,font=("arial",15,"bold"))
        fnametxt.grid(row=3, column=1,pady=5,sticky='W',padx=10)
        
        
        lname= Label(Manage_Frame,text="Last Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        lname.grid(row=4, column=0,pady=5,sticky='W',padx=10)
        lnametxt=Entry(Manage_Frame,textvariable=lastname,font=("arial",15,"bold"))
        lnametxt.grid(row=4, column=1,pady=5,sticky='W',padx=10)
        
        
        
        mobile= Label(Manage_Frame,text="Mobile No",font=("arial",15,"bold"),bg="#001a66",fg="white")
        mobile.grid(row=5, column=0,pady=5,sticky='W',padx=10)
        mobiletxt=Entry(Manage_Frame,textvariable=Mobile_no,font=("arial",15,"bold"))
        mobiletxt.grid(row=5, column=1,pady=5,sticky='W',padx=10)
        
        
        
    
        address= Label(Manage_Frame,text="Address",font=("arial",15,"bold"),bg="#001a66",fg="white")
        address.grid(row=6, column=0,pady=5,sticky='W',padx=10)
        addresstxt=Entry(Manage_Frame,textvariable=address,font=("arial",15,"bold"))
        addresstxt.grid(row=6, column=1,pady=5,sticky='W',padx=10)
        
        
        
        
    
        pin= Label(Manage_Frame,text="Pin Code",font=("arial",15,"bold"),bg="#001a66",fg="white")
        pin.grid(row=7, column=0,pady=5,sticky='W',padx=10)
        pintxt=Entry(Manage_Frame,textvariable=pincode,font=("arial",15,"bold"))
        pintxt.grid(row=7, column=1,pady=5,sticky='W',padx=10)
        
        
        genre= Label(Manage_Frame,text="Genre",font=("arial",15,"bold"),fg="white",bg="#001a66")
        genre.grid(row=8,column=0 , pady=5,padx=10,sticky='W')
        genrecmb=ttk.Combobox(Manage_Frame,textvariable=var4,width=19,state="readonly",font=("arial",12,"bold"))
        genrecmb["values"]=("","Male","Female")
        genrecmb.current(0)
        genrecmb.grid(row=8,column=1 , padx=10,pady=5,sticky='w')
        
        
        id= Label(Manage_Frame,text="ID Proof",font=("arial",15,"bold"),fg="white",bg="#001a66")
        id.grid(row=9,column=0 , pady=5,padx=10,sticky='W')
        idcmb=ttk.Combobox(Manage_Frame,textvariable=var3,width=19,state="readonly",font=("arial",12,"bold"))
        idcmb["values"]=("","Adhaar Card","Passport","Driving License","Pan Card","Student ID")
        idcmb.current(0)
        idcmb.grid(row=9,column=1 , padx=10,pady=5,sticky='w')
        
        
        
        type= Label(Manage_Frame,text="Membre Type",font=("arial",15,"bold"),fg="white",bg="#001a66")
        type.grid(row=10,column=0 , pady=5,padx=10,sticky='W')
        typecmb=ttk.Combobox(Manage_Frame,textvariable=var2,width=19,state="readonly",font=("arial",12,"bold"))
        typecmb["values"]=("","Ayushman Card","Insurance","Pay Immediatly","Pay when leaving")
        typecmb.current(0)
        typecmb.grid(row=10,column=1 , padx=10,pady=5,sticky='w')
        
        
        payment= Label(Manage_Frame,text="Payment",font=("arial",15,"bold"),fg="white",bg="#001a66")
        payment.grid(row=11,column=0 , pady=5,padx=10,sticky='W')
        paymentcmb=ttk.Combobox(Manage_Frame,textvariable=var1,width=19,state="readonly",font=("arial",12,"bold"))
        paymentcmb["values"]=("","Cash","Debit Card -RuPay","Debit Card -Visa","Debit Card -Mastrcard","Credit Card","Phonepe","Google Play","Paytm")
        paymentcmb.current(0)
        paymentcmb.grid(row=11,column=1 , padx=10,pady=5,sticky='w')
        
        
        
        membre_membreship=Checkbutton(Manage_Frame,text="Membreship Fees",command=membership_fees,font=("arial",15,"bold"),fg="white",bg="#001a66",variable=var5,onvalue=1,offvalue=0)
        membre_membreship.grid(row=12,column=0 ,sticky='W')
        membre_membreshiptxt=Entry(Manage_Frame,textvariable=membreship,state=DISABLED,justify=RIGHT,font=("arial",15,"bold"))
        membre_membreshiptxt.grid(row=12, column=1,pady=5,padx=5,sticky='W')
        
        
        
        
        
        
        
        
        
        
        
        
        
         
         
          
        




        #################detail frame
        detail_Frame=Frame(self.root,relief= RIDGE,bg="#001a66")
        detail_Frame.place(x=500,y=100,width=850,height= 630)
        
        detail_Label= Label(detail_Frame,text="Date\t  Ref ID\t  Firdt Name   Last Name   Mobile No   Address   Pincode   Payment  ID Proof ",font=("arial",9,"bold"),width=95
                            ,padx=2,pady=10)
        detail_Label.grid(row=0, column=0,columnspan=4,sticky="w")
        
        
        detail_Labeltxt=Text(detail_Frame,width=100,height=28,font=("arial",10))
        detail_Labeltxt.grid(row=1, column=0,columnspan=4)
        
        
        ######button in dtail frame
        receipbtn=Button(detail_Frame,padx=10,bd=5,font=("arial",12,"bold"),bg="#ff9966",command=receeipt,width=17,text="Receipt")
        receipbtn.grid(row=2,column=0)
        
        resetbtn=Button(detail_Frame,padx=15,bd=5,font=("arial",12,"bold"),bg="#ff9966",width=17,text="Reset",command=reeesetbtt)
        resetbtn.grid(row=2,column=1)
        
        
        exirbtn=Button(detail_Frame,padx=15,bd=5,font=("arial",12,"bold"),bg="#ff9966",width=17,text="Exit",command=exitbtt)
        exirbtn.grid(row=2,column=2)
class Hospital():
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry('1350x750+0+0')
        self.root.configure(background="black")
        
        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        
        
        Ref=StringVar()
        cmbTabletNames=StringVar()
        HospitalCode=StringVar()
        Number_of_Tablets=StringVar()
        Lot=StringVar()
        IssueDate=StringVar()
        ExpiryDate=StringVar()
        DailyDose=StringVar()
        SideEffets=StringVar()
        MoreInformation=StringVar()
        StorageAdvice=StringVar()
        Medication=StringVar()
        PatientId=StringVar()
        PatientNumber=StringVar()
        PatientName=StringVar()
        DateofBirth=StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()
        NHSnumber=StringVar()
        
        
        def Refnum_func():
           ranumber=random.randint(10000,999999)
           randomnumber=str(ranumber)
           Ref.set(randomnumber)
           
           
           
        def Presciptiondatafunc():
            Refnum_func()
            textprescreptionData.insert(END,Date_of_Registration.get()+"\t\t"+Ref.get()+"\t\t"+PatientName.get()+"\t\t"+DateofBirth.get()+
                       "\t\t"+ NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t\t"+Number_of_Tablets.get()+"\t\t"
                                        +IssueDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+StorageAdvice.get()+PatientId.get()+"\n")
            return
        
        
               
 
        def exitbtnfunc():
            exitbtnfunc=tkinter.messagebox.askyesno("Hospital Management System","Are you sure you want to exit ?")
            if exitbtnfunc > 0:
                root.destroy()
            return
        def prescreptionbtnfunc():
            Refnum_func()
            textprescreption.insert(END,"Date: \t\t"+Date_of_Registration.get()+"\n")
            textprescreption.insert(END,"Patient ID\t\t"+PatientId.get()+"\n")
            textprescreption.insert(END,"Patient Name: \t\t"+PatientName.get()+"\n")
            textprescreption.insert(END,"Tablet: \t\t"+cmbTabletNames.get()+"\n")
            textprescreption.insert(END,"Number of Tablet: \t\t"+Number_of_Tablets.get()+"\n")
            textprescreption.insert(END,"Daily Dose: \t\t"+DailyDose.get()+"\n")
            textprescreption.insert(END,"Issued Date: \t\t"+IssueDate.get()+"\n")
            textprescreption.insert(END,"Expiry Date: \t\t"+ExpiryDate.get()+"\n")
            textprescreption.insert(END,":Storage\t\t"+StorageAdvice.get()+"\n")
            textprescreption.insert(END,"More Information: \t\t"+MoreInformation.get()+"\n")
            return
        
        
        def deletebtnfunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            Prescription.set("")
            NHSnumber.set("")
            PatientAddress.set("")
            IssueDate.set("")
            DailyDose.set("")
            ExpiryDate.set("")
            PatientAddress.set("")
            SideEffets.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            textprescreption.delete("1.0",END)
            textprescreptionData.delete("1.0",END)
              
            return
        
        def resetbtnfunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            Prescription.set("")
            NHSnumber.set("")
            PatientAddress.set("")
            IssueDate.set("")
            DailyDose.set("")
            ExpiryDate.set("")
            PatientAddress.set("")
            SideEffets.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNumber.set("")
            PatientName.set("")
            DateofBirth.set("")
            textprescreption.delete("1.0",END)
            return
        
        

        title = Label(self.root,font=("monotype corsiva",42,"bold"),text="Hospital Management system", bd = 5,relief ="groove",fg="black",bg="#2eb8b8")
        title.pack(side = TOP ,fill= X)
        
        
        Manage_Frame=Frame(self.root, width=1510 , height= 400 , bd=5 ,relief= RIDGE,bg="#0099cc")
        Manage_Frame.place(x=0,y=100)
        
        buttons_Frame=Frame(self.root, width=2500 , height= 55 , bd=4 ,relief=RIDGE,bg="#328695")
        buttons_Frame.place(x=0,y=560)
        
        Data_Frame=Frame(self.root, width=2000 , height= 300 , bd=4 ,relief= RIDGE,bg="#266E73")
        Data_Frame.place(x=0,y=620)
        
        
        
        Data_FrameLeft = LabelFrame(Manage_Frame,width=1050 ,text="General Information",font=("arial",20,"italic bold"),height= 390,bd = 7,relief =RIDGE,bg="#0099cc")
        Data_FrameLeft.pack(side=LEFT)
        Data_FrameRigth= LabelFrame(Manage_Frame,width=2000 ,text="Prescription",font=("arial",15,"italic bold"),height= 390,bd = 7,relief =RIDGE,bg="#0099cc")
        Data_FrameRigth.pack(side=RIGHT)
        Data_Framedata= LabelFrame(Data_Frame,width=1050 ,text="Prescription Data",font=("arial",12,"italic bold"),height= 390,bd=4 ,relief =RIDGE,bg="#3eb7bb")
        Data_Framedata.pack(side=LEFT)
        
        
        
        datebl= Label(Data_FrameLeft,text="Date",font=("arial",12,"bold"),bg="#0099cc",width=20)
        datebl.grid(row=0,column=0 , padx=10,columnspan= 2 ,sticky=W)
        datebltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),state=DISABLED,width=27, textvariable=Date_of_Registration)
        datebltxt.grid(row=0,column=1 ,padx=10,pady=5,sticky=E)
        
        
        
        
        Refbl= Label(Data_FrameLeft,text="Reference Number",font=("arial",12,"bold"),bg="#0099cc",width=20)
        Refbl.grid(row=1,column=0 , padx=10,columnspan= 2 ,sticky=W)
        Reftxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Ref,state=DISABLED)
        Reftxt.grid(row=1,column=1 ,padx=10,pady=5,sticky=E)
        
        
        patientidbl= Label(Data_FrameLeft,text="Patient ID",font=("arial",12,"bold"),bg="#0099cc",width=20)
        patientidbl.grid(row=2,column=0 , padx=10,sticky=W)
        patientidbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PatientId)
        patientidbltxt.grid(row=2,column=1 ,padx=10,pady=5,sticky=E)
        
        
        
        patientnamebl= Label(Data_FrameLeft,text="Patient Name",font=("arial",12,"bold"),bg="#0099cc",width=20)
        patientnamebl.grid(row=3,column=0 , padx=10,sticky=W)
        patientnamebltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PatientName)
        patientnamebltxt.grid(row=3,column=1 ,padx=10,pady=5,sticky=E)
        
        
        DateofBirthbl= Label(Data_FrameLeft,text="Date of Birth",font=("arial",12,"bold"),bg="#0099cc",width=20)
        DateofBirthbl.grid(row=4,column=0 , padx=10,sticky=W)
        DateofBirthbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=DateofBirth)
        DateofBirthbltxt.grid(row=4,column=1 ,padx=10,pady=5,sticky=E)
        
        Addressbl= Label(Data_FrameLeft,text="Address",font=("arial",12,"bold"),bg="#0099cc",width=20)
        Addressbl.grid(row=5,column=0 , padx=10,sticky=W)
        Addressbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PatientAddress)
        Addressbltxt.grid(row=5,column=1 ,padx=10,pady=5,sticky=E)
        
        
        
        NHSnumberbl= Label(Data_FrameLeft,text="NHS Unique Number ",font=("arial",12,"bold"),bg="#0099cc",width=20)
        NHSnumberbl.grid(row=6,column=0 , padx=10,sticky=W)
        NHSnumbertxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6,column=1 ,padx=10,pady=5,sticky=E)
        
        
        tabletbl= Label(Data_FrameLeft,text="Tablet",font=("arial",12,"bold"),bg="#0099cc",width=20,padx=2)
        tabletbl.grid(row=7,column=0 , padx=10,pady=5,sticky=W)
        tabletblcmb=ttk.Combobox(Data_FrameLeft,textvariable=cmbTabletNames,width=25,state="readonly",font=("arial",12,"bold"))
        tabletblcmb["values"]=("","Parcetamol","Dan-p","Dio-l one","Amlodipine Bestylate","Nexium"
                               ,"Singulair","Plavix","Amoxicillian","Azithromycin","Limcin-900")
        tabletblcmb.current(0)
        tabletblcmb.grid(row=7,column=1 , padx=10,pady=5,sticky=E)
        
        
        no_of_tabletbl= Label(Data_FrameLeft,text="Number of Tablets",font=("arial",12,"bold"),bg="#0099cc",width=20)
        no_of_tabletbl.grid(row=8,column=0 , padx=10,sticky=W)
        no_of_tabletbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Number_of_Tablets)
        no_of_tabletbltxt.grid(row=8,column=1 ,padx=10,pady=5,sticky=E)
        
        
        
        HospitalCodebl= Label(Data_FrameLeft,text="Hospital Code",font=("arial",12,"bold"),bg="#0099cc",width=20)
        HospitalCodebl.grid(row=0,column=2 , padx=10,sticky=W)
        HospitalCodebltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=HospitalCode)
        HospitalCodebltxt.grid(row=0,column=3 ,padx=10,pady=5,sticky=E)
        
        storageadvicebl= Label(Data_FrameLeft,text="Storage Advice",font=("arial",12,"bold"),bg="#0099cc",width=20,padx=2)
        storageadvicebl.grid(row=1,column=2 , padx=10,pady=5,sticky=W)
        storageadviceblcmb=ttk.Combobox(Data_FrameLeft,textvariable=StorageAdvice,width=23,state="readonly",font=("arial",12,"bold"))
        storageadviceblcmb["values"]=("","Under room temp","bellow 5°C","bellow 0°C","Refrigation")
        storageadviceblcmb.current(0)
        storageadviceblcmb.grid(row=1,column=3 , padx=10,pady=5,sticky=E)
        
        
        Lotbl= Label(Data_FrameLeft,text="Lot Number",font=("arial",12,"bold"),bg="#0099cc",width=20)
        Lotbl.grid(row=2,column=2 , padx=10,sticky=W)
        Lotbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=Lot)
        Lotbltxt.grid(row=2,column=3 ,padx=10,pady=5,sticky=E)
        
        
        IssueDatebl= Label(Data_FrameLeft,text="Date of Issue",font=("arial",12,"bold"),bg="#0099cc",width=20)
        IssueDatebl.grid(row=3,column=2 , padx=10,sticky=W)
        IssueDatebltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=IssueDate)
        IssueDatebltxt.grid(row=3,column=3 ,padx=10,pady=5,sticky=E)
        
        
        ExpiryDatebl= Label(Data_FrameLeft,text="Date of Expiry",font=("arial",12,"bold"),bg="#0099cc",width=20)
        ExpiryDatebl.grid(row=4,column=2 , padx=10,sticky=W)
        ExpiryDatebltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=ExpiryDate)
        ExpiryDatebltxt.grid(row=4,column=3 ,padx=10,pady=5,sticky=E)
        
        
        DailyDosebl= Label(Data_FrameLeft,text="Daily Dosage",font=("arial",12,"bold"),bg="#0099cc",width=20)
        DailyDosebl.grid(row=5,column=2 , padx=10,sticky=W)
        DailyDosetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=DailyDose)
        DailyDosetxt.grid(row=5,column=3 ,padx=10,pady=5,sticky=E)
        
        
        SideEffetsbl= Label(Data_FrameLeft,text="Side Effects",font=("arial",12,"bold"),bg="#0099cc",width=20)
        SideEffetsbl.grid(row=6,column=2 , padx=10,sticky=W)
        SideEffetsbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=SideEffets)
        SideEffetsbltxt.grid(row=6,column=3 ,padx=10,pady=5,sticky=E)
        
        
        MoreInformationbl= Label(Data_FrameLeft,text="More Information",font=("arial",12,"bold"),bg="#0099cc",width=20)
        MoreInformationbl.grid(row=7,column=2 , padx=10,sticky=W)
        MoreInformationbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=MoreInformation)
        MoreInformationbltxt.grid(row=7,column=3 ,padx=10,pady=5,sticky=E)
        
        
        Medicationbl= Label(Data_FrameLeft,text="Medication",font=("arial",12,"bold"),bg="#0099cc",width=20)
        Medicationbl.grid(row=8,column=2 , padx=10,sticky=W)
        Medicationbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25, textvariable=Medication)
        Medicationbltxt.grid(row=8,column=3 ,padx=10,pady=5,sticky=E)
        
        
        
        textprescreption=Text(Data_FrameRigth,font=("arial",12,"bold"),width=65 , height= 17,padx=3,pady=5)
        textprescreption.grid(row=0,column=0)
        textprescreptionData=Text(Data_Framedata,font=("arial",12,"bold"),width=173 , height=14) 
        textprescreptionData.grid(row=1,column=0)
        
        
        
        ###############button
        prescreptionbtn=Button(buttons_Frame,text="Presciption",bg="#ffaab0",activebackground="#fcceb2",
                           font=("arial",15,"bold"),width=23,command=prescreptionbtnfunc)
        prescreptionbtn.grid(row=0,column=0,padx=15)
        
        
        receiptbtn=Button(buttons_Frame,text="Presciption Data",bg="#ffaab0",activebackground="#fcceb2",
                           font=("arial",15,"bold"),width=23,command=Presciptiondatafunc)
        receiptbtn.grid(row=0,column=1,padx=15)
        
        
        
        resetbtn=Button(buttons_Frame,text="Reset",bg="#ffaab0",activebackground="#fcceb2",
                           font=("arial",15,"bold"),width=23,command=resetbtnfunc)
        resetbtn.grid(row=0,column=2,padx=15)
        
        
        
        
        deletebtn=Button(buttons_Frame,text="Delete",bg="#ffaab0",activebackground="#fcceb2",
                           font=("arial",15,"bold"),width=23,command=deletebtnfunc)
        deletebtn.grid(row=0,column=3,padx=15)
        
        
        exitbtn=Button(buttons_Frame,text="Exit",bg="#ffaab0",activebackground="#fcceb2",
                           font=("arial",15,"bold"),width=23,command=exitbtnfunc)
        exitbtn.grid(row=0,column=4,padx=15)
        
        
        prescreptiondatarow=Label(Data_Framedata,bg="white",font=("arial",12,"bold"),text=
                                  "Date\t Reference Id\t     Patient Name\t  Date of Birth  \t NHS Number\t Tablet\t No of Tablet\t Issued Date\t Expiry Date\tDaily Dose\t Storage Advice \tPatientID\t         ")
        prescreptiondatarow.grid(row=0,column=0,sticky=W)       


class Doctor():
    def __init__(self,root):
        self.root=root
        self.root.title("Doctor Management system")
        self.root.geometry('1350x750+0+0')
        self.root.configure(background="black")
        
        ###########we will declare all fonction
        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        
        
        DrId=StringVar()
        Drname=StringVar()
        DateofBirth=StringVar()
        Spes=StringVar()
        GovtPri=StringVar()
        Surgeies=StringVar()
        Experiences=StringVar()
        Nurses=StringVar()
        DrMobile=StringVar()
        PtName=StringVar()
        PtAge=StringVar()
        PatientAddress=StringVar()
        PtMobile=StringVar()
        Disease=StringVar()
        Case=StringVar()
        BenefitCard=StringVar()
        apptime=StringVar()
        
        def Patien_idFunc():
           ranumber=random.randint(10000,999999)
           randomnumber=str(ranumber)
           DrId.set(randomnumber)
            
        def prescreptionbtnfunc():
            textprescreption.insert(END,"Date: \t\t"+Date_of_Registration.get()+"\n")
            textprescreption.insert(END,"Patient Name"+PtName.get()+"\n")
            textprescreption.insert(END,"Appointement Time: \t\t"+apptime.get()+"\n")
            textprescreption.insert(END,"Age: \t\t"+PtAge.get()+"\n")
            textprescreption.insert(END,"Address: \t\t"+PatientAddress.get()+"\n")
            textprescreption.insert(END,"Disease: \t\t"+Disease.get()+"\n")
            textprescreption.insert(END,"case: \t\t"+Case.get()+"\n")
            textprescreption.insert(END,"Benefit Card: \t\t"+BenefitCard.get()+"\n")
            textprescreption.insert(END,":To meet Dr \t\t"+Drname.get()+"\n")
            textprescreption.insert(END,"Dr.Mobile no Card: \t\t"+DrMobile.get()+"\n")
            return
        
        
        def Doctordetailbtnfunc():
            Patien_idFunc()
            textprescreptionData.insert(END,Date_of_Registration.get()+"\t"+DrId.get()+"\t"+Drname.get()+"\t\t"+DateofBirth.get()+
                       "\t\t"+ Spes.get()+"\t\t"+GovtPri.get()+"\t\t"+Surgeies.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t\t"+DrMobile.get()+"\t\t"+PtName.get()+"\t\t"+Case.get()+"\n")
            return
        
        
        def resetbtnfunc():
            
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeies.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            apptime.set("")
            textprescreption.delete("1.0",END)
            return
        
        
        def deletebtnfunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeies.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            apptime.set("")
            textprescreption.delete("1.0",END)
            textprescreptionData.delete("1.0",END)
              
            return
        
        
        def exitbtnfunc():
            exitbtnfunc=tkinter.messagebox.askyesno("Doctor Management System","Are you sure you want to exit ?")
            if exitbtnfunc > 0:
                root.destroy()
            return
        
        
        
        
        title = Label(self.root,font=("monotype corsiva",42,"bold"),text="Doctor Managment System", bd = 5,relief ="groove",fg="black",bg="#b7d8d6")
        title.pack(side = TOP ,fill= X)
        
        
        Manage_Frame=Frame(self.root, width=2000 , height= 400 , bd=5 ,relief= RIDGE,bg="#789e9e")
        Manage_Frame.place(x=0,y=100)
        
        buttons_Frame=Frame(self.root, width=3000 , height= 55 , bd=4 ,relief=RIDGE,bg="#eef3db")
        buttons_Frame.place(x=0,y=560)
        
        Data_Frame=Frame(self.root, width=2000 , height= 400 , bd=4 ,relief= RIDGE,bg="#266E73")
        Data_Frame.place(x=0,y=620)
        
        
        
        
        
        
        
        
        
        
        
        Data_FrameLeft = LabelFrame(Manage_Frame,width=1050 ,text="General Information",font=("arial",20,"italic bold"),height= 390,bd = 7,pady=1,relief =RIDGE,bg="#789e9e")
        Data_FrameLeft.pack(side=LEFT)
        Data_FrameRigth= LabelFrame(Manage_Frame,width=2000 ,text="Patient Information",font=("arial",15,"italic bold"),height= 390,bd = 7,relief =RIDGE,bg="#789e9e")
        Data_FrameRigth.pack(side=RIGHT)
        Data_Framedata= LabelFrame(Data_Frame,width=1050 ,text="Doctor's Details",font=("arial",12,"italic bold"),height= 390,bd=4 ,relief =RIDGE,bg="#b7d8d6")
        Data_Framedata.pack(side=LEFT)
     
        

        
        
        
         #####doctor's Id
        
        
        DrIdbl= Label(Data_FrameLeft,text="Doctor ID",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrIdbl.grid(row=0,column=0 , padx=10,columnspan= 2 ,sticky=W)
        DrIdbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),state=DISABLED,width=27, textvariable=DrId)
        DrIdbltxt.grid(row=0,column=1 ,padx=10,pady=5,sticky=E)
        
        
        DrNamebl= Label(Data_FrameLeft,text="Doctor Name",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrNamebl.grid(row=1,column=0 , padx=10,sticky=W)
        DrNamebltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Drname)
        DrNamebltxt.grid(row=1,column=1 ,padx=10,pady=5,sticky=E)
        
        
        
        DrDateofBirthbl= Label(Data_FrameLeft,text="Date of Birth",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrDateofBirthbl.grid(row=2,column=0 , padx=10,sticky=W)
        DrDateofBirthbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=DateofBirth)
        DrDateofBirthbltxt.grid(row=2,column=1 ,padx=10,pady=5,sticky=E)
        
        
        
        Drspesbl= Label(Data_FrameLeft,text="Specialisation",font=("arial",12,"bold"),bg="#789e9e",width=20)
        Drspesbl.grid(row=3,column=0 , padx=10,sticky=W)
        Drspestxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Spes)
        Drspestxt.grid(row=3,column=1 ,padx=10,pady=5,sticky=E)
        
        
        DrGovtPrbl= Label(Data_FrameLeft,text="Govt/Private",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrGovtPrbl.grid(row=4,column=0 , padx=10,sticky=W)
        DrGovtPrtxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=GovtPri)
        DrGovtPrtxt.grid(row=4,column=1 ,padx=10,pady=5,sticky=E)
        GovtPrcmb=ttk.Combobox(Data_FrameLeft,textvariable=GovtPri,width=25,state="readonly",font=("arial",12,"bold"))
        GovtPrcmb["values"]=("","Goverment","Private")
        GovtPrcmb.current(0)
        GovtPrcmb.grid(row=4,column=1 , padx=10,pady=5,sticky=E)
        
        DrSurgeiesbl= Label(Data_FrameLeft,text="Surgeies",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrSurgeiesbl.grid(row=5,column=0 , padx=10,sticky=W)
        DrSurgeiestxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Surgeies)
        DrSurgeiestxt.grid(row=5,column=1 ,padx=10,pady=5,sticky=E)
        
        
        
        DrExperiencesbl= Label(Data_FrameLeft,text="Experiences",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrExperiencesbl.grid(row=6,column=0 , padx=10,sticky=W)
        DrExperiencestxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=Experiences)
        DrExperiencestxt.grid(row=6,column=1 ,padx=10,pady=5,sticky=E)
        
        
        DrNursessbl=Label(Data_FrameLeft,text="Nurses under Dr",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrNursessbl.grid(row=7,column=0 , padx=10,sticky=W)
        DrNursestxt=Entry(Data_FrameLeft,font=("arial",12,"bold") ,width=27,textvariable=Nurses)
        DrNursestxt.grid(row=7,column=1 ,padx=10,pady=5,sticky=E)
        
        DrMobilebl=Label(Data_FrameLeft,text="Doctor Mobile no",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrMobilebl.grid(row=8,column=0 , padx=10,sticky=W)
        DrMobiletxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=DrMobile)
        DrMobiletxt.grid(row=8,column=1 ,padx=10,pady=5,sticky=E)
        
        ########Patient######
        DrDate_of_Registrationbl= Label(Data_FrameLeft,text="Date",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrDate_of_Registrationbl.grid(row=0,column=2 , padx=10,columnspan= 2 ,sticky=W)
        DrDate_of_Registrationbltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),state=DISABLED,width=27, textvariable=Date_of_Registration)
        DrDate_of_Registrationbltxt.grid(row=0,column=3 ,padx=10,pady=5,sticky=E)
        
        
        PtNamebl= Label(Data_FrameLeft,text="Patient Name",font=("arial",12,"bold"),bg="#789e9e",width=20)
        PtNamebl.grid(row=1,column=2 , padx=10,sticky=W)
        PtNametxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PtName)
        PtNametxt.grid(row=1,column=3 ,padx=10,pady=5,sticky=E)
        
        
        
        apptimebl= Label(Data_FrameLeft,text="Appointement time",font=("arial",12,"bold"),bg="#789e9e",width=20)
        apptimebl.grid(row=2,column=2 , padx=10,sticky=W)
        apptimebltxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=apptime)
        apptimebltxt.grid(row=2,column=3 ,padx=10,pady=5,sticky=E)
        
        
        
        PtAgebl= Label(Data_FrameLeft,text="Patient Age",font=("arial",12,"bold"),bg="#789e9e",width=20)
        PtAgebl.grid(row=3,column=2 , padx=10,sticky=W)
        PtAgetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PtAge)
        PtAgetxt.grid(row=3,column=3 ,padx=10,pady=5,sticky=E)
        
        

        
        DrPatientAddressbl= Label(Data_FrameLeft,text="Patient Address",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrPatientAddressbl.grid(row=4,column=2 , padx=10,sticky=W)
        DrPatientAddresstxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PatientAddress)
        DrPatientAddresstxt.grid(row=4,column=3 ,padx=10,pady=5,sticky=E)
        
        
        
        DrPtMobilebl= Label(Data_FrameLeft,text="Patient Mobile no",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrPtMobilebl.grid(row=5,column=2 , padx=10,sticky=W)
        DrPtMobiletxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27, textvariable=PtMobile)
        DrPtMobiletxt.grid(row=5,column=3 ,padx=10,pady=5,sticky=E)
        
        
        DrDiseasebl=Label(Data_FrameLeft,text="Patient Disease",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrDiseasebl.grid(row=6,column=2 , padx=10,sticky=W)
        DrDiseasetxt=Entry(Data_FrameLeft,font=("arial",12,"bold") ,width=27,textvariable=Disease)
        DrDiseasetxt.grid(row=6,column=3 ,padx=10,pady=5,sticky=E)
        
        
        Casebl= Label(Data_FrameLeft,text="Case",font=("arial",12,"bold"),bg="#789e9e",width=20)
        Casebl.grid(row=7,column=2 , padx=10,sticky=W)
        Casecmb=ttk.Combobox(Data_FrameLeft,textvariable=Case,width=25,state="readonly",font=("arial",12,"bold"))
        Casecmb["values"]=("","New Case","Old Case")
        Casecmb.current(0)
        Casecmb.grid(row=7,column=3 , padx=10,pady=5,sticky=E)
        
        DrBenefitCardbl= Label(Data_FrameLeft,text="Benefit Card",font=("arial",12,"bold"),bg="#789e9e",width=20)
        DrBenefitCardbl.grid(row=8,column=2 , padx=10,sticky=W)
        BenefitCardcmb=ttk.Combobox(Data_FrameLeft,textvariable=BenefitCard,width=25,state="readonly",font=("arial",12,"bold"))
        BenefitCardcmb["values"]=("","Ayushman Card ","Health Insurance","Senior Citizen","Army Card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row=8,column=3 , padx=10,pady=5,sticky=E)
        
        textprescreption=Text(Data_FrameRigth,font=("arial",12,"bold"),width=55 , height= 17,padx=3,pady=5)
        textprescreption.grid(row=0,column=0)
        textprescreptionData=Text(Data_Framedata,font=("arial",12,"bold"),width=203 , height=12) 
        textprescreptionData.grid(row=1,column=0)
        
        
        
        ###############button
        prescreptionbtn=Button(buttons_Frame,text="Patient Information",bg="#fe615a",activebackground="#cc6686",
                           font=("arial",15,"bold"),width=22,command=prescreptionbtnfunc)
        prescreptionbtn.grid(row=0,column=0,padx=15)
        
        
        Doctordetailbtn=Button(buttons_Frame,text="Doctor's Details",bg="#fe615a",activebackground="#cc6686",
                           font=("arial",15,"bold"),width=22,command=Doctordetailbtnfunc)
        Doctordetailbtn.grid(row=0,column=1,padx=15)
        
        
        
        resetbtn=Button(buttons_Frame,text="Reset",bg="#fe615a",activebackground="#cc6686",
                           font=("arial",15,"bold"),width=22,command=resetbtnfunc)
        resetbtn.grid(row=0,column=2,padx=15)
        
        
        
        deletebtn=Button(buttons_Frame,text="Delete",bg="#fe615a",activebackground="#cc6686",
                           font=("arial",15,"bold"),width=22,command=deletebtnfunc)
        deletebtn.grid(row=0,column=3,padx=15)
        
        
        exitbtn=Button(buttons_Frame,text="Exit",bg="#fe615a",activebackground="#cc6686",
                           font=("arial",15,"bold"),width=22,command=exitbtnfunc)
        exitbtn.grid(row=0,column=4,padx=15)
        
        
        prescreptiondatarow=Label(Data_Framedata,bg="white",font=("arial",12,"bold"),text=
                                  "Date\tDoctor Id\t     Doctor Name\t Date of Birth \tSpeialisation\tGovr/Private\tSurgeries\tExperience\tNurses\tDr Mobile No \tPatient Name\t Case\tPL Age")
        prescreptiondatarow.grid(row=0,column=0,sticky=W)

if __name__ =="__main__":
    main()