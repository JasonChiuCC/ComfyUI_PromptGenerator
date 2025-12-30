"""Animals & Creatures theme handlers."""

from .cat_handler import CatHandler
from .dog_handler import DogHandler
from .wolf_handler import WolfHandler
from .fox_handler import FoxHandler
from .horse_handler import HorseHandler
from .wildlife_art_handler import WildlifeArtHandler
from .pets_handler import PetsHandler
from .birds_handler import BirdsHandler
from .marine_life_handler import MarineLifeHandler
from .underwater_creatures_handler import UnderwaterCreaturesHandler
from .insects_handler import InsectsHandler
from .dragon_handler import DragonHandler
from .unicorn_handler import UnicornHandler
from .phoenix_handler import PhoenixHandler
from .dinosaur_handler import DinosaurHandler
from .kaiju_handler import KaijuHandler
from .mythical_beasts_handler import MythicalBeastsHandler
from .mermaid_handler import MermaidHandler
from .monster_handler import MonsterHandler

ANIMALS_HANDLERS = {
    "cat": CatHandler,
    "dog": DogHandler,
    "wolf": WolfHandler,
    "fox": FoxHandler,
    "horse": HorseHandler,
    "wildlife_art": WildlifeArtHandler,
    "pets": PetsHandler,
    "birds": BirdsHandler,
    "marine_life": MarineLifeHandler,
    "underwater_creatures": UnderwaterCreaturesHandler,
    "insects": InsectsHandler,
    "dragon": DragonHandler,
    "unicorn": UnicornHandler,
    "phoenix": PhoenixHandler,
    "dinosaur": DinosaurHandler,
    "kaiju": KaijuHandler,
    "mythical_beasts": MythicalBeastsHandler,
    "mermaid": MermaidHandler,
    "monster": MonsterHandler,
}

__all__ = [
    "CatHandler",
    "DogHandler",
    "WolfHandler",
    "FoxHandler",
    "HorseHandler",
    "WildlifeArtHandler",
    "PetsHandler",
    "BirdsHandler",
    "MarineLifeHandler",
    "UnderwaterCreaturesHandler",
    "InsectsHandler",
    "DragonHandler",
    "UnicornHandler",
    "PhoenixHandler",
    "DinosaurHandler",
    "KaijuHandler",
    "MythicalBeastsHandler",
    "MermaidHandler",
    "MonsterHandler",
    "ANIMALS_HANDLERS",
]






