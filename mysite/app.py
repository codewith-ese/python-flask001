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


@app.route("/class1")
def class1():
    title = "Class One"
    return render_template("class1.html", title=title)

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
