"""Norse Mythology theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class NorseMythologyHandler(BaseThemeHandler):
    """Handler for Norse mythology aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Norse mythology prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("norse_mythology.subjects", "Odin Allfather")
        
        shot_type = self._get_random_choice("norse_mythology.shot_types", "godly portrait")
        
        components["subject"] = (
            f"((Norse mythology art)) of {subject}, "
            f"{shot_type}, Viking gods and Nordic legends"
        )
        
        if include_environment:
            environment = self._get_random_choice("norse_mythology.environments", "Asgard realm")
            lighting = self._get_random_choice("norse_mythology.lighting", "northern lights")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("norse_mythology.styles", "Norse mythology")
            components["style"] = f"{style}, Viking inspired, Ragnarok epic"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("norse_mythology.effects", "lightning crackling")
            components["effects"] = f"{effect}, ice and frost, runic magic"
        else:
            components["effects"] = ""
        
        return components





