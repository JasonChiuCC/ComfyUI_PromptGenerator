from typing import Dict
from ...base_handler import BaseThemeHandler


class TempleHandler(BaseThemeHandler):
    """Handler for Temple theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "temple"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "ancient temple")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "grand entrance approach")
        famous = self._get_random_choice(f"{theme_name}.famous_temples", "sacred temple style")

        components["subject"] = (
            f"((temple photography)) of {subject}, "
            f"{view_type}, {famous}, "
            f"sacred architecture, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                element = self._get_random_choice(f"{theme_name}.elements", "carved stone pillars")
                environment = f"featuring {element}"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "divine sunrise")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "sacred devotion")
            components["style"] = f"temple aesthetic, {mood}, spiritual architecture"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "ancient stone, sacred atmosphere, devotional detail"
        else:
            components["effects"] = ""

        return components

