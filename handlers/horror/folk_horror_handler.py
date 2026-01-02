"""Folk horror theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FolkHorrorHandler(BaseThemeHandler):
    """Handler for folk horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate folk horror prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("folk_horror.communities", "isolated village cult")
        
        shot_type = self._get_random_choice("folk_horror.shot_types", "ritual gathering aerial view")
        ritual = self._get_random_choice("folk_horror.rituals", "harvest sacrifice")
        element = self._get_random_choice("folk_horror.elements", "wicker man effigy")
        mood = self._get_random_choice("folk_horror.moods", "creeping unease")
        
        components["subject"] = (
            f"((folk horror)) {subject}, "
            f"{shot_type}, performing {ritual}, "
            f"with {element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("folk_horror.environments", "pastoral countryside")
            lighting = self._get_random_choice("folk_horror.lighting", "overcast grey sky")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "folk horror style, Midsommar and The Wicker Man inspired, "
                "pagan ritual aesthetic, pastoral nightmare"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("folk_horror.effects", "pastoral color grading")
            components["effects"] = f"{effect}, daylight horror, ancient tradition dread"
        else:
            components["effects"] = ""
        
        return components



