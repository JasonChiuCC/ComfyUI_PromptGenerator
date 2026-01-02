from .mountains_handler import MountainsHandler
from .forest_handler import ForestHandler
from .desert_handler import DesertHandler
from .canyon_handler import CanyonHandler
from .cave_handler import CaveHandler
from .arctic_handler import ArcticHandler
from .volcano_handler import VolcanoHandler
from .meadow_handler import MeadowHandler
from .ocean_handler import OceanHandler
from .underwater_handler import UnderwaterHandler
from .waterfall_handler import WaterfallHandler
from .lake_handler import LakeHandler
from .coastal_handler import CoastalHandler
from .sunset_handler import SunsetHandler
from .sunrise_handler import SunriseHandler
from .night_sky_handler import NightSkyHandler
from .aurora_handler import AuroraHandler
from .storm_handler import StormHandler
from .fog_handler import FogHandler
from .rainbow_handler import RainbowHandler
from .cherry_blossom_handler import CherryBlossomHandler
from .autumn_foliage_handler import AutumnFoliageHandler

NATURE_HANDLERS = {
    # Terrain
    "mountains": MountainsHandler,
    "forest": ForestHandler,
    "desert": DesertHandler,
    "canyon": CanyonHandler,
    "cave": CaveHandler,
    "arctic": ArcticHandler,
    "volcano": VolcanoHandler,
    "meadow": MeadowHandler,
    # Water
    "ocean": OceanHandler,
    "underwater": UnderwaterHandler,
    "waterfall": WaterfallHandler,
    "lake": LakeHandler,
    "coastal": CoastalHandler,
    # Sky & Atmosphere
    "sunset": SunsetHandler,
    "sunrise": SunriseHandler,
    "night_sky": NightSkyHandler,
    "aurora": AuroraHandler,
    "storm": StormHandler,
    "fog": FogHandler,
    "rainbow": RainbowHandler,
    # Seasonal
    "cherry_blossom": CherryBlossomHandler,
    "autumn_foliage": AutumnFoliageHandler,
}

__all__ = [
    # Terrain
    "MountainsHandler", "ForestHandler", "DesertHandler", "CanyonHandler",
    "CaveHandler", "ArcticHandler", "VolcanoHandler", "MeadowHandler",
    # Water
    "OceanHandler", "UnderwaterHandler", "WaterfallHandler", "LakeHandler",
    "CoastalHandler",
    # Sky & Atmosphere
    "SunsetHandler", "SunriseHandler", "NightSkyHandler", "AuroraHandler",
    "StormHandler", "FogHandler", "RainbowHandler",
    # Seasonal
    "CherryBlossomHandler", "AutumnFoliageHandler",
    # Mapping
    "NATURE_HANDLERS",
]



