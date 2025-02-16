import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import datetime
from controllers.AddController import Addcontroller
from controllers.EditController import Editcontroller
from controllers.SearchController import Searchcontroller
from controllers.DeleteController import Deletecontroller
from controllers.DataExporter import DataExporterC
from tkcalendar import Calendar
import pandas as pd
from constants import GEOMETRY
from constants import IMAG_TENT, IMAG_SAERCH_2, IMAG_BACK, IMAG_TRASH, IMAG_EDIT, IMAG_ADD, IMAG_SAERCH, IMAG_HOME

class DashboardPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        IMAG_ADD_ = PhotoImage(file=IMAG_ADD).subsample(3,3)
        IMAG_EDIT_ = PhotoImage(file=IMAG_EDIT).subsample(3,3)
        IMAG_TRASH_ = PhotoImage(file=IMAG_TRASH).subsample(3,3)
        IMAG_SAERCH_ = PhotoImage(file=IMAG_SAERCH).subsample(3,3)
        IMAG_HOME_ = PhotoImage(file=IMAG_HOME).subsample(12, 12)
        IMAG_TENT_ = PhotoImage(file=IMAG_TENT).subsample(10, 10)
        self.frame_2 = tk.LabelFrame(self, border=1, relief="ridge")
        self.frame_2.grid()
        self.frame_2.place(relx=0.5, rely=0.2, anchor="center", width=925, height=150)
        # العنوان الرئيسي
        title_label = tk.Label(self.frame_2,
                               text=" إدارة مخيم الشهداء ",
                               font=("Arial", 50, "bold"),
                               image=IMAG_TENT_,
                               compound=RIGHT,
                               fg="#45a049")
        title_label.image = IMAG_TENT_
        title_label.pack(pady=40)

        # زر تسجيل الدخول
        add_button = tk.Button(self,
                               text="أضافة(أسرة, أفراد)",
                               font=("Arial", 20, "bold"),
                               image=IMAG_ADD_,
                               relief=SOLID,
                               border=0,
                               activebackground="#45a049",
                               activeforeground="white",
                               fg="#45a049",
                               compound=TOP,
                               command=self.add)
        add_button.image = IMAG_ADD_
        add_button.pack()
        add_button.place(x=140,y=300)
        edit_button = tk.Button(self,
                                text="تعديل",
                                font=("Arial", 20, "bold"),
                                image=IMAG_EDIT_,
                                relief=SOLID,
                                border=0,
                                activebackground="#45a049",
                                activeforeground="white",
                                fg="#45a049",
                                compound=TOP,
                                command=self.edit)
        edit_button.image = IMAG_EDIT_
        edit_button.pack()
        edit_button.place(x=390,y=300)
        delete_button = tk.Button(self,
                                  text="حذف",
                                  font=("Arial", 20, "bold"),
                                  image=IMAG_TRASH_,
                                  relief=SOLID,
                                  border=0,
                                  activebackground="#45a049",
                                  activeforeground="white",
                                  fg="#45a049",
                                  compound=TOP,
                                  command=self.delete)
        delete_button.image = IMAG_TRASH_
        delete_button.pack()
        delete_button.place(x=640,y=300)
        saerch_button = tk.Button(self,
                                  text="بحث",
                                  font=("Arial", 20, "bold"),
                                  image=IMAG_SAERCH_,
                                  relief=SOLID,
                                  border=0,
                                  activebackground="#45a049",
                                  activeforeground="white",
                                  fg="#45a049",
                                  compound=TOP,
                                  # command=lambda: master.show_frame(SearchPage, GEOMETRY)).pack()
                                  command=self.search)
        saerch_button.image = IMAG_SAERCH_
        saerch_button.pack()
        saerch_button.place(x=885,y=300)

        self.bind('<Return>', lambda event: self.add())



    def add(self):
        self.master.show_frame(AddPage, GEOMETRY)
    def edit(self):
        self.master.show_frame(EditPage, GEOMETRY)
    def delete(self):
        self.master.show_frame(DeletePage, GEOMETRY)
    def search(self):
        self.master.show_frame(SearchPage, GEOMETRY)

class AddPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.sex = tk.IntVar()
        self.maternity = tk.IntVar()
        self.chronicdisease = tk.IntVar()
        self.socialstatus = tk.IntVar()
        self.alliance = tk.IntVar()
        self.obstruction_kinetic = tk.BooleanVar()
        self.obstruction_audio = tk.BooleanVar()
        self.obstruction_sensuality = tk.BooleanVar()
        self.obstruction_visual = tk.BooleanVar()
        self.obstruction_fatness = tk.BooleanVar()
        IMAG_BACK_ = PhotoImage(file=IMAG_BACK).subsample(12, 12)
        frame_ = tk.LabelFrame(self, border=0, relief="ridge")
        frame_.grid()
        frame_.place(relx=0.5,
                     rely=0.07,
                     anchor="center",
                     width=1200,
                     height=95)
        return_button = tk.Button(frame_,
                                  text="رجوع",
                                  font=("Arial", 18, "bold"),
                                  image=IMAG_BACK_,
                                  relief=SOLID,
                                  border=0,
                                  activebackground="#45a049",
                                  activeforeground="white",
                                  fg="#45a049",
                                  compound=TOP,
                                  command=self.go_back)
        return_button.image = IMAG_BACK_
        return_button.pack()
        return_button.place(x=1, y=1)
        # العنوان الرئيسي
        title_label = tk.Label(frame_,
                               text="أضافة الأسرة والأفراد",
                               font=("Arial", 50, "bold"),
                               # image=IMAG_SAERCH_2_,
                               compound=RIGHT,
                               fg="#45a049")
        # title_label.image = IMAG_SAERCH_2_
        title_label.pack(pady=10)
        # ***********************************
        self.frame_2 = ttk.Frame(self)
        self.frame_2.pack()
        self.frame_2.place(x=10,
                           relx=0.5,
                           rely=0.64,
                           anchor="center",
                           width=1200,
                           height=700)
        # Create a Frame for input widgets
        widgets_frame = ttk.LabelFrame(self.frame_2, text="Add Data", padding=(5, 5, 5, 5))
        widgets_frame.grid(row=0, column=0, padx=80, pady=(5, 5), sticky="nsew")
        widgets_frame.columnconfigure(index=0, weight=0)
        # ******************/////////
        address_frame = ttk.LabelFrame(widgets_frame, text="العنوان", padding=(5, 5, 5, 5))
        address_frame.grid(row=0, column=0, padx=1, pady=(0, 5), columnspan=3, sticky="ew")
        address_frame.columnconfigure(index=0, weight=0)
        self.city_entry = ttk.Entry(address_frame,font=("Arial", 14, "bold"))
        self.city_entry.insert(0, "مدينة السابقة")
        self.city_entry.bind("<FocusIn>", lambda e: self.city_entry.delete('0', 'end'))
        self.city_entry.grid(row=0, column=0,padx=2, pady=(0, 5), sticky="ew")
        self.borhood_entry = ttk.Entry(address_frame,font=("Arial", 14, "bold"))
        self.borhood_entry.insert(0, "الحي")
        self.borhood_entry.bind("<FocusIn>", lambda e: self.borhood_entry.delete('0', 'end'))
        self.borhood_entry.grid(row=0, column=1, padx=2, pady=(0, 5), sticky="ew")
        self.place_entry = ttk.Entry(address_frame,font=("Arial", 14, "bold"))
        self.place_entry.insert(0, "أقرب معلم")
        self.place_entry.bind("<FocusIn>", lambda e: self.place_entry.delete('0', 'end'))
        self.place_entry.grid(row=1, column=0, padx=2, pady=(0, 5),columnspan=2,  sticky="ew")
        # ******************////////
        # ******************/////////
        person_frame = ttk.LabelFrame(widgets_frame, text="معلومات اساسية", padding=(5, 5, 5, 5))
        person_frame.grid(row=0, column=3, padx=2, pady=(0, 5), columnspan=2, sticky="ew")
        person_frame.columnconfigure(index=0, weight=0)
        self.name_entry = ttk.Entry(person_frame,font=("Arial", 14, "bold"))
        self.name_entry.insert(0, "الأسم رباعي")
        self.name_entry.bind("<FocusIn>", lambda e: self.name_entry.delete('0', 'end'))
        self.name_entry.grid(row=0, column=0, padx=2, pady=(0, 5), sticky="ew")
        self.identity_entry = ttk.Entry(person_frame,font=("Arial", 14, "bold"))
        self.identity_entry.insert(0, "رقم الهوية")
        self.identity_entry.bind("<FocusIn>", lambda e: self.identity_entry.delete('0', 'end'))
        self.identity_entry.grid(row=0, column=1, padx=2, pady=(0, 5), sticky="ew")
        self.phone_entry = ttk.Entry(person_frame,font=("Arial", 14, "bold"))
        self.phone_entry.insert(0, "رقم الجوال")
        self.phone_entry.bind("<FocusIn>", lambda e: self.phone_entry.delete('0', 'end'))
        self.phone_entry.grid(row=1, column=0, padx=2, pady=(0, 5),columnspan=2, sticky="ew")
        # ******************////////
        # ******************/////////

        # self.num_entry = ttk.Entry(widgets_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=0, column=4, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        # ******************/////////
        sex_frame = ttk.LabelFrame(widgets_frame, text="الجنس", padding=(5, 5, 5, 5))
        sex_frame.grid(row=1, column=0, padx=2, pady=(0, 5), sticky="ew")
        sex_frame.columnconfigure(index=0, weight=0)
        # Radiobuttons
        self.mail = ttk.Radiobutton(sex_frame, text="ذكر", variable=self.sex, value=1)
        self.mail.grid(row=0, column=0, padx=2, pady=5, sticky="nsew")
        self.femail = ttk.Radiobutton(sex_frame, text="انثى", variable=self.sex, value=2)
        self.femail.grid(row=0, column=1, padx=2, pady=5, sticky="nsew")

        # self.num_entry = ttk.Entry(address_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        # ******************/////////
        maternity_frame = ttk.LabelFrame(widgets_frame, text="حامل / مرضعة", padding=(5, 5, 5, 5))
        maternity_frame.grid(row=1, column=1, padx=10, pady=(0, 5), sticky="ew")
        maternity_frame.columnconfigure(index=0, weight=0)
        radio_1 = ttk.Radiobutton(maternity_frame, text="حامل", variable=self.maternity, value=1)
        radio_1.grid(row=0, column=0, padx=2, pady=5, sticky="nsew")
        radio_2 = ttk.Radiobutton(maternity_frame, text="مرضعة", variable=self.maternity, value=2)
        radio_2.grid(row=0, column=1, padx=2, pady=5, sticky="nsew")
        # ******************////////
        # ******************/////////
        chronicdisease_frame = ttk.LabelFrame(widgets_frame, text="أمراض مزمنة", padding=(5, 5, 5, 5))
        chronicdisease_frame.grid(row=1, column=2, padx=2, pady=(0, 5), columnspan=1, sticky="ew")
        chronicdisease_frame.columnconfigure(index=0, weight=0)
        radio_1 = ttk.Radiobutton(chronicdisease_frame, text="سكري", variable=self.chronicdisease, value=1)
        radio_1.grid(row=0, column=0, padx=2, pady=5, sticky="nsew")
        radio_2 = ttk.Radiobutton(chronicdisease_frame, text="ضغط", variable=self.chronicdisease, value=2)
        radio_2.grid(row=0, column=1, padx=2, pady=5, sticky="nsew")
        radio_3 = ttk.Radiobutton(chronicdisease_frame, text="كلاهما", variable=self.chronicdisease, value=3)
        radio_3.grid(row=0, column=2, padx=2, pady=5, sticky="nsew")
        # ******************////////
        # ******************/////////
        note_frame = ttk.LabelFrame(widgets_frame, text="ملاحظة", padding=(5, 5, 5, 5))
        note_frame.grid(row=1, column=3, padx=2, pady=(0, 5), rowspan=2, sticky="ew")
        note_frame.columnconfigure(index=0, weight=0)
        self.note_entry = ttk.Entry(note_frame, font=("Arial", 14, "bold"))
        self.note_entry.insert(0, "ملاحظة")
        self.note_entry.bind("<FocusIn>", lambda e: self.note_entry.delete('0', 'end'))
        self.note_entry.grid(row=0, column=0, ipadx=5, ipady=100, padx=2, pady=(0, 5), sticky="ew")
        # self.num_entry = ttk.Entry(address_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        # ******************/////////

        # self.num_entry = ttk.Entry(widgets_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=1, column=4, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        # ******************/////////
        socialstatus_frame = ttk.LabelFrame(widgets_frame, text="الحالة الأجتماعية", padding=(5, 5, 5, 5))
        socialstatus_frame.grid(row=2, column=0, padx=2, pady=(0, 5), rowspan=2, sticky="ew")
        socialstatus_frame.columnconfigure(index=0, weight=0)
        radio_1 = ttk.Radiobutton(socialstatus_frame, text="متزوج", variable=self.socialstatus, value=1)
        radio_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        radio_2 = ttk.Radiobutton(socialstatus_frame, text="أعزب", variable=self.socialstatus, value=2)
        radio_2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        radio_3 = ttk.Radiobutton(socialstatus_frame, text="أرمل", variable=self.socialstatus, value=3)
        radio_3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        radio_4 = ttk.Radiobutton(socialstatus_frame, text="مطلقة", variable=self.socialstatus, value=4)
        radio_4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        # self.num_entry = ttk.Entry(address_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=0, column=0, ipadx=10, ipady=10, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        # ******************/////////
        alliance_frame = ttk.LabelFrame(widgets_frame, text="صلة القرابة", padding=(5, 5, 5, 5))
        alliance_frame.grid(row=2, column=1, padx=10, pady=(0, 5), rowspan=2, sticky="ew")
        alliance_frame.columnconfigure(index=0, weight=0)
        radio_1 = ttk.Radiobutton(alliance_frame, text="رب الأسرة", variable=self.alliance, value=1)
        radio_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        radio_2 = ttk.Radiobutton(alliance_frame, text="زوجة", variable=self.alliance, value=2)
        radio_2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        radio_3 = ttk.Radiobutton(alliance_frame, text="ابن", variable=self.alliance, value=3)
        radio_3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        radio_4 = ttk.Radiobutton(alliance_frame, text="بنت", variable=self.alliance, value=4)
        radio_4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        # self.num_entry = ttk.Entry(address_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=0, column=0, ipadx=10, ipady=100, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        # ******************/////////
        obstruction_frame = ttk.LabelFrame(widgets_frame, text="أعاقة", padding=(5, 5, 5, 5))
        obstruction_frame.grid(row=2, column=2, padx=10, pady=(0, 5), rowspan=2, sticky="ew")
        obstruction_frame.columnconfigure(index=0, weight=0)
        self.check_1 = ttk.Checkbutton(obstruction_frame, text="حركية", variable=self.obstruction_kinetic)
        self.check_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        check_2 = ttk.Checkbutton(obstruction_frame, text="سمعية", variable=self.obstruction_audio)
        check_2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        check_3 = ttk.Checkbutton(obstruction_frame, text="حسية", variable=self.obstruction_sensuality)
        check_3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        check_4 = ttk.Checkbutton(obstruction_frame, text="بصرية", variable=self.obstruction_visual)
        check_4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        check_5 = ttk.Checkbutton(obstruction_frame, text="دهنية", variable=self.obstruction_fatness)
        check_5.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        # self.num_entry = ttk.Entry(address_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=0, column=0, ipadx=10, ipady=100, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        # ******************/////////

        # self.num_entry = ttk.Entry(address_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=0, column=0, ipadx=10, ipady=100, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        # ******************/////////
        dateofconstruction_frame = ttk.LabelFrame(widgets_frame, text="تاريخ الميلاد", padding=(5, 5, 5, 5))
        dateofconstruction_frame.grid(row=1, column=4, padx=15, pady=(0, 5), columnspan=2, rowspan=2, sticky="ew")
        dateofconstruction_frame.columnconfigure(index=0, weight=0)
        # self.date_entry = ttk.D
        self.sel = tk.StringVar()
        self.date_Calendar = Calendar(dateofconstruction_frame,
                                      selectmode='day',
                                      year=2000,
                                      month=1,
                                      day=25,
                                      # textvariable=self.sel,
                                    # text=cal,
                                    # background=cal,
                                    )
        self.date_Calendar.grid(row=0, column=0, ipadx=10, ipady=20, padx=10, pady=(0, 5), sticky="ew")
        # ******************////////
        widgets_frame_2 = ttk.LabelFrame(self.frame_2, text="أزرار الاضافة", padding=(5, 5, 5, 5))
        widgets_frame_2.grid(row=1, column=0, padx=320, pady=(5, 5), sticky="nsew")
        widgets_frame_2.columnconfigure(index=0, weight=0)

        addpersonbutton = ttk.Button(widgets_frame_2,
                                     text="أضافة فرد للأسرة",
                                     style="Accent.TButton",
                                     command=self.goaddperson
                                     )
        addpersonbutton.grid(row=0, column=0, ipadx=50, ipady=18, padx=30, pady=(0, 5), sticky="nsew")

        addfamilybutton = ttk.Button(widgets_frame_2,
                                     text="أضافة أسرة",
                                     style="Accent.TButton",
                                     command=self.goaddfamily
                                     )
        addfamilybutton.grid(row=0, column=1, ipadx=50, ipady=18, padx=10, pady=(0, 5), sticky="nsew")

    def goaddfamily(self):
        dict_family ={}
        dict_person = {}
        dict_obstruction = {}
        localtime = datetime.datetime.now()
        dict_family["Identity_Person"] = self.identity_entry.get()
        dict_family["PhoneNumber"] = self.phone_entry.get()
        address = self.city_entry.get() + " - " + self.borhood_entry.get() + " - " + self.place_entry.get()
        dict_family["Address"] = address
        dict_family["DateOFConstruction"] = str(localtime.date())
        # print(dict_family)
        # print(localtime.date())
        dict_person["PhoneNumber"] = self.phone_entry.get()
        dict_person["IdentityPerson"] = self.identity_entry.get()
        # dict_person["null"] = None
        dict_person["FullName"] = self.name_entry.get()
        dict_person["DateOFBirth"] = self.date_Calendar.selection_get()
        dict_person["Sex"] = self.sex.get()
        dict_person["SocialStatus"] = self.socialstatus.get()
        dict_person["Alliance"] = self.alliance.get()
        dict_obstruction["kinetic"] = self.obstruction_kinetic.get()
        dict_obstruction["audio"] = self.obstruction_audio.get()
        dict_obstruction["sensuality"] = self.obstruction_sensuality.get()
        dict_obstruction["visual"] = self.obstruction_visual.get()
        dict_obstruction["fatness"] = self.obstruction_fatness.get()
        # print(dict_obstruction)
        dict_person["Obstruction"] = dict_obstruction
        dict_person["ChronicDiseases"] = self.chronicdisease.get()
        dict_person["Maternity"] = self.maternity.get()
        dict_person["Note"] = self.note_entry.get()
        dict_person["DateOFConstructionPerson"] = str(localtime.date())
        Addcontroller.addfamily_rul(self,dict_family)
        if self.name_entry.get() != "الأسم رباعي" and self.sex.get()!= 0 and self.socialstatus.get() != 0 and self.alliance.get() != 0:
            Addcontroller.addperson_rul(self,dict_person)
        else:
            messagebox.showinfo("خطأ", "يوجد بيانات غير كاملة لاضافة رب الأسرة")
        # print(dict_person)
        self.claerdata()

    def goaddperson(self):
        dict_person = {}
        dict_obstruction = {}
        localtime = datetime.datetime.now()
        dict_person["PhoneNumber"] = self.phone_entry.get()
        dict_person["IdentityPerson"] = self.identity_entry.get()
        dict_person["FullName"] = self.name_entry.get()
        dict_person["DateOFBirth"] = self.date_Calendar.selection_get()
        dict_person["Sex"] = self.sex.get()
        dict_person["SocialStatus"] = self.socialstatus.get()
        dict_person["Alliance"] = self.alliance.get()
        dict_obstruction["kinetic"] = self.obstruction_kinetic.get()
        dict_obstruction["audio"] = self.obstruction_audio.get()
        dict_obstruction["sensuality"] = self.obstruction_sensuality.get()
        dict_obstruction["visual"] = self.obstruction_visual.get()
        dict_obstruction["fatness"] = self.obstruction_fatness.get()
        dict_person["Obstruction"] = dict_obstruction
        dict_person["ChronicDiseases"] = self.chronicdisease.get()
        dict_person["Maternity"] = self.maternity.get()
        dict_person["Note"] = self.note_entry.get()
        dict_person["DateOFConstructionPerson"] = str(localtime.date())
        Addcontroller.addperson_rul(self, dict_person)
        # print(dict_person)
        self.claerdata()

    def claerdata(self):
        self.city_entry.delete('0', 'end')
        self.city_entry.insert(0, "مدينة السابقة")
        self.borhood_entry.delete('0', 'end')
        self.borhood_entry.insert(0, "الحي")
        self.place_entry.delete('0', 'end')
        self.place_entry.insert(0, "أقرب معلم")
        self.name_entry.delete('0', 'end')
        self.name_entry.insert(0, "الأسم رباعي")
        self.identity_entry.delete('0', 'end')
        self.identity_entry.insert(0, "رقم الهوية")
        self.phone_entry.delete('0', 'end')
        self.phone_entry.insert(0, "رقم الجوال")
        self.sex.set(0)
        self.maternity.set(0)
        self.chronicdisease.set(0)
        self.socialstatus.set(0)
        self.alliance.set(0)
        self.obstruction_kinetic.set(0)
        self.obstruction_audio.set(0)
        self.obstruction_sensuality.set(0)
        self.obstruction_visual.set(0)
        self.obstruction_fatness.set(0)



        # ******************

    def go_back(self):
        """الرجوع إلى الإطار السابق"""
        self.master.show_frame(DashboardPage, GEOMETRY)

class EditPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        IMAG_EDIT_ = PhotoImage(file=IMAG_EDIT).subsample(10, 10)
        self.combo_list_person = ["حامل/مرضعة", "أمراض مزمنة", "إعاقة" ,
                           "ملاحظة","هوية","الأسم الرباعي","تاريخ الميلادي",
                           "الجنس","الحالة الاجتماعية","صلة القرابة" ]

        self.combo_list_family = ["رقم الجوال", "العنوان"]

        IMAG_BACK_ = PhotoImage(file=IMAG_BACK).subsample(12, 12)
        self.sex = tk.IntVar()
        self.maternity = tk.IntVar()
        self.chronicdisease = tk.IntVar()
        self.socialstatus = tk.IntVar()
        self.alliance = tk.IntVar()
        self.obstruction_kinetic = tk.BooleanVar()
        self.obstruction_audio = tk.BooleanVar()
        self.obstruction_sensuality = tk.BooleanVar()
        self.obstruction_visual = tk.BooleanVar()
        self.obstruction_fatness = tk.BooleanVar()
        frame_ = tk.LabelFrame(self, border=0, relief="ridge")
        frame_.grid()
        frame_.place(relx=0.5,
                     rely=0.07,
                     anchor="center",
                     width=1200,
                     height=95)
        return_button = tk.Button(frame_,
                                  text="رجوع",
                                  font=("Arial", 18, "bold"),
                                  image=IMAG_BACK_,
                                  relief=SOLID,
                                  border=0,
                                  activebackground="#45a049",
                                  activeforeground="white",
                                  fg="#45a049",
                                  compound=TOP,
                                  command=self.go_back)
        return_button.image = IMAG_BACK_
        return_button.pack()
        return_button.place(x=1, y=1)
        #     **************************
        title_label = tk.Label(frame_,
                               text=" تعديل على بيانات مخيم الشهداء ",
                               font=("Arial", 50, "bold"),
                               image=IMAG_EDIT_,
                               compound=RIGHT,
                               fg="#45a049")
        title_label.image = IMAG_EDIT_
        title_label.pack(pady=10)
        #   ************************************************
        self.frame_2 = ttk.Frame(self)
        self.frame_2.pack()
        self.frame_2.place(x=10,
                           relx=0.5,
                           rely=0.64,
                           anchor="center",
                           width=1200,
                           height=700)
        # Create a Frame for input widgets
        self.widgets_frame = ttk.LabelFrame(self.frame_2, text="Edit", padding=(20, 5, 20, 3))
        self.widgets_frame.grid(row=0, column=0, padx=(80,10), pady=5, sticky="nsew", rowspan=3)
        self.widgets_frame.columnconfigure(index=0, weight=0)
        # ********
        onefamilybutton = ttk.Button(self.widgets_frame,
                                     text="واجهة التعديل على بيانات الأسرة",
                                     style="Accent.TButton",
                                     command=self.deleteframeeditfamily
                                     )
        onefamilybutton.grid(row=0, column=0, ipady=2, padx=10, pady=5, sticky="nsew")
        onefamilybutton = ttk.Button(self.widgets_frame,
                                     text="واجهة التعديل على بيانات الفرد",
                                     style="Accent.TButton",
                                     command=self.deleteframeeditperson
                                     )
        onefamilybutton.grid(row=1, column=0, ipady=2, padx=10, pady=5, sticky="nsew")
        self.editfamily_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.editfamily_frame.grid(row=2, column=0, padx=2, pady=3, sticky="ew")
        self.editfamily_frame.columnconfigure(index=0, weight=0)
        self.editperson_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.editperson_frame.grid(row=2, column=0, padx=2, pady=3, sticky="ew")
        self.editperson_frame.columnconfigure(index=0, weight=0)
        self.treeFrame = ttk.LabelFrame(self.frame_2, text="بيانات الفرد", padding=(20, 20, 20, 10))



    def treeoneperson(self):
        dataonep = Editcontroller.getdataoneperson(self, self.identityentry.get())
        self.treeFrame = ttk.LabelFrame(self.frame_2, text="بيانات الفرد", padding=(20, 20, 20, 10))
        self.treeFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew", rowspan=3)
        title_label = tk.Label(self.treeFrame,
                               text=" كل بيانات الفرد ",
                               font=("Arial", 20, "bold"),
                               compound=RIGHT,
                               fg="#45a049",

                               )
        title_label.grid(row=0, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), columnspan=4, sticky="ew")
        idfamily = tk.Label(self.treeFrame,
                            text=dataonep["IdentityPerson"],
                            font=("Arial", 16, "bold"),
                            compound=RIGHT,
                            fg="white")
        idfamily.grid(row=1, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidfamily = tk.Label(self.treeFrame,
                                 text="رقم الهوية",
                                 font=("Arial", 16, "bold"),
                                 compound=RIGHT,
                                 fg="#45a049")
        titleidfamily.grid(row=1, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        identity = tk.Label(self.treeFrame,
                            text=dataonep["Sex"],
                            font=("Arial", 16, "bold"),
                            compound=RIGHT,
                            fg="white")
        identity.grid(row=2, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidentity = tk.Label(self.treeFrame,
                                 text="الجنس",
                                 font=("Arial", 16, "bold"),
                                 compound=RIGHT,
                                 fg="#45a049")
        titleidentity.grid(row=2, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        phonenumber = tk.Label(self.treeFrame,
                               text=dataonep["Alliance"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        phonenumber.grid(row=3, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlephonenumber = tk.Label(self.treeFrame,
                                    text="صلة القرابة",
                                    font=("Arial", 16, "bold"),
                                    compound=RIGHT,
                                    fg="#45a049")
        titlephonenumber.grid(row=3, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        address = tk.Label(self.treeFrame,
                           text=dataonep["ChronicDiseases"],
                           font=("Arial", 16, "bold"),
                           compound=RIGHT,
                           fg="white")
        address.grid(row=4, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleaddress = tk.Label(self.treeFrame,
                                text="الأمراض المزمنة",
                                font=("Arial", 16, "bold"),
                                compound=RIGHT,
                                fg="#45a049")
        titleaddress.grid(row=4, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        numberfamily = tk.Label(self.treeFrame,
                                text=dataonep["Note"],
                                font=("Arial", 16, "bold"),
                                compound=RIGHT,
                                fg="white")
        numberfamily.grid(row=5, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlenumberfmaily = tk.Label(self.treeFrame,
                                     text="ملاحظة",
                                     font=("Arial", 16, "bold"),
                                     compound=RIGHT,
                                     fg="#45a049")
        titlenumberfmaily.grid(row=5, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        # ************************************
        # ***********************************
        idfamily = tk.Label(self.treeFrame,
                            text=dataonep["FullName"],
                            font=("Arial", 16, "bold"),
                            compound=RIGHT,
                            fg="white")
        idfamily.grid(row=1, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidfamily = tk.Label(self.treeFrame,
                                 text="الأسم رباعي",
                                 font=("Arial", 16, "bold"),
                                 compound=RIGHT,
                                 fg="#45a049")
        titleidfamily.grid(row=1, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        identity = tk.Label(self.treeFrame,
                            text=dataonep["DateOFBirth"],
                            font=("Arial", 16, "bold"),
                            compound=RIGHT,
                            fg="white")
        identity.grid(row=2, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidentity = tk.Label(self.treeFrame,
                                 text="تاريخ الميلاد",
                                 font=("Arial", 16, "bold"),
                                 compound=RIGHT,
                                 fg="#45a049")
        titleidentity.grid(row=2, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        phonenumber = tk.Label(self.treeFrame,
                               text=dataonep["SocialStatus"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        phonenumber.grid(row=3, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlephonenumber = tk.Label(self.treeFrame,
                                    text="الحالة الأجتماعية",
                                    font=("Arial", 16, "bold"),
                                    compound=RIGHT,
                                    fg="#45a049")
        titlephonenumber.grid(row=3, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        address = tk.Label(self.treeFrame,
                           text=dataonep["Obstruction"],
                           font=("Arial", 16, "bold"),
                           compound=RIGHT,
                           fg="white")
        address.grid(row=4, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleaddress = tk.Label(self.treeFrame,
                                text="الأعاقة",
                                font=("Arial", 16, "bold"),
                                compound=RIGHT,
                                fg="#45a049")
        titleaddress.grid(row=4, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        numberfamily = tk.Label(self.treeFrame,
                                text=dataonep["Maternity"],
                                font=("Arial", 16, "bold"),
                                compound=RIGHT,
                                fg="white")
        numberfamily.grid(row=5, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlenumberfmaily = tk.Label(self.treeFrame,
                                     text="الأمومة",
                                     font=("Arial", 16, "bold"),
                                     compound=RIGHT,
                                     fg="#45a049")
        titlenumberfmaily.grid(row=5, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")


    def treeonefamily(self):
        self.treeFrame.grid_forget()
        dataonef = Editcontroller.getdataonefamily(self, self.identityentry.get())
        treeFrame = ttk.LabelFrame(self.frame_2, text="بيانات الأسرة", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0, column=1, padx=100, pady=10, sticky="nsew", rowspan=3)
        title_label = tk.Label(treeFrame,
                               text=" كل بيانات الأسرة ",
                               font=("Arial", 20, "bold"),
                               compound=RIGHT,
                               fg="#45a049",

                               )
        title_label.grid(row=0, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5),columnspan=2, sticky="ew")
        idfamily = tk.Label(treeFrame,
                               text=dataonef["Id"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        idfamily.grid(row=1, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidfamily = tk.Label(treeFrame,
                               text="رقم الأسرة",
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="#45a049")
        titleidfamily.grid(row=1, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        identity = tk.Label(treeFrame,
                               text=dataonef["Identity_Person"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        identity.grid(row=2, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidentity = tk.Label(treeFrame,
                               text="رقم هوية رب الأسرة",
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="#45a049")
        titleidentity.grid(row=2, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        phonenumber = tk.Label(treeFrame,
                               text=dataonef["PhoneNumber"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        phonenumber.grid(row=3, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlephonenumber = tk.Label(treeFrame,
                               text="رقم الجوال",
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="#45a049")
        titlephonenumber.grid(row=3, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        address = tk.Label(treeFrame,
                               text=dataonef["Address"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        address.grid(row=4, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleaddress = tk.Label(treeFrame,
                               text="العنوان",
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="#45a049")
        titleaddress.grid(row=4, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        numberfamily = tk.Label(treeFrame,
                               text=dataonef["Numberfamily"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        numberfamily.grid(row=5, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlenumberfmaily = tk.Label(treeFrame,
                               text="عدد أفراد الأسرة",
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="#45a049")
        titlenumberfmaily.grid(row=5, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")

        # self.print_data_one_family(dataonef)

    def treeeditperson(self):
        self.editperson_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.editperson_frame.grid(row=2, column=0, padx=2, pady=5, sticky="ew")
        self.editperson_frame.columnconfigure(index=0, weight=0)
        self.edit_frame_person = ttk.Frame(self.editperson_frame, padding=(5, 5, 5, 5))
        self.edit_frame_person.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        self.edit_frame_person.columnconfigure(index=0, weight=0)
        self.identityentry = ttk.Entry(self.editperson_frame, font=("Arial", 10, "bold"))
        self.identityentry.insert(0, "رقم هوية الشخص")
        self.identityentry.bind("<FocusIn>", lambda e: self.identityentry.delete('0', 'end'))
        self.identityentry.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="ew")

        onefamilybutton = ttk.Button(self.editperson_frame,
                                     text="عرض البيانات الشخص",
                                     style="Accent.TButton",
                                     command=self.treeoneperson
                                     )
        onefamilybutton.grid(row=1, column=0, ipady=2, padx=10, pady=10, sticky="nsew")
        # Combobox
        self.comboboxperson_rol = ttk.Combobox(self.editperson_frame, values=self.combo_list_person)
        self.comboboxperson_rol.current(0)
        self.comboboxperson_rol.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
        personbutton_rol = ttk.Button(self.editperson_frame,
                                      text=f"عرض واجهة التعديل",
                                      style="Accent.TButton",
                                      command=self.deleteframeitemperson
                                      )
        personbutton_rol.grid(row=3, column=0, ipady=2, padx=10, pady=10, sticky="nsew")


    def treeeditfamily(self):
        self.editfamily_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.editfamily_frame.grid(row=2, column=0, padx=2, pady=5, sticky="ew")
        self.editfamily_frame.columnconfigure(index=0, weight=0)
        self.edit_frame = ttk.Frame(self.editfamily_frame, padding=(5, 5, 5, 5))
        self.edit_frame.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        self.edit_frame.columnconfigure(index=0, weight=0)
        self.identityentry = ttk.Entry(self.editfamily_frame, font=("Arial", 10, "bold"))
        self.identityentry.insert(0, "رقم هوية رب الأسرة")
        self.identityentry.bind("<FocusIn>", lambda e: self.identityentry.delete('0', 'end'))
        self.identityentry.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="ew")

        onefamilybutton = ttk.Button(self.editfamily_frame,
                                     text="عرض البيانات الأسرة",
                                     style="Accent.TButton",
                                     command=self.treeonefamily
                                     )
        onefamilybutton.grid(row=1, column=0, ipady=2, padx=10, pady=10, sticky="nsew")
        # Combobox
        self.comboboxperson_rol = ttk.Combobox(self.editfamily_frame, values=self.combo_list_family)
        self.comboboxperson_rol.current(0)
        self.comboboxperson_rol.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
        personbutton_rol = ttk.Button(self.editfamily_frame,
                                      text=f"عرض واجهة التعديل",
                                      style="Accent.TButton",
                                      command=self.deleteframeitemfamily
                                      )
        personbutton_rol.grid(row=3, column=0, ipady=2, padx=10, pady=10, sticky="nsew")


    def frameitemfamily(self):
        item = self.comboboxperson_rol.get()
        self.edit_frame = ttk.Frame(self.editfamily_frame, padding=(5, 5, 5, 5))
        self.edit_frame.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        self.edit_frame.columnconfigure(index=0, weight=0)
        if item == "رقم الجوال":
            self.phone_entry = ttk.Entry(self.edit_frame, font=("Arial", 14, "bold"))
            self.phone_entry.insert(0, "رقم الجوال")
            self.phone_entry.bind("<FocusIn>", lambda e: self.phone_entry.delete('0', 'end'))
            self.phone_entry.grid(row=1, column=0, padx=2, pady=(0, 5), columnspan=2, sticky="ew")
        elif item == "العنوان":
            address_frame = ttk.LabelFrame(self.edit_frame, text="العنوان", padding=(5, 5, 5, 5))
            address_frame.grid(row=0, column=0, padx=1, pady=(0, 5), columnspan=3, sticky="ew")
            address_frame.columnconfigure(index=0, weight=0)
            self.city_entry = ttk.Entry(address_frame, font=("Arial", 14, "bold"))
            self.city_entry.insert(0, "مدينة السابقة")
            self.city_entry.bind("<FocusIn>", lambda e: self.city_entry.delete('0', 'end'))
            self.city_entry.grid(row=0, column=0, padx=2, pady=(0, 5), sticky="ew")
            self.borhood_entry = ttk.Entry(address_frame, font=("Arial", 14, "bold"))
            self.borhood_entry.insert(0, "الحي")
            self.borhood_entry.bind("<FocusIn>", lambda e: self.borhood_entry.delete('0', 'end'))
            self.borhood_entry.grid(row=1, column=0, padx=2, pady=(0, 5), sticky="ew")
            self.place_entry = ttk.Entry(address_frame, font=("Arial", 14, "bold"))
            self.place_entry.insert(0, "أقرب معلم")
            self.place_entry.bind("<FocusIn>", lambda e: self.place_entry.delete('0', 'end'))
            self.place_entry.grid(row=2, column=0, padx=2, pady=(0, 5), sticky="ew")

        else:
            messagebox.showinfo("خطأ", "لم يتم أدخال العنصر للتعديل!")
        onefamilybutton = ttk.Button(self.editfamily_frame,
                                     text="تعديل",
                                     style="Accent.TButton",
                                     command=self.edititeminfamily
                                     )
        onefamilybutton.grid(row=5, column=0, ipady=2, padx=10, pady=2, sticky="nsew")

    def edititeminfamily(self):
        item = self.comboboxperson_rol.get()
        if item == "رقم الجوال":
            Editcontroller.editdatafamily_phone(self, self.phone_entry.get(), self.identityentry.get())
        elif item == "العنوان":
            address = self.city_entry.get() + " - " + self.borhood_entry.get() + " - " + self.place_entry.get()
            Editcontroller.editdatafamily_address(self, address, self.identityentry.get())




    def frameitemperson(self):
        item = self.comboboxperson_rol.get()
        self.edit_frame_person = ttk.Frame(self.editperson_frame, padding=(5, 5, 5, 5))
        self.edit_frame_person.grid(row=4, column=0, padx=5, pady=3, sticky="ew")
        self.edit_frame_person.columnconfigure(index=0, weight=0)
        if item == "حامل/مرضعة":
            maternity_frame = ttk.LabelFrame(self.edit_frame_person, text="حامل / مرضعة", padding=(5, 5, 5, 5))
            maternity_frame.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="ew")
            maternity_frame.columnconfigure(index=0, weight=0)
            radio_1 = ttk.Radiobutton(maternity_frame, text="حامل", variable=self.maternity, value=1)
            radio_1.grid(row=0, column=0, padx=2, pady=5, sticky="nsew")
            radio_2 = ttk.Radiobutton(maternity_frame, text="مرضعة", variable=self.maternity, value=2)
            radio_2.grid(row=1, column=0, padx=2, pady=5, sticky="nsew")
        elif item == "أمراض مزمنة":
            chronicdisease_frame = ttk.LabelFrame(self.edit_frame_person, text="أمراض مزمنة", padding=(5, 5, 5, 5))
            chronicdisease_frame.grid(row=4, column=0, padx=2, pady=(0, 5), columnspan=1, sticky="ew")
            chronicdisease_frame.columnconfigure(index=0, weight=0)
            radio_1 = ttk.Radiobutton(chronicdisease_frame, text="سكري", variable=self.chronicdisease, value=1)
            radio_1.grid(row=0, column=0, padx=2, pady=5, sticky="nsew")
            radio_2 = ttk.Radiobutton(chronicdisease_frame, text="ضغط", variable=self.chronicdisease, value=2)
            radio_2.grid(row=1, column=0, padx=2, pady=5, sticky="nsew")
            radio_3 = ttk.Radiobutton(chronicdisease_frame, text="كلاهما", variable=self.chronicdisease, value=3)
            radio_3.grid(row=2, column=0, padx=2, pady=5, sticky="nsew")
        elif item == "إعاقة":
            obstruction_frame = ttk.LabelFrame(self.edit_frame_person, text="أعاقة", padding=(5, 5, 5, 5))
            obstruction_frame.grid(row=4, column=0, padx=10, pady=(0, 5), rowspan=1, sticky="ew")
            obstruction_frame.columnconfigure(index=0, weight=0)
            self.check_1 = ttk.Checkbutton(obstruction_frame, text="حركية", variable=self.obstruction_kinetic)
            self.check_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
            check_2 = ttk.Checkbutton(obstruction_frame, text="سمعية", variable=self.obstruction_audio)
            check_2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
            check_3 = ttk.Checkbutton(obstruction_frame, text="حسية", variable=self.obstruction_sensuality)
            check_3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
            check_4 = ttk.Checkbutton(obstruction_frame, text="بصرية", variable=self.obstruction_visual)
            check_4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
            check_5 = ttk.Checkbutton(obstruction_frame, text="دهنية", variable=self.obstruction_fatness)
            check_5.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        elif item == "ملاحظة":
            self.note_entry = ttk.Entry(self.edit_frame_person, font=("Arial", 14, "bold"))
            self.note_entry.insert(0, "ملاحظة")
            self.note_entry.bind("<FocusIn>", lambda e: self.note_entry.delete('0', 'end'))
            self.note_entry.grid(row=4, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        elif item == "هوية":
            self.identity_entry = ttk.Entry(self.edit_frame_person, font=("Arial", 14, "bold"))
            self.identity_entry.insert(0, "رقم الهوية الجديد")
            self.identity_entry.bind("<FocusIn>", lambda e: self.identity_entry.delete('0', 'end'))
            self.identity_entry.grid(row=4, column=0, padx=2, pady=(0, 5), sticky="ew")
        elif item == "الأسم الرباعي":
            self.name_entry = ttk.Entry(self.edit_frame_person, font=("Arial", 14, "bold"))
            self.name_entry.insert(0, "الأسم رباعي")
            self.name_entry.bind("<FocusIn>", lambda e: self.name_entry.delete('0', 'end'))
            self.name_entry.grid(row=4, column=0, padx=2, pady=(0, 5), sticky="ew")
        elif item == "تاريخ الميلادي":
            self.sel = tk.StringVar()
            self.date_Calendar = Calendar(self.edit_frame_person,
                                          selectmode='day',
                                          year=2000,
                                          month=1,
                                          day=25,
                                          )
            self.date_Calendar.grid(row=4, column=0, ipadx=2, ipady=5, padx=5, pady=(0, 3), sticky="ew")
        elif item == "الجنس":
            sex_frame = ttk.LabelFrame(self.edit_frame_person, text="الجنس", padding=(5, 5, 5, 5))
            sex_frame.grid(row=4, column=0, padx=2, pady=(0, 5), sticky="ew")
            sex_frame.columnconfigure(index=0, weight=0)
            # Radiobuttons
            self.mail = ttk.Radiobutton(sex_frame, text="ذكر", variable=self.sex, value=1)
            self.mail.grid(row=0, column=0, padx=2, pady=5, sticky="nsew")
            self.femail = ttk.Radiobutton(sex_frame, text="انثى", variable=self.sex, value=2)
            self.femail.grid(row=1, column=0, padx=2, pady=5, sticky="nsew")
        elif item == "الحالة الاجتماعية":
            socialstatus_frame = ttk.LabelFrame(self.edit_frame_person, text="الحالة الأجتماعية", padding=(5, 5, 5, 5))
            socialstatus_frame.grid(row=4, column=0, padx=2, pady=(0, 5), rowspan=1, sticky="ew")
            socialstatus_frame.columnconfigure(index=0, weight=0)
            radio_1 = ttk.Radiobutton(socialstatus_frame, text="متزوج", variable=self.socialstatus, value=1)
            radio_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
            radio_2 = ttk.Radiobutton(socialstatus_frame, text="أعزب", variable=self.socialstatus, value=2)
            radio_2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
            radio_3 = ttk.Radiobutton(socialstatus_frame, text="أرمل", variable=self.socialstatus, value=3)
            radio_3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
            radio_4 = ttk.Radiobutton(socialstatus_frame, text="مطلقة", variable=self.socialstatus, value=4)
            radio_4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        elif item == "صلة القرابة":
            alliance_frame = ttk.LabelFrame(self.edit_frame_person, text="صلة القرابة", padding=(5, 5, 5, 5))
            alliance_frame.grid(row=4, column=0, padx=10, pady=(0, 5), rowspan=1, sticky="ew")
            alliance_frame.columnconfigure(index=0, weight=0)
            radio_1 = ttk.Radiobutton(alliance_frame, text="رب الأسرة", variable=self.alliance, value=1)
            radio_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
            radio_2 = ttk.Radiobutton(alliance_frame, text="زوجة", variable=self.alliance, value=2)
            radio_2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
            radio_3 = ttk.Radiobutton(alliance_frame, text="ابن", variable=self.alliance, value=3)
            radio_3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
            radio_4 = ttk.Radiobutton(alliance_frame, text="بنت", variable=self.alliance, value=4)
            radio_4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        else:
            messagebox.showinfo("خطأ", "لم يتم أدخال العنصر للتعديل!")
        onefamilybutton = ttk.Button(self.edit_frame_person,
                                     text="تعديل",
                                     style="Accent.TButton",
                                     command=self.edititeminperson
                                     )
        onefamilybutton.grid(row=5, column=0, ipady=2, padx=10, pady=2, sticky="nsew")

    def edititeminperson(self):
        item = self.comboboxperson_rol.get()
        if item == "حامل/مرضعة":
            Editcontroller.editdataperson_maternity(self, self.maternity.get(), self.identityentry.get())
        elif item == "أمراض مزمنة":
            Editcontroller.editdataperson_chronicdiseases(self, self.chronicdisease.get(), self.identityentry.get())
        elif item == "إعاقة":
            lisobstruction = []
            lisobstruction.append(self.obstruction_kinetic.get())
            lisobstruction.append(self.obstruction_audio.get())
            lisobstruction.append(self.obstruction_sensuality.get())
            lisobstruction.append(self.obstruction_visual.get())
            lisobstruction.append(self.obstruction_fatness.get())
            Editcontroller.editdataperson_obstruction(self,lisobstruction,self.identityentry.get())
        elif item == "ملاحظة":
            Editcontroller.editdataperson_note(self,self.note_entry.get(),self.identityentry.get())
        elif item == "هوية":
            Editcontroller.editdataperson_identityperson(self,self.identity_entry.get(),self.identityentry.get())
        elif item == "الأسم الرباعي":
            Editcontroller.editdataperson_fullname(self,self.name_entry.get(),self.identityentry.get())
        elif item == "تاريخ الميلادي":
            Editcontroller.editdataperson_dateofbirth(self,self.date_Calendar.selection_get(),self.identityentry.get())
        elif item == "الجنس":
            Editcontroller.editdataperson_sex(self, self.sex.get(), self.identityentry.get())
        elif item == "الحالة الاجتماعية":
            Editcontroller.editdataperson_socialstatus(self, self.socialstatus.get(), self.identityentry.get())
        elif item == "صلة القرابة":
            Editcontroller.editdataperson_alliance(self, self.alliance.get(), self.identityentry.get())

    def deleteframeitemfamily(self):
        self.edit_frame.grid_forget()
        self.frameitemfamily()

    def deleteframeitemperson(self):
        self.edit_frame_person.grid_forget()
        self.frameitemperson()

    def deleteframeeditfamily(self):
        self.editperson_frame.grid_forget()
        self.treeeditfamily()


    def deleteframeeditperson(self):
        self.editfamily_frame.grid_forget()
        self.treeeditperson()



    def go_back(self):
        """الرجوع إلى الإطار السابق"""
        self.master.show_frame(DashboardPage, GEOMETRY)
        pass

class DeletePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        IMAG_EDIT_ = PhotoImage(file=IMAG_EDIT).subsample(10, 10)

        IMAG_BACK_ = PhotoImage(file=IMAG_BACK).subsample(12, 12)
        frame_ = tk.LabelFrame(self, border=0, relief="ridge")
        frame_.grid()
        frame_.place(relx=0.5,
                     rely=0.07,
                     anchor="center",
                     width=1200,
                     height=95)
        return_button = tk.Button(frame_,
                                  text="رجوع",
                                  font=("Arial", 18, "bold"),
                                  image=IMAG_BACK_,
                                  relief=SOLID,
                                  border=0,
                                  activebackground="#45a049",
                                  activeforeground="white",
                                  fg="#45a049",
                                  compound=TOP,
                                  command=self.go_back)
        return_button.image = IMAG_BACK_
        return_button.pack()
        return_button.place(x=1, y=1)
        #     **************************
        title_label = tk.Label(frame_,
                               text=" حذف على بيانات مخيم الشهداء ",
                               font=("Arial", 50, "bold"),
                               image=IMAG_EDIT_,
                               compound=RIGHT,
                               fg="#45a049")
        title_label.image = IMAG_EDIT_
        title_label.pack(pady=10)
        #   ************************************************
        self.frame_2 = ttk.Frame(self)
        self.frame_2.pack()
        self.frame_2.place(x=10,
                           relx=0.5,
                           rely=0.64,
                           anchor="center",
                           width=1200,
                           height=700)
        # Create a Frame for input widgets
        self.widgets_frame = ttk.LabelFrame(self.frame_2, text="Edit", padding=(20, 20, 20, 10))
        self.widgets_frame.grid(row=0, column=0, padx=(80, 10), pady=50, sticky="nsew", rowspan=3)
        self.widgets_frame.columnconfigure(index=0, weight=0)
        # ********
        onefamilybutton = ttk.Button(self.widgets_frame,
                                     text="حذف بيانات الأسرة",
                                     style="Accent.TButton",
                                     command=self.deleteframedeletefamily
                                     )
        onefamilybutton.grid(row=0, column=0, ipady=2, padx=10, pady=10, sticky="nsew")
        onefamilybutton = ttk.Button(self.widgets_frame,
                                     text="حذف بيانات الفرد",
                                     style="Accent.TButton",
                                     command=self.deleteframedeleteperson
                                     )
        onefamilybutton.grid(row=1, column=0, ipady=2, padx=10, pady=10, sticky="nsew")
        self.deletefamily_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.deletefamily_frame.grid(row=2, column=0, padx=2, pady=5, sticky="ew")
        self.deletefamily_frame.columnconfigure(index=0, weight=0)
        self.deleteperson_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.deleteperson_frame.grid(row=2, column=0, padx=2, pady=5, sticky="ew")
        self.deleteperson_frame.columnconfigure(index=0, weight=0)
        self.treeFrame = ttk.LabelFrame(self.frame_2, text="بيانات الأسرة", padding=(20, 20, 20, 10))


    # ****++++
    def treeoneperson(self):
        self.treeFrame.grid_forget()
        dataonep = Editcontroller.getdataoneperson(self, self.identityentry.get())
        treeFrame_ = ttk.LabelFrame(self.frame_2, text="بيانات الفرد", padding=(20, 20, 20, 10))
        treeFrame_.grid(row=0, column=1, padx=10, pady=50, sticky="nsew", rowspan=3)
        title_label = tk.Label(treeFrame_,
                               text=" كل بيانات الفرد ",
                               font=("Arial", 20, "bold"),
                               compound=RIGHT,
                               fg="#45a049",

                               )
        title_label.grid(row=0, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), columnspan=4, sticky="ew")
        idfamily = tk.Label(treeFrame_,
                            text=dataonep["IdentityPerson"],
                            font=("Arial", 16, "bold"),
                            compound=RIGHT,
                            fg="white")
        idfamily.grid(row=1, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidfamily = tk.Label(treeFrame_,
                                 text="رقم الهوية",
                                 font=("Arial", 16, "bold"),
                                 compound=RIGHT,
                                 fg="#45a049")
        titleidfamily.grid(row=1, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        identity = tk.Label(treeFrame_,
                            text=dataonep["Sex"],
                            font=("Arial", 16, "bold"),
                            compound=RIGHT,
                            fg="white")
        identity.grid(row=2, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidentity = tk.Label(treeFrame_,
                                 text="الجنس",
                                 font=("Arial", 16, "bold"),
                                 compound=RIGHT,
                                 fg="#45a049")
        titleidentity.grid(row=2, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        phonenumber = tk.Label(treeFrame_,
                               text=dataonep["Alliance"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        phonenumber.grid(row=3, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlephonenumber = tk.Label(treeFrame_,
                                    text="صلة القرابة",
                                    font=("Arial", 16, "bold"),
                                    compound=RIGHT,
                                    fg="#45a049")
        titlephonenumber.grid(row=3, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        address = tk.Label(treeFrame_,
                           text=dataonep["ChronicDiseases"],
                           font=("Arial", 16, "bold"),
                           compound=RIGHT,
                           fg="white")
        address.grid(row=4, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleaddress = tk.Label(treeFrame_,
                                text="الأمراض المزمنة",
                                font=("Arial", 16, "bold"),
                                compound=RIGHT,
                                fg="#45a049")
        titleaddress.grid(row=4, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        numberfamily = tk.Label(treeFrame_,
                                text=dataonep["Note"],
                                font=("Arial", 16, "bold"),
                                compound=RIGHT,
                                fg="white")
        numberfamily.grid(row=5, column=0, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlenumberfmaily = tk.Label(treeFrame_,
                                     text="ملاحظة",
                                     font=("Arial", 16, "bold"),
                                     compound=RIGHT,
                                     fg="#45a049")
        titlenumberfmaily.grid(row=5, column=1, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        # ************************************
        # ***********************************
        idfamily = tk.Label(treeFrame_,
                            text=dataonep["FullName"],
                            font=("Arial", 16, "bold"),
                            compound=RIGHT,
                            fg="white")
        idfamily.grid(row=1, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidfamily = tk.Label(treeFrame_,
                                 text="الأسم رباعي",
                                 font=("Arial", 16, "bold"),
                                 compound=RIGHT,
                                 fg="#45a049")
        titleidfamily.grid(row=1, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        identity = tk.Label(treeFrame_,
                            text=dataonep["DateOFBirth"],
                            font=("Arial", 16, "bold"),
                            compound=RIGHT,
                            fg="white")
        identity.grid(row=2, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleidentity = tk.Label(treeFrame_,
                                 text="تاريخ الميلاد",
                                 font=("Arial", 16, "bold"),
                                 compound=RIGHT,
                                 fg="#45a049")
        titleidentity.grid(row=2, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        phonenumber = tk.Label(treeFrame_,
                               text=dataonep["SocialStatus"],
                               font=("Arial", 16, "bold"),
                               compound=RIGHT,
                               fg="white")
        phonenumber.grid(row=3, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlephonenumber = tk.Label(treeFrame_,
                                    text="الحالة الأجتماعية",
                                    font=("Arial", 16, "bold"),
                                    compound=RIGHT,
                                    fg="#45a049")
        titlephonenumber.grid(row=3, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        address = tk.Label(treeFrame_,
                           text=dataonep["Obstruction"],
                           font=("Arial", 16, "bold"),
                           compound=RIGHT,
                           fg="white")
        address.grid(row=4, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titleaddress = tk.Label(treeFrame_,
                                text="الأعاقة",
                                font=("Arial", 16, "bold"),
                                compound=RIGHT,
                                fg="#45a049")
        titleaddress.grid(row=4, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        numberfamily = tk.Label(treeFrame_,
                                text=dataonep["Maternity"],
                                font=("Arial", 16, "bold"),
                                compound=RIGHT,
                                fg="white")
        numberfamily.grid(row=5, column=2, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")
        titlenumberfmaily = tk.Label(treeFrame_,
                                     text="الأمومة",
                                     font=("Arial", 16, "bold"),
                                     compound=RIGHT,
                                     fg="#45a049")
        titlenumberfmaily.grid(row=5, column=3, ipadx=5, ipady=10, padx=2, pady=(0, 5), sticky="ew")


    def treedeleteperson(self):
        self.deleteperson_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.deleteperson_frame.grid(row=2, column=0, padx=2, pady=5, sticky="ew")
        self.deleteperson_frame.columnconfigure(index=0, weight=0)
        self.identityentry = ttk.Entry(self.deleteperson_frame, font=("Arial", 10, "bold"))
        self.identityentry.insert(0, "رقم هوية الشخص")
        self.identityentry.bind("<FocusIn>", lambda e: self.identityentry.delete('0', 'end'))
        self.identityentry.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="ew")

        onefamilybutton = ttk.Button(self.deleteperson_frame,
                                     text="عرض البيانات الشخص",
                                     style="Accent.TButton",
                                     command=self.treeoneperson
                                     )
        onefamilybutton.grid(row=1, column=0, ipady=2, padx=10, pady=10, sticky="nsew")
        personbutton_rol = ttk.Button(self.deleteperson_frame,
                                      text=f"حذف الفرد من السجل",
                                      style="Accent.TButton",
                                      command=self.delete__person
                                      )
        personbutton_rol.grid(row=2, column=0, ipady=2, padx=10, pady=10, sticky="nsew")


    def treedeletefamily(self):
        self.deletefamily_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.deletefamily_frame.grid(row=2, column=0, padx=2, pady=5, sticky="ew")
        self.deletefamily_frame.columnconfigure(index=0, weight=0)
        self.identityentry = ttk.Entry(self.deletefamily_frame, font=("Arial", 10, "bold"))
        self.identityentry.insert(0, "رقم هوية رب الأسرة")
        self.identityentry.bind("<FocusIn>", lambda e: self.identityentry.delete('0', 'end'))
        self.identityentry.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="ew")

        onefamilybutton = ttk.Button(self.deletefamily_frame,
                                     text="عرض البيانات الأسرة",
                                     style="Accent.TButton",
                                     command=self.treeonefamily
                                     )
        onefamilybutton.grid(row=1, column=0, ipady=2, padx=10, pady=10, sticky="nsew")
        personbutton_rol = ttk.Button(self.deletefamily_frame,
                                      text=f"حذف الأسرة من المخيم",
                                      style="Accent.TButton",
                                      command=self.delete__family
                                      )
        personbutton_rol.grid(row=3, column=0, ipady=2, padx=10, pady=10, sticky="nsew")



    def deleteframedeleteperson(self):
        self.deletefamily_frame.grid_forget()
        self.treedeleteperson()

    # ****++++
    def treeonefamily(self):
        load_one_family = Searchcontroller.load_one_family(self, self.identityentry.get())

        self.treeFrame = ttk.LabelFrame(self.frame_2, text="بيانات الأسرة", padding=(20, 20, 20, 10))
        self.treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        self.treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(self.treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsperson = ("العدد", "هوية",
                           "الأسم رباعي", "تاريخ الميلاد", "الجنس", "الحالة الاجتماعية",
                           "صلة القرابة", "أعاقة", "أمراض مزمنة",
                           "حامل/مرضعة", "ملاحظة", "تاريخ التسجيل")
        self.treeview = ttk.Treeview(self.treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsperson,
                                     height=20)

        self.treeview.column("العدد", width=20)
        # self.treeview.column("رقم الأسرة", width=60)
        self.treeview.column("هوية", width=80)
        self.treeview.column("الأسم رباعي", width=115)
        self.treeview.column("تاريخ الميلاد", width=70)
        self.treeview.column("الجنس", width=30)
        self.treeview.column("الحالة الاجتماعية", width=70)
        self.treeview.column("صلة القرابة", width=70)
        self.treeview.column("أعاقة", width=40)
        self.treeview.column("أمراض مزمنة", width=60)
        self.treeview.column("حامل/مرضعة", width=60)
        self.treeview.column("ملاحظة", width=40)
        self.treeview.column("تاريخ التسجيل", width=70)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        #     تحميل البيانات
        self.print_data_one_family(load_one_family)

    def deleteframedeletefamily(self):
        self.deleteperson_frame.grid_forget()
        self.treedeletefamily()


    def delete__family(self):
        Deletecontroller.delete_family(self,self.identityentry.get())

    def delete__person(self):
        Deletecontroller.delete_person(self,self.identityentry.get())

    def print_data_one_family(self,load_one_family):
        for col_name in self.colsperson:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in load_one_family:
            self.treeview.insert('', tk.END, values=value_tuple)

    def go_back(self):
        """الرجوع إلى الإطار السابق"""
        self.master.show_frame(DashboardPage, GEOMETRY)
        pass

class SearchPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        IMAG_BACK_ = PhotoImage(file=IMAG_BACK).subsample(12, 12)
        IMAG_TENT_ = PhotoImage(file=IMAG_TENT).subsample(10, 10)
        IMAG_SAERCH_2_ = PhotoImage(file=IMAG_SAERCH_2).subsample(10, 10)


        frame_ = tk.LabelFrame(self, border=0, relief="ridge")
        frame_.grid()
        frame_.place(relx=0.5,
                     rely=0.07,
                     anchor="center",
                     width=1200,
                     height=95)
        return_button = tk.Button(frame_,
                                  text="رجوع",
                                  font=("Arial", 18, "bold"),
                                  image=IMAG_BACK_,
                                  relief=SOLID,
                                  border=0,
                                  activebackground="#45a049",
                                  activeforeground="white",
                                  fg="#45a049",
                                  compound=TOP,
                                  command=self.go_back)
        return_button.image = IMAG_BACK_
        return_button.pack()
        return_button.place(x=1, y=1)
        # العنوان الرئيسي
        title_label = tk.Label(frame_,
                               text=" بحث في بيانات مخيم الشهداء ",
                               font=("Arial", 50, "bold"),
                               image=IMAG_SAERCH_2_,
                               compound=RIGHT,
                               fg="#45a049")
        title_label.image = IMAG_SAERCH_2_
        title_label.pack(pady=10)
        #   ************************************************
        self.frame_2 = ttk.Frame(self)
        self.frame_2.pack()
        self.frame_2.place(x=10,
                           relx=0.5,
                           rely=0.64,
                           anchor="center",
                           width=1200,
                           height=700)
        # Create a Frame for input widgets
        self.widgets_frame = ttk.LabelFrame(self.frame_2, text="Data", padding=(20, 20, 20, 10))
        self.widgets_frame.grid(row=0, column=0, padx=5, pady=(5, 5), sticky="nsew", rowspan=3)
        # widgets_frame.place(width=200, height=580)
        self.widgets_frame.columnconfigure(index=4, weight=0)
        # ********
        # Button
        # Accentbutton
        familybutton = ttk.Button(self.widgets_frame,
                                     text="خيارات العائلات",
                                     style="Accent.TButton",
                                     command=self.clearitemfamily
                                     )
        familybutton.grid(row=0, column=0, ipady=2, pady=10, padx=10, sticky="nsew")
        personbutton = ttk.Button(self.widgets_frame,
                                     text="خيارات الافراد",
                                     style="Accent.TButton",
                                     command=self.clearitemperson
                                     )
        personbutton.grid(row=1, column=0, ipady=2, pady=10, padx=10, sticky="nsew")
        self.family_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.family_frame.grid(row=2, column=0, padx=2, pady=3, sticky="ew")
        self.family_frame.columnconfigure(index=0, weight=0)
        self.person_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.person_frame.grid(row=2, column=0, padx=2, pady=3, sticky="ew")
        self.person_frame.columnconfigure(index=0, weight=0)
        # allfamilybutton = ttk.Button(widgets_frame,
        #                              text="جميع العائلات",
        #                              style="Accent.TButton",
        #                              command=self.treeframefamily
        #                              )
        # allfamilybutton.grid(row=0, column=0,ipady=2, pady=10,padx=10, columnspan=2, sticky="nsew")
        # self.num_entry = ttk.Entry(widgets_frame)
        # self.num_entry.insert(0, "رقم الافراد")
        # self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        # self.num_entry.grid(row=1, column=0, padx=10, pady=(0, 5), columnspan=2, sticky="ew")
        # allfamilybutton = ttk.Button(widgets_frame,
        #                              text="الأسر التي عدد افرادها اكبر من ",
        #                              style="Accent.TButton",
        #                              command=self.treeframefamily_rol
        #                              )
        # allfamilybutton.grid(row=2, column=0,ipady=2, pady=10,padx=10, columnspan=2, sticky="nsew")
        #
        # maternityfamilybutton = ttk.Button(widgets_frame,
        #                                    text="جميع العائلات يوجد فيها حوامل او مرضعة",
        #                                    style="Accent.TButton",
        #                                    command=self.treeframematernityfamily
        #                                    )
        # maternityfamilybutton.grid(row=3, column=0,ipady=2, pady=10,padx=10, columnspan=2, sticky="nsew")
        # maternityfamilybutton = ttk.Button(widgets_frame,
        #                                    text="جميع العائلات يوجد أعاقة او أمراض",
        #                                    style="Accent.TButton",
        #                                    command=self.treeframeobstructionfamily
        #                                    )
        # maternityfamilybutton.grid(row=4, column=0,ipady=2, pady=10,padx=10, columnspan=2, sticky="nsew")
        #
        # personbutton = ttk.Button(widgets_frame,
        #                           text="كل الافراد",
        #                           style="Accent.TButton",
        #                           command=self.treeframeperson
        #                           )
        # personbutton.grid(row=5, column=0,ipady=2, padx=10, pady=10, columnspan=2, sticky="nsew")
        #
        #
        # self.family_entry = ttk.Entry(widgets_frame)
        # self.family_entry.insert(0, "رقم الاسرة, هوية رب الاسرة")
        # self.family_entry.bind("<FocusIn>", lambda e: self.family_entry.delete('0', 'end'))
        # self.family_entry.grid(row=6, column=0, padx=10, pady=(0, 5), columnspan=2, sticky="ew")
        #
        #
        #
        # onefamilybutton = ttk.Button(widgets_frame,
        #                              text="كل افراد الاسرة",
        #                              style="Accent.TButton",
        #                              command=self.treeonefamily
        #                              )
        # onefamilybutton.grid(row=7, column=0, ipady=2, padx=10, pady=10, columnspan=2, sticky="nsew")
        # # Spinbox
        # # self.spinbox = ttk.Spinbox(widgets_frame, from_=0, to=100)
        # # self.spinbox.insert(0, "العداد")
        # # self.spinbox.grid(row=8, column=0, ipadx=0, ipady=0, padx=5, pady=10, columnspan=1, sticky="ew")
        # # # self.spinbox.place(x= 0.60,y= 0.90, width=90, height=30)
        # # Combobox
        # self.comboboxperson_rol = ttk.Combobox(widgets_frame, values=combo_list)
        # self.comboboxperson_rol.current(0)
        # self.comboboxperson_rol.grid(row=8, column=1, padx=5, pady=10, columnspan=1, sticky="ew")
        #
        # personbutton_rol = ttk.Button(widgets_frame,
        #                              text="كل افراد أصغر من أو أكبر من",
        #                              style="Accent.TButton",
        #                              command=self.treeframeperson_rol
        #                              )
        # personbutton_rol.grid(row=9, column=0, ipady=2, padx=10, pady=10, columnspan=2, sticky="nsew")

    def itemfamily(self):
        self.family_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.family_frame.grid(row=2, column=0, padx=2, pady=3, sticky="ew")
        self.family_frame.columnconfigure(index=0, weight=0)
        allfamilybutton = ttk.Button(self.family_frame,
                                     text="جميع العائلات",
                                     style="Accent.TButton",
                                     command=self.treeframefamily
                                     )
        allfamilybutton.grid(row=0, column=0,ipady=2, pady=10,padx=10, sticky="nsew")
        self.num_entry = ttk.Entry(self.family_frame)
        self.num_entry.insert(0, "رقم الافراد")
        self.num_entry.bind("<FocusIn>", lambda e: self.num_entry.delete('0', 'end'))
        self.num_entry.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="ew")
        allfamilybutton = ttk.Button(self.family_frame,
                                     text="الأسر التي عدد افرادها اكبر من ",
                                     style="Accent.TButton",
                                     command=self.treeframefamily_rol
                                     )
        allfamilybutton.grid(row=2, column=0,ipady=2, pady=10,padx=10, sticky="nsew")

        maternityfamilybutton = ttk.Button(self.family_frame,
                                           text="جميع العائلات يوجد فيها حوامل او مرضعة",
                                           style="Accent.TButton",
                                           command=self.treeframematernityfamily
                                           )
        maternityfamilybutton.grid(row=3, column=0,ipady=2, pady=10,padx=10, sticky="nsew")
        maternityfamilybutton = ttk.Button(self.family_frame,
                                           text="جميع العائلات يوجد أعاقة او أمراض",
                                           style="Accent.TButton",
                                           command=self.treeframeobstructionfamily
                                           )
        maternityfamilybutton.grid(row=4, column=0,ipady=2, pady=10,padx=10, sticky="nsew")
        nonefamilybutton = ttk.Button(self.family_frame,
                                           text="جميع العائلات لم يكتمل بياناتهم",
                                           style="Accent.TButton",
                                           command=self.treeframefamily_none
                                           )
        nonefamilybutton.grid(row=5, column=0,ipady=2, pady=10,padx=10, sticky="nsew")

    def itemperson(self):
        combo_list = ["أصغر من", "أكبر من"]
        self.person_frame = ttk.Frame(self.widgets_frame, padding=(5, 5, 5, 5))
        self.person_frame.grid(row=2, column=0, padx=2, pady=3, sticky="ew")
        self.person_frame.columnconfigure(index=0, weight=0)
        self.family_entry = ttk.Entry(self.person_frame)
        self.family_entry.insert(0, "رقم الاسرة, هوية رب الاسرة")
        self.family_entry.bind("<FocusIn>", lambda e: self.family_entry.delete('0', 'end'))
        self.family_entry.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="ew")
        onefamilybutton = ttk.Button(self.person_frame,
                                     text="كل افراد الاسرة",
                                     style="Accent.TButton",
                                     command=self.treeonefamily
                                     )
        onefamilybutton.grid(row=1, column=0, ipady=2, padx=10, pady=10, sticky="nsew")

        # Spinbox
        self.spinbox = ttk.Spinbox(self.person_frame, from_=0, to=100)
        self.spinbox.insert(0, "العداد")
        self.spinbox.grid(row=2, column=0, ipadx=0, ipady=0, padx=5, pady=10, columnspan=1, sticky="ew")

        # Combobox
        self.comboboxperson_rol = ttk.Combobox(self.person_frame, values=combo_list)
        self.comboboxperson_rol.current(0)
        self.comboboxperson_rol.grid(row=3, column=0, padx=5, pady=10, columnspan=1, sticky="ew")

        personbutton_rol = ttk.Button(self.person_frame,
                                     text="كل افراد أصغر من أو أكبر من",
                                     style="Accent.TButton",
                                     command=self.treeframeperson_rol
                                     )
        personbutton_rol.grid(row=4, column=0, ipady=2, padx=10, pady=10, columnspan=2, sticky="nsew")

    def clearitemfamily(self):
        self.person_frame.grid_forget()
        self.itemfamily()
    def clearitemperson(self):
        self.family_frame.grid_forget()
        self.itemperson()


    def treeframefamily(self):
        self.listdatafamily = Searchcontroller.load_data_family(self)
        treeFrame = ttk.LabelFrame(self.frame_2, text="Data", style="TLabelframe", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsfamily = ("رقم الأسرة", "هوية رب الأسرة",
                           "الأسم رباعي", "هوية الزوجة", "اسم الزوجة",
                           "رقم الجوال", "العنوان", "عدد الأفراد", "عدد الذكور", "عدد الأناث")
        self.treeview = ttk.Treeview(treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsfamily,
                                     height=20)

        # self.treeview.column("العدد", width=20)
        self.treeview.column("رقم الأسرة", width=50)
        self.treeview.column("هوية رب الأسرة", width=80)
        self.treeview.column("الأسم رباعي", width=120)
        self.treeview.column("هوية الزوجة", width=70)
        self.treeview.column("اسم الزوجة", width=110)
        self.treeview.column("رقم الجوال", width=70)
        self.treeview.column("العنوان", width=110)
        self.treeview.column("عدد الأفراد", width=60)
        self.treeview.column("عدد الذكور", width=60)
        self.treeview.column("عدد الأناث", width=50)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        #     تحميل البيانات
        self.print_data_family(self.listdatafamily)
        printmaternityfamilybutton = ttk.Button(self.family_frame,
                                      text="طباعة",
                                      style="Accent.TButton",
                                      command=self.printa
                                      )
        printmaternityfamilybutton.grid(row=6, column=0, ipady=2, pady=10, padx=10, sticky="nsew")

    def treeframefamily_none(self):
        listdatafamily = Searchcontroller.load_data_family_none(self)
        treeFrame = ttk.LabelFrame(self.frame_2, text="Data", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsfamily = ("رقم الأسرة", "هوية رب الأسرة",
                           "الأسم رباعي", "هوية الزوجة", "اسم الزوجة",
                           "رقم الجوال", "العنوان", "عدد الأفراد", "تاريخ التسجيل")
        self.treeview = ttk.Treeview(treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsfamily,
                                     height=20)

        # self.treeview.column("العدد", width=20)
        self.treeview.column("رقم الأسرة", width=60)
        self.treeview.column("هوية رب الأسرة", width=80)
        self.treeview.column("الأسم رباعي", width=120)
        self.treeview.column("هوية الزوجة", width=70)
        self.treeview.column("اسم الزوجة", width=110)
        self.treeview.column("رقم الجوال", width=70)
        self.treeview.column("العنوان", width=110)
        self.treeview.column("عدد الأفراد", width=60)
        self.treeview.column("تاريخ التسجيل", width=70)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        #     تحميل البيانات
        self.print_data_family(listdatafamily)


    def treeframefamily_rol(self):
        self.listdatafamily_rol = Searchcontroller.load_data_family_rol(self, self.num_entry.get())

        treeFrame = ttk.LabelFrame(self.frame_2, text="Data", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsfamily = ("رقم الأسرة", "هوية رب الأسرة",
                           "الأسم رباعي", "هوية الزوجة", "اسم الزوجة",
                           "رقم الجوال", "العنوان", "عدد الأفراد", "تاريخ التسجيل")
        self.treeview = ttk.Treeview(treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsfamily,
                                     height=20)

        # self.treeview.column("العدد", width=20)
        self.treeview.column("رقم الأسرة", width=60)
        self.treeview.column("هوية رب الأسرة", width=80)
        self.treeview.column("الأسم رباعي", width=120)
        self.treeview.column("هوية الزوجة", width=70)
        self.treeview.column("اسم الزوجة", width=110)
        self.treeview.column("رقم الجوال", width=70)
        self.treeview.column("العنوان", width=110)
        self.treeview.column("عدد الأفراد", width=60)
        self.treeview.column("تاريخ التسجيل", width=70)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        #     تحميل البيانات
        self.print_data_family_rol(self.listdatafamily_rol)
        printallmaxfamilybutton = ttk.Button(self.family_frame,
                                          text="طباعة",
                                          style="Accent.TButton",
                                          command=self.printb
                                          )
        printallmaxfamilybutton.grid(row=6, column=0, ipady=2, pady=10, padx=10, sticky="nsew")

    def treeframematernityfamily(self):
        self.load_maternity_family = Searchcontroller.load_maternity_family(self)
        treeFrame = ttk.LabelFrame(self.frame_2, text="Data", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsfamily = ("رقم الأسرة", "هوية رب الأسرة",
                           "الأسم رباعي", "هوية الزوجة", "اسم الزوجة",
                           "رقم الجوال", "العنوان", "عدد الأفراد",
                           "حامل/مرضعة")
        self.treeview = ttk.Treeview(treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsfamily,
                                     height=20)

        # self.treeview.column("العدد", width=20)
        self.treeview.column("رقم الأسرة", width=50)
        self.treeview.column("هوية رب الأسرة", width=80)
        self.treeview.column("الأسم رباعي", width=120)
        self.treeview.column("هوية الزوجة", width=70)
        self.treeview.column("اسم الزوجة", width=110)
        self.treeview.column("رقم الجوال", width=70)
        self.treeview.column("العنوان", width=110)
        self.treeview.column("عدد الأفراد", width=50)
        self.treeview.column("حامل/مرضعة", width=80)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        # print(self.load_maternity_family)
        #     تحميل البيانات
        self.print_maternity_family(self.load_maternity_family)
        printallfamilybutton = ttk.Button(self.family_frame,
                                          text="طباعة",
                                          style="Accent.TButton",
                                          command=self.printc
                                          )
        printallfamilybutton.grid(row=6, column=0, ipady=2, pady=10, padx=10, sticky="nsew")

    def treeframeobstructionfamily(self):
        self.load_obstruction_family = Searchcontroller.load_obstruction_family(self)
        treeFrame = ttk.LabelFrame(self.frame_2, text="Data", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsfamily = ("العدد","رقم الأسرة", "هوية", "الأسم رباعي","الجنس",
                           "رقم الجوال", "عدد الأفراد",
                           "إعاقة","أمراض")
        self.treeview = ttk.Treeview(treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsfamily,
                                     height=20)

        self.treeview.column("العدد", width=20)
        self.treeview.column("رقم الأسرة", width=50)
        self.treeview.column("هوية", width=80)
        self.treeview.column("الأسم رباعي", width=120)
        self.treeview.column("الجنس", width=60)
        self.treeview.column("رقم الجوال", width=70)
        self.treeview.column("عدد الأفراد", width=50)
        self.treeview.column("إعاقة", width=80)
        self.treeview.column("أمراض", width=50)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        #     تحميل البيانات
        self.print_obstruction_family(self.load_obstruction_family)
        printobstructionfamilybutton = ttk.Button(self.family_frame,
                                                text="طباعة",
                                                style="Accent.TButton",
                                                command=self.printd
                                                )
        printobstructionfamilybutton.grid(row=6, column=0, ipady=2, pady=10, padx=10, sticky="nsew")


    def treeframeperson_rol(self):
        self.listdataperson_rol = Searchcontroller.load_data_person_rol(self, self.comboboxperson_rol.get(),self.spinbox.get())
        treeFrame = ttk.LabelFrame(self.frame_2, text="Data", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsfamily = ("العدد", "هوية", "الأسم رباعي","الجنس",
                           "رقم الجوال", "العمر",
                           "إعاقة","أمراض")
        self.treeview = ttk.Treeview(treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsfamily,
                                     height=20)

        self.treeview.column("العدد", width=20)
        # self.treeview.column("رقم الأسرة", width=50)
        self.treeview.column("هوية", width=80)
        self.treeview.column("الأسم رباعي", width=120)
        self.treeview.column("الجنس", width=60)
        self.treeview.column("رقم الجوال", width=70)
        self.treeview.column("العمر", width=50)
        self.treeview.column("إعاقة", width=80)
        self.treeview.column("أمراض", width=50)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        #     تحميل البيانات
        self.print_person_rol(self.listdataperson_rol)
        printmaternityfamilybutton = ttk.Button(self.person_frame,
                                                text="طباعة",
                                                style="Accent.TButton",
                                                command=self.printf
                                                )
        printmaternityfamilybutton.grid(row=6, column=0, ipady=2, pady=10, padx=10, sticky="nsew")

    def treeframeperson(self):
        listdataperson = Searchcontroller.load_data_person(self)
        treeFrame = ttk.LabelFrame(self.frame_2, text="Data", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsperson = ("العدد", "هوية",
                           "الأسم رباعي", "تاريخ الميلاد", "الجنس","الحالة الاجتماعية",
                           "صلة القرابة", "أعاقة", "أمراض مزمنة",
                           "حامل/مرضعة","ملاحظة","تاريخ التسجيل")
        self.treeview = ttk.Treeview(treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsperson,
                                     height=20)

        self.treeview.column("العدد", width=20)
        # self.treeview.column("رقم الأسرة", width=60)
        self.treeview.column("هوية", width=80)
        self.treeview.column("الأسم رباعي", width=115)
        self.treeview.column("تاريخ الميلاد", width=70)
        self.treeview.column("الجنس", width=30)
        self.treeview.column("الحالة الاجتماعية", width=70)
        self.treeview.column("صلة القرابة", width=70)
        self.treeview.column("أعاقة", width=70)
        self.treeview.column("أمراض مزمنة", width=60)
        self.treeview.column("حامل/مرضعة", width=60)
        self.treeview.column("ملاحظة", width=40)
        self.treeview.column("تاريخ التسجيل", width=70)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        #     تحميل البيانات
        self.print_data_person(listdataperson)

    def treeonefamily(self):
        load_one_family = Searchcontroller.load_one_family(self, self.family_entry.get())


        treeFrame = ttk.LabelFrame(self.frame_2, text="Data", padding=(20, 20, 20, 10))
        treeFrame.grid(row=0,
                       column=1,
                       padx=10,
                       pady=(30, 10),
                       sticky="nsew",
                       rowspan=3)
        treeFrame.columnconfigure(index=0, weight=0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        # treeScroll = ttk.Scrollbar(treeFrame)
        # treeScroll.pack(side="bottom", fill="x")
        # self.listdatafamily,self.listdataperson = self.load_data()
        self.colsperson = ("العدد", "هوية",
                           "الأسم رباعي", "تاريخ الميلاد", "الجنس","الحالة الاجتماعية",
                           "صلة القرابة", "أعاقة", "أمراض مزمنة",
                           "حامل/مرضعة","ملاحظة","تاريخ التسجيل")
        self.treeview = ttk.Treeview(treeFrame,
                                     show="headings",
                                     yscrollcommand=treeScroll.set,
                                     columns=self.colsperson,
                                     height=20)

        self.treeview.column("العدد", width=20)
        # self.treeview.column("رقم الأسرة", width=60)
        self.treeview.column("هوية", width=80)
        self.treeview.column("الأسم رباعي", width=115)
        self.treeview.column("تاريخ الميلاد", width=70)
        self.treeview.column("الجنس", width=30)
        self.treeview.column("الحالة الاجتماعية", width=70)
        self.treeview.column("صلة القرابة", width=70)
        self.treeview.column("أعاقة", width=60)
        self.treeview.column("أمراض مزمنة", width=60)
        self.treeview.column("حامل/مرضعة", width=60)
        self.treeview.column("ملاحظة", width=40)
        self.treeview.column("تاريخ التسجيل", width=70)
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)
        #     تحميل البيانات
        self.print_data_one_family(load_one_family)

    #   ****************************************************


    def go_back(self):
        """الرجوع إلى الإطار السابق"""
        self.master.show_frame(DashboardPage, GEOMETRY)

    def printa(self):
        # print(len(self.load_maternity_family))
        self.data_frame = pd.DataFrame(self.listdatafamily,columns=self.colsfamily)
        # print(self.data_frame)
        self.exporter = DataExporterC(self.data_frame)
        self.exporter.save_file("excel")
        # print("allfamily")
    def printb(self):
        self.data_frame = pd.DataFrame(self.listdatafamily_rol, columns=self.colsfamily)
        # print(self.data_frame)
        self.exporter = DataExporterC(self.data_frame)
        self.exporter.save_file("excel")
        # print("allmaxfamily")
    def printc(self):
        self.data_frame = pd.DataFrame(self.load_maternity_family, columns=self.colsfamily)
        # print(self.data_frame)
        self.exporter = DataExporterC(self.data_frame)
        self.exporter.save_file("excel")
        # print("allmaternityfamily")
    def printd(self):
        self.data_frame = pd.DataFrame(self.load_obstruction_family, columns=self.colsfamily)
        # print(self.data_frame)
        self.exporter = DataExporterC(self.data_frame)
        self.exporter.save_file("excel")
        # print("allobstructionfamily")

    def printf(self):
        self.data_frame = pd.DataFrame(self.listdataperson_rol, columns=self.colsfamily)
        # print(self.data_frame)
        self.exporter = DataExporterC(self.data_frame)
        self.exporter.save_file("excel")
        # print("allobstructionfamily")


    def print_data_family(self,listdatafamily):
        for col_name in self.colsfamily:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in listdatafamily:
            self.treeview.insert('', tk.END, values=value_tuple)


    def print_data_family_rol(self,listdatafamily_rol):
        for col_name in self.colsfamily:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in listdatafamily_rol:
            self.treeview.insert('', tk.END, values=value_tuple)


    def print_maternity_family(self,load_maternity_family):
        for col_name in self.colsfamily:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in load_maternity_family:
            self.treeview.insert('', tk.END, values=value_tuple)

    def print_obstruction_family(self,load_obstruction_family):
        for col_name in self.colsfamily:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in load_obstruction_family:
            self.treeview.insert('', tk.END, values=value_tuple)

    def print_person_rol(self,listdataperson_rol):
        for col_name in self.colsfamily:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in listdataperson_rol:
            self.treeview.insert('', tk.END, values=value_tuple)

    def print_data_person(self,listdataperson):
        for col_name in self.colsperson:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in listdataperson:
            self.treeview.insert('', tk.END, values=value_tuple)

    def print_data_one_family(self,load_one_family):
        for col_name in self.colsperson:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in load_one_family:
            self.treeview.insert('', tk.END, values=value_tuple)
