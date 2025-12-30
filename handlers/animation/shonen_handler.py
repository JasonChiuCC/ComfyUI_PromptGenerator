"""Shonen anime theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ShonenHandler(BaseThemeHandler):
    """Handler for shonen anime style prompt generation.
    
    Generates prompts for action-packed shonen anime artwork,
    featuring heroes, powers, intense battles, and emotional moments.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate shonen anime style prompt components."""
        components = {}
        
        # Generate character
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("shonen.characters", "young hero")
        
        outfit = self._get_random_choice("shonen.outfits", "battle outfit")
        power = self._get_random_choice("shonen.powers", "special power")
        pose = self._get_random_choice("shonen.poses", "power-up pose")
        expression = self._get_random_choice("shonen.expressions", "determined look")
        shot_type = self._get_random_choice("shonen.shot_types", "full body power-up shot")
        
        components["subject"] = (
            f"((intense shonen anime art)) of {character}, "
            f"{shot_type}, wearing {outfit}, using {power}, {pose}, {expression}, "
            f"dynamic composition, professional shonen illustration"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("shonen.locations", "battle arena")
            
            components["environment"] = (
                f"in {location}, "
                f"epic scale battle scene, destruction and debris, "
                f"dramatic atmosphere"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            style = self._get_random_choice("shonen.styles", "shonen anime style")
            
            components["style"] = (
                f"{style}, bold line art, "
                f"high contrast shading, vibrant energy colors, "
                f"Weekly Shonen Jump quality, 8k resolution"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("shonen.effects", "power aura")
            lighting = self._get_random_choice("shonen.lighting", "dramatic power glow")
            
            components["effects"] = (
                f"{effect}, {lighting}, "
                f"impact lines, energy crackling, "
                f"explosive visual effects"
            )
        else:
            components["effects"] = ""
        
        return components

