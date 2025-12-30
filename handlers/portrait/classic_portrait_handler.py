"""Classic Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ClassicPortraitHandler(BaseThemeHandler):
    """Handler for Classic Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate classic portrait prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("classic_portrait.subjects", "elegant person")
        
        expression = self._get_random_choice("classic_portrait.expressions", "gentle smile")
        pose = self._get_random_choice("classic_portrait.poses", "three-quarter pose")
        outfit = self._get_random_choice("classic_portrait.outfits", "elegant attire")
        shot_type = self._get_random_choice("classic_portrait.shot_types", "portrait")
        
        components["subject"] = (
            f"((professional portrait)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, "
            f"{shot_type}"
        )
        
        # Generate environment
        if include_environment:
            background = self._get_random_choice("classic_portrait.backgrounds", "studio backdrop")
            lighting = self._get_random_choice("classic_portrait.lighting", "Rembrandt lighting")
            
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            style = self._get_random_choice("classic_portrait.styles", "classic portrait photography")
            
            components["style"] = (
                f"{style}, professional portrait, "
                f"high quality, sharp focus, 8K"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = "catch light in eyes, flattering lighting, timeless"
        else:
            components["effects"] = ""
        
        return components
