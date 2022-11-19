from distutils import command
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import up, update
from PIL import Image,ImageTk
import mysql.connector

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1275x800+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #varables
        self.var_cse_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupetion=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()
        



        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',32,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=10,width=1275,height=70)

        #ncr logo
        img_logo=Image.open('rablogo6.png')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=50,y=15,width=60,height=60)

        #img_frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=80,width=1275,height=130)

        img1 = Image.open('rabimage2.jpg')
        img1 = img1.resize((500, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=500, height=160)

        # #img2

        img_2 = Image.open('rabimage3.jpg')
        img_2 = img_2.resize((500, 160),Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img_2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=400, y=0, width=500, height=160)

        # # img3

        img_3 = Image.open('rabeimage4.jpg')
        img_3 = img_3.resize((500, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img_3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=850, y=0, width=500, height=160)

        # # main frame

        main_frame=Frame(bd=3,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=210,width=1250,height=560)

        # Upper Frame

        upper_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1220,height=270)

        #Label Entry

        #case id
        caseid=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_cse_id,width=18,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        ##criminal number

        lbl_criminal=Label(upper_frame,text='Criminal NO:',font=('arial',11,'bold'))
        lbl_criminal.grid(row=0,column=2,padx=2,pady=7)

        text_criminal_No=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=18,font=('arial',11,'bold'))
        text_criminal_No.grid(row=0,column=3,padx=2,pady=7)

        ##criminal Name
        lbl_name = Label(upper_frame, text='Criminal Name:', font=('arial', 11, 'bold'))
        lbl_name.grid(row=1, column=0,sticky=W,padx=2, pady=7)

        text_name = ttk.Entry(upper_frame, textvariable=self.var_name,width=18, font=('arial', 11, 'bold'))
        text_name.grid(row=1, column=1,sticky=W,padx=2, pady=7)

        ###Nick nmae

        lbl_nickname=Label(upper_frame,text='Nick name',font=('arial',11,'bold'))
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        text_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=18,font=('arial',11,'bold'))
        text_nickname.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        ###Arrest date

        lbl_arrestDate=Label(upper_frame,text='Arrest Date:',font=('arial',11,'bold'))
        lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        text_arrestdate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=18,font=('arial',11,'bold'))
        text_arrestdate.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Date of crime

        lbl_dateofCrime=Label(upper_frame,text='Date of Crime',font=('arial',11,'bold'))
        lbl_dateofCrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        text_dateofCrime = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width=18, font=('arial', 11, 'bold'))
        text_dateofCrime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Address
        lbl_address = Label(upper_frame, text='Address:', font=('arial', 11, 'bold'))
        lbl_address.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        text_address = ttk.Entry(upper_frame,textvariable=self.var_address,width=18, font=('arial', 11, 'bold'))
        text_address.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        #Age

        lbl_address = Label(upper_frame, text='Age:', font=('arial', 11, 'bold'))
        lbl_address.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        text_dateofCrime = ttk.Entry(upper_frame, textvariable=self.var_age,width=18, font=('arial', 11, 'bold'))
        text_dateofCrime.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        #occupution

        lbl_occopetion = Label(upper_frame, text='Occupution:', font=('arial', 11, 'bold'))
        lbl_occopetion.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        text_occupution = ttk.Entry(upper_frame,textvariable=self.var_occupetion, width=18, font=('arial', 11, 'bold'))
        text_occupution.grid(row=4, column=1, sticky=W, padx=2, pady=7)

        #birthMark

        lbl_birthmark = Label(upper_frame, text='Birth Mark:', font=('arial', 11, 'bold'))
        lbl_birthmark.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        text_birthmark = ttk.Entry(upper_frame,textvariable=self.var_birthMark, width=18, font=('arial', 11, 'bold'))
        text_birthmark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        #Crime Type

        lbl_crimetype = Label(upper_frame, text='Crime Type:', font=('arial', 11, 'bold'))
        lbl_crimetype.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        text_crimetype = ttk.Entry(upper_frame,textvariable=self.var_crime_type, width=18, font=('arial', 11, 'bold'))
        text_crimetype.grid(row=0, column=5, sticky=W, padx=2, pady=7)

        ##fother_name

        lbl_Father_Name = Label(upper_frame, text='Fothers Name:', font=('arial', 11, 'bold'))
        lbl_Father_Name.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        text_crimetype = ttk.Entry(upper_frame,textvariable=self.var_father_name, width=18, font=('arial', 11, 'bold'))
        text_crimetype.grid(row=1, column=5, sticky=W, padx=2, pady=7)

        #gender

        lbl_gender = Label(upper_frame, text='Gender:', font=('arial', 11, 'bold'))
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        #Radio frame
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=645,y=82,width=150,height=26)

        # Radio button gender
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        self.var_gender.set("male")

        female = Radiobutton(radio_frame_gender, variable=self.var_gender,text='Female', value='female', font=('arial', 9, 'bold'),bg='white')
        female.grid(row=0, column=2, pady=2, padx=5, sticky=W)



        # Most Wanted

        lbl_most_wanted = Label(upper_frame,text='Most Wanted:', font=('arial', 11, 'bold'))
        lbl_most_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)




        ### Most wanted radio

        radio_frame_most_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_most_wanted.place(x=645, y=117, width=150, height=26)

        yes = Radiobutton(radio_frame_most_wanted, variable=self.var_wanted,text='Yes', value='yes', font=('arial', 9, 'bold'), bg='white')
        yes.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        no = Radiobutton(radio_frame_most_wanted,variable=self.var_wanted, text='NO', value='no', font=('arial', 9, 'bold'), bg='white')
        no.grid(row=0, column=2, pady=2, padx=5, sticky=W)

        #buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=620,height=45)

        #add boutons

        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)


        #update

        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)


        #Delete

        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)


        #clear

        btn_clear=Button(button_frame, command=self.clear_data,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #background side imager

        img_crime = Image.open('rabimage11.jpeg')
        img_crime = img_crime.resize((400,260), Image.ANTIALIAS)
        self.photocrime = ImageTk.PhotoImage(img_crime)

        self.img_crime = Label(upper_frame, image=self.photocrime)
        self.img_crime.place(x=810, y=0, width=400, height=260)





        ### down Frame

        down_frame=LabelFrame(main_frame, bd=3,relief=RIDGE,text='Criminal Information table',font=('times new roman',11,'bold'),fg='red', bg='white')
        down_frame.place(x=10, y=280, width=1220, height=270)



        #  # Search frame

        search_frame = LabelFrame(down_frame,bd=3, relief=RIDGE, text='Search Criminal Information',font=('times new roman',11,'bold'), fg='red', bg='white')
        search_frame.place(x=10, y=5, width=1200, height=60)

        search_by = Label(search_frame, text='Search By', font=('arial', 11, 'bold'),bg='red',fg='white')
        search_by.grid(row=0, column=0, sticky=W, padx=5,)

        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame, textvariable=self.var_com_search,font=('arial',11,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select options','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search = StringVar()
        search_text = ttk.Entry(search_frame,textvariable=self.var_search, width=18, font=('arial', 11, 'bold'))
        search_text.grid(row=0, column=2, sticky=W, padx=5)

        ##Search frame

        btn_delete = Button(search_frame, command=self.search_data,text='Search', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=3, padx=3, pady=5)

        # all button

        show_all_button = Button(search_frame,command=self.fetch_data,text='Show All', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        show_all_button.grid(row=0, column=4, padx=3, pady=5)

        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=8,y=65,width=1200,height=170)

        #Tabel Frame
        crimeagency = Label(search_frame, text=' BANGLADESH CRIME AGENCY',bg='white',fg='crimson',font=('arial', 20, 'bold'))
        crimeagency.grid(row=0, column=5, sticky=W, padx=10)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseID')
        self.criminal_table.heading('2',text='CrimeNO')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nick Name')
        self.criminal_table.heading('5', text='Arrest Date')
        self.criminal_table.heading('6', text='Crime of Date')
        self.criminal_table.heading('7', text='Address')
        self.criminal_table.heading('8', text='Age')
        self.criminal_table.heading('9', text='Occupation')
        self.criminal_table.heading('10', text='Birth Mark')
        self.criminal_table.heading('11', text='Crime Type')
        self.criminal_table.heading('12', text='Father Name')
        self.criminal_table.heading('13', text='Gender')
        self.criminal_table.heading('14', text='Wanted')

        self.criminal_table['show']='headings'
        self.criminal_table.column('1',width=90)
        self.criminal_table.column('2',width=90)
        self.criminal_table.column('3',width=90)
        self.criminal_table.column('4',width=90)
        self.criminal_table.column('5',width=90)
        self.criminal_table.column('6',width=90)
        self.criminal_table.column('7',width=90)
        self.criminal_table.column('8',width=90)
        self.criminal_table.column('9',width=90)
        self.criminal_table.column('10',width=90)
        self.criminal_table.column('11',width=90)
        self.criminal_table.column('12',width=90)
        self.criminal_table.column('13',width=90)
        self.criminal_table.column('14',width=90)

        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #Add Function
    def add_data(self):
        if self.var_cse_id.get()=="":
            messagebox.showerror("Error","All Fields are requride")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="481826@48",database="myserver2")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into criminal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_cse_id.get(),
                                                                                                            self.var_criminal_no.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_nickname.get(),
                                                                                                            self.var_arrest_date.get(),
                                                                                                            self.var_date_of_crime.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_occupetion.get(),
                                                                                                            self.var_birthMark.get(),
                                                                                                            self.var_crime_type.get(),
                                                                                                            self.var_father_name.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_wanted.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo("Success","Criminal hase been added")
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}")

    ###fetch dat
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="481826@48",database="myserver2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from criminal1")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #get cursor

    def get_cursor(self,events=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content["values"]

        self.var_cse_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupetion.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    #update

    def update_data(self):
        if self.var_cse_id.get()=="":
            messagebox.showerror("Error","All Fields are requride")
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="481826@48",database="myserver2")
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal1 set Criminal_no=%s,Criminal_Name=%s,Nick_name=%s,arrest_date=%s,dateofcrime=%s,address=%s,age=%s,occupation=%s,Birthmark=%s,crimetype=%s,fathername=%s,gender=%s,wanted=%s where Case_id=%s',(

                                                                                                                                                                                                                                                self.var_criminal_no.get(),
                                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                                self.var_nickname.get(),
                                                                                                                                                                                                                                                self.var_arrest_date.get(),
                                                                                                                                                                                                                                                self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                                self.var_age.get(),
                                                                                                                                                                                                                                                self.var_occupetion.get(),
                                                                                                                                                                                                                                                self.var_birthMark.get(),
                                                                                                                                                                                                                                                self.var_crime_type.get(),
                                                                                                                                                                                                                                                self.var_father_name.get(),
                                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                                self.var_wanted.get(),  
                                                                                                                                                                                                                                                self.var_cse_id.get(),
                                                                                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Crime record Successfully updated')
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}")
    #delete
    def delete_data(self):
        if self.var_cse_id.get() == "":
            messagebox.showerror("Error", "All Fields are requrided")
        else:
            try:
                Delete = messagebox.askyesno('Delete', 'Are you sure delete this criminal record')
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="myserver2")
                    my_cursor = conn.cursor()

                    sql='delete from criminal1 where Case_id=%s'
                    value=(self.var_cse_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success', 'Crime record Successfully deleted ')
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")
    #clear
    def clear_data(self):
        self.var_cse_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupetion.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    # search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror("Error", "All Fields are requrided")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="481826@48",database="myserver2")
                my_cursor = conn.cursor()
                my_cursor.execute('select * from criminal1 where ' +str(self.var_com_search.get())+" LIKE'"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!= 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to{str(es)}")






    

if __name__=='__main__':
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
