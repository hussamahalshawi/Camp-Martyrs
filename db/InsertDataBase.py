import sqlite3
import time
from tkinter import messagebox

from constants import DATABASE_PATH
from db.ContactDataBase import contactdatabase

def getidfamily(PhoneNumber):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        # cursor_ = contactdatabase()
        # print(IdentityPerson)
        id = cursor_.execute(F"""SELECT Id FROM Family WHERE PhoneNumber LIKE '{PhoneNumber}'""", )
        id_data = id.fetchall()
        # print(id_data)
        connection.commit()
        connection.close()
        return id_data
    except Exception as E:
        # messagebox.showinfo("خطأ", E)
        pass


def addfamily(colum_data,row_data):
    try:
        # print(f"""INSERT INTO Family
        #         {tuple(colum_data)}
        #         VALUES (?, ?, ?, ?)""",
        #         tuple(row_data))
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        # cursor_ = contactdatabase()
        cursor_.execute(F"""INSERT INTO Family 
                {tuple(colum_data)} 
                VALUES (?, ?, ?, ?)""", row_data)
        connection.commit()
        connection.close()
        return True
    except Exception as E:
        # messagebox.showinfo("خطأ", E)
        pass



def addperson_8(colum_data,row_data):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(F"""INSERT INTO Person 
                {tuple(colum_data)} 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", row_data)
        connection.commit()
        connection.close()
        return True
    except Exception as E:
        messagebox.showinfo("خطأ", E)
        # pass

def addperson_9(colum_data,row_data):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(F"""INSERT INTO Person 
                {tuple(colum_data)} 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", row_data)
        connection.commit()
        connection.close()
        return True
    except Exception as E:
        messagebox.showinfo("خطأ", E)
        # pass

def addperson_10(colum_data,row_data):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(F"""INSERT INTO Person 
                {tuple(colum_data)} 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", row_data)
        connection.commit()
        connection.close()
        return True
    except Exception as E:
        messagebox.showinfo("خطأ", E)
        # pass

def addperson_11(colum_data,row_data):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(F"""INSERT INTO Person 
                {tuple(colum_data)} 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", row_data)
        connection.commit()
        connection.close()
        return True
    except Exception as E:
        messagebox.showinfo("خطأ", E)
        # pass


def addperson_12(colum_data,row_data):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(F"""INSERT INTO Person 
                {tuple(colum_data)} 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", row_data)
        connection.commit()
        connection.close()
        return True
    except Exception as E:
        messagebox.showinfo("خطأ", E)
        # pass


# cursor_.execute("""
# INSERT INTO Operations (
#     UserName_Employment,
#     TypeOperations,
#     TopicOperations,
#     DateOFConstruction
#     ) VALUES (?, ?, ?, ?)""",
#         ("hussam",
#          "login",
#          "",
#          localtime
#          ))
# cursor_.execute("""
# INSERT INTO Company (
#     Name_Company,
#     Profession,
#     DateOFConstruction
#     ) VALUES (?,?,?)""",
#         ("slem_2",
#          "shabs",
#          localtime
#          ))
# cursor_.execute("""
# INSERT INTO Customer (
#     NameCustomer,
#     Profession,
#     DateOFConstruction
#     ) VALUES (?,?,?)""",
#         ("hane",
#          "حداد",
#          localtime
#          ))

# cursor_.execute("""
# INSERT INTO Connect (
#     Id_Customer,
#     ConnectPhone,
#     DateOFConstruction
#     ) VALUES (?,?,?)""",
#         (2,
#          "0567769425",
#          localtime
#          ))
# cursor_.execute("""
# INSERT INTO Address (
#     Id_Customer,
#     AddressCustomer,
#     DateOFConstruction
#     ) VALUES (?,?,?)""",
#         (3,
#          "رفح-السلطان",
#          localtime
#          ))

# cursor_.execute("""
# INSERT INTO Producer (
#     Name_Producer,
#     ClassProducer,
#     ManufacturerCompany,
#     Punch,
#     Unit,
#     UnityPrice,
#     DateOfProduction,
#     ExpirationDate,
#     DateOFConstruction
#     ) VALUES (?,?,?,?,?,?,?,?,?)""",
#         ("بسكوت",
#          "بسكوت",
#          "سالي",
#          "6",
#          "c",
#          "28",
#          "7/7/2022",
#          "20/12/2027",
#          localtime
#          ))

# cursor_.execute("""
# INSERT INTO Invoice (
#     UserName_Employment,
#     TypeOperations,
#     PaymentAmount,
#     DateOFConstruction
#     ) VALUES (?,?,?,?)""",
#         ("hussam",
#          "بيع",
#          96,
#          localtime
#          ))

# cursor_.execute("""
# INSERT INTO InvoiceDetails (
#     Id_Invoice,
#     ClassProducer,
#     Punch,
#     Unit,
#     UnityPrice,
#     TotalAmount
#     ) VALUES (?,?,?,?,?,?)""",
#         (7,
#          "عصير",
#          1,
#          "c",
#          126,
#          126
#          ))
