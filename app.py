"""
Author: Monday Erirore Eseinone erirore

Purpose: Displaying  project from 09/02/2024.
"""
import sqlite3
from time import strftime
from datetime import datetime

from time import strftime
from datetime import datetime

import os
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import datetime

from flask import Flask, render_template, redirect, request, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename
import os
import re


# import mysql.connector
# from flask_mysqldb import MySQL
# import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = "hello"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK-MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=5)

UPLOAD_FOLDER = './upload'

db = SQLAlchemy(app)
app.app_context().push()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# creating a model
class users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
  

    def __init__(self, name, email):
        self.name = name
        self.email = email

        
# # creating a model
# class students(db.Model):
#     stdtid = db.Column("id", db.Integer, primary_key=True)
#     stdname = db.Column(db.String(100))
#     stdemail = db.Column(db.String(100))

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email


@app.route("/")
def index():
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    return render_template("index.html", display_time=display_time)


@app.route("/it_class")
def it_class():
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    
    return render_template("it_class.html", display_time=display_time)

@app.route("/class1", methods= ["POST"])
def class1():
    title = "Class One"
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    
    project_name = request.form.get("project_name")
    lenght_one = request.form.get("lenght_one")
    width_one = request.form.get("width_one")
    quantity_one = request.form.get("quantity_one")
    
    lenght_two = request.form.get("lenght_two")
    width_two = request.form.get("width_two")
    quantity_two = request.form.get("quantity_two")
    

    # calculating measurement from entries 
    f_measure = float(lenght_one) * float(width_one)
    f_total = float(f_measure) * float(quantity_one)
    
    s_measure =  float(lenght_two) * float(width_two)
    s_total = float(s_measure) * float(quantity_two)
 
    
    # adding all entries total 
    total_sq_area_measurement = f_total + s_total
    display_total_sq_area_measurement = round(total_sq_area_measurement, 1)

    # variable for standard board measurement 
    # standard_board_measurement = 243.84 * 121.92
    standard_board_measurement = 240 * 120
    display_standard_board_measurement = round(standard_board_measurement, 1)
    
    board_used = total_sq_area_measurement / standard_board_measurement
    #  global display_board_used
    display_board_used = round(board_used, 1)
    
    first_lenght = int(lenght_one)
    first_width = int(width_one)
    first_quantity = int(quantity_one)
    second_lenght = int(lenght_two)
    second_width = int(width_two)
    second_quantity = int(quantity_two)
  

 # writing to a text file 
        # Here I added all transaction into text file 
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    dba = open(f"{project_name}.txt", "a")
    dba.write(f" Date: **************{display_time} **************\n ")
    dba.write(f" |*************Cutting list calculation ************|\n ".upper())
    dba.write(f" \n ")
    dba.write(f"   Project Name is **** | {project_name} |**** \n ".upper())
    dba.write("\n")
    
    dba.write(f"  First Lenght: {lenght_one}\n ")
    dba.write(f"  First width:  {width_one}\n")
    dba.write(f"  Quantity of first Ms:  {quantity_one}\n ")
    dba.write("\n")
    dba.write(f"  Second Lenght: {lenght_two}\n ")
    dba.write(f"  Second width:  {width_two}\n")
    dba.write(f"  Quantity of Second Ms :   {quantity_two}\n ")
    dba.write("\n")
    dba.write(f"   Total Number of Board **** | {display_board_used} |**** \n ".upper())
    dba.write("\n")
    
    
    dba = open("wood_cutting.txt", "a")
    dba.write(f" Date: **************{display_time} **************\n ")
    dba.write(f" |*************Cutting list calculation ************|\n ".upper())
    dba.write(f" \n ")
    dba.write(f"   Project Name is **** | {project_name} |**** \n ".upper())
    dba.write("\n")
    
    dba.write(f"  First Lenght: {lenght_one}\n ")
    dba.write(f"  First width:  {width_one}\n")
    dba.write(f"  Quantity of first Ms:  {quantity_one}\n ")
    dba.write("\n")
    dba.write(f"  Second Lenght: {lenght_two}\n ")
    dba.write(f"  Second width:  {width_two}\n")
    dba.write(f"  Quantity of Second Ms :   {quantity_two}\n ")
    dba.write("\n")
    dba.write(f"   Total Number of Board **** | {display_board_used} |**** \n ".upper())
    dba.write("\n")


    # cleint_expencse = float(cleint_tithe) + float(cleint_feeding) + float(cleint_rent) + float(cleint_out) + float(cleint_soft) + float(cleint_others)
    # total_calulation = float(cleint_income) - float(cleint_expencse)
    
    # # calculate percentage of total income variable expenses
    # total_percent_income = float(cleint_income) * 100 / float(cleint_income)
    
    # # calculate percentage of total total expenses
    # expense_amount_percent = float(cleint_expencse) * 100 / float(cleint_income)
    
    # # calculate percentage of savings expenses
    # exp_percent = float(total_calulation) * 100 / float(cleint_income)   # * float(cleint_expencse) 
    
    # expences_percent = f" {exp_percent:.1f} "
    

    # var_goodSavings ="  Great job! your expenses is less than your income today.\
    #     This is quite good for your finance.  Congratulations "

    # var_badSavings = " ho no! This is not very good. Your expenses is way more greater than your income "

    # if float(cleint_expencse) > float(cleint_income):
    #     user_savings = var_badSavings
        

    # else:
    #     user_savings = var_goodSavings

    # # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # #  creating an exel file
    # # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


    # # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # #  creating an exel file
    # # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # return render_template("finance_house.html", cleint_name=cleint_name.upper(),
    #                        cleint_tithe= cleint_tithe,
    #                        cleint_income=cleint_income,cleint_feeding=cleint_feeding,
    #                         cleint_rent=cleint_rent, cleint_out=cleint_out,
    #                             cleint_soft=cleint_soft, cleint_others=cleint_others,
    #                               total_calulation=total_calulation, cleint_expencse=cleint_expencse, user_savings=user_savings, expences_percent=expences_percent,
    #                               total_percent_income=total_percent_income, expense_amount_percent=expense_amount_percent, display_time=display_time ) 

    
    return render_template("class1.html", display_time=display_time, title=title,
                           project_name=project_name,
                           standard_board_measurement=standard_board_measurement,
                           display_board_used=display_board_used,
                           display_total_sq_area_measurement=display_total_sq_area_measurement,
                           first_lenght=first_lenght, first_width=first_width,
                           first_quantity=first_quantity,
                           second_lenght=second_lenght, second_width=second_width,
                           second_quantity=second_quantity
                           )

@app.route("/design")
def design():
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    
    return render_template("design.html", display_time=display_time)
    
# This code will preper a cutting list
@app.route("/furniture", methods= ["POST"])
def furniture():
    title = "furnitrue"
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    
    project_name = request.form.get("project_name")
    design_lenght = request.form.get("design_lenght")
    design_width = request.form.get("design_width")
    design_hight = request.form.get("design_hight")
    
    number_of_partation = request.form.get("number_of_partation")
    number_of_dimacation = request.form.get("number_of_dimacation")
    quantity_doors = request.form.get("quantity_doors") 
    quantity_drawers = request.form.get("quantity_drawers") 
    
    b = number_of_dimacation.isdigit()
    c = float(number_of_partation) + 0
    number_of_partation_c = round(c)
    
 
    # a = 0
    # d = int(a) + int(number_of_dimacation)
    # standard board of mdf in Nigeria cm
    d = int()
    global board_ticknes
    board_ticknes = 1.5875
    
    reduse_from_side = board_ticknes * 2
    h_standing = 2
    down_pannel_width =  9
    all_4_pannel = 4
    standard_board_measurement = 240 * 120
    
    # standing cutting list 
    hight_one = float(design_hight)
    hight_cutting = round(hight_one, 1)
    
    width_one = float(design_width)
    main_cutting_width = round(width_one, 1)
    
    total_hight = f"     {hight_cutting}cm x {main_cutting_width}cm "
    
    # lenght cutting minus the sice stand tickness 
    demacation_cutting_total_before_rounding = float(design_lenght) - reduse_from_side
    round_total = round(demacation_cutting_total_before_rounding, 1)
    demacation_cutting_total = f"     {round_total}cm x {main_cutting_width}cm "
    
    # this will deduct 4 cm of the buttom pannel and 
    # board_ticknes = 1.5875 from the hight of the furniture
    p_hight = hight_cutting - float(down_pannel_width + board_ticknes)
    round_partation = round(p_hight, 1)
    
    partation_hight = f" {round_partation}cm x {main_cutting_width}cm "
    
    
    # Down and top pannel (4 pices )
    down_and_top_pannel = f" {down_pannel_width}cm X {round_total}cm " # round_total is the measurement of the dimacation 
    
    # Door calculation 
    door_cal = float(design_lenght) - 1.5
    door_one_width_c = door_cal / 3
    door_one_width = round(door_one_width_c, 2)
    
    door_one_hight = hight_cutting - 7
     
    door_one = f" {door_one_hight}cm x {door_one_width}cm"
    door_one_quantity = 1
    
    # Door 2 start here 
    door_two_hight = hight_cutting - 48
    round_door_two = round(door_two_hight, 1)
    door_two = f" {round_door_two}cm x {door_one_width}cm"
    door_two_quantity = 2
    
    # ================================
    #   cutting list starts from here 
    # ================================
    standing_pic =  (hight_cutting * main_cutting_width) * 2
    demacation_pic = (round_total * main_cutting_width) * float(number_of_dimacation)
    partation_pic = (round_partation * main_cutting_width) * float(number_of_partation)
    door_one_pic = (door_one_width * door_one_hight) * float(door_one_quantity)
    door_two_pic = (door_one_width * door_two_hight) * float(door_two_quantity)
    down_top_pannel_pic = (down_pannel_width * round_total) * float(all_4_pannel)
    
    # Adding the total area cm of all measure 
    adding_cutting = standing_pic + demacation_pic + partation_pic + door_one_pic + door_two_pic + down_top_pannel_pic
    
    # Dividing the total area with standard Board measuremnet
    # Here is the standard_board_measurement useed for the project:  240 * 120
    board_quantity = (adding_cutting / standard_board_measurement)
    board_value = round(board_quantity, 1)
    
    
     
    return render_template("furniture.html", total_hight=total_hight,
                           demacation_cutting_total=demacation_cutting_total,
                           number_of_dimacation=number_of_dimacation,
                           h_standing=h_standing,
                           project_name=project_name,
                           display_time=display_time,
                           partation_hight=partation_hight,
                           number_of_partation_c=number_of_partation_c,
                           down_and_top_pannel=down_and_top_pannel,
                           all_4_pannel=all_4_pannel, door_one=door_one,
                           door_two=door_two, door_one_quantity=door_one_quantity,
                           door_two_quantity=door_two_quantity, adding_cutting_list=adding_cutting,
                           board_value=board_value)

@app.route("/stools")
def stools():
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    
    return render_template("stools.html", display_time=display_time)

@app.route("/table_display", methods= ["POST"])
def table_display():
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    
    # Tickness of baord 
    board_ticknes = 1.5875
    leg_width = 9
    # This fuction will return the legs cutting size
    def display_stool_top(user_h):
        user_hight = float(user_h)
        w = float(leg_width)
        legString = f" {user_hight} x {w}"
        return legString
    
         # This function  will minus the tickness of the stand by 2 and also 
         # minus the 5 cmm for allowance of both side of the  stool
    def stool_conn_lenght(user_lenght):
          
        l_connection = float(user_lenght) - float(5 + board_ticknes * 4)
        round_conn_lenght = round(l_connection, 1)
        stool_connet = f" {round_conn_lenght}cm x {leg_width}cm "
        return stool_connet
    
             # This function  will minus the tickness of the stand by 2 and also 
         # minus the 5 cmm for allowance of both side of the  stool
    def stool_conn_width(user_width):
        w_connection = float(user_width) - float(5 + board_ticknes * 2)
        round_conn_width = round(w_connection, 1)
        
        stool_connet = f" {round_conn_width}cm x {leg_width}cm "
        return stool_connet
    
    def topLipping_l(user_lenght):
        lipping_width = 6
        a = float(user_lenght) 
        top_lipping = f"  {a}cm x {lipping_width} "
        return top_lipping
    
    
    def topLipping_w(user_width):
        lipping_width = 6
        b = float(user_width) - 6
        top_lipping = f" {b} x {lipping_width}"
        return top_lipping
    
    project_name = request.form.get("project_name")
    design_lenght = request.form.get("table_lenght")
    design_width = request.form.get("table_width")
    design_hight = request.form.get("table_hight")
    
    h = float(design_hight)
    l = float(design_lenght)
    w = float(design_width) 
    
    stool_conn_quantity = 2   
    
    # lenght of tabel or stool top cutting list 
    table_lenght_one = float(design_lenght)
    lenght_round = round(table_lenght_one, 1)
     
    # lenght of tabel or stool top cutting list 
    table_width_one = float(design_width)
    table_main_width = round(table_width_one, 1)
    
    display_table_top = f" {lenght_round}cm x {table_main_width}cm "
    
    #  dislay stool leg 
    dispaly_leg = display_stool_top(h)
    
    # display stool connection 
    display_stool_connection_lenght = stool_conn_lenght(l)
    display_stool_connection_width = stool_conn_width(w)
    
    # Display top liping 
    display_top_lipping_a =  topLipping_l(l)
    display_top_lipping_b =  topLipping_w(w)
    
    
    
    return render_template("table_display.html", display_time=display_time,
                           display_table_top=display_table_top,
                           dispaly_leg=dispaly_leg, project_name=project_name,
                           display_stool_connection_lenght=display_stool_connection_lenght, 
                           display_stool_connection_width=display_stool_connection_width,
                           stool_conn_quantity=stool_conn_quantity,
                           display_top_lipping_a=display_top_lipping_a,
                           display_top_lipping_b=display_top_lipping_b
                           )

@app.route("/ta")
def ta():
    title = "Class One"
    return "<p> ddd <\p> "

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


@app.route("/minor")
def minor():
    return render_template("minor.html")

@app.route("/about")
def about():
                                # time code
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))

    admin = "Admin of this page is [ Monday Eseinone ]"
    ese_pro = ["Website Design", "Dinamic Website", "Web/ Mobile App"]
    return render_template("about.html", adminkk=admin, schedue1=ese_pro, display_time=display_time)


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/class_room", methods=["POST"])
def class_room():
    user_name = request.form.get("user_name")
    user_email = request.form.get("user_email")
    user_phone = request.form.get("user_phone")
    user_file = request.form.get("user_file")
    user_age = request.form.get("user_age")
    
    if user_name == "" or user_age < "18" or user_email =="" or user_phone == "":
        flash("you are not eligible for this programing class room  ")
        return redirect(url_for("minor"))

    elif user_name =="" and user_age > "18":
        flash(" Please type in a valid user name. filled can be empty ")
        return redirect(url_for("minor"))

    elif user_age > "18" and user_name != "" and user_email != "" and user_phone != "":
        flash("You have login succesfull!")
        
  
    
        return render_template("class_room.html", user_name=user_name.upper(), user_email=user_email.lower(), user_phone=user_phone, user_file=user_file, user_age=user_age)
    else:
        flash(" Check your entery and try again ")
        return render_template("contact.html")



  
 # income calculation starts here
@app.route("/income")
def income():
    return render_template("income.html")



@app.route("/add_item", methods= ["POST"])
def add_item():
    # HERE IS MY TIME CALCULATOR
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))


    import time
    import random
    magic_number = random.randint(1, 100)

    count = 0

    while True:

        guess_entery= request.form.get("guess_game")
        count += 1
        return render_template("add_item.html", display_time=display_time)

        if magic_number < guess_entery:
            flash1 = "Gess lower "
            return render_template("add_item.html", flash1=flash1)


        elif magic_number > guess_entery:
            flah2 = " Guess Higer "
            return render_template("add_item.html", flash2=flash2)

        # else:
        #     flash = "You Guessed it "
        #     if magic_number == guess_entery:
        #         print()
        #         print(" would you like to play more? ")


            return render_template("add_item.html", display_time=display_time, flash=flash)


    return render_template("add_item.html", guess_entery=guess_entery, display_time=display_time)




    #     lenght_entery = request.form.get("user_length")
    #     width_entery = request.form.get("user_width")

    #     if lenght_entery.isdigit() and width_entery.isdigit():
    #         break
    #     else:
    #         flash = "Your entry has to be a number"
    #         return render_template("add_item.html", display_time=display_time, flash=flash)

    # area_cal = int(lenght_entery) * int(width_entery)
    # return render_template("add_item.html", area_cal=area_cal, display_time=display_time, menu_item=menu_item)


@app.route("/finance_house", methods= ["POST"])
def finance_house():
    # ese_time = datetime.datetime.now()
    # display_time = (ese_time.strftime(f"%A"  "%X" "" "%Y"  "%p"))
   # %d-%m-%Y------- %H:%M:%S %p
    date2 = datetime.datetime.now().strftime(f"%A - %d-%m-%Y -- TIME -- %H:%M:%S %p")  # Get current date
    display_time = date2

    cleint_name = request.form.get("cleint_name")
    cleint_tithe = request.form.get("cleint_tithe")
    cleint_income = request.form.get("cleint_income")
    cleint_feeding = request.form.get("cleint_feeding")
    cleint_rent = request.form.get("cleint_rent")
    cleint_out = request.form.get("cleint_out")
    cleint_soft = request.form.get("cleint_soft")
    cleint_others = request.form.get("cleint_others")

    cleint_expencse = float(cleint_tithe) + float(cleint_feeding) + float(cleint_rent) + float(cleint_out) + float(cleint_soft) + float(cleint_others)
    total_calulation = float(cleint_income) - float(cleint_expencse)
    
    # calculate percentage of total income variable expenses
    total_percent_income = float(cleint_income) * 100 / float(cleint_income)
    
    # calculate percentage of total total expenses
    expense_amount_percent = float(cleint_expencse) * 100 / float(cleint_income)
    
    # calculate percentage of savings expenses
    exp_percent = float(total_calulation) * 100 / float(cleint_income)   # * float(cleint_expencse) 
    
    expences_percent = f" {exp_percent:.1f} "
    

    var_goodSavings ="  Great job! your expenses is less than your income today.\
        This is quite good for your finance.  Congratulations "

    var_badSavings = " ho no! This is not very good. Your expenses is way more greater than your income "

    if float(cleint_expencse) > float(cleint_income):
        user_savings = var_badSavings
        

    else:
        user_savings = var_goodSavings

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #  creating an exel file
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #  creating an exel file
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    return render_template("finance_house.html", cleint_name=cleint_name.upper(),
                           cleint_tithe= cleint_tithe,
                           cleint_income=cleint_income,cleint_feeding=cleint_feeding,
                            cleint_rent=cleint_rent, cleint_out=cleint_out,
                                cleint_soft=cleint_soft, cleint_others=cleint_others,
                                  total_calulation=total_calulation, cleint_expencse=cleint_expencse, user_savings=user_savings, expences_percent=expences_percent,
                                  total_percent_income=total_percent_income, expense_amount_percent=expense_amount_percent, display_time=display_time ) 

    user_client = cleint_nam(cleint_nam, " ")
    db.session.add(cleint_nam)
    db.session.commit()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# app.config['MYSQL'] = "localhost"
# app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = "monday12ESE"
# app.config['MYSQL_DB'] = "esedb1"

# mysql = MySQL(app)


#  admin     
@app.route("/admin", methods=["POST", "GET"])
def admin():
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    
    if request.method == "POST":
        adname = request.form["admin_name"]
        ademail = request.form["admin_email"]
        adpassw = request.form["admin_passw"]
      
                
        # #  Reading from my data base 
        # conn = sqlite3.connect('newusers.db')
        # c = conn.cursor()
        
        # query = "SELECT uname, upassword, uemail FROM adminone WHERE uname='"+adname+"' and upassword='"+adpassw+"' and uemail='"+ademail+"' "  
        # c.execute(query)
        
        # results = c.fetchall()
        
        # if len(results) == 0 or adname =="" or adpassw =="" or ademail =="":
        #     flash("Sorry Incorrect Credential provided")
        #     return render_template('admin.html')
        # else:
        #     return redirect(url_for("alluser"))
            
    return render_template('admin.html')

################################################################################
#  Sing In    
@app.route("/signin", methods=["POST", "GET"])
def signin():
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))
    
    if request.method == "POST":
        sssemail = request.form["us_email"]
        sssname = request.form["us_name"]
                
        #  Reading from my data base 
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        query = "SELECT susername, spassword FROM students1 WHERE susername='"+sssname+"' and spassword='"+sssemail+"'"  
        c.execute(query)
        
        results = c.fetchall()
        
        if len(results) == 0 or sssemail =="" or sssname =="":
            flash("Sorry Incorrect Credential provided")
            return render_template('signin.html')
        else:
            return redirect(url_for("class1"))
            
    return render_template('signin.html')

  
#  Sing up    
@app.route("/signup", methods=["POST", "GET"])
def signup():
    
    ese_time = datetime.datetime.now()
    display_time = (ese_time.strftime("%A" "%X"))

    if request.method == "POST" and 'username_s' in request.form and 'useremail_s' in request.form:
   # if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
    
            # collect names and email from users 
        stdname = request.form["username_s"]
        stdemail = request.form["useremail_s"]
        
        #  Adding new register member to a database 13-04-2024
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        # check if username allready exist 
              
        query = "SELECT * FROM students1 WHERE spassword='"+stdemail+"'"  
        c.execute(query)
        account = c.fetchone()
        
        if account:
            flash("Account already exists !")
            
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', stdemail):
            flash("Invalid email address ! !!")
        # elif not userName or not password or not stdemail:
        #     mesage = 'Please fill out the form !'
        else:
        
            
            c.execute("INSERT INTO students1 (susername, spassword, sdate) VALUES (?, ?, ?)", (stdname, stdemail, display_time))

            conn.commit()
            conn.close()
            
        if stdname =="" and stdemail =="":
            flash("Invalid entry, try again with a proper emial ") 
            return render_template("signup.html")
            
            
        else:
            flash("Account created sucessfuly")  
            return redirect(url_for("signin"))

    return render_template("signup.html")    
    
    # ese_time = datetime.datetime.now()
    # display_time = (ese_time.strftime("%A" "%X"))
    
    # if request.method == "POST":
    #     try:
        
    #             # collect names and email from users 
    #         stdname = request.form["username_s"]
    #         stdemail = request.form["useremail_s"]
            
    #         #  Adding new register member to a database 13-04-2024
    #         conn = sqlite3.connect('newusers.db')
    #         c = conn.cursor()
    #         c.execute("INSERT INTO students1 (susername, spassword, sdate) VALUES (?, ?, ?)", (stdname, stdemail, display_time))
        
    #         conn.commit()
    #         conn.close()
            
    #         if stdname =="" and stdemail =="":
    #             flash("Invalid entry, try again with a proper emial ") 
    #             return render_template("signup.html")
            
          
    #         else:
    #             flash("Account created sucessfuly")  
    #             return redirect(url_for("signin"))
            
            
    #     except Exception as e:
    #         flash(" user allready exist, Try a diffrent email or move to the login page")
    #       #  ("Error", str(e))
    # else:
    #     flash(" user allready exist, Try a diffrent email or move to the login page")
    #    # ("Error", "Please fill in the entry box to add data")  
        
    # return render_template("signup.html")      
#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


@app.route("/alluser")
def alluser():

  #  Reading from my data base 
    conn = sqlite3.connect('newusers.db')
    c = conn.cursor()
    
    query = "SELECT * FROM students1"  
    c.execute(query)
    
    alluser = c.fetchall()

    # for row in alluser:
    #     print(row)
        
        # userDetails = row
    userDetails = alluser
  
        
    return render_template("alluser.html", userDetails=userDetails)   
    
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        
        session.permanent = True
        user = request.form['username']
        useremail = request.form["useremail"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
            print(user)


        else:
            usr = users(user, " ")
            db.session.add(usr)
            db.session.commit()

        flash(" Login succesfull!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Allready Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    
    button_display = "TUTORIALS"
   
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            # this will change the user email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash(" Email was saved!")
            
           


        else:
            if "email" in session:
                email = session["email"]
               
               
                
        return render_template("user.html", email=email, button_display=button_display)
    else:
        flash(" You are not Logged In! ")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():

    # here i flash the logout message
    flash(" you have been logged out! ", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return path
        return render_template("upload_file.html")


        return 'ok'
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    <img src="{{ file1 }}" alt="User Image">
    '''



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

