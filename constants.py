import os

file_path = os.path.realpath(__file__) # ***********
current_directory = os.path.dirname(file_path) # **********

# ---------------- FILE  ------------------------------------------------
FOREST_LIGHT_PATH = os.path.join(current_directory, 'views/forest-light.tcl')
FOREST_DAEK_PATH = os.path.join(current_directory, 'views/forest-dark.tcl')
DATABASE_PATH = os.path.join(current_directory, 'db/CampMartyrs.db')
# ----------------  IMAGE  -----------------------
IMAG_TENT = os.path.join(current_directory,'imags/tent.png')
IMAG_TENT_ico = os.path.join(current_directory,'imags/tent_ico_.ico')
IMAG_TRASH = os.path.join(current_directory,"imags/trash.png")
IMAG_HOME = os.path.join(current_directory,"imags/home.png")
IMAG_EDIT = os.path.join(current_directory,"imags/edit.png")
IMAG_ADD = os.path.join(current_directory,"imags/add.png")
IMAG_SAERCH = os.path.join(current_directory,"imags/loupe.png")
IMAG_SAERCH_2 = os.path.join(current_directory,"imags/search.png")
IMAG_KEY = os.path.join(current_directory,"imags/key.png")
IMAG_BACK = os.path.join(current_directory,"imags/back.png")

GEOMETRY = "1200x700+160+80"




