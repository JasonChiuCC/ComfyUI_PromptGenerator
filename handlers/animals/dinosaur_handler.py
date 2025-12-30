"""Dinosaur theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DinosaurHandler(BaseThemeHandler):
    """Handler for dinosaur art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate dinosaur prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("dinosaur.subjects", "tyrannosaurus rex")
        
        pose = self._get_random_choice("dinosaur.poses", "roaring powerfully")
        expression = self._get_random_choice("dinosaur.expressions", "fierce predator")
        shot_type = self._get_random_choice("dinosaur.shot_types", "dramatic portrait")
        
        components["subject"] = (
            f"((paleoart)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("dinosaur.environments", "prehistoric jungle")
            lighting = self._get_random_choice("dinosaur.lighting", "prehistoric sun")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("dinosaur.styles", "paleoart")
            components["style"] = f"{style}, scientifically accurate, highly detailed"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "prehistoric world, ancient earth, primal power"
        else:
            components["effects"] = ""
        
        return components






