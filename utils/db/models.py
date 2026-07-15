from sqlalchemy import BigInteger, String, DateTime, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id:         Mapped[int] = mapped_column(primary_key=True)
    tg_id:      Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    full_name:  Mapped[str] = mapped_column(String, nullable=False)
    phone:      Mapped[str] = mapped_column(String, nullable=False)
    create_at:  Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    stores: Mapped[list["Store"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"<User tg_id={self.tg_id} full_name={self.full_name}>"

class Store(Base):
    __tablename__ = "stores"

    id:          Mapped[int] = mapped_column(primary_key=True)
    user_id:     Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False) # Qaysi userga tegishli ekanligi
    name:        Mapped[str] = mapped_column(String, nullable=False)   # Do'kon nomi
    platform:    Mapped[str] = mapped_column(String, nullable=False)   # Uzum yoki Yandex market
    create_at:   Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="stores")

    def __repr__(self):
        return f"<Store name={self.name} platform={self.platform}>"