from typing import Dict
from ...base_handler import BaseThemeHandler


class ArtDecoArchHandler(BaseThemeHandler):
    """Handler for Art Deco Architecture theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "art_deco_arch"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "Art Deco building")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "dramatic upward angle")
        element = self._get_random_choice(f"{theme_name}.elements", "geometric ornamentation")

        components["subject"] = (
            f"((Art Deco architecture)) of {subject}, "
            f"{view_type}, {element}, "
            f"1920s glamour, architectural photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "Manhattan New York")
                environment = f"in {location}"
            material = self._get_random_choice(f"{theme_name}.materials", "polished granite")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden hour glow")
            components["environment"] = f"{environment}, {material}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "glamorous elegance")
            components["style"] = f"Art Deco style, {mood}, Jazz Age aesthetic"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "ornate details, geometric patterns, luxurious finish"
        else:
            components["effects"] = ""

        return components



