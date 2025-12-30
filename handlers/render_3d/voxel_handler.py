import random
from ...base_handler import BaseThemeHandler

class VoxelHandler(BaseThemeHandler):
    """Handler for Voxel 3D art style"""
    
    def get_theme_name(self) -> str:
        return "voxel"
    
    def generate_prompt(self, config: dict, seed: int = None) -> str:
        if seed is not None:
            random.seed(seed)
        
        subject = random.choice(config.get("subjects", ["voxel scene"]))
        style = random.choice(config.get("styles", ["voxel art"]))
        environment = random.choice(config.get("environments", ["simple background"]))
        lighting = random.choice(config.get("lighting", ["soft ambient occlusion"]))
        composition = random.choice(config.get("composition_types", ["isometric voxel view"]))
        detail = random.choice(config.get("details", ["detailed small voxels"]))
        
        prompt_parts = [
            f"{subject}",
            f"{style}",
            f"{detail}",
            f"{composition}",
            f"{lighting}",
            f"{environment}",
            "voxel art, cubic blocks, blocky 3D",
            "MagicaVoxel style, clean render"
        ]
        
        return ", ".join(prompt_parts)
    
    def get_negative_prompt(self) -> str:
        return "smooth curves, high poly, realistic, organic shapes, photographic, 2D pixel art"

