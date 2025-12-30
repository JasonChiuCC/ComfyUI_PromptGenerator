"""Monster theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MonsterHandler(BaseThemeHandler):
    """Handler for monster creature design."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate monster prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("monster.subjects", "terrifying monster")
        
        pose = self._get_random_choice("monster.poses", "lurking in shadows")
        expression = self._get_random_choice("monster.expressions", "terrifying fierce")
        feature = self._get_random_choice("monster.features", "sharp claws")
        shot_type = self._get_random_choice("monster.shot_types", "full creature design")
        
        components["subject"] = (
            f"((creature design)) of {subject}, "
            f"{pose}, {expression}, {feature}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("monster.environments", "dark forest")
            lighting = self._get_random_choice("monster.lighting", "dim eerie")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("monster.styles", "creature design")
            components["style"] = f"{style}, horror creature, detailed design"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "menacing presence, nightmare fuel, creature horror"
        else:
            components["effects"] = ""
        
        return components






