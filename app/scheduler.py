from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.config import settings

scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")


async def scrape_autoria():
    print("Scraping started...")
    # тут пізніше буде scraper


async def dump_database():
    print("Database dump started...")
    # тут пізніше буде pg_dump


def parse_time(time_str: str) -> tuple[int, int]:
    hour, minute = time_str.split(":")
    return int(hour), int(minute)


def start_scheduler():
    scrape_hour, scrape_minute = parse_time(settings.scrape_time)
    dump_hour, dump_minute = parse_time(settings.dump_time)

    scheduler.add_job(
        scrape_autoria,
        CronTrigger(hour=scrape_hour, minute=scrape_minute),
        name="daily_autoria_scrape",
        replace_existing=True,
    )

    scheduler.add_job(
        dump_database,
        CronTrigger(hour=dump_hour, minute=dump_minute),
        name="daily_db_dump",
        replace_existing=True,
    )

    scheduler.start()
