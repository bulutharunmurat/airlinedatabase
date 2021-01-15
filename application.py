import mysql.connector
import csv
import os
import pandas

connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    database = "AirlineDatabase"
    )


cursor = connection.cursor()


#   INSERTING NEW ROW TO DATABASE

request = int(input("""Which command do you want to do? 

1.Inserting new data to database
2.Deleting data from database
3.Sending Query to database \n"""))

if request == 1:
    
    table = input("""Which table that you wanna insert data?
    airline
    airplane
    arrival_airport
    bag
    captain
    departure_airport
    flight
    passenger
    payment
    ticket
    ticket_flight 
    :""")
    values = str(tuple(input("Please enter values seperated by space :").split()))
 
    sql = "INSERT INTO " + table + " VALUES " + values 
    cursor.execute(sql)

#   DELETING ROW FROM DATABASE

elif request == 2:

    table = input("""Which table that you wanna delete data? 
    airline
    airplane
    arrival_airport
    bag
    captain
    departure_airport
    flight
    passenger
    payment
    ticket
    ticket_flight 
    :""")
    attibute = input("Please enter Table's attribute:")
    value = input("Please Enter attribute's values:")
    if type(value) == str:
        sql = " DELETE FROM " + table + " WHERE " + table + "." + attibute + " = " + '"' + value + '"'
    else:
        sql = " DELETE FROM " + table + " WHERE " + table + "." + attibute + " = " + value

    cursor.execute(sql)

#   SELECTING AND FILTERING FROM DATABASE, result would be written to excel file in this directory

elif request == 3 :

    query = input("Please enter the query that you wanna send to Airline Database:")

    cursor.execute(query)

    myresult = cursor.fetchall()

    with open("database.csv","a",newline="") as myfile:
        csvfile = csv.writer(myfile, delimiter=";")
        for tup in myresult:
            csvfile.writerow(tup)
            print(tup)
        
    df = pandas.DataFrame(myresult)
    print(df)