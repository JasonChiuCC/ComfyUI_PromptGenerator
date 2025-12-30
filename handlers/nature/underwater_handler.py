from typing import Dict
from ...base_handler import BaseThemeHandler


class UnderwaterHandler(BaseThemeHandler):
    """Handler for Underwater theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "underwater"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "coral reef")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "diver perspective")

        components["subject"] = (
            f"((underwater photography)) of {subject}, "
            f"{view_type}, marine world, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                env = self._get_random_choice(f"{theme_name}.environments", "coral reef")
                environment = env
            marine_life = self._get_random_choice(f"{theme_name}.marine_life", "tropical fish")
            components["environment"] = f"in {environment}, {marine_life}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "alien world wonder")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "surface light rays")
            components["style"] = f"{mood}, {lighting}, underwater photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "water caustics, marine life, underwater colors"
        else:
            components["effects"] = ""

        return components

