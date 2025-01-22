import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import Publisher, Book, Shop, Stock, Sale

Base = declarative_base()

DSN = "postgresql://postgres:5555@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()


def get_shops(publisher_input):
    query = session.query(
        Shop, Stock, Book, Publisher, Sale
    ).select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)

    if publisher_input.isdigit():
        query = query.filter(Publisher.id_publisher == int(publisher_input))
    else:
        query = query.filter(Publisher.publisher_name == publisher_input)

    results = query.all()

    for shop, stock, book, publisher, sale in results:
        print(f"{book.name: <40} | {shop.name: <10} | {sale.price: <8} | {sale.date:%d-%m-%Y}")


if __name__ == '__main__':
    publisher_input = input("Введите имя или идентификатор издателя: ")
    get_shops(publisher_input)

    session.close()