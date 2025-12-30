"""South Park cartoon style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SouthParkHandler(BaseThemeHandler):
    """Handler for South Park cartoon style prompt generation.
    
    Generates prompts for crude paper cutout animation style,
    featuring simple shapes, flat colors, and minimalist design.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate South Park style prompt components."""
        components = {}
        
        # Generate character
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("south_park.characters", "cartoon kid")
        
        outfit = self._get_random_choice("south_park.outfits", "simple outfit")
        expression = self._get_random_choice("south_park.expressions", "cartoon expression")
        shot_type = self._get_random_choice("south_park.shot_types", "full body paper cutout shot")
        
        components["subject"] = (
            f"((South Park cartoon style)) of {character}, "
            f"{shot_type}, wearing {outfit}, with {expression}, "
            f"simple geometric shapes, paper cutout character design"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("south_park.locations", "snowy town")
            
            components["environment"] = (
                f"in {location}, "
                f"flat simple background, "
                f"Colorado small town aesthetic"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            art_style = self._get_random_choice("south_park.art_styles", "paper cutout style")
            style = self._get_random_choice("south_park.styles", "South Park style")
            
            components["style"] = (
                f"{art_style}, {style}, "
                f"intentionally crude animation, flat colors, "
                f"bold black outlines, minimalist character design"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("south_park.effects", "simple effects")
            lighting = self._get_random_choice("south_park.lighting", "flat lighting")
            
            components["effects"] = (
                f"{effect}, {lighting}, "
                f"construction paper texture, "
                f"deliberately unpolished aesthetic"
            )
        else:
            components["effects"] = ""
        
        return components

