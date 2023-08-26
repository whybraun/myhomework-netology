import os
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Stock, Shop, Sale, create_tables
import sqlalchemy as sq
import json

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

publisher_name = input("Введите имя издателя: ")

publisher = session.query(Publisher).filter(Publisher.name.like(f'%{publisher_name}%')).first()

if publisher:
    books = session.query(Book).filter(Book.id_publisher == publisher.id).all()

    for book in books:
        sales = (
            session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
            .select_from(Book)
            .join(Stock)
            .join(Shop)
            .join(Sale)
            .filter(Book.id == book.id)
            .all()
        )

        for sale in sales:
            title, shop_name, price, sale_date = sale
            formatted_date = sale_date.strftime("%d-%m-%Y")
            print(f"{title} | {shop_name} | {price} | {formatted_date}")
else:
    print("Издатель не найден.")

# data_file_path = 'myhomework-netology/12. Working with SQL Database creation/Python and DB.ORM/fixtures/tests_data.json'

# with open(data_file_path, 'r') as fd:
#     data = json.load(fd)

# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     print(f"Adding record: {record}")
#     session.add(model(id=record.get('pk'), **record.get('fields')))

#     session.commit()

session.close()
