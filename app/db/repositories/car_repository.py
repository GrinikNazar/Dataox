from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Car


class CarRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert_car(self, car_data: dict) -> None:
        # Вставка одного авто з ігноруванням дублів
        stmt = (
            insert(Car)
            .values(**car_data)
            .on_conflict_do_nothing(index_elements=["url"])
        )

        await self.session.execute(stmt)
        await self.session.commit()

    async def bulk_insert_cars(self, cars_data: list[dict]) -> None:
        # Масова вставка
        if not cars_data:
            return

        stmt = (
            insert(Car)
            .values(cars_data)
            .on_conflict_do_nothing(index_elements=["url"])
        )

        await self.session.execute(stmt)
        await self.session.commit()
