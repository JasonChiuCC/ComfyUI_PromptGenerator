"""Horror & Dark theme handlers."""

from .vampire_handler import VampireHandler
from .werewolf_handler import WerewolfHandler
from .zombie_handler import ZombieHandler
from .witch_handler import WitchHandler
from .slasher_handler import SlasherHandler
from .j_horror_handler import JHorrorHandler
from .psychological_handler import PsychologicalHandler
from .body_horror_handler import BodyHorrorHandler
from .folk_horror_handler import FolkHorrorHandler
from .survival_horror_handler import SurvivalHorrorHandler
from .victorian_gothic_handler import VictorianGothicHandler
from .southern_gothic_handler import SouthernGothicHandler
from .haunted_handler import HauntedHandler
from .nightmare_handler import NightmareHandler
from .lovecraftian_handler import LovecraftianHandler
from .demonic_handler import DemonicHandler
from .occult_handler import OccultHandler
from .creepypasta_handler import CreepypastaHandler

HORROR_HANDLERS = {
    "vampire": VampireHandler,
    "werewolf": WerewolfHandler,
    "zombie": ZombieHandler,
    "witch": WitchHandler,
    "slasher": SlasherHandler,
    "j_horror": JHorrorHandler,
    "psychological": PsychologicalHandler,
    "body_horror": BodyHorrorHandler,
    "folk_horror": FolkHorrorHandler,
    "survival_horror": SurvivalHorrorHandler,
    "victorian_gothic": VictorianGothicHandler,
    "southern_gothic": SouthernGothicHandler,
    "haunted": HauntedHandler,
    "nightmare": NightmareHandler,
    "lovecraftian": LovecraftianHandler,
    "demonic": DemonicHandler,
    "occult": OccultHandler,
    "creepypasta": CreepypastaHandler,
}

__all__ = [
    "VampireHandler",
    "WerewolfHandler",
    "ZombieHandler",
    "WitchHandler",
    "SlasherHandler",
    "JHorrorHandler",
    "PsychologicalHandler",
    "BodyHorrorHandler",
    "FolkHorrorHandler",
    "SurvivalHorrorHandler",
    "VictorianGothicHandler",
    "SouthernGothicHandler",
    "HauntedHandler",
    "NightmareHandler",
    "LovecraftianHandler",
    "DemonicHandler",
    "OccultHandler",
    "CreepypastaHandler",
    "HORROR_HANDLERS",
]



