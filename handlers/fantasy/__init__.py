"""Fantasy theme handlers."""

from .epic_fantasy_handler import EpicFantasyHandler
from .dark_fantasy_handler import DarkFantasyHandler
from .high_fantasy_handler import HighFantasyHandler
from .low_fantasy_handler import LowFantasyHandler
from .urban_fantasy_handler import UrbanFantasyHandler
from .grimdark_handler import GrimdarkHandler
from .fairy_tale_handler import FairyTaleHandler
from .sword_sorcery_handler import SwordSorceryHandler
from .portal_fantasy_handler import PortalFantasyHandler
from .wizard_handler import WizardHandler
from .elven_handler import ElvenHandler
from .dwarven_handler import DwarvenHandler
from .greek_mythology_handler import GreekMythologyHandler
from .norse_mythology_handler import NorseMythologyHandler
from .celtic_fantasy_handler import CelticFantasyHandler
from .arabian_fantasy_handler import ArabianFantasyHandler
from .arthurian_handler import ArthurianHandler
from .wuxia_handler import WuxiaHandler
from .xianxia_handler import XianxiaHandler
from .isekai_handler import IsekaiHandler

FANTASY_HANDLERS = {
    "epic_fantasy": EpicFantasyHandler,
    "dark_fantasy": DarkFantasyHandler,
    "high_fantasy": HighFantasyHandler,
    "low_fantasy": LowFantasyHandler,
    "urban_fantasy": UrbanFantasyHandler,
    "grimdark": GrimdarkHandler,
    "fairy_tale": FairyTaleHandler,
    "sword_sorcery": SwordSorceryHandler,
    "portal_fantasy": PortalFantasyHandler,
    "wizard": WizardHandler,
    "elven": ElvenHandler,
    "dwarven": DwarvenHandler,
    "greek_mythology": GreekMythologyHandler,
    "norse_mythology": NorseMythologyHandler,
    "celtic_fantasy": CelticFantasyHandler,
    "arabian_fantasy": ArabianFantasyHandler,
    "arthurian": ArthurianHandler,
    "wuxia": WuxiaHandler,
    "xianxia": XianxiaHandler,
    "isekai": IsekaiHandler,
}

__all__ = [
    "EpicFantasyHandler",
    "DarkFantasyHandler",
    "HighFantasyHandler",
    "LowFantasyHandler",
    "UrbanFantasyHandler",
    "GrimdarkHandler",
    "FairyTaleHandler",
    "SwordSorceryHandler",
    "PortalFantasyHandler",
    "WizardHandler",
    "ElvenHandler",
    "DwarvenHandler",
    "GreekMythologyHandler",
    "NorseMythologyHandler",
    "CelticFantasyHandler",
    "ArabianFantasyHandler",
    "ArthurianHandler",
    "WuxiaHandler",
    "XianxiaHandler",
    "IsekaiHandler",
    "FANTASY_HANDLERS",
]






