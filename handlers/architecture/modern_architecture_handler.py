from typing import Dict
from ...base_handler import BaseThemeHandler


class ModernArchitectureHandler(BaseThemeHandler):
    """Handler for Modern Architecture theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "modern_architecture"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "contemporary building")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "exterior wide shot")
        architect = self._get_random_choice(f"{theme_name}.architects", "modern design")

        components["subject"] = (
            f"((modern architecture photography)) of {subject}, "
            f"{view_type}, {architect}, "
            f"architectural visualization, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                material = self._get_random_choice(f"{theme_name}.materials", "glass and steel")
                environment = f"featuring {material}"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour warmth")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            style = self._get_random_choice(f"{theme_name}.styles", "minimalist modern")
            mood = self._get_random_choice(f"{theme_name}.moods", "clean precision")
            components["style"] = f"{style}, {mood}, high-end architectural photography"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "sharp focus, architectural detail, professional composition"
        else:
            components["effects"] = ""

        return components

