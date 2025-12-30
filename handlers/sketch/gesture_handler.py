"""Gesture Drawing style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GestureHandler(BaseThemeHandler):
    """Handler for gesture drawing style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate gesture drawing prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("gesture.subjects", "figure in motion")
        
        composition = self._get_random_choice("gesture.composition_types", "dynamic action")
        technique = self._get_random_choice("gesture.techniques", "continuous line")
        time_frame = self._get_random_choice("gesture.time_frames", "quick capture")
        
        components["subject"] = (
            f"((gesture drawing)), {subject}, "
            f"{composition}, {technique}, {time_frame}"
        )
        
        if include_environment:
            tool = self._get_random_choice("gesture.tools", "soft graphite")
            mood = self._get_random_choice("gesture.moods", "dynamic energy")
            
            components["environment"] = (
                f"drawn with {tool}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"life drawing, quick sketch, "
                f"expressive linework, movement capture"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"flowing lines, captured motion, "
                f"essential form, rhythmic energy"
            )
        else:
            components["effects"] = ""
        
        return components

