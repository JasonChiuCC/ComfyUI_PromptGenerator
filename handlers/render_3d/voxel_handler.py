"""Voxel 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class VoxelHandler(BaseThemeHandler):
    """Handler for voxel 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate voxel 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("voxel.subjects", "voxel character")
        
        view = self._get_random_choice("voxel.view_types", "voxel art view")
        
        components["subject"] = (
            f"((voxel art 3D)) {subject}, "
            f"{view}, cubic pixel style"
        )
        
        if include_environment:
            scene = self._get_random_choice("voxel.scenes", "voxel world")
            components["environment"] = f"in {scene}, blocky environment"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("voxel.styles", "MagicaVoxel style")
            components["style"] = f"{style}, 3D pixel art, Minecraft aesthetic"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "cubic voxels, blocky charm, retro 3D pixels"
        else:
            components["effects"] = ""
        
        return components
