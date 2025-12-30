"""Insects theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class InsectsHandler(BaseThemeHandler):
    """Handler for insect macro photography."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate insects prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("insects.subjects", "beautiful insect")
        
        pose = self._get_random_choice("insects.poses", "resting on flower")
        expression = self._get_random_choice("insects.expressions", "intricate detail")
        shot_type = self._get_random_choice("insects.shot_types", "extreme macro")
        
        components["subject"] = (
            f"((macro photography)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("insects.environments", "flower garden")
            lighting = self._get_random_choice("insects.lighting", "soft macro light")
            components["environment"] = f"on {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("insects.styles", "macro photography")
            components["style"] = f"{style}, incredible detail, sharp focus"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "tiny world, nature's miniatures, macro wonder"
        else:
            components["effects"] = ""
        
        return components





