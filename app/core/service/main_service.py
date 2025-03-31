from asyncio import sleep
from datetime import datetime, timedelta
from random import randint

from app.core.dependencies import get_db
from app.core.models.models import FactModel
from logger import logger


async def loop():
    count = 0
    timestamp: datetime = datetime(2026, 7, 6, 1)
    while count < 2840:
        for sector_id in range(2, 66):
            async with get_db() as session_instance:
                fact_instance = FactModel(
                    is_avalanche=bool(randint(0, 1)),
                    timestamp=timestamp,
                    sector_id=sector_id,
                )
                session_instance.add(fact_instance)
                await session_instance.flush()
                await session_instance.commit()
                logger.info(f"Создана запись для {fact_instance.sector_id}")
            count += 1
            timestamp += timedelta(hours=1)
            await sleep(5)
