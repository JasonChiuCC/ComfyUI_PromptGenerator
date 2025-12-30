"""Sketch & Drawing theme handlers."""

from .pencil_sketch_handler import PencilSketchHandler
from .charcoal_handler import CharcoalHandler
from .ink_drawing_handler import InkDrawingHandler
from .ballpoint_pen_handler import BallpointPenHandler
from .blueprint_handler import BlueprintHandler
from .technical_drawing_handler import TechnicalDrawingHandler
from .conte_handler import ConteHandler
from .graphite_handler import GraphiteHandler
from .gesture_handler import GestureHandler
from .stippling_handler import StipplingHandler
from .calligraphy_handler import CalligraphyHandler

__all__ = [
    'PencilSketchHandler',
    'CharcoalHandler',
    'InkDrawingHandler',
    'BallpointPenHandler',
    'BlueprintHandler',
    'TechnicalDrawingHandler',
    'ConteHandler',
    'GraphiteHandler',
    'GestureHandler',
    'StipplingHandler',
    'CalligraphyHandler',
]

# Handler class mapping
SKETCH_HANDLERS = {
    'pencil_sketch': PencilSketchHandler,
    'charcoal': CharcoalHandler,
    'ink_drawing': InkDrawingHandler,
    'ballpoint_pen': BallpointPenHandler,
    'blueprint': BlueprintHandler,
    'technical_drawing': TechnicalDrawingHandler,
    'conte': ConteHandler,
    'graphite': GraphiteHandler,
    'gesture': GestureHandler,
    'stippling': StipplingHandler,
    'calligraphy': CalligraphyHandler,
}





