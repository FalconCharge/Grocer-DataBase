from db import get_db_connection

def create_products_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id int AUTO_INCREMENT primary key,
            name varchar(100) not null unique,
            price Decimal(10, 2),    
            section varchar(100) default 'Not Set',
            supplier varchar(100) default 'Unknown'
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products ORDER BY id")
    products = cursor.fetchall()

    cursor.close()
    conn.close()
    return products


def add_product(name, price):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, price) VALUES (%s, %s)",
        (name, price)
    )
    
    product_id = cursor.lastrowid

    conn.commit()

    cursor.close()
    conn.close()


    return product_id

def insert_product_syntheic_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT IGNORE INTO products (name, price, section, supplier) VALUES
    ('Whole Milk', 3.50, 'Dairy', 'Generic'),
    ('Skim Milk', 3.20, 'Dairy', 'Generic'),
    ('Chocolate Milk', 3.80, 'Dairy', 'Generic'),
    ('Butter', 4.50, 'Dairy', 'Generic'),
    ('Cheddar Cheese', 5.00, 'Dairy', 'Generic'),
    ('Mozzarella Cheese', 4.80, 'Dairy', 'Generic'),
    ('Yogurt', 1.50, 'Dairy', 'Generic'),
    ('Eggs (dozen)', 2.80, 'Dairy', 'Generic'),
    ('Orange Juice', 3.00, 'Beverages', 'Generic'),
    ('Apple Juice', 3.00, 'Beverages', 'Generic'),
    ('Bread (White)', 2.50, 'Bakery', 'Generic'),
    ('Bread (Whole Wheat)', 2.70, 'Bakery', 'Generic'),
    ('Bagels', 3.00, 'Bakery', 'Generic'),
    ('Croissants', 3.50, 'Bakery', 'Generic'),
    ('Rice', 2.20, 'Pantry', 'Generic'),
    ('Pasta', 1.80, 'Pantry', 'Generic'),
    ('Spaghetti Sauce', 3.20, 'Pantry', 'Generic'),
    ('Tomato Paste', 1.50, 'Pantry', 'Generic'),
    ('Olive Oil', 6.00, 'Pantry', 'Generic'),
    ('Canola Oil', 5.50, 'Pantry', 'Generic'),
    ('Apples (per lb)', 1.80, 'Produce', 'Generic'),
    ('Bananas (per lb)', 1.20, 'Produce', 'Generic'),
    ('Oranges (per lb)', 2.00, 'Produce', 'Generic'),
    ('Strawberries (1 lb)', 3.50, 'Produce', 'Generic'),
    ('Blueberries (1 lb)', 4.00, 'Produce', 'Generic'),
    ('Lettuce', 1.50, 'Produce', 'Generic'),
    ('Spinach', 2.00, 'Produce', 'Generic'),
    ('Carrots', 1.20, 'Produce', 'Generic'),
    ('Broccoli', 2.50, 'Produce', 'Generic'),
    ('Bell Peppers', 3.00, 'Produce', 'Generic'),
    ('Tomatoes', 2.50, 'Produce', 'Generic'),
    ('Potatoes', 1.50, 'Produce', 'Generic'),
    ('Onions', 1.30, 'Produce', 'Generic'),
    ('Garlic', 0.50, 'Produce', 'Generic'),
    ('Chicken Breast (lb)', 5.50, 'Meat', 'Generic'),
    ('Ground Beef (lb)', 6.00, 'Meat', 'Generic'),
    ('Pork Chops (lb)', 5.80, 'Meat', 'Generic'),
    ('Salmon (lb)', 8.00, 'Seafood', 'Generic'),
    ('Tuna (canned)', 2.20, 'Seafood', 'Generic'),
    ('Shrimp (lb)', 9.50, 'Seafood', 'Generic'),
    ('Frozen Pizza', 4.50, 'Frozen', 'Generic'),
    ('Ice Cream (pint)', 3.50, 'Frozen', 'Generic'),
    ('Cereal', 4.00, 'Pantry', 'Generic'),
    ('Oatmeal', 3.00, 'Pantry', 'Generic'),
    ('Peanut Butter', 3.50, 'Pantry', 'Generic'),
    ('Jelly', 2.80, 'Pantry', 'Generic'),
    ('Coffee', 6.50, 'Beverages', 'Generic'),
    ('Tea Bags', 3.00, 'Beverages', 'Generic'),
    ('Sugar (per lb)', 2.00, 'Pantry', 'Generic'),
    ('Flour (per lb)', 1.50, 'Pantry', 'Generic'),
    ('Salt', 0.80, 'Pantry', 'Generic'),
    ('Black Pepper', 2.50, 'Pantry', 'Generic')""")

    cursor.execute("""INSERT IGNORE INTO products (name, price, section, supplier) VALUES
    ('Smartphone Model A', 699.99, 'Electronics', 'TechCorp'),
    ('Smartphone Model B', 799.99, 'Electronics', 'TechCorp'),
    ('Smartphone Model C', 999.99, 'Electronics', 'Gadgetron'),
    ('Laptop 13-inch', 1199.99, 'Electronics', 'CompWorld'),
    ('Laptop 15-inch', 1399.99, 'Electronics', 'CompWorld'),
    ('Laptop Gaming Pro', 1899.99, 'Electronics', 'GamerTech'),
    ('Tablet 10-inch', 499.99, 'Electronics', 'TechCorp'),
    ('Tablet 12-inch', 599.99, 'Electronics', 'Gadgetron'),
    ('Wireless Mouse', 49.99, 'Electronics', 'PeriphCo'),
    ('Mechanical Keyboard', 129.99, 'Electronics', 'PeriphCo'),
    ('Monitor 24-inch', 199.99, 'Electronics', 'DisplayWorks'),
    ('Monitor 27-inch', 299.99, 'Electronics', 'DisplayWorks'),
    ('4K TV 50-inch', 799.99, 'Electronics', 'HomeVision'),
    ('4K TV 65-inch', 1199.99, 'Electronics', 'HomeVision'),
    ('Bluetooth Speaker', 149.99, 'Electronics', 'SoundMax'),
    ('Noise Cancelling Headphones', 249.99, 'Electronics', 'SoundMax'),
    ('Smartwatch Series 1', 399.99, 'Electronics', 'TechCorp'),
    ('Smartwatch Series 2', 499.99, 'Electronics', 'Gadgetron'),
    ('Gaming Console X', 499.99, 'Electronics', 'GameWorld'),
    ('Gaming Console Y', 599.99, 'Electronics', 'GameWorld'),
    ('VR Headset', 399.99, 'Electronics', 'ImmersiTech'),
    ('Drone Pro', 899.99, 'Electronics', 'SkyFlyer'),
    ('Digital Camera', 699.99, 'Electronics', 'PhotoPro'),
    ('DSLR Camera', 1199.99, 'Electronics', 'PhotoPro'),
    ('Action Camera', 349.99, 'Electronics', 'ActionCam Co'),
    ('Smart Home Hub', 199.99, 'Electronics', 'SmartHome Inc'),
    ('Smart Thermostat', 249.99, 'Electronics', 'SmartHome Inc'),
    ('Security Camera Indoor', 99.99, 'Electronics', 'SecureTech'),
    ('Security Camera Outdoor', 149.99, 'Electronics', 'SecureTech'),
    ('Router AC1200', 89.99, 'Electronics', 'NetGear Inc'),
    ('Router AC2000', 129.99, 'Electronics', 'NetGear Inc'),
    ('External SSD 500GB', 149.99, 'Electronics', 'StoragePlus'),
    ('External SSD 1TB', 249.99, 'Electronics', 'StoragePlus'),
    ('Portable Charger 10000mAh', 49.99, 'Electronics', 'PowerGo'),
    ('Portable Charger 20000mAh', 79.99, 'Electronics', 'PowerGo'),
    ('USB-C Hub', 59.99, 'Electronics', 'PeriphCo'),
    ('Webcam HD', 79.99, 'Electronics', 'CamWorks'),
    ('Projector 1080p', 399.99, 'Electronics', 'HomeVision'),
    ('Projector 4K', 799.99, 'Electronics', 'HomeVision'),
    ('Electric Scooter', 699.99, 'Electronics', 'MoveTech'),
    ('Wireless Earbuds', 149.99, 'Electronics', 'SoundMax'),
    ('Smart Light Bulb', 29.99, 'Electronics', 'SmartHome Inc'),
    ('Smart Door Lock', 199.99, 'Electronics', 'SecureTech'),
    ('Gaming Chair', 299.99, 'Electronics', 'GamerTech'),
    ('Graphic Tablet', 399.99, 'Electronics', 'DesignPro'),
    ('3D Printer', 999.99, 'Electronics', 'MakerTech'),
    ('Smart Refrigerator', 2199.99, 'Electronics', 'HomeVision'),
    ('Smart Oven', 1299.99, 'Electronics', 'HomeVision'),
    ('Air Purifier', 249.99, 'Electronics', 'CleanAir Co'),
    ('Smart Scale', 99.99, 'Electronics', 'HealthTech'),
    ('Fitness Tracker', 149.99, 'Electronics', 'TechCorp'),
    ('E-Reader', 129.99, 'Electronics', 'ReadTech'),
    ('Laser Printer', 349.99, 'Electronics', 'PrintWorks'),
    ('Inkjet Printer', 199.99, 'Electronics', 'PrintWorks')""")

    conn.commit()
    cursor.close()
    conn.close()