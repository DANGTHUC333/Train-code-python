import mysql.connector

# Kết nối đến MySQL server mà không chỉ định database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Tạo con trỏ để thực hiện các câu lệnh SQL
mycursor = mydb.cursor()

# Tạo cơ sở dữ liệu nếu chưa tồn tại
mycursor.execute("CREATE DATABASE IF NOT EXISTS ql_vemaybay")

# Kết nối lại đến cơ sở dữ liệu vừa tạo
mydb.close()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ql_vemaybay"
)

mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS airlines(
        id VARCHAR(10) PRIMARY KEY,
        tenhang VARCHAR(100),
        namthanhlap VARCHAR(20),
        trusochinh VARCHAR(100)
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS flightroutes(
        id VARCHAR(10) PRIMARY KEY,
        sanbaydi VARCHAR(200),
        sanbayden VARCHAR(200)
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS flights(
        id VARCHAR(10) PRIMARY KEY,
        idtuyenbay VARCHAR(10) NOT NULL,
        idhang VARCHAR(10) NOT NULL,
        ngaybay DATETIME NOT NULL,
        thoigianbay VARCHAR(10),
        soghe INT,
        giave INT,
        FOREIGN KEY (idtuyenbay) REFERENCES flightroutes(id),
        FOREIGN KEY (idhang) REFERENCES airlines(id)
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INT AUTO_INCREMENT PRIMARY KEY,
        tenkh VARCHAR(255) NOT NULL,
        ngaysinh DATE,
        CCCD VARCHAR(20),
        quoctich VARCHAR(50),
        hochieu VARCHAR(20),
        SDT VARCHAR(15)
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets(
        id VARCHAR(10) PRIMARY KEY,
        idchuyenbay VARCHAR(10) NOT NULL,
        idkhach INT NOT NULL,
        soghetrong INT,
        giave DECIMAL(10, 2),
        ngaymua DATE,
        FOREIGN KEY (idchuyenbay) REFERENCES flights(id),
        FOREIGN KEY (idkhach) REFERENCES customers(id)
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id VARCHAR(10) PRIMARY KEY,
        idve VARCHAR(10) NOT NULL,
        ngaythanhtoan DATE,
        phuongthuctt VARCHAR(100),
        FOREIGN KEY (idve) REFERENCES tickets(id)
    )
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS revenue(
        id INT AUTO_INCREMENT PRIMARY KEY,
        idchuyenbay VARCHAR(10) NOT NULL,
        tongve INT,
        doanhthuthang DECIMAL(20, 2),
        doanhthunam DECIMAL(20, 2),
        chiphivanhanh DECIMAL(20, 2),
        loinhuan DECIMAL(20, 2),
        FOREIGN KEY (idchuyenbay) REFERENCES flights(id)
    )
""")

# Insert data into tables
mycursor.execute("INSERT INTO airlines (id, tenhang, namthanhlap, trusochinh) "
                 "VALUES ('A1', 'Vietnam Airlines', '1956', 'Hanoi, Vietnam'), "
                 "('A2', 'VietJet Air', '2007', 'Ho Chi Minh City, Vietnam'), "
                 "('A3', 'Bamboo Airways', '2017', 'Hanoi, Vietnam')")
mycursor.execute("INSERT INTO flightroutes (id, sanbaydi, sanbayden) "
                 "VALUES ('R1', 'Noi Bai International Airport', 'Tan Son Nhat International Airport'), "
                 "('R2', 'Tan Son Nhat International Airport', 'Da Nang International Airport'), "
                 "('R3', 'Da Nang International Airport', 'Noi Bai International Airport'), "
                 "('RF1', 'Tan Son Nhat International Airport', 'Seoul International Airport'), "
                 "('RF2', 'Ha Noi International Airport', 'Maxcova International Airport'), "
                 "('RF3', 'Maxcova International Airport', 'Da Nang International Airport'), "
                 "('RF4', 'Washington International Airport', 'Ha Noi International Airport'), "
                 "('R4', 'Phu Quoc International Airport', 'Ha Noi International Airport'), "
                 "('R5', 'Ha Noi International Airport', 'Ho Chi Minh International Airport')")

mycursor.execute("INSERT INTO flights (id, idtuyenbay, idhang, ngaybay, thoigianbay, soghe, giave) "
                 "VALUES ('F1', 'R1', 'A1', '2024-07-01 08:00:00', '2h00m', 180, 1000000), "
                 "('F2', 'R2', 'A2', '2024-07-02 09:00:00', '1h30m', 150, 800000), "
                 "('F3', 'R3', 'A3', '2024-07-03 10:00:00', '1h45m', 200, 900000)")

mycursor.execute("INSERT INTO customers (tenkh, ngaysinh, CCCD, quoctich, hochieu, SDT) "
                 "VALUES ('Nguyen Van A', '1985-01-01', '0011223344', 'Vietnam', 'B1234567', '0901234567'), "
                 "('Tran Thi B', '1990-02-02', '0055667788', 'Vietnam', 'C1234567', '0912345678'), "
                 "('Le Van C', '1995-03-03', '0099001122', 'Vietnam', 'D1234567', '0923456789')")

mycursor.execute("INSERT INTO tickets (id, idchuyenbay, idkhach, soghetrong, giave, ngaymua) "
                 "VALUES ('T1', 'F1', 1, 20, 1000000,'2002-11-15'), "
                 "('T2', 'F2', 2, 15, 800000,'2002-11-15'), "
                 "('T3', 'F3', 3, 30, 900000,'2002-11-15')")

mycursor.execute("INSERT INTO payments (id, idve, ngaythanhtoan, phuongthuctt) "
                 "VALUES ('P1', 'T1', '2024-06-01', 'Credit Card'), "
                 "('P2', 'T2', '2024-06-02', 'Debit Card'), "
                 "('P3', 'T3', '2024-06-03', 'PayPal')")

mycursor.execute("INSERT INTO revenue (idchuyenbay, tongve, doanhthuthang, doanhthunam, chiphivanhanh, loinhuan) "
                 "VALUES ('F1', 160, 160000000, 1920000000, 120000000, 720000000), " 
                 "('F2', 135, 108000000, 1296000000, 90000000, 396000000), "
                 "('F3', 170, 153000000, 1836000000, 110000000, 736000000)")

mydb.commit()
mydb.close()
