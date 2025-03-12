from flask import Flask, render_template, flash, request, session

import mysql.connector
import sys

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/AdminLogin")
def DoctorLogin():
    return render_template('AdminLogin.html')


@app.route("/SellerLogin")
def SellerLogin():
    return render_template('SellerLogin.html')


@app.route("/NewSeller")
def NewSeller():
    return render_template('NewSeller.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/NewProduct")
def NewProduct():
    return render_template('NewProduct.html')


@app.route("/NewService")
def NewService():
    return render_template('NewService.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM manuftb ")
    data1 = cur.fetchall()
    return render_template('AdminHome.html', data1=data1)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            flash("Login successfully")

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM manuftb ")
            data1 = cur.fetchall()
            return render_template('AdminHome.html', data1=data1)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/mlogin", methods=['GET', 'POST'])
def mlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['mname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from manuftb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('SellerLogin.html', data=data)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM manuftb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('SellerHome.html', data=data)


@app.route("/SellerHome")
def SellerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  manuftb where username='" + session['mname'] + "' ")
    data = cur.fetchall()
    return render_template('SellerHome.html', data=data)


@app.route("/newproduct", methods=['GET', 'POST'])
def newproduct():
    if request.method == 'POST':
        pid = request.form['pid']
        pname = request.form['pname']
        ptype = request.form['ptype']
        price = request.form['price']
        qty = request.form['qty']
        mdate = request.form['mdate']

        info = request.form['info']

        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save("static/upload/" + savename)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO  protb VALUES ('','" + pid + "','" + pname + "','" + ptype + "','" + price + "','" + qty
            + "','" + mdate + "','" + info + "','" + savename + "')")
        conn.commit()
        conn.close()

        flash('Product Register successfully')
        return render_template('NewProduct.html')


@app.route("/newservice", methods=['GET', 'POST'])
def newservice():
    if request.method == 'POST':
        pid = request.form['pid']

        ptype = request.form['ptype']
        price = request.form['price']

        info = request.form['info']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO  Servicetb VALUES ('','" + pid + "','" + ptype + "','" + price + "','" + info + "','" +
            session['mname'] + "')")
        conn.commit()
        conn.close()

        flash('Service Register successfully')
        return render_template('NewService.html')


@app.route("/MProductInfo")
def MProductInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  protb  ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Servicetb  ")
    data1 = cur.fetchall()
    return render_template('MProductInfo.html', data=data, data1=data1)

@app.route("/Remove")
def Remove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()
    flash('Product Remove Successfully!')

    return render_template('MProductInfo.html')


@app.route("/dlogin", methods=['GET', 'POST'])
def dlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['dname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from distributortb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('DistributorLogin.html', data=data)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
            cur = conn.cursor()
            cur.execute(
                "SELECT * FROM distributortb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('DistributorHome.html', data=data)


@app.route("/DVerify")
def DVerify():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  protb where Distributor='" + session['dname'] + "' and Supplier='' ")
    data = cur.fetchall()
    return render_template('DVerify.html', data=data)


@app.route("/newman", methods=['GET', 'POST'])
def newman():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO manuftb VALUES ('','" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('  Register Successfully')
        return render_template('SellerLogin.html')


@app.route("/ARemove")
def ARemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('AProductInfo.html', data=data)


@app.route("/AProductInfo")
def AProductInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('AProductInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('User Register successfully')

    return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/Search")
def Search():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()

    return render_template('Search.html', data=data)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ptype = request.form['ptype']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb where  ProductType ='" + ptype + "'")
        data = cur.fetchall()

        return render_template('Search.html', data=data)


@app.route("/Service")
def Service():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Servicetb ")
    data = cur.fetchall()

    return render_template('Service.html', data=data)


@app.route("/ssearch", methods=['GET', 'POST'])
def ssearch():
    if request.method == 'POST':
        ptype = request.form['ptype']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Servicetb where  ServiceType ='" + ptype + "'")
        data = cur.fetchall()
        return render_template('Search.html', data=data)


@app.route("/Book")
def Book():
    id = request.args.get('id')
    session['pid'] = id
    amt = request.args.get('amt')

    return render_template('SBook.html', amt=amt)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where username='" + uname + "'  ")
    data = cur.fetchall()

    return render_template('UserHome.html', data=data)


@app.route("/payment1", methods=['GET', 'POST'])
def payment1():
    if request.method == 'POST':

        uname = session['uname']
        Date =  request.form['date']
        cname = request.form['cname']
        Cardno = request.form['cno']
        Cvno = request.form['cvno']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  *   FROM  Servicetb where id ='" + session['pid'] + "' ")
        data1 = cursor.fetchone()
        if data1:
            sname = data1[1]
            tprice = data1[3]


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Sbooktb VALUES ('','" + uname + "','" + sname + "','" + str(tprice) + "','" + str(
                Date) + "')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
        data2 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  Sbooktb where username='" + uname + "'")
        data3 = cur.fetchall()



    return render_template('BookingInfo.html', data1=data1, data2=data2,data3=data3)


@app.route("/Add")
def Add():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  where id='" + id + "' ")
    data = cur.fetchall()
    return render_template('AddCart.html', data=data)


@app.route("/addcart", methods=['GET', 'POST'])
def addcart():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        pid = session['pid']
        uname = session['uname']
        qty = request.form['qty']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb  where  id='" + pid + "'")
        data = cursor.fetchone()

        if data:
            ProductName = data[2]
            Producttype = data[3]
            price = data[4]
            cQty = data[5]

            Image = data[8]

        else:
            return 'No Record Found!'

        tprice = float(price) * float(qty)

        clqty = float(cQty) - float(qty)

        if clqty < 0:

            flash('Low  Product ')

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM protb  where id='" + pid + "' ")
            data = cur.fetchall()
            return render_template('AddCart.html', data=data)

        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO carttb VALUES ('','" + uname + "','" + ProductName + "','" + Producttype + "','" + str(
                    price) + "','" + str(qty) + "','" + str(tprice) + "','" +
                Image + "','" + date + "','0','')")
            conn.commit()
            conn.close()

            flash('Add To Cart  Successfully')
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM protb  where id='" + pid + "' ")
            data = cur.fetchall()
            return render_template('AddCart.html', data=data)


@app.route("/Cart")
def Cart():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data1 = cursor.fetchone()
    if data1:
        tqty = data1[0]
        tprice = data1[1]
    else:
        return 'No Record Found!'

    return render_template('Cart.html', data=data, tqty=tqty, tprice=tprice)


@app.route("/RemoveCart")
def RemoveCart():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from carttb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product Remove Successfully!')

    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data1 = cursor.fetchone()
    if data1:
        tqty = data1[0]
        tprice = data1[1]

    return render_template('Cart.html', data=data, tqty=tqty, tprice=tprice)


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        uname = session['uname']
        cname = request.form['cname']
        Cardno = request.form['cno']
        Cvno = request.form['cvno']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
        data1 = cursor.fetchone()
        if data1:
            tqty = data1[0]
            tprice = data1[1]

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  count(*) As count  FROM booktb ")
        data = cursor.fetchone()
        if data:
            bookno = data[0]
            print(bookno)

            if bookno == 'Null' or bookno == 0:
                bookno = 1
            else:
                bookno += 1

        else:
            return 'Incorrect username / password !'

        bookno = 'BOOKID' + str(bookno)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "update   carttb set status='1',Bookid='" + bookno + "' where UserName='" + uname + "' and Status='0' ")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO booktb VALUES ('','" + uname + "','" + bookno + "','" + str(tqty) + "','" + str(
                tprice) + "','" + cname + "','" + Cardno + "','" + Cvno + "','" + date + "')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
        data2 = cur.fetchall()

    return render_template('BookingInfo.html', data1=data1, data2=data2)


@app.route("/BookingInfo")
def BookingInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
    data2 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Sbooktb where username='" + uname + "'")
    data3 = cur.fetchall()
    return render_template('BookingInfo.html', data1=data1, data2=data2,data3=data3)


@app.route("/ASalesInf")
def ASalesInf():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where  Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb ")
    data2 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Sbooktb ")
    data3 = cur.fetchall()
    return render_template('ASalesInf.html', data1=data1, data2=data2,data3=data3)


@app.route("/ESalesInfo")
def ESalesInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where  Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb ")
    data2 = cur.fetchall()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='3ecommercepy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Sbooktb ")
    data3 = cur.fetchall()
    return render_template('ESalesInfo.html', data1=data1, data2=data2,data3=data3)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
