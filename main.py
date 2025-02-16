import tkinter as tk
from tkinter import ttk
from views.Login import LoginPage
from views.DashBoard import DashboardPage, AddPage, EditPage, DeletePage, SearchPage
from constants import FOREST_DAEK_PATH, GEOMETRY
from constants import IMAG_TENT_ico

# -*- coding: utf-8 -*-

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        style = ttk.Style(self)
        # self.tk.call("source", FOREST_LIGHT_PATH)
        self.tk.call("source", FOREST_DAEK_PATH)
        style.theme_use("forest-dark")
        self.title("إدارة مخيم الشهداء")
        # self.geometry(GEOMETRY)
        # self.pack_slaves()
        # تحميل الصورة
        # icon_image = Image.open(IMAG_TENT_ico)  # استبدل بـ مسار صورتك
        # # icon_photo = ImageTk.PhotoImage(icon_image)

        # تعيين الصورة كأيقونة للبرنامج
        # self.iconbitmap(IMAG_TENT_ico)


        # تخزين الإطارات المختلفة
        self.frames = {}
        # self.bind('<Return>', lambda event: LoginPage.login)



        # إنشاء الإطارات المختلفة
        for F in (LoginPage, DashboardPage, AddPage, EditPage, DeletePage, SearchPage):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # إظهار أول إطار
        self.show_frame(LoginPage, GEOMETRY)

    def show_frame(self, page, geometry):
        """إظهار الإطار المطلوب"""
        frame = self.frames[page]
        self.geometry(geometry)  # تحديث العنوان
        frame.place(relx=0.5, rely=0.5, anchor="center", width=1200, height=700)
        # frame.pack(fill="both", expand=True)
        frame.tkraise()


# تشغيل التطبيق
if __name__ == "__main__":
    app = App()
    app.mainloop()

#
#
# Traceback (most recent call last):
#   File "D:\work\programming\python\PycharmProjects\CampMartyrs\dist\CampMartyrs\_internal\tkcalendar\calendar_.py", line 30, in <module>
#     from tkinter.font import Font
# ModuleNotFoundError: No module named 'tkinter.font'
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "main.py", line 6, in <module>
#   File "PyInstaller\loader\pyimod02_importers.py", line 378, in exec_module
#   File "views\Login.py", line 4, in <module>
#   File "PyInstaller\loader\pyimod02_importers.py", line 378, in exec_module
#   File "views\DashBoard.py", line 10, in <module>
#   File "D:\work\programming\python\PycharmProjects\CampMartyrs\dist\CampMartyrs\_internal\tkcalendar\__init__.py", line 26, in <module>
#     from tkcalendar.dateentry import DateEntry
#   File "D:\work\programming\python\PycharmProjects\CampMartyrs\dist\CampMartyrs\_internal\tkcalendar\dateentry.py", line 35, in <module>
#     from tkcalendar.calendar_ import Calendar
#   File "D:\work\programming\python\PycharmProjects\CampMartyrs\dist\CampMartyrs\_internal\tkcalendar\calendar_.py", line 32, in <module>
#     import ttk
# ModuleNotFoundError: No module named 'ttk'



