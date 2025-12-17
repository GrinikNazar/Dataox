from sqlalchemy import String, Integer, DateTime, func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)

    url: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    price_usd: Mapped[int] = mapped_column(Integer, nullable=False)

    odometer: Mapped[int] = mapped_column(Integer, nullable=False)

    username: Mapped[str] = mapped_column(String, nullable=True)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)

    image_url: Mapped[str] = mapped_column(String, nullable=True)
    images_count: Mapped[int] = mapped_column(Integer, nullable=True)

    car_number: Mapped[str] = mapped_column(String, nullable=True)
    car_vin: Mapped[str] = mapped_column(String, nullable=True)

    datetime_found: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    __table_args__ = (
        UniqueConstraint("url", name="uq_car_url"),
    )
