CREATE DATABASE hotel_mang_prj;
USE hotel_mang_prj;

-- Creating the rooms table
CREATE TABLE rooms (
    room_no INT PRIMARY KEY,
    room_type VARCHAR(10),
    room_rent DECIMAL(10,2),
    status VARCHAR(10)
);

-- Inserting values into rooms
INSERT INTO rooms (room_no, room_type, room_rent, status) VALUES
(101, 'AC', 3200.00, 'free'),
(102, 'AC', 3200.00, 'free'),
(103, 'AC', 3200.00, 'free'),
(104, 'AC', 3200.00, 'free'),
(105, 'AC', 3200.00, 'reserved'),
(106, 'NONAC', 2200.00, 'free'),
(107, 'NONAC', 2200.00, 'reserved'),
(108, 'NONAC', 2200.00, 'reserved'),
(109, 'NONAC', 2200.00, 'reserved'),
(110, 'DELUX', 3000.00, 'reserved'),
(111, 'DELUX', 3000.00, 'reserved'),
(112, 'DELUX', 3000.00, 'free'),
(113, 'DELUX', 3000.00, 'free');

-- Creating the customer table
CREATE TABLE customer (
    r_no INT PRIMARY KEY,
    name VARCHAR(50),
    addr VARCHAR(50),
    phno VARCHAR(15),
    room_status VARCHAR(10)
);

-- Inserting values into customer
INSERT INTO customer (r_no, name, addr, phno, room_status) VALUES
(1221, 'Rishi', 'Chennai', '567891234', 'reserved'),
(1234, 'RAJ', 'CHENNAI', '3456789012', 'reserved'),
(1256, 'Aditya', 'Mumbai', '7689032145', 'reserved'),
(1331, 'Harsh', 'Pune', '7658900003', 'reserved'),
(1809, 'Rohit', 'Mumbai', '7890905643', 'reserved'),
(2000, 'Rohan', 'Bangalore', '7215494099', 'reserved'),
(2001, 'Manjot', 'Bangalore', '7410959089', 'reserved'),
(2002, 'Chirag', 'Kolkata', '9456789010', 'reserved');

-- Creating the cust_book table
CREATE TABLE cust_book (
    reg_no INT PRIMARY KEY,
    name VARCHAR(50),
    room_no INT,
    ch_in DATE,
    ch_out DATE,
    menu_type VARCHAR(10),
    advance DECIMAL(10,2),
    room_type VARCHAR(10),
    FOREIGN KEY (room_no) REFERENCES rooms(room_no)
);

-- Inserting values into cust_book
INSERT INTO cust_book (reg_no, name, room_no, ch_in, ch_out, menu_type, advance, room_type) VALUES
(1221, 'Rishi', 111, '2025-02-02', '2025-02-04', 'NONVEG', 1200.00, 'DELUX'),
(1234, 'RAJ', 105, '2025-01-02', '2025-01-04', 'NONVEG', 1500.00, 'AC'),
(1256, 'Aditya', 107, '2025-01-01', '2025-01-04', 'VEG', 1200.00, 'NONAC'),
(1331, 'Harsh', 106, '2025-01-10', '2025-01-13', 'VEG', 2000.00, 'NONAC'),
(1809, 'Rohit', 108, '2025-12-12', '2025-12-13', 'NONVEG', 1200.00, 'NONAC'),
(2000, 'Rohan', 109, '2025-02-03', '2025-02-04', 'VEG', 1300.00, 'AC'),
(2001, 'Manjot', 110, '2025-01-02', '2025-01-07', 'VEG', 1200.00, 'DELUX'),
(2002, 'Chirag', 109, '2025-03-11', '2025-03-12', 'VEG', 1000.00, 'NONAC');

-- Creating the bill table
CREATE TABLE bill (
    reg_no INT PRIMARY KEY,
    no_days INT,
    ch_out DATE,
    total_amt DECIMAL(10,2),
    room_no INT,
    paid DECIMAL(10,2),
    advance DECIMAL(10,2),
    menu VARCHAR(10),
    FOREIGN KEY (reg_no) REFERENCES cust_book(reg_no)
);

-- Inserting values into bill
INSERT INTO bill (reg_no, no_days, ch_out, total_amt, room_no, paid, advance, menu) VALUES
(1234, 4, NULL, NULL, NULL, NULL, NULL, NULL);
