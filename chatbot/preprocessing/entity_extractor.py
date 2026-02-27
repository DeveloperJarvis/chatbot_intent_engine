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
# entity_extractor MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import re


# --------------------------------------------------
# entity extractor
# --------------------------------------------------
class EntityExtractor:
    """
    Rule-based entity extractor
    Detects:
    - order_id
    - city (basic pattern)
    """

    CITY_PATTERN = r"\b(?:to|in)\s+([A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)*)"
    ORDER_PATTERN = r"\b\d{3,}\b"

    def extract(self, original_text: str) -> dict:
        entities = {}

        # Order ID detection
        order_match = re.search(self.ORDER_PATTERN,
                                original_text)
        if order_match:
            entities["order_id"] = order_match.group()
        
        # City detection (very basic rule-based)
        city_match = re.search(self.CITY_PATTERN,
                               original_text)
        if city_match:
            entities["city"] = city_match.group(1)
        
        return entities
