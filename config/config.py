# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Chatbot Intent Engine Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Chatbot Intent Engine - Intent classification using rules and patterns
#      Skills: NLP, pattern matching
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# config MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import os
import yaml


# --------------------------------------------------
# app config
# --------------------------------------------------
class AppConfig:
    """
    Loads and manages application configuration
    """

    def __init__(self, config_dir: str = "config"):
        self.config_dir = config_dir

        self.settings = self._load_yaml("settings.yaml")
        self.intents = self._load_yaml("intents.yaml")
        self.rules = self._load_yaml("rules.yaml")

        self._parse_basic_settings()
    
    # ------------------------
    # Internal Methods
    # ------------------------
    def _load_yaml(self, filename: str) -> dict:
        """
        Load YAML safely
        """
        path = os.path.join(self.config_dir, filename)

        if not os.path.exists(path):
            raise FileNotFoundError(
                f"Configuration file not found: {path}"
            )
        
        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def _parse_basic_settings(self):
        """
        Extract frequently used application settings
        """
        app_config = self.settings.get("application", {})

        self.app_name = app_config.get("name", "Chatbot")
        self.version = app_config.get("version", "1.0.0")
        self.debug = app_config.get("debug", False)

        logging_config = logging_config.get("logging", {})
        self.log_level = logging_config.get("log_level",
                                            "INFO")
        self.log_to_file = logging_config.get(
            "log_to_file", False
        )
        self.log_file_path = logging_config.get(
            "log_file_path", "logs/chatbot.log"
        )
    
    # ------------------------
    # Public Access Methods
    # ------------------------
    def get_intents(self) -> dict:
        return self.intents.get("intents", {})
    
    def get_rules(self) -> dict:
        return self.rules.get("rules", {})
    
    def get_settings(self) -> dict:
        return self.settings
    
    def __repr__(self):
        return (f"<AppConfig app_name={self.app_name}, "
                f"version={self.version}>")
