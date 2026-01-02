"""Werewolf theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WerewolfHandler(BaseThemeHandler):
    """Handler for werewolf horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate werewolf prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("werewolf.characters", "alpha werewolf")
        
        shot_type = self._get_random_choice("werewolf.shot_types", "full body howling at moon")
        transformation = self._get_random_choice("werewolf.transformation_stages", "full wolf-human hybrid")
        element = self._get_random_choice("werewolf.elements", "massive clawed hands")
        mood = self._get_random_choice("werewolf.moods", "primal rage")
        
        components["subject"] = (
            f"((werewolf horror)) {subject}, "
            f"{shot_type}, {transformation}, {element}, "
            f"{mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("werewolf.environments", "dark forest under full moon")
            lighting = self._get_random_choice("werewolf.lighting", "bright full moon")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "lycanthrope horror style, An American Werewolf in London inspired, "
                "practical effects aesthetic, monster transformation"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("werewolf.effects", "motion blur of speed")
            components["effects"] = f"{effect}, moonlit atmosphere, primal energy"
        else:
            components["effects"] = ""
        
        return components



