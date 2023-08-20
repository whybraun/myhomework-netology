import psycopg2

def create_db(conn):
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Clients (
            client_id SERIAL PRIMARY KEY,
            first_name VARCHAR(60) NOT NULL,
            last_name VARCHAR(60) NOT NULL,
            email VARCHAR(60) NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Phones (
            phone_id SERIAL PRIMARY KEY,
            client_id INTEGER,
            phone_number VARCHAR(120),
            FOREIGN KEY (client_id) REFERENCES Clients(client_id)
        )
    ''')

    conn.commit()

def add_client(conn, first_name, last_name, email):
    cur = conn.cursor()

    cur.execute('''
            INSERT INTO Clients (first_name, last_name, email)
            VALUES(%s, %s, %s)
            RETURNING client_id''', (first_name, last_name, email))
    
    conn.commit()

    return cur.fetchone()[0]
    
def add_phone(conn, client_id, phone_number):
    cur = conn.cursor()

    cur.execute('''
            INSERT INTO Phones (client_id, phone_number)
            VALUES(%s, %s)''', (client_id, phone_number))
    
    conn.commit()

def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    cur = conn.cursor()

    change_query = '''
            UPDATE Clients
            SET first_name = %s, last_name = %s, email = %s
            WHERE client_id = %s'''
    
    cur.execute(change_query, (first_name, last_name, email, client_id))

    conn.commit()

def delete_phone(conn, client_id, phone):
    cur = conn.cursor()

    select_phone_query = '''
        SELECT phone_id
        FROM Phones
        WHERE client_id = %s AND phone_number = %s'''
    
    cur.execute(select_phone_query, (client_id, phone))
    phone_id = cur.fetchone()[0]

    delete_query = '''
        DELETE FROM Phones
        WHERE phone_id = %s
    '''
    cur.execute(delete_query, (phone_id,))
    conn.commit()

def delete_client(conn, client_id):
    cur = conn.cursor()

    del_query_phones = '''
            DELETE FROM Phones
            WHERE client_id = %s'''    
    
    cur.execute(del_query_phones, (client_id,))

    del_query_clients = '''
            DELETE FROM Clients
            WHERE client_id = %s'''
    
    cur.execute(del_query_clients, (client_id,))

    conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur = conn.cursor()

    select_query = '''
        SELECT client_id, first_name, last_name, email
        FROM Clients
        WHERE 
            (first_name = %s OR %s IS NULL) AND
            (last_name = %s OR %s IS NULL) AND
            (email = %s OR %s IS NULL) AND
            client_id IN (
                SELECT client_id
                FROM Phones
                WHERE phone_number = %s OR %s IS NULL
            )'''

    cur.execute(select_query, (first_name, first_name, last_name, last_name, email, email, phone, phone))
    results = cur.fetchall()

    return results

conn_params = {
    "database": "client_db",
    "user": "postgres",
    "password": "postgres"
}

with psycopg2.connect(**conn_params) as conn:
    # create_db(conn)
    
    # add_client(conn, "Netology", "Client", "netology@netology.ru")
    
    # add_phone(conn, 1, "+74951525528")
    
    # change_client(conn, 1, first_name="Netology-test", last_name="Client", email="netology@netology.ru")
    
    # delete_phone(conn, 1, "+74951525528")
    
    # delete_client(conn, 1)

    results = find_client(conn, first_name="Netology", last_name="Client")
    for row in results:
        client_id, first_name, last_name, email = row
        print(f"Client: {client_id}, {first_name} {last_name}, {email}")