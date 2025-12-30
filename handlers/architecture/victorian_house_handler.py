from typing import Dict
from ...base_handler import BaseThemeHandler


class VictorianHouseHandler(BaseThemeHandler):
    """Handler for Victorian House theme."""

    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        components = {}
        theme_name = "victorian_house"

        # Subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice(f"{theme_name}.subjects", "Victorian mansion")

        view_type = self._get_random_choice(f"{theme_name}.view_types", "full facade portrait")
        element = self._get_random_choice(f"{theme_name}.elements", "ornate gingerbread trim")

        components["subject"] = (
            f"((Victorian architecture)) of {subject}, "
            f"{view_type}, {element}, "
            f"historic residential, professional photography"
        )

        # Environment
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                location = self._get_random_choice(f"{theme_name}.locations", "San Francisco")
                environment = f"in {location}"
            color = self._get_random_choice(f"{theme_name}.colors", "Painted Lady multicolor")
            lighting = self._get_random_choice(f"{theme_name}.lighting", "golden afternoon")
            components["environment"] = f"{environment}, {color}, {lighting}"
        else:
            components["environment"] = ""

        # Style
        if include_style:
            mood = self._get_random_choice(f"{theme_name}.moods", "romantic elegance")
            components["style"] = f"Victorian aesthetic, {mood}, ornate craftsmanship"
        else:
            components["style"] = ""

        # Effects
        if include_effects:
            components["effects"] = "architectural detail, period authenticity, preserved heritage"
        else:
            components["effects"] = ""

        return components

