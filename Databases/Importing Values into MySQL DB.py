import mysql.connector

cnx = mysql.connector.connect(user='root', password='test', host='127.0.0.1', database='test')
mycursor = cnx.cursor()

sql = "INSERT INTO users (ID, Name, Department, Location, Pay) VALUES (%s, %s, %s, %s, %d)"
val = [
('0001', 'George Michaels', 'Maintenance', 'Warehouse 5', '50000', ),
('0002', 'Michael Jackson', 'Sales', 'Warehouse 5', '80000'),
('0003', 'Phil Collins', 'IT', 'Warehouse 2', '75000'),
('0004', 'Matthew Bellamy', 'IT', 'Warehouse 3', '75000'),
('0005', 'Till Lindermann', 'Security', 'Warehouse 1', '70000'),
('0006', 'Weird Al Yankovich', 'Sales', 'Warehouse 4', '80000'),
('0008', 'Joe Shmo', 'Security', 'Warehouse 3', '70000')
('0009', 'John Doe', 'Sales', 'Warehouse 2', '80000')
('0010', 'Max Payne', 'Maintenance', 'Warehouse 4', '50000')
('0011', 'Dean Martin', 'Sales', 'Warehouse 5', '80000')
('0012', 'Jayne Doe', 'Security', 'Warehouse 4', '70000')
('0013', 'meghan markle', 'Sales', 'Warehouse 1', '80000')
('0014', 'William Anderson', 'Maintenance', 'Warehouse 4', '50000')
('0015', 'Jack Sparrow', 'IT', 'Warehouse 3', '75000')
('0016', 'Thomas Anderson', 'Security', 'Warehouse 4', '70000')
('0017', 'Dean Richards', 'Maintenance', 'Warehouse 2', '50000')
]

mycursor.executemany(sql, val)

cnx.commit()

print(mycursor.rowcount, "was inserted.")