from flask import Flask, request, redirect, render_template, url_for, flash
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'prop@@'


@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("properties.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from property_listing")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


# CRUD Functionality on properties


@app.route("/add_property", methods=['POST', 'GET'])
def add_property():
    if request.method == 'POST':
        property_address = request.form['property_address']
        listing_price = request.form['listing_price']
        con = sql.connect("properties.db")
        cur = con.cursor()
        cur.execute("insert into property_listing(property_address,listing_price) "
                    "values (?,?)", (property_address, listing_price))
        con.commit()
        flash('Property Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_property.html")


@app.route("/edit_property/<string:property_id>", methods=['POST', 'GET'])
def edit_property(property_id):
    if request.method == 'POST':
        property_address = request.form['property_address']
        listing_price = request.form['listing_price']
        con = sql.connect("properties.db")
        cur = con.cursor()
        cur.execute("update property_listing "
                    "set property_address=?,listing_price=?"
                    "where id=?", (property_address, listing_price, property_id))
        con.commit()
        flash('Property Updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect("properties.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from property_listing where id=?", (property_id,))
    data = cur.fetchone()
    return render_template("edit_property.html", datas=data)


@app.route("/delete_property/<string:property_id>", methods=['GET'])
def delete_property(property_id):
    con = sql.connect("properties.db")
    cur = con.cursor()
    cur.execute("delete from property_listing where id=?", (property_id,))
    con.commit()
    flash('Property Deleted', 'warning')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
