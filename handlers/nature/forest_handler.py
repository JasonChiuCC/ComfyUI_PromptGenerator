from typing import Dict
from ...base_handler import BaseThemeHandler


class ForestHandler(BaseThemeHandler):
    """Handler for Forest theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "forest"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "enchanted forest")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "path through trees")

        components["subject"] = (
            f"((forest photography)) of {subject}, "
            f"{view_type}, woodland scenery, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                forest_type = self._get_random_choice(f"{theme_name}.forest_types", "temperate forest")
                environment = forest_type
            lighting = self._get_random_choice(f"{theme_name}.lighting", "dappled sunlight")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "mystical enchantment")
            season = self._get_random_choice(f"{theme_name}.seasons", "summer lush green")
            components["style"] = f"{mood}, {season}, nature photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "atmospheric depth, natural beauty, forest atmosphere"
        else:
            components["effects"] = ""

        return components

