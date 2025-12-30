"""Oil Painting style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class OilPaintingHandler(BaseThemeHandler):
    """Handler for oil painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate oil painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("oil_painting.subjects", "classical portrait")
        
        composition = self._get_random_choice("oil_painting.composition_types", "classical composition")
        technique = self._get_random_choice("oil_painting.techniques", "glazing layers")
        brushwork = self._get_random_choice("oil_painting.brushwork", "visible brushstrokes")
        
        components["subject"] = (
            f"((oil painting masterpiece)), {subject}, "
            f"{composition}, {technique}, {brushwork}"
        )
        
        if include_environment:
            color = self._get_random_choice("oil_painting.color_palettes", "rich earth tones")
            mood = self._get_random_choice("oil_painting.moods", "classical grandeur")
            
            components["environment"] = (
                f"{color}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional oil painting, fine art quality, "
                f"museum masterpiece, gallery exhibition"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"rich pigments, canvas texture, "
                f"luminous depth, professional quality"
            )
        else:
            components["effects"] = ""
        
        return components





