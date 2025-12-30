from .isometric_handler import IsometricHandler
from .low_poly_handler import LowPolyHandler
from .clay_render_handler import ClayRenderHandler
from .wireframe_handler import WireframeHandler
from .voxel_handler import VoxelHandler
from .unreal_engine_handler import UnrealEngineHandler
from .stylized_3d_handler import Stylized3DHandler
from .octane_handler import OctaneHandler
from .cinema4d_handler import Cinema4DHandler
from .blender_handler import BlenderHandler
from .product_render_handler import ProductRenderHandler
from .arch_viz_handler import ArchVizHandler
from .glass_3d_handler import Glass3DHandler
from .holographic_handler import HolographicHandler

RENDER3D_HANDLERS = {
    "isometric": IsometricHandler,
    "low_poly": LowPolyHandler,
    "clay_render": ClayRenderHandler,
    "wireframe": WireframeHandler,
    "voxel": VoxelHandler,
    "unreal_engine": UnrealEngineHandler,
    "stylized_3d": Stylized3DHandler,
    "octane": OctaneHandler,
    "cinema4d": Cinema4DHandler,
    "blender": BlenderHandler,
    "product_render": ProductRenderHandler,
    "arch_viz": ArchVizHandler,
    "glass_3d": Glass3DHandler,
    "holographic": HolographicHandler,
}

__all__ = [
    "IsometricHandler",
    "LowPolyHandler",
    "ClayRenderHandler",
    "WireframeHandler",
    "VoxelHandler",
    "UnrealEngineHandler",
    "Stylized3DHandler",
    "OctaneHandler",
    "Cinema4DHandler",
    "BlenderHandler",
    "ProductRenderHandler",
    "ArchVizHandler",
    "Glass3DHandler",
    "HolographicHandler",
    "RENDER3D_HANDLERS",
]

