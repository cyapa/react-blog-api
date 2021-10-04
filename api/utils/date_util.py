import datetime

UTC = datetime.timezone.utc

def get_utcnow() -> datetime.datetime:
    return datetime.datetime.now(tz=UTC)
