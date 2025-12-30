"""Fitness Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FitnessHandler(BaseThemeHandler):
    """Handler for Fitness portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate fitness portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("fitness.subjects", "athletic model")
        
        expression = self._get_random_choice("fitness.expressions", "focused intensity")
        pose = self._get_random_choice("fitness.poses", "action pose")
        outfit = self._get_random_choice("fitness.outfits", "athletic wear")
        shot_type = self._get_random_choice("fitness.shot_types", "dynamic action shot")
        
        components["subject"] = (
            f"((fitness photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("fitness.locations", "gym studio")
            lighting = self._get_random_choice("fitness.lighting", "dramatic sports lighting")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("fitness.styles", "fitness photography")
            components["style"] = f"{style}, athletic excellence, powerful physique"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "muscle definition, sweat glistening, peak performance"
        else:
            components["effects"] = ""
        
        return components
