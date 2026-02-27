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
# scorer MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# intent scorer
# --------------------------------------------------
class IntentScorer:
    """
    Calculates intent score based on:
    - Exact match
    - Regex match
    - Keyword score
    - Entity bonus
    - Rule penalties
    """

    def __init__(self, rule_config: dict):
        weights = rule_config.get("scoring_weights", {})
        self.exact_weight = weights.get("exact_match", 5)
        self.regex_weight = weights.get("regex_match", 4)
        self.keyword_multiplier = weights.get(
            "keyword_match_multiplier", 1
        )
        self.entity_bonus = weights.get("entity_bonus", 2)
    
    def calculate(
            self,
            exact_matches: int,
            regex_matches: int,
            keyword_score: int,
            entity_count: int,
            penalties:int,
    ) -> int:

        score = 0
        score += exact_matches * self.exact_weight
        score += regex_matches * self.regex_weight
        score += keyword_score * self.keyword_multiplier
        score += entity_count * self.entity_bonus
        score += penalties

        return score
