"""Mixed Media style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MixedMediaHandler(BaseThemeHandler):
    """Handler for mixed media art style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate mixed media prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("mixed_media.subjects", "abstract assemblage")
        
        composition = self._get_random_choice("mixed_media.composition_types", "collage assembly")
        technique = self._get_random_choice("mixed_media.techniques", "collage layering")
        material = self._get_random_choice("mixed_media.materials", "paper ephemera")
        
        components["subject"] = (
            f"((mixed media art)), {subject}, "
            f"{composition}, {technique}, incorporating {material}"
        )
        
        if include_environment:
            combination = self._get_random_choice("mixed_media.combinations", "paint and paper")
            mood = self._get_random_choice("mixed_media.moods", "experimental freedom")
            
            components["environment"] = (
                f"{combination} combination, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"contemporary mixed media, collage art, "
                f"assemblage piece, experimental art"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"layered textures, found materials, "
                f"dimensional surface, artistic alchemy"
            )
        else:
            components["effects"] = ""
        
        return components






