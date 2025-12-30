"""Bokeh photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BokehHandler(BaseThemeHandler):
    """Handler for bokeh photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate bokeh photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("bokeh.subjects", "portrait with bokeh")
        
        composition = self._get_random_choice("bokeh.composition_types", "shallow depth portrait")
        
        components["subject"] = (
            f"((bokeh photography)) {subject}, "
            f"{composition}, beautiful background blur"
        )
        
        if include_environment:
            background = self._get_random_choice("bokeh.backgrounds", "colorful lights")
            components["environment"] = f"with {background} bokeh, dreamy background"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("bokeh.styles", "artistic bokeh")
            components["style"] = f"{style}, f/1.4 aperture, creamy bokeh balls"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "beautiful bokeh, shallow DOF, light orbs, dreamy blur"
        else:
            components["effects"] = ""
        
        return components
