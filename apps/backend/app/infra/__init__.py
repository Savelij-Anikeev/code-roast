from .config import ConfigExtension
from .logger import LoggerExtension
from .pg import PgExtension
from .redis import RedisExtension

infra_list = [
    ConfigExtension,
    LoggerExtension,
    PgExtension,
    RedisExtension
]