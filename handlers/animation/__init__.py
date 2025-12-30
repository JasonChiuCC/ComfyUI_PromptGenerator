"""Animation theme handlers."""

from .anime_handler import AnimeHandler
from .ghibli_handler import GhibliHandler
from .manga_handler import MangaHandler
from .webtoon_handler import WebtoonHandler
from .mecha_handler import MechaHandler
from .shonen_handler import ShonenHandler
from .retro_anime_handler import RetroAnimeHandler
from .disney_handler import DisneyHandler
from .pixar_handler import PixarHandler
from .dreamworks_handler import DreamworksHandler
from .illumination_handler import IlluminationHandler
from .looney_tunes_handler import LooneyTunesHandler
from .south_park_handler import SouthParkHandler
from .marvel_handler import MarvelHandler
from .dc_comics_handler import DCComicsHandler
from .stop_motion_handler import StopMotionHandler
from .chibi_handler import ChibiHandler

__all__ = [
    'AnimeHandler',
    'GhibliHandler',
    'MangaHandler',
    'WebtoonHandler',
    'MechaHandler',
    'ShonenHandler',
    'RetroAnimeHandler',
    'DisneyHandler',
    'PixarHandler',
    'DreamworksHandler',
    'IlluminationHandler',
    'LooneyTunesHandler',
    'SouthParkHandler',
    'MarvelHandler',
    'DCComicsHandler',
    'StopMotionHandler',
    'ChibiHandler',
]

# Handler class mapping
ANIMATION_HANDLERS = {
    'anime': AnimeHandler,
    'ghibli': GhibliHandler,
    'manga': MangaHandler,
    'webtoon': WebtoonHandler,
    'mecha': MechaHandler,
    'shonen': ShonenHandler,
    'retro_anime': RetroAnimeHandler,
    'disney': DisneyHandler,
    'pixar': PixarHandler,
    'dreamworks': DreamworksHandler,
    'illumination': IlluminationHandler,
    'looney_tunes': LooneyTunesHandler,
    'south_park': SouthParkHandler,
    'marvel': MarvelHandler,
    'dc_comics': DCComicsHandler,
    'stop_motion': StopMotionHandler,
    'chibi': ChibiHandler,
}






