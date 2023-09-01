import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Stock, Shop, Sale, create_tables
import sqlalchemy as sq
import json

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DSN = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = sq.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def get_publisher_data(session, input_data):
    query = session.query(
        Book.title, Shop.name, Sale.price, Sale.date_sale
    ).select_from(Book).join(Stock).join(Shop).join(Sale).join(Publisher)

    if input_data.isdigit():
        publisher_data = query.filter(Publisher.id == int(input_data)).all()
    else:
        publisher_data = query.filter(Publisher.name.like(f'%{input_data}%')).all()

    for data in publisher_data:
        title, shop_name, price, sale_date = data
        formatted_date = sale_date.strftime("%d-%m-%Y")
        print(f"{title: <40} | {shop_name: <10} | {price: <8} | {formatted_date}")

def add_data_to_tables(session):
    data_file_path = 'myhomework-netology/12. Working with SQL Database creation/Python and DB.ORM/fixtures/tests_data.json'

    with open(data_file_path, 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))

        session.commit()
    
if __name__ == '__main__':
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    add_data_to_tables(session)

    user_input = input("Введите имя или ID издателя: ")
    get_publisher_data(session, user_input)

    session.close()