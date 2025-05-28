from sqlalchemy import create_engine, text

# Update with your DB connection details
DB_URL = 'mysql+pymysql://root:1234@localhost/pyDb'
engine = create_engine(DB_URL)

# SQL statements to drop, create and insert records
sql_script = """
-- Drop tables in reverse dependency order
DROP TABLE IF EXISTS warranty;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS part;

-- Step 1: Create part table
CREATE TABLE part (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50)
);

-- Step 2: Create product table
CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    serial_no VARCHAR(50) UNIQUE NOT NULL,
    part_id INT,
    name VARCHAR(100),
    FOREIGN KEY (part_id) REFERENCES part(id)
);

-- Step 3: Create warranty table
CREATE TABLE warranty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    serial_no VARCHAR(50),
    price DECIMAL(10, 2),
    expiry_date DATE,
    FOREIGN KEY (serial_no) REFERENCES product(serial_no)
);

"""

# Execute the SQL script
with engine.connect() as connection:
    for statement in sql_script.strip().split(';'):
        stmt = statement.strip()
        if stmt:
            connection.execute(text(stmt))
    print("✅ Tables created successfully.")
