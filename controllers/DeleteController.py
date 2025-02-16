from tkinter import messagebox

from db.ContactDataBase import deletefamily, deleteperson, onefamily, allpersonforfamily



class Deletecontroller():
    def __init__(self):
        pass
    def delete_family(self, identityperson):
        try:
            cursor_f = onefamily(identityperson)
            datefamily = cursor_f.fetchall()
            # print(datefamily)
            bol = deletefamily(identityperson)
            cursor_p = allpersonforfamily(datefamily[0][0])
            dateallperson = cursor_p.fetchall()
            for i in dateallperson:
                bolp = deleteperson(i[1])
                if bolp == True:
                    messagebox.showinfo("خطأ", f" تم الحذف{i[2]}!")

                elif bolp == False:
                    messagebox.showinfo("خطأ", "لم يتم الحذق!")
                # for j in i:
                #     print(j)
            if bol == True:
                messagebox.showinfo("خطأ", "تم الحذف للاسرة!")

            elif bol == False:
                messagebox.showinfo("خطأ", "لم يتم الحذق!")
            else:
                messagebox.showinfo("خطأ", "لا يوجد بيانات!")
        except IndexError:
            messagebox.showinfo("خطأ", "لا يوجد بيانات!")



    def delete_person(self, identityperson):
        bolp = deleteperson(identityperson)
        if bolp == True:
            messagebox.showinfo("خطأ", "تم الحذف الفرد!")

        elif bolp == False:
            messagebox.showinfo("خطأ", "لم يتم الحذف!")