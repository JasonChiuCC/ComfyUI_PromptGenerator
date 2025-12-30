"""Graphite style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GraphiteHandler(BaseThemeHandler):
    """Handler for graphite drawing style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate graphite drawing prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("graphite.subjects", "realistic portrait")
        
        composition = self._get_random_choice("graphite.composition_types", "photorealistic portrait")
        technique = self._get_random_choice("graphite.techniques", "smooth blending")
        grade = self._get_random_choice("graphite.graphite_grades", "2B soft")
        
        components["subject"] = (
            f"((graphite drawing)), {subject}, "
            f"{composition}, {technique}, using {grade} graphite"
        )
        
        if include_environment:
            finish = self._get_random_choice("graphite.finishes", "silvery sheen")
            mood = self._get_random_choice("graphite.moods", "photorealistic precision")
            
            components["environment"] = (
                f"{finish} finish, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"hyperrealistic graphite, photorealistic drawing, "
                f"fine art pencil work, museum quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"smooth tonal range, silvery reflections, "
                f"incredible detail, flawless gradation"
            )
        else:
            components["effects"] = ""
        
        return components

