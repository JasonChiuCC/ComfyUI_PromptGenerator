from .cinematic_handler import CinematicHandler
from .studio_photo_handler import StudioPhotoHandler
from .street_photo_handler import StreetPhotoHandler
from .documentary_handler import DocumentaryHandler
from .macro_handler import MacroHandler
from .long_exposure_handler import LongExposureHandler
from .aerial_drone_handler import AerialDroneHandler
from .tilt_shift_handler import TiltShiftHandler
from .bokeh_handler import BokehHandler
from .double_exposure_handler import DoubleExposureHandler
from .hdr_handler import HDRHandler
from .black_white_handler import BlackWhiteHandler
from .film_grain_handler import FilmGrainHandler
from .food_photo_handler import FoodPhotoHandler
from .sports_photo_handler import SportsPhotoHandler
from .wildlife_photo_handler import WildlifePhotoHandler
from .golden_hour_handler import GoldenHourHandler
from .blue_hour_handler import BlueHourHandler
from .silhouette_handler import SilhouetteHandler

PHOTOGRAPHY_HANDLERS = {
    "cinematic": CinematicHandler,
    "studio_photo": StudioPhotoHandler,
    "street_photo": StreetPhotoHandler,
    "documentary": DocumentaryHandler,
    "macro": MacroHandler,
    "long_exposure": LongExposureHandler,
    "aerial_drone": AerialDroneHandler,
    "tilt_shift": TiltShiftHandler,
    "bokeh": BokehHandler,
    "double_exposure": DoubleExposureHandler,
    "hdr": HDRHandler,
    "black_white": BlackWhiteHandler,
    "film_grain": FilmGrainHandler,
    "food_photo": FoodPhotoHandler,
    "sports_photo": SportsPhotoHandler,
    "wildlife_photo": WildlifePhotoHandler,
    "golden_hour": GoldenHourHandler,
    "blue_hour": BlueHourHandler,
    "silhouette": SilhouetteHandler,
}

__all__ = [
    "CinematicHandler",
    "StudioPhotoHandler",
    "StreetPhotoHandler",
    "DocumentaryHandler",
    "MacroHandler",
    "LongExposureHandler",
    "AerialDroneHandler",
    "TiltShiftHandler",
    "BokehHandler",
    "DoubleExposureHandler",
    "HDRHandler",
    "BlackWhiteHandler",
    "FilmGrainHandler",
    "FoodPhotoHandler",
    "SportsPhotoHandler",
    "WildlifePhotoHandler",
    "GoldenHourHandler",
    "BlueHourHandler",
    "SilhouetteHandler",
    "PHOTOGRAPHY_HANDLERS",
]






