from typing import Dict
from ...base_handler import BaseThemeHandler


class IndustrialArchHandler(BaseThemeHandler):
    """Handler for Industrial Architecture theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "industrial_arch"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "factory building")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "dramatic factory exterior")
        element = self._get_random_choice(f"{theme_name}.elements", "exposed brick walls")

        components["subject"] = (
            f"((industrial architecture)) of {subject}, "
            f"{view_type}, {element}, "
            f"industrial heritage, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                material = self._get_random_choice(f"{theme_name}.materials", "red brick masonry")
                environment = f"featuring {material}"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "harsh industrial")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "working heritage")
            components["style"] = f"industrial aesthetic, {mood}, functional architecture"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "rust patina, weathered texture, manufacturing atmosphere"
        else:
            components["effects"] = ""

        return components



