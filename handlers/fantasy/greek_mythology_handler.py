"""Greek Mythology theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GreekMythologyHandler(BaseThemeHandler):
    """Handler for Greek mythology aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Greek mythology prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("greek_mythology.subjects", "Zeus thundering")
        
        shot_type = self._get_random_choice("greek_mythology.shot_types", "divine portrait")
        
        components["subject"] = (
            f"((Greek mythology art)) of {subject}, "
            f"{shot_type}, ancient Greek gods and heroes"
        )
        
        if include_environment:
            environment = self._get_random_choice("greek_mythology.environments", "Mount Olympus")
            lighting = self._get_random_choice("greek_mythology.lighting", "divine radiance")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("greek_mythology.styles", "Greek mythology")
            components["style"] = f"{style}, classical inspired, heroic Greek"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("greek_mythology.effects", "divine power")
            components["effects"] = f"{effect}, godly aura, mythical creatures"
        else:
            components["effects"] = ""
        
        return components





