from db import get_db_connection

def create_customer_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        create table if not exists customers(
            id int AUTO_INCREMENT primary key, 
            name varchar(100) NOT NULL,
            address varchar(255),
            email varchar(100) NOT NULL unique,
            phone varchar(20),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


def get_all_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customers as c ORDER BY c.id")
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

def add_customer(name, address, email=None, phone=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, address, email, phone) VALUES (%s, %s, %s, %s)",
        (name, address, email, phone)
    )

    conn.commit()
    cursor.close()
    conn.close()

def update_customer_Info(customer_id, name=None, address=None, email=None, phone=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    if name is not None:
        cursor.execute(
            """
            UDPATE customers set name as %s
            where id = %s
            """, (name, customer_id)
        )
    if address is not None:
        cursor.execute(
            """
            UPDATE customers set address as %s where id = %s)
            """, (address, customer_id)
        )
    if email is not None:
        cursor.execute(
            "UPDATE customers set email as %s where id = %s", (email, customer_id)
        )
    if email is not None:
        cursor.execute(
            "UPDATE customers set phone as %s where id = %s", (phone, customer_id)
        )

def get_customer_id(name=None, email=None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if name is None and email is None:
        return None

    if name is not None:
        cursor.execute("Select c.id from customers as c where c.name = %s", (name, ))
    
    if email is not None:
        cursor.execute("Select c.id from customers as c where c.email = %s", (email, ))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

def get_customer_name(customer_id=None, email=None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if customer_id is None and email is None:
        return None

    if customer_id is not None:
        cursor.execute("SELECT c.name from customers where c.id = %s", (customer_id, ))

    if email is not None:
        cursor.execute("Select c.name from customers where c.email = %s", (email, ))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result
        

def insert_syn_customer_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""INSERT IGNORE INTO customers (name, email, address, phone) VALUES
    ('Emma Johnson', 'emma.johnson@example.com', '123 Maple St, Springfield', '555-123-4567'),
    ('Liam Smith', 'liam.smith@example.com', '456 Oak Ave, Shelbyville', '555-234-5678'),
    ('Olivia Brown', 'olivia.brown@example.com', '789 Pine Rd, Capital City', '555-345-6789'),
    ('Noah Davis', 'noah.davis@example.com', '321 Cedar St, Springfield', '555-456-7890'),
    ('Ava Wilson', 'ava.wilson@example.com', '654 Birch Ln, Shelbyville', '555-567-8901'),
    ('William Martinez', 'william.martinez@example.com', '987 Elm St, Capital City', '555-678-9012'),
    ('Sophia Anderson', 'sophia.anderson@example.com', '147 Willow Dr, Springfield', '555-789-0123'),
    ('James Taylor', 'james.taylor@example.com', '258 Aspen Rd, Shelbyville', '555-890-1234'),
    ('Isabella Thomas', 'isabella.thomas@example.com', '369 Cherry Ln, Capital City', '555-901-2345'),
    ('Benjamin Lee', 'benjamin.lee@example.com', '159 Hickory St, Springfield', '555-012-3456'),
    ('Mia Harris', 'mia.harris@example.com', '753 Walnut Ave, Shelbyville', '555-234-5670'),
    ('Elijah Clark', 'elijah.clark@example.com', '852 Poplar St, Capital City', '555-345-6780'),
    ('Charlotte Lewis', 'charlotte.lewis@example.com', '951 Chestnut Rd, Springfield', '555-456-7891'),
    ('Lucas Robinson', 'lucas.robinson@example.com', '357 Maple St, Shelbyville', '555-567-8902'),
    ('Amelia Walker', 'amelia.walker@example.com', '258 Oak Ave, Capital City', '555-678-9013'),
    ('Mason Young', 'mason.young@example.com', '159 Pine Rd, Springfield', '555-789-0124'),
    ('Harper Hall', 'harper.hall@example.com', '753 Cedar St, Shelbyville', '555-890-1235'),
    ('Logan Allen', 'logan.allen@example.com', '852 Birch Ln, Capital City', '555-901-2346'),
    ('Evelyn King', 'evelyn.king@example.com', '951 Elm St, Springfield', '555-012-3457'),
    ('Ethan Wright', 'ethan.wright@example.com', '357 Willow Dr, Shelbyville', '555-123-4568'),
    ('Abigail Scott', 'abigail.scott@example.com', '258 Aspen Rd, Capital City', '555-234-5679'),
    ('Alexander Green', 'alexander.green@example.com', '159 Cherry Ln, Springfield', '555-345-6781'),
    ('Ella Baker', 'ella.baker@example.com', '753 Hickory St, Shelbyville', '555-456-7892'),
    ('Daniel Adams', 'daniel.adams@example.com', '852 Walnut Ave, Capital City', '555-567-8903'),
    ('Scarlett Nelson', 'scarlett.nelson@example.com', '951 Poplar St, Springfield', '555-678-9014'),
    ('Matthew Carter', 'matthew.carter@example.com', '357 Chestnut Rd, Shelbyville', '555-789-0125'),
    ('Victoria Mitchell', 'victoria.mitchell@example.com', '258 Maple St, Capital City', '555-890-1236'),
    ('Henry Perez', 'henry.perez@example.com', '159 Oak Ave, Springfield', '555-901-2347'),
    ('Aria Roberts', 'aria.roberts@example.com', '753 Pine Rd, Shelbyville', '555-012-3458'),
    ('Jackson Turner', 'jackson.turner@example.com', '852 Cedar St, Capital City', '555-123-4569'),
    ('Lily Phillips', 'lily.phillips@example.com', '951 Birch Ln, Springfield', '555-234-5671'),
    ('Sebastian Campbell', 'sebastian.campbell@example.com', '357 Elm St, Shelbyville', '555-345-6782'),
    ('Hannah Parker', 'hannah.parker@example.com', '258 Willow Dr, Capital City', '555-456-7893'),
    ('Aiden Evans', 'aiden.evans@example.com', '159 Aspen Rd, Springfield', '555-567-8904'),
    ('Grace Edwards', 'grace.edwards@example.com', '753 Cherry Ln, Shelbyville', '555-678-9015'),
    ('Owen Collins', 'owen.collins@example.com', '852 Hickory St, Capital City', '555-789-0126'),
    ('Chloe Stewart', 'chloe.stewart@example.com', '951 Walnut Ave, Springfield', '555-890-1237'),
    ('Luke Sanchez', 'luke.sanchez@example.com', '357 Poplar St, Shelbyville', '555-901-2348'),
    ('Zoey Morris', 'zoey.morris@example.com', '258 Chestnut Rd, Capital City', '555-012-3459'),
    ('Jack Rogers', 'jack.rogers@example.com', '159 Maple St, Springfield', '555-123-4570'),
    ('Penelope Reed', 'penelope.reed@example.com', '753 Oak Ave, Shelbyville', '555-234-5672'),
    ('Wyatt Cook', 'wyatt.cook@example.com', '852 Pine Rd, Capital City', '555-345-6783'),
    ('Riley Morgan', 'riley.morgan@example.com', '951 Cedar St, Springfield', '555-456-7894'),
    ('Gabriel Bell', 'gabriel.bell@example.com', '357 Birch Ln, Shelbyville', '555-567-8905'),
    ('Lillian Murphy', 'lillian.murphy@example.com', '258 Elm St, Capital City', '555-678-9016'),
    ('Carter Bailey', 'carter.bailey@example.com', '159 Willow Dr, Springfield', '555-789-0127'),
    ('Nora Rivera', 'nora.rivera@example.com', '753 Aspen Rd, Shelbyville', '555-890-1238'),
    ('Jayden Cooper', 'jayden.cooper@example.com', '852 Cherry Ln, Capital City', '555-901-2349'),
    ('Eleanor Richardson', 'eleanor.richardson@example.com', '951 Hickory St, Springfield', '555-012-3460'),
    ('Dylan Cox', 'dylan.cox@example.com', '357 Walnut Ave, Shelbyville', '555-123-4571'),
    ('Madison Howard', 'madison.howard@example.com', '258 Poplar St, Capital City', '555-234-5673'),
    ('Grayson Ward', 'grayson.ward@example.com', '159 Chestnut Rd, Springfield', '555-345-6784'),
    ('Hazel Torres', 'hazel.torres@example.com', '753 Maple St, Shelbyville', '555-456-7895'),
    ('Lincoln Peterson', 'lincoln.peterson@example.com', '852 Oak Ave, Capital City', '555-567-8906'),
    ('Aurora Gray', 'aurora.gray@example.com', '951 Pine Rd, Springfield', '555-678-9017'),
    ('Anthony Ramirez', 'anthony.ramirez@example.com', '357 Cedar St, Shelbyville', '555-789-0128'),
    ('Violet James', 'violet.james@example.com', '258 Birch Ln, Capital City', '555-890-1239'),
    ('Leo Watson', 'leo.watson@example.com', '159 Elm St, Springfield', '555-901-2350'),
    ('Savannah Brooks', 'savannah.brooks@example.com', '753 Willow Dr, Shelbyville', '555-012-3461'),
    ('Joshua Kelly', 'joshua.kelly@example.com', '852 Aspen Rd, Capital City', '555-123-4572'),
    ('Addison Sanders', 'addison.sanders@example.com', '951 Cherry Ln, Springfield', '555-234-5674'),
    ('Caleb Price', 'caleb.price@example.com', '357 Hickory St, Shelbyville', '555-345-6785'),
    ('Stella Bennett', 'stella.bennett@example.com', '258 Walnut Ave, Capital City', '555-456-7896'),
    ('Nathan Wood', 'nathan.wood@example.com', '159 Poplar St, Springfield', '555-567-8907'),
    ('Vera Barnes', 'vera.barnes@example.com', '753 Chestnut Rd, Shelbyville', '555-678-9018'),
    ('Christian Ross', 'christian.ross@example.com', '852 Maple St, Capital City', '555-789-0129'),
    ('Lucy Henderson', 'lucy.henderson@example.com', '951 Oak Ave, Springfield', '555-890-1240'),
    ('Hunter Coleman', 'hunter.coleman@example.com', '357 Pine Rd, Shelbyville', '555-901-2351'),
    ('Skylar Jenkins', 'skylar.jenkins@example.com', '258 Cedar St, Capital City', '555-012-3462'),
    ('Eli Perry', 'eli.perry@example.com', '159 Birch Ln, Springfield', '555-123-4573'),
    ('Claire Powell', 'claire.powell@example.com', '753 Elm St, Shelbyville', '555-234-5675'),
    ('Thomas Long', 'thomas.long@example.com', '852 Willow Dr, Capital City', '555-345-6786'),
    ('Paisley Patterson', 'paisley.patterson@example.com', '951 Aspen Rd, Springfield', '555-456-7897'),
    ('Isaac Hughes', 'isaac.hughes@example.com', '357 Cherry Ln, Shelbyville', '555-567-8908'),
    ('Anna Flores', 'anna.flores@example.com', '258 Hickory St, Capital City', '555-678-9019'),
    ('Charles Washington', 'charles.washington@example.com', '159 Walnut Ave, Springfield', '555-789-0130'),
    ('Emily Butler', 'emily.butler@example.com', '753 Poplar St, Shelbyville', '555-890-1241'),
    ('Christopher Simmons', 'christopher.simmons@example.com', '852 Chestnut Rd, Capital City', '555-901-2352'),
    ('Elizabeth Foster', 'elizabeth.foster@example.com', '951 Maple St, Springfield', '555-012-3463'),
    ('Andrew Gonzales', 'andrew.gonzales@example.com', '357 Oak Ave, Shelbyville', '555-123-4574'),
    ('Sofia Bryant', 'sofia.bryant@example.com', '258 Pine Rd, Capital City', '555-234-5676'),
    ('Joshua Alexander', 'joshua.alexander@example.com', '159 Cedar St, Springfield', '555-345-6787'),
    ('Nora Russell', 'nora.russell@example.com', '753 Birch Ln, Shelbyville', '555-456-7898'),
    ('Ryan Griffin', 'ryan.griffin@example.com', '852 Elm St, Capital City', '555-567-8909'),
    ('Hannah Diaz', 'hannah.diaz@example.com', '951 Willow Dr, Springfield', '555-678-9020'),
    ('Nathaniel Hayes', 'nathaniel.hayes@example.com', '357 Aspen Rd, Shelbyville', '555-789-0131'),
    ('Lillian Myers', 'lillian.myers@example.com', '258 Cherry Ln, Capital City', '555-890-1242'),
    ('Cameron Ford', 'cameron.ford@example.com', '159 Hickory St, Springfield', '555-901-2353'),
    ('Leah Hamilton', 'leah.hamilton@example.com', '753 Walnut Ave, Shelbyville', '555-012-3464'),
    ('Brayden Graham', 'brayden.graham@example.com', '852 Poplar St, Capital City', '555-123-4575'),
    ('Zoe Sullivan', 'zoe.sullivan@example.com', '951 Chestnut Rd, Springfield', '555-234-5677'),
    ('Christian Wallace', 'christian.wallace@example.com', '357 Maple St, Shelbyville', '555-345-6788'),
    ('Stella West', 'stella.west@example.com', '258 Oak Ave, Capital City', '555-456-7899'),
    ('Aaron Cole', 'aaron.cole@example.com', '159 Pine Rd, Springfield', '555-567-8910'),
    ('Victoria Jordan', 'victoria.jordan@example.com', '753 Cedar St, Shelbyville', '555-678-9021'),
    ('Wyatt Reynolds', 'wyatt.reynolds@example.com', '852 Birch Ln, Capital City', '555-789-0132'),
    ('Ella Griffin', 'ella.griffin@example.com', '951 Elm St, Springfield', '555-890-1243'),
    ('Lincoln Simmons', 'lincoln.simmons@example.com', '357 Willow Dr, Shelbyville', '555-901-2354'),
    ('Lila Price', 'lila.price@example.com', '258 Aspen Rd, Capital City', '555-012-3465'),
    ('Julian Bennett', 'julian.bennett@example.com', '159 Cherry Ln, Springfield', '555-123-4576'),
    ('Zara Coleman', 'zara.coleman@example.com', '753 Hickory St, Shelbyville', '555-234-5678'),
    ('Asher Reed', 'asher.reed@example.com', '852 Walnut Ave, Capital City', '555-345-6789'),
    ('Savannah Powell', 'savannah.powell@example.com', '951 Poplar St, Springfield', '555-456-7900'),
    ('Levi Russell', 'levi.russell@example.com', '357 Chestnut Rd, Shelbyville', '555-567-8911'),
    ('Penelope Ward', 'penelope.ward@example.com', '258 Maple St, Capital City', '555-678-9022'),
    ('Ezra Brooks', 'ezra.brooks@example.com', '159 Oak Ave, Springfield', '555-789-0133'),
    ('Audrey Diaz', 'audrey.diaz@example.com', '753 Pine Rd, Shelbyville', '555-890-1244'),
    ('Thomas Bryant', 'thomas.bryant@example.com', '852 Cedar St, Capital City', '555-901-2355'),
    ('Clara Patterson', 'clara.patterson@example.com', '951 Birch Ln, Springfield', '555-012-3466'),
    ('Isaiah Henderson', 'isaiah.henderson@example.com', '357 Elm St, Shelbyville', '555-123-4577'),
    ('Violet Wells', 'violet.wells@example.com', '258 Willow Dr, Capital City', '555-234-5679'),
    ('Nathan Fisher', 'nathan.fisher@example.com', '159 Aspen Rd, Springfield', '555-345-6790'),
    ('Hannah Ellis', 'hannah.ellis@example.com', '753 Cherry Ln, Shelbyville', '555-456-7901'),
    ('Owen Simmons', 'owen.simmons@example.com', '852 Hickory St, Capital City', '555-567-8912'),
    ('Nora Griffin', 'nora.griffin@example.com', '951 Walnut Ave, Springfield', '555-678-9023'),
    ('Julian Bryant', 'julian.bryant@example.com', '357 Poplar St, Shelbyville', '555-789-0134'),
    ('Clara Morris', 'clara.morris@example.com', '258 Chestnut Rd, Capital City', '555-890-1245'),
    ('Isaac Wood', 'isaac.wood@example.com', '159 Maple St, Springfield', '555-901-2356'),
    ('Lydia James', 'lydia.james@example.com', '753 Oak Ave, Shelbyville', '555-012-3467')""")

    conn.commit()
    cursor.close()
    conn.close()

