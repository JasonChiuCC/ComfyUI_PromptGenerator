"""Art Styles theme handlers."""

from .abstract_handler import AbstractHandler
from .concept_art_handler import ConceptArtHandler
from .minimalist_handler import MinimalistHandler
from .surrealism_handler import SurrealismHandler
from .pop_art_handler import PopArtHandler
from .art_nouveau_handler import ArtNouveauHandler
from .art_deco_handler import ArtDecoHandler
from .cubism_handler import CubismHandler
from .expressionism_handler import ExpressionismHandler
from .impressionism_handler import ImpressionismHandler
from .baroque_handler import BaroqueHandler
from .renaissance_handler import RenaissanceHandler
from .psychedelic_handler import PsychedelicHandler
from .glitch_art_handler import GlitchArtHandler
from .graffiti_handler import GraffitiHandler
from .flat_design_handler import FlatDesignHandler
from .pointillism_handler import PointillismHandler
from .fauvism_handler import FauvismHandler
from .romanticism_handler import RomanticismHandler
from .bauhaus_handler import BauhausHandler
from .gothic_art_handler import GothicArtHandler
from .street_art_handler import StreetArtHandler

__all__ = [
    'AbstractHandler',
    'ConceptArtHandler',
    'MinimalistHandler',
    'SurrealismHandler',
    'PopArtHandler',
    'ArtNouveauHandler',
    'ArtDecoHandler',
    'CubismHandler',
    'ExpressionismHandler',
    'ImpressionismHandler',
    'BaroqueHandler',
    'RenaissanceHandler',
    'PsychedelicHandler',
    'GlitchArtHandler',
    'GraffitiHandler',
    'FlatDesignHandler',
    'PointillismHandler',
    'FauvismHandler',
    'RomanticismHandler',
    'BauhausHandler',
    'GothicArtHandler',
    'StreetArtHandler',
]

# Handler class mapping
ART_STYLES_HANDLERS = {
    'abstract': AbstractHandler,
    'concept_art': ConceptArtHandler,
    'minimalist': MinimalistHandler,
    'surrealism': SurrealismHandler,
    'pop_art': PopArtHandler,
    'art_nouveau': ArtNouveauHandler,
    'art_deco': ArtDecoHandler,
    'cubism': CubismHandler,
    'expressionism': ExpressionismHandler,
    'impressionism': ImpressionismHandler,
    'baroque': BaroqueHandler,
    'renaissance': RenaissanceHandler,
    'psychedelic': PsychedelicHandler,
    'glitch_art': GlitchArtHandler,
    'graffiti': GraffitiHandler,
    'flat_design': FlatDesignHandler,
    'pointillism': PointillismHandler,
    'fauvism': FauvismHandler,
    'romanticism': RomanticismHandler,
    'bauhaus': BauhausHandler,
    'gothic_art': GothicArtHandler,
    'street_art': StreetArtHandler,
}






