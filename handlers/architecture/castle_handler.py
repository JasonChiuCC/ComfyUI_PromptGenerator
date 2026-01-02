from typing import Dict
from ...base_handler import BaseThemeHandler


class CastleHandler(BaseThemeHandler):
    """Handler for Castle theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "castle"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "medieval fortress")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "dramatic hilltop silhouette")
        famous = self._get_random_choice(f"{theme_name}.famous_castles", "fairy tale castle style")

        components["subject"] = (
            f"((castle photography)) of {subject}, "
            f"{view_type}, {famous}, "
            f"historic architecture, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                element = self._get_random_choice(f"{theme_name}.elements", "stone battlements")
                environment = f"featuring {element}"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour warmth")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "medieval grandeur")
            components["style"] = f"castle aesthetic, {mood}, fortress architecture"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "ancient stone, dramatic landscape, historic atmosphere"
        else:
            components["effects"] = ""

        return components



