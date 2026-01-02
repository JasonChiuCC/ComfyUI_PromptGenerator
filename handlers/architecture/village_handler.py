from typing import Dict
from ...base_handler import BaseThemeHandler


class VillageHandler(BaseThemeHandler):
    """Handler for Village theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "village"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "European village")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "hilltop overview")
        region = self._get_random_choice(f"{theme_name}.regions", "countryside")

        components["subject"] = (
            f"((village photography)) of {subject}, "
            f"{view_type}, {region}, "
            f"rural architecture, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                element = self._get_random_choice(f"{theme_name}.elements", "stone cottages")
                environment = f"featuring {element}"
            season = self._get_random_choice(f"{theme_name}.seasons", "golden hour")
            components["environment"] = f"{environment}, {season}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "rustic charm")
            components["style"] = f"village aesthetic, {mood}, pastoral beauty"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "countryside atmosphere, traditional architecture, peaceful setting"
        else:
            components["effects"] = ""

        return components



