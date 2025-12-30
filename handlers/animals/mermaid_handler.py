"""Mermaid theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MermaidHandler(BaseThemeHandler):
    """Handler for mermaid fantasy art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate mermaid prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("mermaid.subjects", "beautiful mermaid")
        
        pose = self._get_random_choice("mermaid.poses", "swimming gracefully")
        expression = self._get_random_choice("mermaid.expressions", "ethereal beauty")
        tail_type = self._get_random_choice("mermaid.tail_types", "iridescent scales")
        shot_type = self._get_random_choice("mermaid.shot_types", "portrait beautiful")
        
        components["subject"] = (
            f"((mermaid fantasy art)) of {subject}, "
            f"{pose}, {expression}, {tail_type} tail, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("mermaid.environments", "coral reef kingdom")
            lighting = self._get_random_choice("mermaid.lighting", "underwater sunbeams")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("mermaid.styles", "fantasy art")
            components["style"] = f"{style}, ocean magic, ethereal underwater"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "flowing hair, shimmering scales, underwater wonder"
        else:
            components["effects"] = ""
        
        return components





