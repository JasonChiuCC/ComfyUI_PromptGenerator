from .classic_portrait_handler import ClassicPortraitHandler
from .fine_art_portrait_handler import FineArtPortraitHandler
from .environmental_portrait_handler import EnvironmentalPortraitHandler
from .moody_portrait_handler import MoodyPortraitHandler
from .dramatic_portrait_handler import DramaticPortraitHandler
from .ethereal_handler import EtherealHandler
from .fashion_handler import FashionHandler
from .beauty_handler import BeautyHandler
from .editorial_handler import EditorialHandler
from .corporate_handler import CorporateHandler
from .glamour_handler import GlamourHandler
from .lifestyle_handler import LifestyleHandler
from .fitness_handler import FitnessHandler
from .boudoir_handler import BoudoirHandler
from .cosplay_handler import CosplayHandler
from .maternity_handler import MaternityHandler
from .headshot_handler import HeadshotHandler
from .couple_handler import CoupleHandler
from .group_photo_handler import GroupPhotoHandler
from .street_style_handler import StreetStyleHandler
from .vintage_portrait_handler import VintagePortraitHandler
from .candid_portrait_handler import CandidPortraitHandler
from .character_portrait_handler import CharacterPortraitHandler
from .film_portrait_handler import FilmPortraitHandler

PORTRAIT_HANDLERS = {
    "classic_portrait": ClassicPortraitHandler,
    "fine_art_portrait": FineArtPortraitHandler,
    "environmental_portrait": EnvironmentalPortraitHandler,
    "moody_portrait": MoodyPortraitHandler,
    "dramatic_portrait": DramaticPortraitHandler,
    "ethereal": EtherealHandler,
    "fashion": FashionHandler,
    "beauty": BeautyHandler,
    "editorial": EditorialHandler,
    "corporate": CorporateHandler,
    "glamour": GlamourHandler,
    "lifestyle": LifestyleHandler,
    "fitness": FitnessHandler,
    "boudoir": BoudoirHandler,
    "cosplay": CosplayHandler,
    "maternity": MaternityHandler,
    "headshot": HeadshotHandler,
    "couple": CoupleHandler,
    "group_photo": GroupPhotoHandler,
    "street_style": StreetStyleHandler,
    "vintage_portrait": VintagePortraitHandler,
    "candid_portrait": CandidPortraitHandler,
    "character_portrait": CharacterPortraitHandler,
    "film_portrait": FilmPortraitHandler,
}

__all__ = [
    "ClassicPortraitHandler",
    "FineArtPortraitHandler",
    "EnvironmentalPortraitHandler",
    "MoodyPortraitHandler",
    "DramaticPortraitHandler",
    "EtherealHandler",
    "FashionHandler",
    "BeautyHandler",
    "EditorialHandler",
    "CorporateHandler",
    "GlamourHandler",
    "LifestyleHandler",
    "FitnessHandler",
    "BoudoirHandler",
    "CosplayHandler",
    "MaternityHandler",
    "HeadshotHandler",
    "CoupleHandler",
    "GroupPhotoHandler",
    "StreetStyleHandler",
    "VintagePortraitHandler",
    "CandidPortraitHandler",
    "CharacterPortraitHandler",
    "FilmPortraitHandler",
    "PORTRAIT_HANDLERS",
]





