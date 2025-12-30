from typing import Dict
from ...base_handler import BaseThemeHandler


class BrutalistHandler(BaseThemeHandler):
    """Handler for Brutalist Architecture theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "brutalist"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "concrete building")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "monumental low angle")
        architect = self._get_random_choice(f"{theme_name}.architects", "brutalist design")

        components["subject"] = (
            f"((brutalist architecture)) of {subject}, "
            f"{view_type}, {architect}, "
            f"raw concrete béton brut, architectural photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                feature = self._get_random_choice(f"{theme_name}.features", "raw exposed concrete")
                environment = f"featuring {feature}"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "overcast dramatic")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "monumental power")
            components["style"] = f"brutalist aesthetic, {mood}, high contrast photography"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "dramatic shadows, geometric forms, monolithic presence"
        else:
            components["effects"] = ""

        return components

