from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
Base = declarative_base()

# Definicja klasy reprezentującej tabelę w bazie danych
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Tworzenie wszystkich tabel
Base.metadata.create_all(engine)

# Utworzenie sesji
with Session(engine) as session:
    new_user = User(name="Jan Kowalski", age=30)
    session.add(new_user)
    session.commit()

# oeczyt danych z sesji
with Session(engine) as session:
    users = session.execute(text("SELECT * FROM users")).all()
    for user in users:
        print(f'{user.name}, {user.age}')

# aktualizacja istniejącego rekordu
with Session(engine) as session:
    user_to_update = session.get(User, 1) # Zalóżmy, że rekord z ID 1 istnieje
    if user_to_update:
        user_to_update.name = "Jan Nowak"
        session.commit()

# oeczyt danych z sesji
with Session(engine) as session:
    users = session.execute(text("SELECT * FROM users")).all()
    for user in users:
        print(f'{user.name}, {user.age}')


# Usuwanie rekordy z bazy
with Session(engine) as session:
    user_to_delete = session.get(User, 1)
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()