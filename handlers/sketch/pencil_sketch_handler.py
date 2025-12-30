"""Pencil Sketch style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PencilSketchHandler(BaseThemeHandler):
    """Handler for pencil sketch style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate pencil sketch prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("pencil_sketch.subjects", "portrait study")
        
        composition = self._get_random_choice("pencil_sketch.composition_types", "detailed study")
        technique = self._get_random_choice("pencil_sketch.techniques", "light hatching")
        pencil_type = self._get_random_choice("pencil_sketch.pencil_types", "2B pencil")
        
        components["subject"] = (
            f"((pencil sketch)), {subject}, "
            f"{composition}, {technique}, drawn with {pencil_type}"
        )
        
        if include_environment:
            paper = self._get_random_choice("pencil_sketch.paper_textures", "sketchbook paper")
            mood = self._get_random_choice("pencil_sketch.moods", "artistic study")
            
            components["environment"] = (
                f"on {paper}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional pencil drawing, graphite artwork, "
                f"hand-drawn illustration, fine art quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"visible pencil strokes, tonal gradation, "
                f"clean linework, professional sketch quality"
            )
        else:
            components["effects"] = ""
        
        return components






