from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL 
 
 
app = Flask(__name__)
 

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'turan2003'
app.config['MYSQL_DB'] = 's.o.s.'
 
app.secret_key = 'super secret key'

mysql = MySQL(app)


@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/donation')
def donation():
    return render_template('donation.html')


@app.route('/donation/donator')
def donator():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM donator')
    donators =  cursor.fetchall()
    return render_template('donator.html', donators=donators)

@app.route('/donation/donator/delete/<int:id>', methods=['POST'])
def delete_donator(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('DELETE FROM donator WHERE DonatorID=%s', (id,))
    mysql.connection.commit()
    return redirect('/donation/donator')

@app.route('/donation/donator/create', methods=['POST'])
def create_donator():
    id = request.form['id']
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('INSERT INTO donator VALUES (%s, %s, %s, %s)', (id, name, surname, phone, ))
    mysql.connection.commit()
    return redirect('/donation/donator')

@app.route('/donation/donator/<int:id>', methods=['POST'])
def edit_donator(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM donator')
    donators =  cursor.fetchall()

    return render_template('donator.html', donators=donators, id=id)

@app.route('/donation/donator/update/<int:id>', methods=['POST'])
def update_donator(id):
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('UPDATE donator SET Name=%s, Surname=%s, Phone=%s WHERE DonatorID=%s', (name, surname, phone, id, ))
    mysql.connection.commit()
    return redirect('/donation/donator')

@app.route('/donation/donation')
def donationinfo():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM donation LEFT OUTER JOIN donation_has_items as d ON d.donation_donationid=donation.donationid LEFT OUTER JOIN items ON d.items_itemid=items.itemid LEFT OUTER JOIN donation_has_currency as dc ON dc.donation_donationid=donation.donationid LEFT OUTER JOIN currency ON currency.currencytype=dc.currency_currencytype')
    donations =  cursor.fetchall()
    return render_template('donationinfo.html', donations=donations)

@app.route('/donation/donation/delete/<int:id>', methods=['POST'])
def delete_donation(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('DELETE donation, d, dc, items, currency FROM donation LEFT OUTER JOIN donation_has_items as d ON d.donation_donationid=donation.donationid LEFT OUTER JOIN items ON d.items_itemid=items.itemid LEFT OUTER JOIN donation_has_currency as dc ON dc.donation_donationid=donation.donationid LEFT OUTER JOIN currency ON currency.currencytype=dc.currency_currencytype WHERE donation.donationid=%s', (id,))
    mysql.connection.commit()
    return redirect('/donation/donation')

@app.route('/donation/donation/create', methods=['POST'])
def create_donation():
    id = request.form['id']
    time = request.form['time']
    deliverytime = request.form['deliverytime']
    requestid = request.form['requestid']
    donatorid = request.form['donatorid']
    itemid = request.form['itemid']
    itemcategory = request.form['itemcategory']
    quantity = request.form['quantity']
    currency = request.form['currency']
    amount = request.form['amount']
    exchange = request.form['exchange']
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('INSERT INTO donation VALUES (%s, %s, %s, %s, %s, %s)', (id, time, deliverytime, requestid, donatorid, requestid ))
    if itemid != '' and itemid != 'None':
        cursor.execute('INSERT INTO donation_has_items VALUES (%s, %s, %s)', (id, itemid, quantity))
        cursor.execute('INSERT INTO items VALUES (%s, %s, %s)', (itemid, itemcategory, quantity))
    if currency != '' and currency != 'None':
        cursor.execute('INSERT INTO donation_has_currency VALUES (%s, %s, %s)', (id, currency, amount))
        cursor.execute('INSERT INTO currency VALUES (%s, %s)', (currency, exchange))
    mysql.connection.commit()
    return redirect('/donation/donation')

@app.route('/donation/donation/<int:donationid>/<int:itemid>/<string:currency>', methods=['POST'])
def edit_donation(donationid, itemid, currency):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM donation LEFT OUTER JOIN donation_has_items as d ON d.donation_donationid=donation.donationid LEFT OUTER JOIN items ON d.items_itemid=items.itemid LEFT OUTER JOIN donation_has_currency as dc ON dc.donation_donationid=donation.donationid LEFT OUTER JOIN currency ON currency.currencytype=dc.currency_currencytype')
    donations =  cursor.fetchall()
    return render_template('donationinfo.html', donations=donations, donationid=donationid, itemid=itemid, currency=currency)

@app.route('/donation/donation/update/<int:donationid>/<int:itemid>', methods=['POST'])
def update_donation(donationid, itemid):
    time = request.form['time']
    deliverytime = request.form['deliverytime']
    requestid = request.form['requestid']
    donatorid = request.form['donatorid']
    itemcategory = request.form['itemcategory']
    quantity = request.form['quantity']
    currency = request.form['currency']
    amount = request.form['amount']
    exchange = request.form['exchange']
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('UPDATE donation SET DonationTime=%s, DonationDeliveryTime=%s, RequestID=%s, Donator_DonatorID=%s, Request_RequestID=%s WHERE DonationID=%s', (time, deliverytime, requestid, donatorid, requestid, donationid, ))
    if itemid != '' and itemid != 'None':
        cursor.execute('UPDATE donation_has_items SET Quantity=%s WHERE donation_donationid=%s AND items_itemid=%s', (quantity, donationid, itemid, ))
        cursor.execute('UPDATE items SET ItemCategory=%s, Amount=%s WHERE itemid=%s', (itemcategory, quantity, itemid ))
    if currency != '' and currency != 'None':
        cursor.execute('UPDATE donation_has_currency SET Currency_CurrencyType=%s, Amount=%s WHERE donation_donationid=%s', (currency, amount, donationid, ))
        cursor.execute('UPDATE currency SET ExchangeRate=%s WHERE currencytype=%s', (exchange, currency))
    mysql.connection.commit()
    return redirect('/donation/donation')

@app.route('/logistics')
def logistics():
    return render_template('logistics.html')

@app.route('/logistics/insource')
def insourcing():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM request_vehicle_courrier_assignment r INNER JOIN courier ON r.courier_courierid=courier.courierid INNER JOIN vehicle ON r.vehicle_vehicleid=vehicle.vehicleid')
    insourcings =  cursor.fetchall()
    return render_template('insource.html', insourcings=insourcings)

@app.route('/logistics/insource/delete/<int:vehicleid>/<int:courierid>', methods=['POST'])
def delete_insourcing(vehicleid, courierid):
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('DELETE r, vehicle, courier FROM request_vehicle_courrier_assignment r INNER JOIN vehicle ON r.vehicle_vehicleid=vehicle.vehicleid INNER JOIN courier ON r.courier_courierid=courier.courierid WHERE vehicle.vehicleid=%s AND courier.courierid=%s', (vehicleid, courierid))
    mysql.connection.commit()
    return redirect('/logistics/insource')

@app.route('/logistics/insource/create', methods=['POST'])
def create_insourcing():
    requestid = request.form['requestid']
    deliverytime = request.form['deliverytime']
    courierid = request.form['courierid']
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    licensetype = request.form['licencetype']
    vehicleid = request.form['vehicleid']
    vehicletype = request.form['vehicletype']
    capacity = request.form['capacity']
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('INSERT INTO request_vehicle_courrier_assignment VALUES (%s, %s, %s, %s)', (requestid, courierid, vehicleid, deliverytime))
    cursor.execute('INSERT INTO courier VALUES (%s, %s, %s, %s, %s)', (courierid, name, surname, phone, licensetype))
    cursor.execute('INSERT INTO vehicle VALUES (%s, %s, %s)', (vehicleid, vehicletype, capacity))
    mysql.connection.commit()
    return redirect('/logistics/insource')

@app.route('/logistics/insource/<int:vehicleid>/<int:courierid>', methods=['POST'])
def edit_insourcing(vehicleid, courierid):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM request_vehicle_courrier_assignment r INNER JOIN courier ON r.courier_courierid=courier.courierid INNER JOIN vehicle ON r.vehicle_vehicleid=vehicle.vehicleid')
    insourcings =  cursor.fetchall()
    return render_template('insource.html', insourcings=insourcings, vehicleid=vehicleid, courierid=courierid)

@app.route('/logistics/insource/update/<int:vehicleid>/<int:courierid>', methods=['POST'])
def update_insourcing(vehicleid, courierid):
    requestid = request.form['requestid']
    deliverytime = request.form['deliverytime']
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    licensetype = request.form['licencetype']
    vehicletype = request.form['vehicletype']
    capacity = request.form['capacity']
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('UPDATE request_vehicle_courrier_assignment SET Request_RequestID=%s, DeliveryTime=%s WHERE courier_courierid=%s AND vehicle_vehicleid=%s', (requestid, deliverytime, courierid, vehicleid, ))
    cursor.execute('UPDATE vehicle SET VehicleType=%s, Capacity=%s WHERE vehicleid=%s', (vehicletype, capacity, vehicleid, ))
    cursor.execute('UPDATE courier SET Name=%s, Surname=%s, Phone=%s, LicenseType=%s WHERE courierid=%s', (name, surname, phone, licensetype, courierid))
    mysql.connection.commit()
    return redirect('/logistics/insource')

@app.route('/logistics/outsource')
def outsourcing():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM LogisticsCompany_has_District h INNER JOIN District ON h.District_DistrictID=District.DistrictID INNER JOIN LogisticsCompany l ON h.LogisticsCompany_CompanyID=l.CompanyID INNER JOIN Request_has_LogisticsCompany r ON l.CompanyID=r.LogisticsCompany_CompanyID')
    outsourcings =  cursor.fetchall()
    return render_template('outsource.html', outsourcings=outsourcings)

@app.route('/logistics/outsource/delete/<int:districtid>/<int:companyid>', methods=['POST'])
def delete_outsourcing(districtid, companyid):
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('DELETE h, l, r, district FROM LogisticsCompany_has_District h INNER JOIN District ON h.District_DistrictID=District.DistrictID INNER JOIN LogisticsCompany l ON h.LogisticsCompany_CompanyID=l.CompanyID INNER JOIN Request_has_LogisticsCompany r ON l.CompanyID=r.LogisticsCompany_CompanyID WHERE district.districtid=%s AND l.companyid=%s', (districtid, companyid))
    mysql.connection.commit()
    return redirect('/logistics/outsource')

@app.route('/logistics/outsource/create', methods=['POST'])
def create_outsourcing():
    districtid = request.form['districtid']
    districtname = request.form['districtname']
    coordination = request.form['coordination']
    population = request.form['population']
    companyid = request.form['companyid']
    companyname = request.form['companyname']
    phone = request.form['phone']
    cost = request.form['cost']
    requestid = request.form['requestid']
    deliverytime = request.form['deliverytime']
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    if districtid != '' and districtid != 'None':
        cursor.execute('INSERT INTO district VALUES (%s, %s, %s, %s)', (districtid, districtname, coordination, population))
        cursor.execute('INSERT INTO logisticscompany_has_district VALUES (%s, %s, %s)', (companyid, districtid, cost))
    cursor.execute('INSERT INTO logisticscompany VALUES (%s, %s, %s)', (companyid, companyname, phone))
    cursor.execute('INSERT INTO request_has_logisticscompany VALUES (%s, %s, %s)', (requestid, companyid, deliverytime))
    mysql.connection.commit()
    return redirect('/logistics/outsource')

@app.route('/logistics/outsource/<int:districtid>/<int:companyid>', methods=['POST'])
def edit_outsourcing(districtid, companyid):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM LogisticsCompany_has_District h INNER JOIN District ON h.District_DistrictID=District.DistrictID INNER JOIN LogisticsCompany l ON h.LogisticsCompany_CompanyID=l.CompanyID INNER JOIN Request_has_LogisticsCompany r ON l.CompanyID=r.LogisticsCompany_CompanyID')
    outsourcings =  cursor.fetchall()
    return render_template('outsource.html', outsourcings=outsourcings, districtid=districtid, companyid=companyid)

@app.route('/logistics/outsource/update/<int:districtid>/<int:companyid>', methods=['POST'])
def update_outsourcing(districtid, companyid):
    districtname = request.form['districtname']
    coordination = request.form['coordination']
    population = request.form['population']
    companyname = request.form['companyname']
    phone = request.form['phone']
    cost = request.form['cost']
    requestid = request.form['requestid']
    deliverytime = request.form['deliverytime']
    cursor = mysql.connection.cursor()
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute('UPDATE district SET districtname=%s, coordination=%s, population=%s WHERE districtid=%s', (districtname, coordination, population, districtid, ))
    cursor.execute('UPDATE logisticscompany_has_district SET costofoutsource=%s WHERE logisticscompany_companyid=%s AND district_districtid=%s', (cost, companyid, districtid ))
    cursor.execute('UPDATE logisticscompany SET companyname=%s, phone=%s WHERE companyid=%s', (companyname, phone, companyid ))
    cursor.execute('UPDATE request_has_logisticscompany SET request_requestid=%s, deliverytime=%s WHERE logisticscompany_companyid=%s', (requestid, deliverytime, companyid))
    mysql.connection.commit()
    return redirect('/logistics/outsource')


if __name__ == "__name__":
    app.run()

