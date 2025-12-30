"""Sci-Fi theme handlers."""

from .cyberpunk_handler import CyberpunkHandler
from .steampunk_handler import SteampunkHandler
from .dieselpunk_handler import DieselpunkHandler
from .atompunk_handler import AtompunkHandler
from .solarpunk_handler import SolarpunkHandler
from .biopunk_handler import BiopunkHandler
from .raypunk_handler import RaypunkHandler
from .space_opera_handler import SpaceOperaHandler
from .spacecraft_handler import SpacecraftHandler
from .space_station_handler import SpaceStationHandler
from .alien_world_handler import AlienWorldHandler
from .colony_planet_handler import ColonyPlanetHandler
from .futuristic_city_handler import FuturisticCityHandler
from .neon_future_handler import NeonFutureHandler
from .ai_dystopia_handler import AIDystopiaHandler
from .post_apocalyptic_handler import PostApocalypticHandler
from .robot_handler import RobotHandler
from .retrofuturism_handler import RetrofuturismHandler
from .hard_scifi_handler import HardSciFiHandler
from .pulp_scifi_handler import PulpSciFiHandler

SCIFI_HANDLERS = {
    "cyberpunk": CyberpunkHandler,
    "steampunk": SteampunkHandler,
    "dieselpunk": DieselpunkHandler,
    "atompunk": AtompunkHandler,
    "solarpunk": SolarpunkHandler,
    "biopunk": BiopunkHandler,
    "raypunk": RaypunkHandler,
    "space_opera": SpaceOperaHandler,
    "spacecraft": SpacecraftHandler,
    "space_station": SpaceStationHandler,
    "alien_world": AlienWorldHandler,
    "colony_planet": ColonyPlanetHandler,
    "futuristic_city": FuturisticCityHandler,
    "neon_future": NeonFutureHandler,
    "ai_dystopia": AIDystopiaHandler,
    "post_apocalyptic": PostApocalypticHandler,
    "robot": RobotHandler,
    "retrofuturism": RetrofuturismHandler,
    "hard_scifi": HardSciFiHandler,
    "pulp_scifi": PulpSciFiHandler,
}

__all__ = [
    "CyberpunkHandler",
    "SteampunkHandler",
    "DieselpunkHandler",
    "AtompunkHandler",
    "SolarpunkHandler",
    "BiopunkHandler",
    "RaypunkHandler",
    "SpaceOperaHandler",
    "SpacecraftHandler",
    "SpaceStationHandler",
    "AlienWorldHandler",
    "ColonyPlanetHandler",
    "FuturisticCityHandler",
    "NeonFutureHandler",
    "AIDystopiaHandler",
    "PostApocalypticHandler",
    "RobotHandler",
    "RetrofuturismHandler",
    "HardSciFiHandler",
    "PulpSciFiHandler",
    "SCIFI_HANDLERS",
]






