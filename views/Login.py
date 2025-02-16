import tkinter as tk
from tkinter import ttk
from tkinter import *
from views.DashBoard import DashboardPage
from services.auth_service import loginuser
from constants import GEOMETRY
from constants import IMAG_KEY

# -*- coding: utf-8 -*-

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        import arabic_reshaper
        from bidi.algorithm import get_display

        text = " تسجيل الدخول "
        reshaped_text = arabic_reshaper.reshape(text)  # إعادة تشكيل النص
        bidi_text = get_display(reshaped_text)  # ترتيب النص
        print(text)
        print(bidi_text)
        # ****************************
        # self.master.show_frame(Dashboard, "1200x700")
        # ***************************
        IMAG_KEY_ = PhotoImage(file=IMAG_KEY).subsample(12, 12)

        # إعداد إطار مركزي لتجميع العناصر
        self.frame_2 = tk.LabelFrame(self, border=1, relief="ridge")
        self.frame_2.grid(row=0, column=0, padx=(20, 10), pady=(20, 10),sticky="nsew")
        self.frame_2.place(relx=0.5, rely=0.5, anchor="center", width=700, height=350)
        # self.frame_2.grid()

        # العنوان الرئيسي
        title_label = tk.Label(self.frame_2,
                               text=bidi_text,
                               font=("Arial", 20, "bold"),
                               image= IMAG_KEY_,
                               compound= RIGHT,
                               fg="white")
        title_label.image = IMAG_KEY_
        title_label.pack(pady=10)
        # حقول الإدخال لاسم المستخدم
        username_label = tk.Label(self.frame_2, text=":اسم المستخدم", font=("Arial", 16), fg="#d1d1e0")
        username_label.pack(pady=5)
        self.username_entry = ttk.Entry(self.frame_2, font=("Arial", 14), justify="center")
        self.username_entry.pack(ipady=5, pady=5, fill="x", padx=20)
        # حقول الإدخال لكلمة المرور
        password_label = tk.Label(self.frame_2, text=":كلمة المرور", font=("Arial", 16), fg="#d1d1e0")
        password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self.frame_2, font=("Arial", 14), justify="center", show="*")
        self.password_entry.pack(ipady=5, pady=5, fill="x", padx=20)

        # self.bind('<Enter>', self.login())
        # زر تسجيل الدخول
        login_button = ttk.Button(self.frame_2,
                                 text="تسجيل الدخول",
                                  style="Accent.TButton",
                                 command=self.login)
        login_button.pack(ipady=5, pady=20, fill="x",padx=150)

    def login(self):
        booluser = loginuser(self.username_entry, self.password_entry)
        if booluser == True:
            # self.master.withdraw()
            self.master.show_frame(DashboardPage, GEOMETRY)


