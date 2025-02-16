from db.ContactDataBase import gitdatafamily,gitdataperson, gitdataperson_s
from tkinter import messagebox
import time



class Searchcontroller():
    def __init__(self):
        pass

    def load_data_family(self):
        listdatafamily_ = []
        listdatafamily_new = []
        dectdata = {}
        countm = 0
        countf = 0
        cursor_family = gitdatafamily()
        datafamily = cursor_family.fetchall()
        cursor_person = gitdataperson_s()
        dataperson = cursor_person.fetchall()
        # print(datafamily)
        # print(dataperson)
        for identityfamily in datafamily:
            dectdata["Id"] = identityfamily[0]
            dectdata["Identity_Person"] = identityfamily[1]
            dectdata["PhoneNumber"] = identityfamily[2]
            dectdata["Address"] = identityfamily[3]
            dectdata["COUNT_Id_Family"] = identityfamily[4]
            dectdata["COUNT_Id_M"] = 0
            dectdata["COUNT_Id_F"] = 0
            dectdata["Nameh"] = "لا يوجد الاسم"
            dectdata["Identity_w"] = "لا يوجد رقم هوية"
            dectdata["Namew"] = "لا يوجد الاسم"
            listdatafamily_.append(dectdata)
            dectdata = {}
        # print(listdatafamily_)
        for itm in listdatafamily_:
            for identityperson in dataperson:
                if itm["Id"] == identityperson[0]:
                    if identityperson[4] == "ذكر":
                        countm += 1
                        itm["COUNT_Id_M"] = countm
                    elif identityperson[4] == "انثى":
                        countf += 1
                        itm["COUNT_Id_F"] = countf
                    # print(itm["Id"])
                    if identityperson[6] == "رب الأسرة":
                        itm["Nameh"] = identityperson[2:3][0]
                    if identityperson[6] == "الزوجة":
                        itm["Identity_w"] = identityperson[1:2][0]
                        itm["Namew"] = identityperson[2:3][0]
                    elif identityperson[5] == "ارمل":
                        itm["Identity_w"] = "ارمل"
                        itm["Namew"] = "ارمل"
                    elif identityperson[5] == "مطلقة":
                        itm["Identity_w"] = "مطلقة"
                        itm["Namew"] = "مطلقة"
                    elif identityperson[5] == "متزوج" :
                        itm["Identity_w"] = "لا يوجد رقم هوية"
                        itm["Namew"] = "لا يوجد الاسم"
            countf = 0
            countm = 0

        for i in listdatafamily_:
            # print(i)
            if i["Nameh"] != "لا يوجد الاسم":
                lis1 = tuple(i.values())[:2]
                lis2 = tuple(i.values())[2:7]
                lis3 = tuple(i.values())[7:]
                lis = lis1 + lis3 + lis2
                listdatafamily_new.append(lis)
            # listdatafamily_new.append(tuple(i.values()))
        # print(listdatafamily_)
        # print(listdatafamily_new)

        # for identityfamily in datafamily:
        #     for identityperson in dataperson:
        #         if identityfamily[1] == identityperson[1]:
        #                 identityfamily += identityperson[2:3]
        #
        #     for identityperson in dataperson:
        #         if identityfamily[0] == identityperson[0]:
        #             if identityperson[6] == "الزوجة":
        #                 identityfamily += identityperson[1:3]
        #                 listdatafamily_.append(identityfamily)
        #             if identityperson[5] == "ارمل":
        #                 identityfamily += ("ارمل", "ارمل")
        #                 listdatafamily_.append(identityfamily)
        #             elif identityperson[5] == "مطلقة":
        #                 identityfamily += ("مطلقة", "مطلقة")
        #                 listdatafamily_.append(identityfamily)
        #             # elif identityfamily[5] == "متزوج":
        #             #     continue
        #             # elif identityfamily[5] == "متزوجة":
        #             #     continue
        #             # elif identityfamily[5] == "اعزب":
        #             #     continue
        #             # elif identityfamily[5] == "عزبا":
        #             #     continue
        #             # else:
        #             #     # identityfamily += tuple(["لا يوجد الاسم"])
        #             #     identityfamily += ("لا توجد بيانات", "لا توجد بيانات")
        #     # listdatafamily_.append(identityfamily)
        # for i in listdatafamily_:
        #     lis1 = i[:2]
        #     lis2 = i[2:6]
        #     lis3 = i[6:]
        #     lis = lis1 + lis3 + lis2
        #     listdatafamily_new.append(lis)
        return listdatafamily_new

    def load_data_family_none(self):
        listdatafamily_ = []
        listdatafamily_new = []
        dectdata = {}
        cursor_family = gitdatafamily()
        datafamily = cursor_family.fetchall()
        cursor_person = gitdataperson_s()
        dataperson = cursor_person.fetchall()
        # print(datafamily)
        # print(dataperson)
        for identityfamily in datafamily:
            dectdata["Id"] = identityfamily[0]
            dectdata["Identity_Person"] = identityfamily[1]
            dectdata["PhoneNumber"] = identityfamily[2]
            dectdata["Address"] = identityfamily[3]
            dectdata["COUNT_Id_Family"] = identityfamily[4]
            dectdata["DateOFConstruction"] = identityfamily[5]
            dectdata["Nameh"] = "لا يوجد الاسم"
            dectdata["Identity_w"] = "لا يوجد رقم هوية"
            dectdata["Namew"] = "لا يوجد الاسم"
            listdatafamily_.append(dectdata)
            dectdata = {}
        for itm in listdatafamily_:
            for identityperson in dataperson:
                if itm["Id"] == identityperson[0]:
                    if identityperson[6] == "رب الأسرة":
                        itm["Nameh"] = identityperson[2:3][0]
                    if identityperson[6] == "الزوجة":
                        itm["Identity_w"] = identityperson[1:2][0]
                        itm["Namew"] = identityperson[2:3][0]
                    elif identityperson[5] == "ارمل":
                        itm["Identity_w"] = "ارمل"
                        itm["Namew"] = "ارمل"
                    elif identityperson[5] == "مطلقة":
                        itm["Identity_w"] = "مطلقة"
                        itm["Namew"] = "مطلقة"
                    elif identityperson[5] == "متزوج" :
                        itm["Identity_w"] = "لا يوجد رقم هوية"
                        itm["Namew"] = "لا يوجد الاسم"
        for i in listdatafamily_:
            if i["Nameh"] == "لا يوجد الاسم" or i["Identity_w"] == "لا يوجد رقم هوية" or i["Nameh"] == "لا يوجد الاسم":
                lis1 = tuple(i.values())[:2]
                lis2 = tuple(i.values())[2:6]
                lis3 = tuple(i.values())[6:]
                lis = lis1 + lis3 + lis2
                listdatafamily_new.append(lis)

        return listdatafamily_new


    def load_data_family_rol(self, num_entry):
        listdatafamily_ = []
        listdatafamily_new = []
        dectdata = {}
        cursor_family = gitdatafamily()
        datafamily = cursor_family.fetchall()
        cursor_person = gitdataperson_s()
        dataperson = cursor_person.fetchall()
        if num_entry == "رقم الافراد":
            messagebox.showinfo("خطأ", "لم يتم أدخال رقم الافراد")
            return listdatafamily_new
        else:
            num = int(num_entry)
        # print(datafamily)
        # print(dataperson)
        for identityfamily in datafamily:
            dectdata["Id"] = identityfamily[0]
            dectdata["Identity_Person"] = identityfamily[1]
            dectdata["PhoneNumber"] = identityfamily[2]
            dectdata["Address"] = identityfamily[3]
            dectdata["COUNT_Id_Family"] = identityfamily[4]
            dectdata["DateOFConstruction"] = identityfamily[5]
            dectdata["Nameh"] = "لا يوجد الاسم"
            dectdata["Identity_w"] = "لا يوجد رقم هوية"
            dectdata["Namew"] = "لا يوجد الاسم"
            listdatafamily_.append(dectdata)
            dectdata = {}
        # print(listdatafamily_)
        for itm in listdatafamily_:
            for identityperson in dataperson:
                if itm["Id"] == identityperson[0]:
                    if identityperson[6] == "رب الأسرة":
                        itm["Nameh"] = identityperson[2:3][0]
                    if identityperson[6] == "الزوجة":
                        itm["Identity_w"] = identityperson[1:2][0]
                        itm["Namew"] = identityperson[2:3][0]
                    elif identityperson[5] == "ارمل":
                        itm["Identity_w"] = "ارمل"
                        itm["Namew"] = "ارمل"
                    elif identityperson[5] == "مطلقة":
                        itm["Identity_w"] = "مطلقة"
                        itm["Namew"] = "مطلقة"
                    elif identityperson[5] == "متزوج":
                        itm["Identity_w"] = "لا يوجد رقم هوية"
                        itm["Namew"] = "لا يوجد الاسم"
        for i in listdatafamily_:
            if i["COUNT_Id_Family"] >= num:
                lis1 = tuple(i.values())[:2]
                lis2 = tuple(i.values())[2:6]
                lis3 = tuple(i.values())[6:]
                lis = lis1 + lis3 + lis2
                listdatafamily_new.append(lis)

        return listdatafamily_new


    def load_maternity_family(self):
        lis_maternity = []
        lis_maternity_new = []
        cursor_family = gitdatafamily()
        datafamily = cursor_family.fetchall()
        cursor_person = gitdataperson()
        dataperson = cursor_person.fetchall()
        for identityfamily in datafamily:
            for identityperson in dataperson:
                if identityfamily[0] == identityperson[0]:
                    if identityperson[6] == "رب الأسرة":
                        identityfamily += identityperson[2:3]
                        # print(identityfamily)

            for identityperson in dataperson:
                if identityperson[9] == "حامل" or identityperson[9] == "مرضعة":
                    if identityfamily[0] == identityperson[0]:
                        if identityperson[6] == "الزوجة" or identityperson[6] == "رب الأسرة":
                            identityfamily += identityperson[1:3]
                            identityfamily += identityperson[9:10]
                            # print(identityfamily)
                            lis_maternity.append(identityfamily)
        # print(lis_maternity)
        for i in lis_maternity:
            lis1 = i[:2]
            lis2 = i[2:5]
            # lis3 = i[5:6]
            lis4 = i[6:9]
            lis5 = i[9:]
            # lis = lis1 + lis4 + lis2+ lis5 + lis3
            lis = lis1 + lis4 + lis2+ lis5
            lis_maternity_new.append(lis)
        return lis_maternity_new



    def load_obstruction_family(self):
        lis_maternity = []
        tupl = ()
        count = 1
        liscount = []
        cursor_family = gitdatafamily()
        datafamily = cursor_family.fetchall()
        cursor_person = gitdataperson()
        dataperson = cursor_person.fetchall()
        for identityfamily in datafamily:
            for identityperson in dataperson:
                if identityperson[7] != None or identityperson[8] != None:
                    if identityfamily[0] == identityperson[0]:
                        liscount.append(count)
                        tupl += tuple(liscount)
                        tupl += identityperson[:3]
                        tupl += identityperson[4:5]
                        tupl += identityfamily[2:3]
                        tupl += identityfamily[4:5]
                        tupl += identityperson[7:9]
                        # print(tupl)
                        lis_maternity.append(tupl)
                        tupl = ()
                        count += 1
                        liscount = []

        return lis_maternity

    def load_data_person_rol(self,ifitem, item):
        # print(ifitem)
        # print(item)
        count = 1
        liscount = []
        localtime = time.asctime(time.localtime(time.time()))
        lis_age = []
        lis_age_new = []
        tupl = ()
        age = []
        cursor_family = gitdatafamily()
        datafamily = cursor_family.fetchall()
        cursor_person = gitdataperson()
        dataperson = cursor_person.fetchall()
        # if family_entry == "رقم الاسرة, هوية رب الاسرة":
        #     messagebox.showinfo("خطأ", "لم يتم أدخال رقم الاسرة أو هوية رب الاسرة")
        #     return listdataperson_id
        # else:
        #     familyid = int(family_entry)
        for identityfamily in datafamily:
            for identityperson in dataperson:
                if identityfamily[0] == identityperson[0]:
                    # print(identityperson[3][-4:])
                    age.append(int(localtime[-4:]) - int(identityperson[3][:4]))
                    # print(age)

                    tupl += identityperson[1:3]
                    tupl += identityperson[4:5]
                    tupl += identityfamily[2:3]
                    tupl += tuple(age)
                    tupl += identityperson[7:9]
                    # print(tupl)
                    lis_age.append(tupl)
                    tupl = ()
                    age = []
        if item == "العداد":
            messagebox.showinfo("خطأ", "لم يتم أدخال العداد")
        elif ifitem == "أصغر من":
            # print(type(item))
            for i in lis_age:
                # print(i[4])
                if int(i[4]) <= int(item):
                    liscount.append(count)
                    i += tuple(liscount)
                    lis1 = i[-1:]
                    lis2 = i[:-1]
                    lis_age_new.append(lis1+lis2)
                    count += 1
                    liscount = []
        elif ifitem == "أكبر من":
            for i in lis_age:
                if int(i[4]) >= int(item):
                    liscount.append(count)
                    i += tuple(liscount)
                    lis1 = i[-1:]
                    lis2 = i[:-1]
                    lis_age_new.append(lis1 + lis2)
                    count += 1
                    liscount = []
        else:
            messagebox.showinfo("خطأ", "لم يتم أدخال فئة")
        return lis_age_new

    def load_data_person(self):
        count = 1
        liscount = []
        listperson = []
        cursor_person = gitdataperson()
        dataperson = cursor_person.fetchall()
        for i in dataperson:
            liscount.append(count)
            i += tuple(liscount)
            lis1 = i[-1:]
            lis2 = i[1:-1]
            listperson.append(lis1 + lis2)
            # print(i)
            count += 1
            liscount = []

        return listperson

    def load_one_family(self, family_entry):
        try:
            count = 1
            liscount = []
            listdataperson_id = []
            listdataperson_identity = []
            cursor_person = gitdataperson()
            dataperson = cursor_person.fetchall()
            listdataperson = list(dataperson)
            if family_entry == "رقم الاسرة, هوية رب الاسرة" or  family_entry == "رقم هوية رب الأسرة":
                messagebox.showinfo("خطأ", "لم يتم أدخال رقم الاسرة أو هوية رب الاسرة")
                return listdataperson_id
            else:
                familyid = int(family_entry)
            for id_family in listdataperson:
                if id_family[1] == familyid:
                    # print(id_family)
                    for id_family_ in listdataperson:
                        if id_family[0] == id_family_[0]:
                            liscount.append(count)
                            id_family_ += tuple(liscount)
                            lis1 = id_family_[-1:]
                            lis2 = id_family_[1:-1]
                            listdataperson_identity.append(lis1+lis2)
                            count += 1
                            liscount = []
                    return listdataperson_identity
                elif id_family[0] == familyid:
                    liscount.append(count)
                    id_family += tuple(liscount)
                    lis1 = id_family[-1:]
                    lis2 = id_family[1:-1]
                    listdataperson_id.append(lis1 + lis2)
                    count += 1
                    liscount = []
            return listdataperson_id
        except EOFError:
            messagebox.showerror("خطأ", EOFError)

