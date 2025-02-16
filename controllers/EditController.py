from tkinter import messagebox

from db.ContactDataBase import onefamily, oneperson
from db.ContactDataBase import editphone, editaddress, editmaternity
from db.ContactDataBase import editchronicdiseases, editobstruction, editnote
from db.ContactDataBase import editidentityperson, editfullnameperson, editdateofbirthperson
from db.ContactDataBase import editsex, editsocialstatus, editalliance



class Editcontroller():
    def __init__(self):
        pass
    def getdataonefamily(self, identityperson):
        dict_one_family = {}
        count = 1
        if identityperson != "رقم هوية رب الأسرة":
            cursor_family = onefamily(identityperson)
            datafamily = cursor_family.fetchall()
            for tupl in datafamily:
                for item in tupl:
                    if item == None:
                        item = "لا يوجد بيانات"
                    if count == 1:
                        dict_one_family["Id"] = item
                    elif count == 2:
                        dict_one_family["Identity_Person"] = item
                    elif count == 3:
                        dict_one_family["PhoneNumber"] = item
                    elif count == 4:
                        dict_one_family["Address"] = item
                    elif count == 5:
                        dict_one_family["Numberfamily"] = item
                    elif count == 6:
                        dict_one_family["DateOFConstruction"] = item
                    count +=1
        elif identityperson == "رقم هوية رب الأسرة":
            messagebox.showinfo("خطأ", "لم يتم أدخال رقم الهوية")
            item = "لا يوجد بيانات"
            dict_one_family["Id"] = item
            dict_one_family["Identity_Person"] = item
            dict_one_family["PhoneNumber"] = item
            dict_one_family["Address"] = item
            dict_one_family["Numberfamily"] = item
            dict_one_family["DateOFConstruction"] = item
        # print(dict_one_family)
        return dict_one_family

    def getdataoneperson(self, identityperson):
        dict_one_person = {}
        count = 1
        if identityperson != "رقم هوية الشخص":
            cursor_family = oneperson(identityperson)
            datafamily = cursor_family.fetchall()
            for tupl in datafamily:
                for item in tupl:
                    if item == None:
                        item = "لا يوجد بيانات"
                    if count == 1:
                        dict_one_person["Id_Family"] = item
                    elif count == 2:
                        dict_one_person["IdentityPerson"] = item
                    elif count == 3:
                        dict_one_person["FullName"] = item
                    elif count == 4:
                        dict_one_person["DateOFBirth"] = item
                    elif count == 5:
                        dict_one_person["Sex"] = item
                    elif count == 6:
                        dict_one_person["SocialStatus"] = item
                    elif count == 7:
                        dict_one_person["Alliance"] = item
                    elif count == 8:
                        dict_one_person["Obstruction"] = item
                    elif count == 9:
                        dict_one_person["ChronicDiseases"] = item
                    elif count == 10:
                        dict_one_person["Maternity"] = item
                    elif count == 11:
                        dict_one_person["Note"] = item
                    elif count == 12:
                        dict_one_person["DateOFConstructionPerson"] = item
                    count += 1
        elif identityperson == "رقم هوية الشخص":
            messagebox.showinfo("خطأ", "لم يتم أدخال رقم الهوية")
            item = "لا يوجد بيانات"
            dict_one_person["Id_Family"] = item
            dict_one_person["IdentityPerson"] = item
            dict_one_person["FullName"] = item
            dict_one_person["DateOFBirth"] = item
            dict_one_person["Sex"] = item
            dict_one_person["SocialStatus"] = item
            dict_one_person["Alliance"] = item
            dict_one_person["Obstruction"] = item
            dict_one_person["ChronicDiseases"] = item
            dict_one_person["Maternity"] = item
            dict_one_person["Note"] = item
            dict_one_person["DateOFConstructionPerson"] = item
        # print(dict_one_person)
        return dict_one_person


    def editdatafamily_phone(self, phonenumber_new, identityentry):
        if identityentry != "رقم هوية رب الأسرة":
            if phonenumber_new != "رقم الجوال":
                boolre = editphone(phonenumber_new, identityentry)
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة رقم الجوال!")
                boolre = False
        else:
            messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
            boolre = False

        if boolre == True:
            messagebox.showinfo("خطأ", "تم التعديل!")

        elif boolre == False:
            messagebox.showinfo("خطأ", "لم يتم التعديل!")

    def editdatafamily_address(self, address, identityentry):
        if identityentry != "رقم هوية رب الأسرة":
            if address != "مدينة السابقة - الحي - أقرب معلم":
                boolre = editaddress(address, identityentry)
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة العنوان!")
                boolre = False
        else:
            messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
            boolre = False

        if boolre == True:
            messagebox.showinfo("خطأ", "تم التعديل!")

        elif boolre == False:
            messagebox.showinfo("خطأ", "لم يتم التعديل!")




    def editdataperson_maternity(self, maternity, identityentry):
        try:
            if identityentry != "رقم هوية الشخص":
                if maternity == 1:
                    boolre = editmaternity("حامل", identityentry)
                elif maternity == 2:
                    boolre = editmaternity("مرضعة", identityentry)
                else:
                    boolre = False
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
                boolre = False

            if boolre == True:
                messagebox.showinfo("خطأ", "تم التعديل!")

            elif boolre == False:
                messagebox.showinfo("خطأ", "لم يتم التعديل!")
        except Exception:
            messagebox.showinfo("خطأ", Exception)

    def editdataperson_chronicdiseases(self, chronicdiseases, identityentry):
        try:
            # print(chronicdiseases)
            if identityentry != "رقم هوية الشخص":
                if chronicdiseases == 1:
                    boolre = editchronicdiseases("سكري", identityentry)
                elif chronicdiseases == 2:
                    boolre = editchronicdiseases("ضغط", identityentry)
                elif chronicdiseases == 3:
                    boolre = editchronicdiseases("سكري وضغط", identityentry)
                else:
                    boolre = False
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
                boolre = False

            if boolre == True:
                messagebox.showinfo("خطأ", "تم التعديل!")

            elif boolre == False:
                messagebox.showinfo("خطأ", "لم يتم التعديل!")
        except Exception:
            messagebox.showinfo("خطأ", Exception)

    def editdataperson_obstruction(self, obstruction, identityentry):
        try:
            lis_ = []
            # print(obstruction)
            if identityentry != "رقم هوية الشخص":
                if obstruction[0] == True:
                    lis_.append("حركية")
                if obstruction[1] == True:
                    lis_.append("سمعية")
                if obstruction[2] == True:
                    lis_.append("حسية")
                if obstruction[3] == True:
                    lis_.append("بصرية")
                if obstruction[4] == True:
                    lis_.append("دهنية")
                # print(lis_)
                strobstruction = ",".join(lis_)
                print(strobstruction)
                if strobstruction != "":
                    boolre = editobstruction(strobstruction, identityentry)
                else:
                    boolre = False
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
                boolre = False

            if boolre == True:
                messagebox.showinfo("خطأ", "تم التعديل!")

            elif boolre == False:
                messagebox.showinfo("خطأ", "لم يتم التعديل!")
        except Exception:
            messagebox.showinfo("خطأ", Exception)

    def editdataperson_note(self, note_new, identityentry):
        if identityentry != "رقم هوية الشخص":
            boolre = editnote(note_new, identityentry)
        else:
            messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
            boolre = False

        if boolre == True:
            messagebox.showinfo("خطأ", "تم التعديل!")

        elif boolre == False:
            messagebox.showinfo("خطأ", "لم يتم التعديل!")


    def editdataperson_identityperson(self, identityperson_new, identityentry):
        if identityentry != "رقم هوية الشخص":
            if identityperson_new != "رقم الهوية الجديد":
                boolre = editidentityperson(identityperson_new, identityentry)
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية الجديد!")
                boolre = False
        else:
            messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
            boolre = False

        if boolre == True:
            messagebox.showinfo("خطأ", "تم التعديل!")

        elif boolre == False:
            messagebox.showinfo("خطأ", "لم يتم التعديل!")

    def editdataperson_fullname(self, fullname_new, identityentry):
        if identityentry != "رقم هوية الشخص":
            if fullname_new != "الأسم رباعي":
                boolre = editidentityperson(fullname_new, identityentry)
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة الأسم رباعي!")
                boolre = False
        else:
            messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
            boolre = False
        if boolre == True:
            messagebox.showinfo("خطأ", "تم التعديل!")
        elif boolre == False:
            messagebox.showinfo("خطأ", "لم يتم التعديل!")


    def editdataperson_dateofbirth(self, dateofbirth_new, identityentry):
        if identityentry != "رقم هوية الشخص":
            boolre = editdateofbirthperson(dateofbirth_new, identityentry)
        else:
            messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
            boolre = False

        if boolre == True:
            messagebox.showinfo("خطأ", "تم التعديل!")
        elif boolre == False:
            messagebox.showinfo("خطأ", "لم يتم التعديل!")


    def editdataperson_sex(self, sex_new, identityentry):
        try:
            if identityentry != "رقم هوية الشخص":
                if sex_new == 1:
                    boolre = editsex("ذكر", identityentry)
                elif sex_new == 2:
                    boolre = editsex("انثى", identityentry)
                else:
                    boolre = False
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
                boolre = False

            if boolre == True:
                messagebox.showinfo("خطأ", "تم التعديل!")
            elif boolre == False:
                messagebox.showinfo("خطأ", "لم يتم التعديل!")
        except Exception:
            messagebox.showinfo("خطأ", Exception)

    def editdataperson_socialstatus(self, socialstatus, identityentry):
        try:
            if identityentry != "رقم هوية الشخص":
                if socialstatus == 1:
                    boolre = editsocialstatus("متزوج", identityentry)
                elif socialstatus == 2:
                    boolre = editsocialstatus("أعزب", identityentry)
                elif socialstatus == 3:
                    boolre = editsocialstatus("أرمل", identityentry)
                elif socialstatus == 4:
                    boolre = editsocialstatus("مطلقة", identityentry)
                else:
                    boolre = False
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
                boolre = False

            if boolre == True:
                messagebox.showinfo("خطأ", "تم التعديل!")
            elif boolre == False:
                messagebox.showinfo("خطأ", "لم يتم التعديل!")
        except Exception:
            messagebox.showinfo("خطأ", Exception)


    def editdataperson_alliance(self, alliance, identityentry):
        try:
            if identityentry != "رقم هوية الشخص":
                if alliance == 1:
                    boolre = editalliance("رب الأسرة", identityentry)
                elif alliance == 2:
                    boolre = editalliance("زوجة", identityentry)
                elif alliance == 3:
                    boolre = editalliance("ابن", identityentry)
                elif alliance == 4:
                    boolre = editalliance("بنت", identityentry)
                else:
                    boolre = False
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة رقم الهوية!")
                boolre = False

            if boolre == True:
                messagebox.showinfo("خطأ", "تم التعديل!")
            elif boolre == False:
                messagebox.showinfo("خطأ", "لم يتم التعديل!")
        except Exception:
            messagebox.showinfo("خطأ", Exception)
