from sqlalchemy import BigInteger, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass



class User(Base):
    __tablename__="users"

    id:  Mapped[int]=mapped_column(primary_key=True)
    tg_id:  Mapped[int]=mapped_column(BigInteger, unique=True, nullable=False)
    full_name:  Mapped[str]=mapped_column(String, nullable=False )
    phone:  Mapped[str]=mapped_column(String, nullable=False )
    create_at:  Mapped[DateTime]=mapped_column(DateTime, server_default=func.now())



    def __repr__(self):
        return f"<User tg_id={self.tg_id} full_name={self.full_name}:"
    