#Q1
'''import pymysql as pm
try:
    con = pm.connect(host='localhost', database='amitdb', user='root', password='root')
    cursor = con.cursor()
    query6 = 'Create table Authors(AuthorID int primary key,FirstName varchar(15),\
    MiddleName varchar(15),LastName varchar(15))'
    cursor.execute(query6)
    query4 = 'Create table Zip_Codes(Zip_Code_ID int primary key,City varchar(15),State varchar(20),Zip_Code int)'
    cursor.execute(query4)
    query3 = 'Create table Publishers(Publisher_ID int primary key,Name varchar(15),Street_Address varchar(50),\
    Suite_Number int,Zip_Code_ID int,foreign key(Zip_Code_ID) references Zip_Codes(Zip_Code_ID))'
    cursor.execute(query3)
    query2 = 'Create table Titles(TitleId int primary key,Title varchar(35),ISBN int,Publisher_ID int,\
    Publication_Year int,foreign key(Publisher_ID) references Publishers(Publisher_ID))'
    cursor.execute(query2)
    query1 = 'Create table Books(BookId int primary key,TitleId int,Location varchar(15),Genre varchar(10),\
    foreign key(TitleId) references Titles(TitleId))'
    cursor.execute(query1)
    query5 = 'Create table Authors_Titles(Author_Title_ID int primary key,AuthorID int ,TitleId int,\
    foreign key(AuthorID) references Authors(AuthorID),foreign key(TitleId) references Titles(TitleId))'
    cursor.execute(query5)
    print('Table Created')
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        print('DONE!!')'''


#Q2
'''import pymysql as pm

try:
    con = pm.connect(host='localhost', database='amitdb', user='root', password='root')
    cursor = con.cursor()
    query6 = "insert into Authors(AuthorID,FirstName,MiddleName,LastName) values(10001,'abc','sss','bbb')"
    cursor.execute(query6)
    query4 = "insert into Zip_Codes(Zip_Code_ID,City,State,Zip_Code) values(101,'rishikesh','Ddun',501)"
    cursor.execute(query4)
    query3 = "insert into Publishers(Publisher_ID,Name,Street_Address,Suite_Number,Zip_Code_ID) values(601,'kumar','12/24 Bihar',11,101)"
    cursor.execute(query3)
    query2 = "insert into Titles(TitleID,Title,ISBN,Publisher_ID,Publication_Year) values(701,'maths',978-3-16-148410-0, 601,2017)"
    cursor.execute(query2)
    query1 = "insert into Books(BookId, TitleId, Location, Genre) values(1001, 701, 'Ddun','math')"
    cursor.execute(query1)
    query5 = "insert into Authors_Titles(Author_Title_ID,AuthorID,TitleId) values(1,10001,701)"
    cursor.execute(query5)
    con.commit()

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')'''

 #Q3
'''import pymysql as pm

try:
    con = pm.connect(host='localhost', database='amitdb',user='root', password='root')
    cursor = con.cursor()

    query = "select * from Authors"

    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print('AuthorID: {}, FirstName: {} MiddleName:{},LastName:{}'.format(row[0], row[1], row[2], row[3]))

    query1 = "update Authors set FirstName='Rahul' "
    cursor.execute(query1)

    data1 = cursor.fetchall()
    for row in data1:
        print('AuthorID: {}, FirstName: {} MiddleName:{},LastName:{}'.format(row[0], row[1], row[2], row[3]))

    con.commit()

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')'''
