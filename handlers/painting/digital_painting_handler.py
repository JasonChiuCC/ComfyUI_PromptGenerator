"""Digital Painting style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DigitalPaintingHandler(BaseThemeHandler):
    """Handler for digital painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate digital painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("digital_painting.subjects", "fantasy character")
        
        composition = self._get_random_choice("digital_painting.composition_types", "character illustration")
        technique = self._get_random_choice("digital_painting.techniques", "digital brushwork")
        aesthetic = self._get_random_choice("digital_painting.aesthetics", "painterly digital")
        
        components["subject"] = (
            f"((digital painting)), {subject}, "
            f"{composition}, {technique}, {aesthetic}"
        )
        
        if include_environment:
            software = self._get_random_choice("digital_painting.software_styles", "Photoshop painting")
            mood = self._get_random_choice("digital_painting.moods", "modern creativity")
            
            components["environment"] = (
                f"{software} style, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"professional digital art, tablet painted, "
                f"artstation quality, concept art style"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"custom brushes, layer effects, "
                f"vibrant colors, professional finish"
            )
        else:
            components["effects"] = ""
        
        return components






