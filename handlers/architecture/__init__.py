from .modern_architecture_handler import ModernArchitectureHandler
from .brutalist_handler import BrutalistHandler
from .art_deco_arch_handler import ArtDecoArchHandler
from .gothic_cathedral_handler import GothicCathedralHandler
from .japanese_arch_handler import JapaneseArchHandler
from .mediterranean_arch_handler import MediterraneanArchHandler
from .skyscraper_handler import SkyscraperHandler
from .castle_handler import CastleHandler
from .temple_handler import TempleHandler
from .bridge_handler import BridgeHandler
from .victorian_house_handler import VictorianHouseHandler
from .industrial_arch_handler import IndustrialArchHandler
from .interior_handler import InteriorHandler
from .cityscape_handler import CityscapeHandler
from .village_handler import VillageHandler
from .abandoned_handler import AbandonedHandler

ARCHITECTURE_HANDLERS = {
    "modern_architecture": ModernArchitectureHandler,
    "brutalist": BrutalistHandler,
    "art_deco_arch": ArtDecoArchHandler,
    "gothic_cathedral": GothicCathedralHandler,
    "japanese_arch": JapaneseArchHandler,
    "mediterranean_arch": MediterraneanArchHandler,
    "skyscraper": SkyscraperHandler,
    "castle": CastleHandler,
    "temple": TempleHandler,
    "bridge": BridgeHandler,
    "victorian_house": VictorianHouseHandler,
    "industrial_arch": IndustrialArchHandler,
    "interior": InteriorHandler,
    "cityscape": CityscapeHandler,
    "village": VillageHandler,
    "abandoned": AbandonedHandler,
}

__all__ = [
    "ModernArchitectureHandler", "BrutalistHandler", "ArtDecoArchHandler",
    "GothicCathedralHandler", "JapaneseArchHandler", "MediterraneanArchHandler",
    "SkyscraperHandler", "CastleHandler", "TempleHandler", "BridgeHandler",
    "VictorianHouseHandler", "IndustrialArchHandler", "InteriorHandler",
    "CityscapeHandler", "VillageHandler", "AbandonedHandler",
    "ARCHITECTURE_HANDLERS",
]



