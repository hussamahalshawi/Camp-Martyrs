from tkinter import messagebox
from db.ContactDataBase import gitdatauser



# دالة لتسجيل الدخول
def loginuser(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    cursor_ = gitdatauser(username)

    datauser = cursor_.fetchall()
    # print(datauser, username)
    try:
        if datauser[0][0] == username and datauser[0][1] == password:
            # print(datauser[0][-1])
            messagebox.showinfo("نجاح", "تم تسجيل الدخول بنجاح!")
            return True
        else:
            messagebox.showerror("خطأ", "اسم المستخدم أو كلمة المرور غير صحيحة!")
    except IndexError:
        messagebox.showerror("خطأ", IndexError)

