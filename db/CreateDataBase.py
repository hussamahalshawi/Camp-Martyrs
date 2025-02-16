import sqlite3


connection = sqlite3.connect("CampMartyrs.db")
cursor_ = connection.cursor()
cursor_.execute("""
CREATE TABLE IF NOT EXISTS Users(
    UserName VARCHAR(100) NOT NULL UNIQUE,
    Password password NOT NULL,
    Name VARCHAR(100) UNIQUE NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY(UserName)
)
""")
cursor_.execute("""
CREATE TABLE IF NOT EXISTS Family(
    Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    Identity_Person INTEGER UNIQUE NOT NULL,
    PhoneNumber INTEGER UNIQUE NOT NULL,
    Address VARCHAR(100),
    DateOFConstruction VARCHAR(50) NOT NULL
)
""")
cursor_.execute("""
CREATE TABLE IF NOT EXISTS Person(
    Id_Family INTEGER NOT NULL,
    IdentityPerson INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    FullName VARCHAR(100) UNIQUE NOT NULL,
    DateOFBirth DATE NOT NULL,
    Sex VARCHAR(10) NOT NULL,
    SocialStatus VARCHAR(10) NOT NULL,
    Alliance VARCHAR(10) NOT NULL,
    Obstruction VARCHAR(30),
    ChronicDiseases VARCHAR(30),
    Maternity VARCHAR(30),
    Note VARCHAR(150),
    DateOFConstructionPerson DATE NOT NULL,
    CONSTRAINT Family_Fk  FOREIGN KEY(Id_Family) REFERENCES Family(Id_Family)
    )
""")
# cursor_.execute("""
# ALTER TABLE Person ADD COLUMN SocialStatus VARCHAR(10) DEFAULT a NOT NULL
#     )
# """)
connection.commit()
connection.close()