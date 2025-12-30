"""Macro photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MacroHandler(BaseThemeHandler):
    """Handler for macro photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate macro photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("macro.subjects", "tiny insect")
        
        composition = self._get_random_choice("macro.composition_types", "extreme close-up")
        
        components["subject"] = (
            f"((macro photography)) {subject}, "
            f"{composition}, incredible detail"
        )
        
        if include_environment:
            background = self._get_random_choice("macro.backgrounds", "soft bokeh")
            lighting = self._get_random_choice("macro.lighting", "natural diffused light")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("macro.styles", "nature macro")
            components["style"] = f"{style}, 1:1 magnification, tack sharp focus"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "extreme detail, shallow depth of field, macro lens quality"
        else:
            components["effects"] = ""
        
        return components
