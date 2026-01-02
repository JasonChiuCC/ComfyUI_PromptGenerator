from typing import Dict
from ...base_handler import BaseThemeHandler


class MediterraneanArchHandler(BaseThemeHandler):
    """Handler for Mediterranean Architecture theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "mediterranean_arch"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "Mediterranean villa")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "whitewashed village overview")
        element = self._get_random_choice(f"{theme_name}.elements", "whitewashed walls")

        components["subject"] = (
            f"((Mediterranean architecture)) of {subject}, "
            f"{view_type}, {element}, "
            f"coastal charm, architectural photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "Santorini Greece")
                environment = f"in {location}"
            lighting = self._get_random_choice(f"{theme_name}.lighting", "brilliant Mediterranean sun")
            components["environment"] = f"{environment}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "sun-drenched bliss")
            components["style"] = f"Mediterranean style, {mood}, azure and white palette"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "blue domes, bougainvillea accents, sea view"
        else:
            components["effects"] = ""

        return components



