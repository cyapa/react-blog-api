import datetime

UTC = datetime.timezone.utc

#TODO: Use this util to Edit Blogs
def get_utcnow() -> datetime.datetime:
    return datetime.datetime.now(tz=UTC)
