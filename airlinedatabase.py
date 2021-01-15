import mysql.connector
import csv
import os

connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    database = "AirlineDatabase"
    )


cursor = connection.cursor()

# cursor.execute("CREATE DATABASE AirlineDatabase")

Q1 = """CREATE TABLE Captain (
    Captain_Certification_Number int PRIMARY KEY NOT NULL, 
    Captain_Name VARCHAR(40), 
    Captain_Surname VARCHAR(40), 
    Captain_Age smallint,
    Captain_Flight_Hour_Experience float)
    """

Q2 = """CREATE TABLE Arrival_Airport (
    Arrival_Airport VARCHAR(10) PRIMARY KEY NOT NULL, 
    Arrival_Airport_Country VARCHAR(50), 
    Arrival_Airport_Total_Passengers int, 
    Arrival_Airport_Elevation_feet float)
    """

Q3 = """CREATE TABLE Departure_Airport (
    Departure_Airport VARCHAR(10) PRIMARY KEY NOT NULL, 
    Departure_Airport_Country VARCHAR(50), 
    Departure_Airport_Total_Passengers int, 
    Departure_Airport_Elevation_feet float)
    """

Q4 = """CREATE TABLE Passenger (
    Passenger_Passport_Number int PRIMARY KEY NOT NULL,  
    Passenger_Name VARCHAR(40), 
    Passenger_Surname VARCHAR(40), 
    Passenger_Age smallint UNSIGNED, 
    Passenger_Gender VARCHAR(10),
    Passenger_Nationality VARCHAR(30))
    """

Q5 = """CREATE TABLE Airplane (
    Airplane_Model VARCHAR(40) PRIMARY KEY NOT NULL, 
    Airplane_Manufacturer VARCHAR(50), 
    Active_Number_of_Airplane_Model int)
    """

Q6 = """CREATE TABLE Bag (
    Bag_ID int PRIMARY KEY NOT NULL,
    Bag_Weight float)
    """

Q7 = """CREATE TABLE Payment (
    Payment_ID int PRIMARY KEY NOT NULL, 
    Payment_Type VARCHAR(20),
    Payment_Date DATETIME,
    Payment_Amount float)
    """

Q8 = """CREATE TABLE Airline (
    Airline_Company_Name VARCHAR(30) PRIMARY KEY NOT NULL, 
    Airline_Company_Total_Passenger int,
    Airline_Company_Country VARCHAR(30))
    """

Q9 = """CREATE TABLE Flight (
    Flight_Number VARCHAR(10) PRIMARY KEY NOT NULL, 
    Captain_Certification_Number int, 
    FOREIGN KEY (Captain_Certification_Number) REFERENCES Captain (Captain_Certification_Number),  
    Airline_Company_Name VARCHAR(30), 
    FOREIGN KEY (Airline_Company_Name) REFERENCES Airline (Airline_Company_Name), 
    Airplane_Model VARCHAR(50), 
    FOREIGN KEY (Airplane_Model) REFERENCES Airplane (Airplane_Model), 
    Departure_Airport VARCHAR(50), 
    FOREIGN KEY (Departure_Airport) REFERENCES Departure_Airport (Departure_Airport),
    Arrival_Airport VARCHAR(50),
    FOREIGN KEY (Arrival_Airport) REFERENCES Arrival_Airport (Arrival_Airport),
    Departure_Date_Time DATETIME,
    Arrival_Date_Time DATETIME)
    """

Q10 = """CREATE TABLE Ticket_Flight ( 
    Passenger_Passport_Number int ,
    Flight_Number VARCHAR(10), 
    Ticket_ID int,
    PRIMARY KEY (Passenger_Passport_Number,Flight_Number),
    FOREIGN KEY (Ticket_ID) REFERENCES Ticket (Ticket_ID),
    FOREIGN KEY (Flight_Number) REFERENCES Flight (Flight_Number),
    FOREIGN KEY (Passenger_Passport_Number) REFERENCES Passenger (Passenger_Passport_Number))
    """
Q11 = """CREATE TABLE Ticket (
    Ticket_ID int PRIMARY KEY NOT NULL, 
    Payment_ID int,
    FOREIGN KEY (Payment_ID) REFERENCES Payment (Payment_ID),
    Flight_Class VARCHAR(20),
    Passenger_Seat VARCHAR(10),
    Bag_ID int,
    FOREIGN KEY (Bag_ID) REFERENCES Bag (Bag_ID))
    """
cursor.execute(Q1)
cursor.execute(Q2)
cursor.execute(Q3)
cursor.execute(Q4)
cursor.execute(Q5)
cursor.execute(Q6)
cursor.execute(Q7)
cursor.execute(Q8)
cursor.execute(Q9)
cursor.execute(Q10)
cursor.execute(Q11)

Q_Captain = """INSERT INTO Captain(
    Captain_Certification_Number, 
    Captain_Name, Captain_Surname, 
    Captain_Age, 
    Captain_Flight_Hour_Experience) 
    VALUES (%s,%s,%s,%s,%s)"""

Q_Flight = """INSERT INTO Flight(
    Flight_Number, 
    Captain_Certification_Number, 
    Airline_Company_ID, 
    Airplane_Model, 
    Departure_Airport, 
    Arrival_Airport,
    Departure_Date_Time,
    Arrival_Date_Time) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

Q_Departure_Airport = """INSERT INTO Departure_Airport(
    Departure_Airport, 
    Departure_Country, 
    Departure_Total_Passengers, 
    Departure_Elevation) 
    VALUES (%s,%s,%s,%s)"""

Q_Airline = """INSERT INTO Airline(
    Airline_Company_Name, 
    Airline_Company_Total_Passenger, 
    Airline_Company_Country) 
    VALUES (%s,%s,%s)"""

Q_Passenger = """INSERT INTO Passenger(
    Passenger_Passport_Number, 
    Passenger_Name, 
    Passenger_Surname, 
    Passenger_Age, 
    Passenger_Gender, 
    Passenger_Nationality) 
    VALUES (%s,%s,%s,%s,%s,%s)"""

Q_Airplane = """INSERT INTO Airplane(
    Airplane_Model,  
    Airplane_Manufacturer, 
    Active_Number_of_Airplane_Model) 
    VALUES (%s,%s,%s)"""

Q_Arrival_Airport = """INSERT INTO Arrival_Airport(
    Arrival_Airport, 
    Arrival_Airport_Country, 
    Arrival_Airport_Total_Passengers, 
    Arrival_Airport_Elevation_feet) 
    VALUES (%s,%s,%s,%s)"""

Q_Departure_Airport = """INSERT INTO Departure_Airport(
    Departure_Airport, 
    Departure_Airport_Country, 
    Departure_Airport_Total_Passengers, 
    Departure_Airport_Elevation_feet) 
    VALUES (%s,%s,%s,%s)"""

Q_Flight = """INSERT INTO Flight(
    Flight_Number, 
    Captain_Certification_Number, 
    Airline_Company_Name, 
    Airplane_Model, 
    Departure_Airport, 
    Arrival_Airport, 
    Departure_Date_Time, 
    Arrival_Date_Time) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

Q_Payment= """INSERT INTO Payment(
    Payment_ID, 
    Payment_Type, 
    Payment_Date, 
    Payment_Amount) 
    VALUES (%s,%s,%s,%s)"""

Q_BAG= """INSERT INTO Bag(
    Bag_ID, 
    Bag_Weight) 
    VALUES (%s,%s)"""

Q_Ticket= """INSERT INTO Ticket(
    Ticket_ID, 
    Payment_ID, 
    Flight_Class, 
    Passenger_Seat, 
    Bag_ID) 
    VALUES (%s,%s,%s,%s,%s)"""

Q_Ticket_Flight = """INSERT INTO Ticket_Flight(
    Ticket_ID, 
    Passenger_Passport_Number, 
    Flight_Number) VALUES (%s,%s,%s)"""

cursor.execute(Q_Ticket_Flight,(212331, 112023,"RA2684"))
cursor.execute(Q_Ticket_Flight,(421422, 552231,"RA2684"))
cursor.execute(Q_Ticket_Flight,(124114, 334233,"RA2684"))
cursor.execute(Q_Ticket_Flight,(122538, 523498,"CA1002"))
cursor.execute(Q_Ticket_Flight,(135983, 716554,"CA1002"))
cursor.execute(Q_Ticket_Flight,(968325, 413213,"THY4526"))
cursor.execute(Q_Ticket_Flight,(906345, 344531,"THY4526"))
cursor.execute(Q_Ticket_Flight,(102358, 433318,"THY4526"))
cursor.execute(Q_Ticket_Flight,(100235, 221319,"LF5202"))
cursor.execute(Q_Ticket_Flight,(869543, 278633,"LF5202"))
cursor.execute(Q_Ticket_Flight,(996300, 721328,"LF5202"))
cursor.execute(Q_Ticket_Flight,(963245, 588138,"LF5202"))
cursor.execute(Q_Ticket_Flight,(420036, 213219,"AA9602"))
cursor.execute(Q_Ticket_Flight,(364205, 213513,"AA9602"))
cursor.execute(Q_Ticket_Flight,(310025, 987946,"AA9602"))
cursor.execute(Q_Ticket_Flight,(355369, 321569,"AA9602"))
cursor.execute(Q_Ticket_Flight,(875589, 213218,"ER7752"))
cursor.execute(Q_Ticket_Flight,(100236, 823126,"ER7752"))
cursor.execute(Q_Ticket_Flight,(200157, 500025,"ER7752"))
cursor.execute(Q_Ticket_Flight,(986534, 528558,"ER7752"))

cursor.execute(Q_Ticket,(212331, 144115,"First Class","B12",1))
cursor.execute(Q_Ticket,(421422, 245313,"First Class","C21",2))
cursor.execute(Q_Ticket,(124114, 525113,"Economy Class","A11",3))
cursor.execute(Q_Ticket,(122538, 235213,"Economy Class","D1",4))
cursor.execute(Q_Ticket,(135983, 122122,"Economy Class","F3",5))
cursor.execute(Q_Ticket,(968325, 100102,"First Class","A24",6))
cursor.execute(Q_Ticket,(906345, 145325,"Business Class","E4",7))
cursor.execute(Q_Ticket,(102358, 978569,"Economy Class","A1",8))
cursor.execute(Q_Ticket,(100235, 231283,"First Class","D24",9))
cursor.execute(Q_Ticket,(869543, 789238,"Economy Class","B18",10))
cursor.execute(Q_Ticket,(996300, 245435,"First Class","D3",11))
cursor.execute(Q_Ticket,(963245, 568478,"Business Class","E18",12))
cursor.execute(Q_Ticket,(420036, 234213,"Economy Class","A21",13))
cursor.execute(Q_Ticket,(364205, 235613,"Economy Class","D22",14))
cursor.execute(Q_Ticket,(310025, 123122,"Business Class","B4",15))
cursor.execute(Q_Ticket,(355369, 125402,"Economy Class","A15",16))
cursor.execute(Q_Ticket,(875589, 134525,"Economy Class","A7",17))
cursor.execute(Q_Ticket,(100236, 978539,"Economy Class","D12",18))
cursor.execute(Q_Ticket,(200157, 231243,"Economy Class","D8",19))
cursor.execute(Q_Ticket,(986534, 713414,"Economy Class","F9",20))

cursor.execute(Q_BAG,(1,42))
cursor.execute(Q_BAG,(2,22))
cursor.execute(Q_BAG,(3,32.8))
cursor.execute(Q_BAG,(5,53.5))
cursor.execute(Q_BAG,(6,39.7))
cursor.execute(Q_BAG,(7,22))
cursor.execute(Q_BAG,(8,50.99))
cursor.execute(Q_BAG,(9,78.9))
cursor.execute(Q_BAG,(10,33.7))
cursor.execute(Q_BAG,(11,67))
cursor.execute(Q_BAG,(12,24.55))
cursor.execute(Q_BAG,(13,39.6))
cursor.execute(Q_BAG,(14,51.2))
cursor.execute(Q_BAG,(15,48.7))
cursor.execute(Q_BAG,(16,39.6))
cursor.execute(Q_BAG,(17,78.7))
cursor.execute(Q_BAG,(18,22.4))
cursor.execute(Q_BAG,(19,87.4))
cursor.execute(Q_BAG,(20,26.5))

cursor.execute(Q_Payment,(144115,"Credit Card","2020-07-05 12:42:44",50))
cursor.execute(Q_Payment,(245313,"PayPal","2020-02-14 16:42:00" ,120.2))
cursor.execute(Q_Payment,(525113,"Credit Card","2020-02-25 08:02:44",78.86))
cursor.execute(Q_Payment,(235213,"Mobile Payment","2020-02-12 23:32:33",58.5))
cursor.execute(Q_Payment,(122122,"Cash","2020-02-11 09:12:12",68.22))
cursor.execute(Q_Payment,(100102,"Credit Card","2020-03-26 14:13:13",120))
cursor.execute(Q_Payment,(145325,"Cash","2020-08-29 17:42:12",500.15))
cursor.execute(Q_Payment,(978569,"Credit Card","2020-06-11 12:12:00",220))
cursor.execute(Q_Payment,(231283,"Bank Transfer","2020-05-05 22:55:34",135))
cursor.execute(Q_Payment,(789238,"Credit Card","2020-03-12 06:55:04",44.8))
cursor.execute(Q_Payment,(245435,"Credit Card","2020-05-23 07:41:06",20.5))
cursor.execute(Q_Payment,(568478,"PayPal","2020-04-14 16:31:05",230))
cursor.execute(Q_Payment,(234213,"Credit Card","2020-08-12 14:22:39",84.5))
cursor.execute(Q_Payment,(235613,"Mobile Payment","2020-10-05 00:30:44",98.45))
cursor.execute(Q_Payment,(123122,"Cash","2020-02-22 10:40:12",346))
cursor.execute(Q_Payment,(125402,"Credit Card","2020-01-28 17:30:54",326.23))
cursor.execute(Q_Payment,(134525,"Cash","2020-04-04 14:20:00",120.20))
cursor.execute(Q_Payment,(978539,"Credit Card","2020-05-15 19:45:40",86))
cursor.execute(Q_Payment,(231243,"Bank Transfer","2020-06-12 18:30:40",125))
cursor.execute(Q_Payment,(713414,"Credit Card","2020-03-11 20:22:00",778.52))

cursor.execute(Q_Flight,("RA2684",102500,"Ryanair","Airbus A320","IST","AMS","2020-11-05 12:00:00","2020-11-05 14:30:00"))
cursor.execute(Q_Flight,("CA1002",253689,"Air Canada","Boeing 737-800","ATL","CDG","2020-04-22 08:00:00","2020-04-22 22:30:00"))
cursor.execute(Q_Flight,("THY4526",887966,"THY","Airbus A319","DEN","FRA","2020-11-05 00:00:00","2020-08-05 08:30:00"))
cursor.execute(Q_Flight,("LF5202",563389,"Lufthansa","Cessna 172","BCN","LGW","2020-11-18 15:30:00","2020-11-18 17:30:00"))
cursor.execute(Q_Flight,("AA9602",889669,"American Airlines","Airbus A320neo","YYZ","SYD","2020-09-08 15:30:00","2020-09-09 00:30:00"))
cursor.execute(Q_Flight,("ER7752",100565,"Emirates","Embraer ERJ-175LR","MUC","LAS","2020-12-02 12:30:00","2020-12-02 23:30:00"))

cursor.execute(Q_Arrival_Airport,("AMS","Netherlands",71706999,-11))
cursor.execute(Q_Arrival_Airport,("CDG","France",76150007,392))
cursor.execute(Q_Arrival_Airport,("FRA","Germany",70560987,364))
cursor.execute(Q_Arrival_Airport,("LGW","United Kingdom",46574786,202))
cursor.execute(Q_Arrival_Airport,("SYD","Australia",44443927,21))
cursor.execute(Q_Arrival_Airport,("LAS","United States",51537638,2184))

cursor.execute(Q_Departure_Airport,("IST","Turkey",52578008,325))
cursor.execute(Q_Departure_Airport,("ATL","United States",110531300,1026))
cursor.execute(Q_Departure_Airport,("DEN","United States",69015703,5431))
cursor.execute(Q_Departure_Airport,("BCN","Spain",52686314,12))
cursor.execute(Q_Departure_Airport,("YYZ","Canada",50499431,569))
cursor.execute(Q_Departure_Airport,("MUC","Germany",47959887,1487))

cursor.execute(Q_Airplane,("Airbus A320","Airbus",7215))
cursor.execute(Q_Airplane,("Boeing 737-800","Boeing",9602))
cursor.execute(Q_Airplane,("Airbus A319","Airbus",1847))
cursor.execute(Q_Airplane,("Cessna 172","Textron Aviation",4098))
cursor.execute(Q_Airplane,("Airbus A320neo","Airbus",3227))
cursor.execute(Q_Airplane,("Embraer ERJ-175LR","Embraer",1738))

cursor.execute(Q_Captain,(102500,"Jaylen","Adams",42,1533))
cursor.execute(Q_Captain,(253689,"Alex","Lioen",30,786))
cursor.execute(Q_Captain,(887966,"Mariana","Dellinton",39,4100))
cursor.execute(Q_Captain,(563389,"Carles","Rexach",38,9622))
cursor.execute(Q_Captain,(889669,"Javier","Saviola",33,2233))
cursor.execute(Q_Captain,(100563,"Vince","Hayes",50,6522))

cursor.execute(Q_Airline,("Ryanair",72020123,"Ireland"))
cursor.execute(Q_Airline,("Air Canada",23056266,"Canada"))
cursor.execute(Q_Airline,("THY",29955568,"Turkey"))
cursor.execute(Q_Airline,("Lufthansa",72020123,"Germany"))
cursor.execute(Q_Airline,("American Airlines",86530123,"USA"))
cursor.execute(Q_Airline,("Emirates",31007756,"United Arab Emirates"))

cursor.execute(Q_Passenger,(112023,"Luis","Enrique",25,"M","Spain"))
cursor.execute(Q_Passenger,(552231,"Jack","London",40,"M","Spain"))
cursor.execute(Q_Passenger,(334233,"Paul","Dennis",29,"M","Spain"))
cursor.execute(Q_Passenger,(523498,"Steven","Nash",28,"M","German"))
cursor.execute(Q_Passenger,(716554,"Mariana","Balet",41,"F","French"))
cursor.execute(Q_Passenger,(413213,"Sebastian","Nulker",19,"F","German"))
cursor.execute(Q_Passenger,(344531,"Mark","Zunner",41,"M","German"))
cursor.execute(Q_Passenger,(433318,"Joshua","Kimmich",28,"M","German"))
cursor.execute(Q_Passenger,(221319,"Eric","Abidal",42,"M","Switzerland"))
cursor.execute(Q_Passenger,(278633,"Julio","Alberto",55,"F","Spain"))
cursor.execute(Q_Passenger,(721328,"Michael","Reiziger",42,"M","Netherlands"))
cursor.execute(Q_Passenger,(588138,"Gary","Lineker",28,"M","England"))
cursor.execute(Q_Passenger,(213219,"Gianluca","Zambrotta",22,"M","Italy"))
cursor.execute(Q_Passenger,(213513,"Ivan","Rakitic",32,"M","Croatia"))
cursor.execute(Q_Passenger,(987946,"Rafael","Marquez",30,"M","Mexico"))
cursor.execute(Q_Passenger,(321569,"Frank","Barrett",18,"M","Scotland"))
cursor.execute(Q_Passenger,(213218,"Johnny","Carey",25,"M","Ireland"))
cursor.execute(Q_Passenger,(823126,"Stan","Pearson",88,"M","England"))
cursor.execute(Q_Passenger,(500025,"Manfred","Bender",26,"F","German"))
cursor.execute(Q_Passenger,(528558,"Dieter","Brenninger",40,"F","German"))


connection.commit()



