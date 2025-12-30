"""Ballpoint Pen style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BallpointPenHandler(BaseThemeHandler):
    """Handler for ballpoint pen drawing style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate ballpoint pen drawing prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("ballpoint_pen.subjects", "realistic portrait")
        
        composition = self._get_random_choice("ballpoint_pen.composition_types", "detailed scene")
        technique = self._get_random_choice("ballpoint_pen.techniques", "fine hatching")
        pen_color = self._get_random_choice("ballpoint_pen.pen_colors", "classic blue")
        style = self._get_random_choice("ballpoint_pen.styles", "photorealistic")
        
        components["subject"] = (
            f"((ballpoint pen drawing)), {subject}, "
            f"{composition}, {technique}, {pen_color} ink"
        )
        
        if include_environment:
            mood = self._get_random_choice("ballpoint_pen.moods", "accessible art")
            
            components["environment"] = (
                f"{mood}, {style} approach"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"ballpoint pen art, biro illustration, "
                f"everyday medium masterpiece"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"layered strokes, smooth gradation, "
                f"impressive detail, humble medium beauty"
            )
        else:
            components["effects"] = ""
        
        return components





