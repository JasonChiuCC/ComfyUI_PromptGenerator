from typing import Dict
from ...base_handler import BaseThemeHandler


class RainbowHandler(BaseThemeHandler):
    """Handler for Rainbow theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "rainbow"

        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "rainbow arc")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "full arc rainbow")

        components["subject"] = (
            f"((rainbow photography)) of {subject}, "
            f"{view_type}, natural wonder, professional photography"
        )

        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                background = self._get_random_choice(f"{theme_name}.backgrounds", "storm clouds")
                environment = background
            rainbow_type = self._get_random_choice(f"{theme_name}.rainbow_types", "primary rainbow")
            components["environment"] = f"against {environment}, {rainbow_type}"
        else:
            components["environment"] = ""

        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "magical wonder")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "sun breaking through")
            components["style"] = f"{mood}, {lighting}, rainbow photography"
        else:
            components["style"] = ""

        if include_effects:
            components["effects"] = "vivid spectrum colors, post-storm light, natural miracle"
        else:
            components["effects"] = ""

        return components



