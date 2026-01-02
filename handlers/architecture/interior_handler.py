from typing import Dict
from ...base_handler import BaseThemeHandler


class InteriorHandler(BaseThemeHandler):
    """Handler for Interior Design theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "interior"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            room = self._get_random_choice(f"{theme_name}.rooms", "living room")
            subject = room

        view_type = self._get_random_choice(f"{theme_name}.view_types", "wide room overview")
        element = self._get_random_choice(f"{theme_name}.elements", "statement lighting")

        components["subject"] = (
            f"((interior design photography)) of {subject}, "
            f"{view_type}, {element}, "
            f"architectural interior, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                style = self._get_random_choice(f"{theme_name}.styles", "minimalist modern")
                environment = f"{style} design"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "natural window light")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "cozy comfort")
            components["style"] = f"interior design aesthetic, {mood}, curated space"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "styled details, warm atmosphere, magazine quality"
        else:
            components["effects"] = ""

        return components



