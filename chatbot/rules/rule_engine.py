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
# rule_engine MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from .mandatory_rule import MandatoryEntityRule
from .negative_rule import NegativeKeywordRule


# --------------------------------------------------
# rule engine
# --------------------------------------------------
class RuleEngine:
    """
    Applies rule logic during intent scoring
    """

    def __init__(self, rules_config: dict):
        self.rules_config = rules_config

        scoring = rules_config.get("scoring_weights", {})

        self.mandatory_rule = MandatoryEntityRule(
            penalty=rules_config.get(
                "mandatory_entity_rule", {}
            ).get("penalty_if_missing", -3)
        )

        self.negative_rule = NegativeKeywordRule(
            penalty=rules_config.get(
                "negative_keyword_rule", {}
            ).get("penalty", -5)
        )
    
    def apply_rules(
            self,
            intent_config: dict,
            tokens: list,
            entities: dict,
    ) -> int:
        penalty = 0

        penalty += self.mandatory_rule.apply(
            intent_config, entities
        )
        penalty += self.negative_rule.apply(
            intent_config, tokens
        )

        return penalty
