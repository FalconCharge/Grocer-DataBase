from db import get_db_connection

def create_products_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id int AUTO_INCREMENT primary key,
            name varchar(100) not null unique,
            price Decimal(10, 2),    
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


def add_product(name, price, supplier):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (name, price, supplier) VALUES (%s, %s, %s)",
        (name, price, supplier)
    )
    
    product_id = cursor.lastrowid

    conn.commit()

    cursor.close()
    conn.close()


    return product_id

def insert_product_syntheic_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT IGNORE INTO products (name, price, supplier) VALUES
    ('Whole Milk', 3.50, 'Dairy'),
    ('Skim Milk', 3.20, 'Dairy'),
    ('Chocolate Milk', 3.80, 'Dairy'),
    ('Butter', 4.50, 'Dairy'),
    ('Cheddar Cheese', 5.00, 'Dairy'),
    ('Mozzarella Cheese', 4.80, 'Dairy'),
    ('Yogurt', 1.50, 'Dairy'),
    ('Eggs (dozen)', 2.80, 'Dairy'),
    ('Orange Juice', 3.00, 'Beverages'),
    ('Apple Juice', 3.00, 'Beverages'),
    ('Bread (White)', 2.50, 'Bakery'),
    ('Bread (Whole Wheat)', 2.70, 'Bakery'),
    ('Bagels', 3.00, 'Bakery'),
    ('Croissants', 3.50, 'Bakery'),
    ('Rice', 2.20, 'Pantry'),
    ('Pasta', 1.80, 'Pantry'),
    ('Spaghetti Sauce', 3.20, 'Pantry'),
    ('Tomato Paste', 1.50, 'Pantry'),
    ('Olive Oil', 6.00, 'Pantry'),
    ('Canola Oil', 5.50, 'Pantry'),
    ('Apples (per lb)', 1.80, 'Produce'),
    ('Bananas (per lb)', 1.20, 'Produce'),
    ('Oranges (per lb)', 2.00, 'Produce'),
    ('Strawberries (1 lb)', 3.50, 'Produce'),
    ('Blueberries (1 lb)', 4.00, 'Produce'),
    ('Lettuce', 1.50, 'Produce'),
    ('Spinach', 2.00, 'Produce'),
    ('Carrots', 1.20, 'Produce'),
    ('Broccoli', 2.50, 'Produce'),
    ('Bell Peppers', 3.00, 'Produce'),
    ('Tomatoes', 2.50, 'Produce'),
    ('Potatoes', 1.50, 'Produce'),
    ('Onions', 1.30, 'Produce'),
    ('Garlic', 0.50, 'Produce'),
    ('Chicken Breast (lb)', 5.50, 'Meat'),
    ('Ground Beef (lb)', 6.00, 'Meat'),
    ('Pork Chops (lb)', 5.80, 'Meat'),
    ('Salmon (lb)', 8.00, 'Seafood'),
    ('Tuna (canned)', 2.20, 'Seafood'),
    ('Shrimp (lb)', 9.50, 'Seafood'),
    ('Frozen Pizza', 4.50, 'Frozen'),
    ('Ice Cream (pint)', 3.50, 'Frozen'),
    ('Cereal', 4.00, 'Pantry'),
    ('Oatmeal', 3.00, 'Pantry'),
    ('Peanut Butter', 3.50, 'Pantry'),
    ('Jelly', 2.80, 'Pantry'),
    ('Coffee', 6.50, 'Beverages'),
    ('Tea Bags', 3.00, 'Beverages'),
    ('Sugar (per lb)', 2.00, 'Pantry'),
    ('Flour (per lb)', 1.50, 'Pantry'),
    ('Salt', 0.80, 'Pantry'),
    ('Black Pepper', 2.50, 'Pantry')""")

    cursor.execute("""INSERT IGNORE INTO products (name, price, supplier) VALUES
    ('Smartphone Model A', 699.99, 'TechCorp'),
    ('Smartphone Model B', 799.99, 'TechCorp'),
    ('Smartphone Model C', 999.99, 'Gadgetron'),
    ('Laptop 13-inch', 1199.99, 'CompWorld'),
    ('Laptop 15-inch', 1399.99, 'CompWorld'),
    ('Laptop Gaming Pro', 1899.99, 'GamerTech'),
    ('Tablet 10-inch', 499.99, 'TechCorp'),
    ('Tablet 12-inch', 599.99, 'Gadgetron'),
    ('Wireless Mouse', 49.99, 'PeriphCo'),
    ('Mechanical Keyboard', 129.99, 'PeriphCo'),
    ('Monitor 24-inch', 199.99, 'DisplayWorks'),
    ('Monitor 27-inch', 299.99, 'DisplayWorks'),
    ('4K TV 50-inch', 799.99, 'HomeVision'),
    ('4K TV 65-inch', 1199.99, 'HomeVision'),
    ('Bluetooth Speaker', 149.99, 'SoundMax'),
    ('Noise Cancelling Headphones', 249.99, 'SoundMax'),
    ('Smartwatch Series 1', 399.99, 'TechCorp'),
    ('Smartwatch Series 2', 499.99, 'Gadgetron'),
    ('Gaming Console X', 499.99, 'GameWorld'),
    ('Gaming Console Y', 599.99, 'GameWorld'),
    ('VR Headset', 399.99, 'ImmersiTech'),
    ('Drone Pro', 899.99, 'SkyFlyer'),
    ('Digital Camera', 699.99, 'PhotoPro'),
    ('DSLR Camera', 1199.99, 'PhotoPro'),
    ('Action Camera', 349.99, 'ActionCam Co'),
    ('Smart Home Hub', 199.99, 'SmartHome Inc'),
    ('Smart Thermostat', 249.99, 'SmartHome Inc'),
    ('Security Camera Indoor', 99.99, 'SecureTech'),
    ('Security Camera Outdoor', 149.99, 'SecureTech'),
    ('Router AC1200', 89.99, 'NetGear Inc'),
    ('Router AC2000', 129.99, 'NetGear Inc'),
    ('External SSD 500GB', 149.99, 'StoragePlus'),
    ('External SSD 1TB', 249.99, 'StoragePlus'),
    ('Portable Charger 10000mAh', 49.99, 'PowerGo'),
    ('Portable Charger 20000mAh', 79.99, 'PowerGo'),
    ('USB-C Hub', 59.99, 'PeriphCo'),
    ('Webcam HD', 79.99, 'CamWorks'),
    ('Projector 1080p', 399.99, 'HomeVision'),
    ('Projector 4K', 799.99, 'HomeVision'),
    ('Electric Scooter', 699.99, 'MoveTech'),
    ('Wireless Earbuds', 149.99, 'SoundMax'),
    ('Smart Light Bulb', 29.99, 'SmartHome Inc'),
    ('Smart Door Lock', 199.99, 'SecureTech'),
    ('Gaming Chair', 299.99, 'GamerTech'),
    ('Graphic Tablet', 399.99, 'DesignPro'),
    ('3D Printer', 999.99, 'MakerTech'),
    ('Smart Refrigerator', 2199.99, 'HomeVision'),
    ('Smart Oven', 1299.99, 'HomeVision'),
    ('Air Purifier', 249.99, 'CleanAir Co'),
    ('Smart Scale', 99.99, 'HealthTech'),
    ('Fitness Tracker', 149.99, 'TechCorp'),
    ('E-Reader', 129.99, 'ReadTech'),
    ('Laser Printer', 349.99, 'PrintWorks'),
    ('Inkjet Printer', 199.99, 'PrintWorks')""")

    conn.commit()
    cursor.close()
    conn.close()