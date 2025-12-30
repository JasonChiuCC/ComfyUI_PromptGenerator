"""Xianxia theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class XianxiaHandler(BaseThemeHandler):
    """Handler for xianxia aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate xianxia prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("xianxia.subjects", "immortal cultivator")
        
        shot_type = self._get_random_choice("xianxia.shot_types", "cultivation pose")
        
        components["subject"] = (
            f"((xianxia art)) of {subject}, "
            f"{shot_type}, Chinese immortal cultivation fantasy"
        )
        
        if include_environment:
            environment = self._get_random_choice("xianxia.environments", "celestial palace")
            lighting = self._get_random_choice("xianxia.lighting", "celestial radiance")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("xianxia.styles", "xianxia")
            components["style"] = f"{style}, celestial beauty, donghua inspired"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("xianxia.effects", "cultivation energy")
            components["effects"] = f"{effect}, flying sword trails, immortal aura"
        else:
            components["effects"] = ""
        
        return components





