from typing import Dict
from ...base_handler import BaseThemeHandler


class SkyscraperHandler(BaseThemeHandler):
    """Handler for Skyscraper theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "skyscraper"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "glass tower")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "dramatic upward angle")
        landmark = self._get_random_choice(f"{theme_name}.landmarks", "modern tower design")

        components["subject"] = (
            f"((skyscraper photography)) of {subject}, "
            f"{view_type}, {landmark}, "
            f"urban architecture, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                feature = self._get_random_choice(f"{theme_name}.features", "glass curtain wall")
                environment = f"featuring {feature}"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "night LED facade")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "urban power")
            components["style"] = f"highrise aesthetic, {mood}, metropolitan grandeur"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "soaring height, urban skyline, architectural scale"
        else:
            components["effects"] = ""

        return components



