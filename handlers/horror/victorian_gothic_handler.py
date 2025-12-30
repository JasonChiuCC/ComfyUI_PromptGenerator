"""Victorian Gothic theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class VictorianGothicHandler(BaseThemeHandler):
    """Handler for Victorian Gothic horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Victorian Gothic prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("victorian_gothic.characters", "brooding aristocrat")
        
        shot_type = self._get_random_choice("victorian_gothic.shot_types", "grand staircase portrait")
        attire = self._get_random_choice("victorian_gothic.attire", "mourning black dress")
        element = self._get_random_choice("victorian_gothic.elements", "candelabra")
        mood = self._get_random_choice("victorian_gothic.moods", "romantic melancholy")
        
        components["subject"] = (
            f"((Victorian Gothic)) {subject}, "
            f"{shot_type}, wearing {attire}, "
            f"with {element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("victorian_gothic.environments", "crumbling manor house")
            lighting = self._get_random_choice("victorian_gothic.lighting", "candlelight and shadow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "Victorian Gothic style, Crimson Peak inspired, "
                "dark romanticism, Edgar Allan Poe atmosphere"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("victorian_gothic.effects", "sepia toning")
            components["effects"] = f"{effect}, antique atmosphere, melancholic beauty"
        else:
            components["effects"] = ""
        
        return components

