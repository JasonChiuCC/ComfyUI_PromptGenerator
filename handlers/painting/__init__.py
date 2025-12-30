"""Painting theme handlers."""

from .oil_painting_handler import OilPaintingHandler
from .watercolor_handler import WatercolorHandler
from .acrylic_handler import AcrylicHandler
from .gouache_handler import GouacheHandler
from .ink_wash_handler import InkWashHandler
from .pastel_handler import PastelHandler
from .colored_pencil_handler import ColoredPencilHandler
from .spray_paint_handler import SprayPaintHandler
from .crayon_handler import CrayonHandler
from .fresco_handler import FrescoHandler
from .tempera_handler import TemperaHandler
from .encaustic_handler import EncausticHandler
from .digital_painting_handler import DigitalPaintingHandler
from .mixed_media_handler import MixedMediaHandler
from .impasto_handler import ImpastoHandler

__all__ = [
    'OilPaintingHandler',
    'WatercolorHandler',
    'AcrylicHandler',
    'GouacheHandler',
    'InkWashHandler',
    'PastelHandler',
    'ColoredPencilHandler',
    'SprayPaintHandler',
    'CrayonHandler',
    'FrescoHandler',
    'TemperaHandler',
    'EncausticHandler',
    'DigitalPaintingHandler',
    'MixedMediaHandler',
    'ImpastoHandler',
]

# Handler class mapping
PAINTING_HANDLERS = {
    'oil_painting': OilPaintingHandler,
    'watercolor': WatercolorHandler,
    'acrylic': AcrylicHandler,
    'gouache': GouacheHandler,
    'ink_wash': InkWashHandler,
    'pastel': PastelHandler,
    'colored_pencil': ColoredPencilHandler,
    'spray_paint': SprayPaintHandler,
    'crayon': CrayonHandler,
    'fresco': FrescoHandler,
    'tempera': TemperaHandler,
    'encaustic': EncausticHandler,
    'digital_painting': DigitalPaintingHandler,
    'mixed_media': MixedMediaHandler,
    'impasto': ImpastoHandler,
}





