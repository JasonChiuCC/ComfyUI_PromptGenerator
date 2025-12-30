"""Mecha anime theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MechaHandler(BaseThemeHandler):
    """Handler for mecha anime style prompt generation.
    
    Generates prompts for giant robot and mecha anime artwork,
    including pilots, mechs, weapons, and epic battle scenes.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate mecha anime style prompt components."""
        components = {}
        
        # Generate character/mech
        if custom_subject:
            subject = custom_subject
        else:
            pilot = self._get_random_choice("mecha.characters", "mecha pilot")
            mech = self._get_random_choice("mecha.mechs", "giant robot")
            subject = f"{pilot} piloting {mech}"
        
        weapon = self._get_random_choice("mecha.weapons", "beam saber")
        pose = self._get_random_choice("mecha.poses", "combat stance")
        shot_type = self._get_random_choice("mecha.shot_types", "full mech body shot")
        
        components["subject"] = (
            f"((epic mecha anime art)) of {subject}, "
            f"{shot_type}, equipped with {weapon}, {pose}, "
            f"detailed mechanical design, professional mecha illustration"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("mecha.locations", "battlefield")
            
            time = self._get_random_choice("mecha.times", "dramatic battle time")
            
            components["environment"] = (
                f"in {location}, {time}, "
                f"epic scale, war-torn atmosphere, detailed background"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            style = self._get_random_choice("mecha.styles", "Gundam style")
            
            components["style"] = (
                f"{style}, highly detailed mechanical design, "
                f"sharp metallic textures, professional animation quality, "
                f"dynamic camera angle, 8k resolution"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("mecha.effects", "thruster flames")
            lighting = self._get_random_choice("mecha.lighting", "epic rim lighting")
            
            components["effects"] = (
                f"{effect}, {lighting}, "
                f"particle effects, motion blur, cinematic quality"
            )
        else:
            components["effects"] = ""
        
        return components

