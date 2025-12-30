"""Unicorn theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class UnicornHandler(BaseThemeHandler):
    """Handler for unicorn fantasy art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate unicorn prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("unicorn.subjects", "beautiful unicorn")
        
        pose = self._get_random_choice("unicorn.poses", "standing in moonlight")
        expression = self._get_random_choice("unicorn.expressions", "pure and innocent")
        shot_type = self._get_random_choice("unicorn.shot_types", "majestic portrait")
        
        components["subject"] = (
            f"((magical unicorn art)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("unicorn.environments", "enchanted forest")
            lighting = self._get_random_choice("unicorn.lighting", "magical glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("unicorn.styles", "fantasy art")
            effect = self._get_random_choice("unicorn.effects", "sparkles and stars")
            components["style"] = f"{style}, ethereal beauty, {effect}"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "magical sparkles, rainbow shimmer, fairytale wonder"
        else:
            components["effects"] = ""
        
        return components





