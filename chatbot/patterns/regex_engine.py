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
# regex_engine MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import re

# --------------------------------------------------
# regex engine
# --------------------------------------------------
class RegexEngine:
    """
    Regex pattern matcher with named entity capture
    """

    def match(self, text: str, regex_patterns: list):
        matches = 0
        extracted_entities = {}

        for pattern in regex_patterns:
            result = re.search(pattern, text, re.IGNORECASE)
            if result:
                matches += 1
                extracted_entities.update(result.groupdict())

        return matches, extracted_entities
