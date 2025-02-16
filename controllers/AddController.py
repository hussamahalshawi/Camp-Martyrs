from tkinter import messagebox

from db.InsertDataBase import addfamily, getidfamily, addperson_12, addperson_8, addperson_9, addperson_10, addperson_11


class Addcontroller():
    def __init__(self):
        pass

    def addfamily_rul(self,dict_family):
        colum_data = []
        row_data = []
        lis = []
        for key_data in dict_family:
            colum_data.append(key_data)

            if key_data == "Identity_Person":
                try:
                    row_data.append(int(dict_family.get(key_data)))
                except Exception:
                    messagebox.showinfo("خطأ", "لم يتم أدخال رقم الهوية أو ليس رقم!")
                    break
            elif key_data == "PhoneNumber":
                try:
                    row_data.append(int(dict_family.get(key_data)))
                except Exception:
                    messagebox.showinfo("خطأ", "لم يتم أدخال رقم الجوال أو ليس رقم!")
                    break
            elif key_data == "Address":
                try:
                    if dict_family.get(key_data) != "مدينة السابقة - الحي - أقرب معلم":
                        row_data.append(str(dict_family.get(key_data)))
                    else:
                        messagebox.showinfo("خطأ", "لم يتم أدخال العنوان!")
                        break
                except Exception:
                    messagebox.showinfo("خطأ", "لم يتم أدخال نص!")
                    break

            elif key_data == "DateOFConstruction":
                row_data.append(str(dict_family.get(key_data)))
            # print(type(key_data),type(dict_family.get(key_data)))
        # for i in row_data:
        #     print(type(i))
        # print(colum_data,row_data)
        boolreturn = addfamily(colum_data,row_data)
        if boolreturn is True:
            messagebox.showinfo("نجاح", "تم أضافة الأسرة  بنجاح!")
        else:
            messagebox.showinfo("خطأ", "لم يتم أضافة الأسرة!")



    def addperson_rul(self,dict_person):
        colum_data = []
        row_data = []
        lis = []
        for key_data in dict_person:
            if key_data == "PhoneNumber":
                try:
                    id = getidfamily(int(dict_person.get(key_data)))
                    # print(id)
                    row_data.append(id[0][0])
                    colum_data.append("Id_Family")
                except Exception:
                    messagebox.showinfo("خطأ", "لم يتم أدخال رقم الجوال أو ليس رقم!")
                    break
            elif key_data == "IdentityPerson":
                try:

                    row_data.append(int(dict_person.get(key_data)))
                    colum_data.append(key_data)
                except Exception:
                    # print(Exception)
                    messagebox.showinfo("خطأ", "لم يتم أدخال رقم الهوية أو ليس رقم!")
                    break
            elif key_data == "FullName":
                try:
                    if dict_person.get(key_data) != "الأسم رباعي":
                        row_data.append(str(dict_person.get(key_data)))
                        colum_data.append(key_data)
                    else:
                        messagebox.showinfo("خطأ", "لم يتم أدخال الأسم!")
                        break
                except Exception:
                    messagebox.showinfo("خطأ", "لم يتم أدخال نص!")
                    break
            elif key_data == "DateOFBirth":
                try:
                    row_data.append(str(dict_person.get(key_data)))
                    colum_data.append(key_data)
                except Exception:
                    messagebox.showinfo("خطأ", "لم يتم أدخال التاريخ!")
                    break
            elif key_data == "Sex":
                try:
                    if dict_person.get(key_data) == 1:
                        row_data.append("ذكر")
                    elif dict_person.get(key_data) == 2:
                        row_data.append("انثى")
                    else:
                        messagebox.showinfo("خطأ", "لم يتم أدخال الجنس!")
                        break
                    colum_data.append(key_data)
                except Exception:
                    messagebox.showinfo("خطأ", Exception)
                    break
            elif key_data == "SocialStatus":
                try:
                    if dict_person.get(key_data) == 1:
                        row_data.append("متزوج")
                    elif dict_person.get(key_data) == 2:
                        row_data.append("أعزب")
                    elif dict_person.get(key_data) == 3:
                        row_data.append("أرمل")
                    elif dict_person.get(key_data) == 4:
                        row_data.append("مطلقة")
                    else:
                        messagebox.showinfo("خطأ", "لم يتم أدخال الحالة الأجتماعية!")
                        break
                    colum_data.append(key_data)
                except Exception:
                    messagebox.showinfo("خطأ", Exception)
                    break
            elif key_data == "Alliance":
                try:
                    if dict_person.get(key_data) == 1:
                        row_data.append("رب الأسرة")
                    elif dict_person.get(key_data) == 2:
                        row_data.append("زوجة")
                    elif dict_person.get(key_data) == 3:
                        row_data.append("ابن")
                    elif dict_person.get(key_data) == 4:
                        row_data.append("بنت")
                    else:
                        messagebox.showinfo("خطأ", "لم يتم أدخال صلة القرابة!")
                        break
                    colum_data.append(key_data)
                except Exception:
                    messagebox.showinfo("خطأ", Exception)
                    break
            elif key_data == "Obstruction":
                try:
                    for obstruction in dict_person.get(key_data):
                        # print(obstruction)
                        if dict_person.get(key_data).get(obstruction) == True:
                            if obstruction == "kinetic":
                                lis.append("حركي")
                            elif obstruction == "audio":
                                lis.append("سمعي")
                            elif obstruction == "sensuality":
                                lis.append("حسية")
                            elif obstruction == "visual":
                                lis.append("بصرية")
                            elif obstruction == "fatness":
                                lis.append("دهنية")
                        string_obstruction = ",".join(lis)
                    # print(str_obstruction)
                    if string_obstruction != ",":
                        row_data.append(str(string_obstruction))
                        colum_data.append(key_data)
                except Exception:
                    messagebox.showinfo("خطأ", Exception)
                    break

            elif key_data == "ChronicDiseases":
                try:
                    if dict_person.get(key_data) == 1:
                        row_data.append("سكري")
                        colum_data.append(key_data)
                    elif dict_person.get(key_data) == 2:
                        row_data.append("ضغط")
                        colum_data.append(key_data)
                    elif dict_person.get(key_data) == 3:
                        row_data.append("سكري وضغط")
                        colum_data.append(key_data)
                except Exception:
                    messagebox.showinfo("خطأ", Exception)
                    break
            elif key_data == "Maternity":
                try:
                    if dict_person.get(key_data) == 1:
                        row_data.append("حامل")
                        colum_data.append(key_data)
                    elif dict_person.get(key_data) == 2:
                        row_data.append("مرضعة")
                        colum_data.append(key_data)
                except Exception:
                    messagebox.showinfo("خطأ", Exception)
                    break
            elif key_data == "Note":
                try:
                    if dict_person.get(key_data) != "ملاحظة":
                        row_data.append(str(dict_person.get(key_data)))
                        colum_data.append(key_data)
                except Exception:
                    messagebox.showinfo("خطأ", Exception)
                    break
            #
            elif key_data == "DateOFConstructionPerson":
                row_data.append(str(dict_person.get(key_data)))
                colum_data.append(key_data)


        # print(colum_data)
        # print(row_data)
        if len(colum_data) == 8:
            boolreturn = addperson_8(colum_data, row_data)
            if boolreturn is True:
                messagebox.showinfo("نجاح", "تم أضافة الفرد  بنجاح!")
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة الفرد!")
        elif len(colum_data) == 9:
            boolreturn = addperson_9(colum_data, row_data)
            if boolreturn is True:
                messagebox.showinfo("نجاح", "تم أضافة الفرد  بنجاح!")
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة الفرد!")
        elif len(colum_data) == 10:
            boolreturn = addperson_10(colum_data, row_data)
            if boolreturn is True:
                messagebox.showinfo("نجاح", "تم أضافة الفرد  بنجاح!")
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة الفرد!")
        elif len(colum_data) == 11:
            boolreturn = addperson_11(colum_data, row_data)
            if boolreturn is True:
                messagebox.showinfo("نجاح", "تم أضافة الفرد  بنجاح!")
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة الفرد!")
        elif len(colum_data) == 12:
            boolreturn = addperson_12(colum_data, row_data)
            if boolreturn is True:
                messagebox.showinfo("نجاح", "تم أضافة الفرد  بنجاح!")
            else:
                messagebox.showinfo("خطأ", "لم يتم أضافة الفرد!")
        else:
            messagebox.showinfo("خطأ", "يوجد بيانات غير صحيح")
