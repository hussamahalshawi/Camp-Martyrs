import sqlite3
from constants import DATABASE_PATH


def contactdatabase():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor_ = connection.cursor()
    return cursor_


def editphone(phonenumber_new, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(
            f"UPDATE Family SET PhoneNumber = '{phonenumber_new}' WHERE Identity_Person = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editaddress(address, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Family SET Address = '{address}' WHERE Identity_Person = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editmaternity(maternity, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Person SET Maternity = '{maternity}' WHERE IdentityPerson = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editchronicdiseases(chronicdiseases, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(
            f"UPDATE Person SET ChronicDiseases = '{chronicdiseases}' WHERE IdentityPerson = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editobstruction(obstruction, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Person SET Obstruction = '{obstruction}' WHERE IdentityPerson = '{identityentry}'")
        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editnote(note, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Person SET Note = '{note}' WHERE IdentityPerson = '{identityentry}'")
        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editidentityperson(editidentityperson, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(
            f"UPDATE Person SET IdentityPerson = '{editidentityperson}' WHERE IdentityPerson = '{identityentry}'")
        cursor_.execute(
            f"UPDATE Family SET Identity_Person = '{editidentityperson}' WHERE Identity_Person = '{identityentry}'")
        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editfullnameperson(fullname, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Person SET FullName = '{fullname}' WHERE IdentityPerson = '{identityentry}'")
        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editdateofbirthperson(dateofbirth, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Person SET DateOFBirth = '{dateofbirth}' WHERE IdentityPerson = '{identityentry}'")
        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editsex(sex, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Person SET Sex = '{sex}' WHERE IdentityPerson = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editsocialstatus(socialstatus, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Person SET SocialStatus = '{socialstatus}' WHERE IdentityPerson = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def editalliance(alliance, identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()
        cursor_.execute(f"UPDATE Person SET Alliance = '{alliance}' WHERE IdentityPerson = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def deletefamily(identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()

        cursor_.execute(f"DELETE FROM Family WHERE Identity_Person = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def deleteperson(identityentry):
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        cursor_ = connection.cursor()

        cursor_.execute(f"DELETE FROM Person WHERE IdentityPerson = '{identityentry}'")

        connection.commit()
        connection.close()

        return True
    except EOFError:
        return False


def gitdatauser(username):
    cursor_ = contactdatabase()
    cursor_.execute(f"SELECT * FROM Users WHERE UserName LIKE '{username}'")
    return cursor_


def onefamily(identityperson):
    cursor_ = contactdatabase()
    cursor_.execute(f"""
            SELECT Id,Identity_Person,PhoneNumber,Address,COUNT(Id_Family),DateOFConstruction
            FROM Family  
            LEFT JOIN Person
            ON Family.Id=Person.Id_Family
            GROUP BY Id
            HAVING Identity_Person LIKE '{identityperson}'

        """)
    return cursor_


def oneperson(identityperson):
    cursor_ = contactdatabase()
    cursor_.execute(f"""
            SELECT *
            FROM Person WHERE IdentityPerson LIKE '{identityperson}'

        """)
    return cursor_


def allpersonforfamily(id):
    cursor_ = contactdatabase()
    cursor_.execute(f"""
            SELECT *
            FROM Person WHERE Id_Family LIKE '{id}'

        """)
    return cursor_


def gitdatafamily():
    cursor_ = contactdatabase()
    # cursor_.execute(f"""
    #
    #     SELECT Id_Family,IdentityPerson,FullName,
    #     IdentityPerson,FullName,
    #     PhoneNumber,Address,COUNT(Id_Family),
    #     DateOFConstruction
    #     FROM Person
    #     LEFT JOIN Family
    #     ON Person.Id_Family=Family.Id
    #     GROUP BY Id_Family
    #     UNION
    #     SELECT IdentityPerson AS IdentityWife ,FullName AS FullNameWife
    #     FROM Person
    #     WHERE Alliance='الزوجة'
    #
    # """)
    cursor_.execute(f"""
        SELECT Id,Identity_Person,PhoneNumber,Address,COUNT(Id_Family),DateOFConstruction
        FROM Family
        LEFT JOIN Person
        ON Family.Id=Person.Id_Family
        GROUP BY Id

    """)
    # cursor_.execute(f"""
    #     SELECT *
    #     FROM Family
    #     ORDER BY Id
    #
    # """)
    return cursor_


def gitdataperson():
    cursor_ = contactdatabase()
    cursor_.execute(f"""
        SELECT *
        FROM Person
        ORDER BY DateOFBirth
        
    """)
    return cursor_


def gitdataperson_s():
    cursor_ = contactdatabase()
    cursor_.execute(f"""
        SELECT *
        FROM Person
        ORDER BY SocialStatus

    """)
    return cursor_

# def gitdatamaternityperson():
#     cursor_ = contactdatabase()
#     cursor_.execute(f"""
#         SELECT Id_Family,IdentityPerson,FullName,sex,
#         Obstruction,ChronicDiseases,Maternity
#         FROM Person
#         LEFT JOIN Family
#         ON Person.Id_Family=Family.Id
#         GROUP BY Id_Family
#         HAVING Maternity NOT NULL
#
#     """)
#     return cursor_
