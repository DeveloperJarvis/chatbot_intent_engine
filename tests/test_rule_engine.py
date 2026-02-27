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
# test_rule_engine MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from chatbot.rules import (
    MandatoryEntityRule,
    NegativeKeywordRule,
    RuleEngine,
)


def test_mandatory_rule_missing_entry():
    rule = MandatoryEntityRule(penalty=-3)

    intent_config = {"required_entities": ["order_id"]}
    entities = {}

    penalty = rule.apply(intent_config, entities)

    assert penalty == -3


def test_mandatory_rule_present_entity():
    rule = MandatoryEntityRule(penalty=-3)

    intent_config = {"required_entities": ["order_id"]}
    entities = {"order_id": "123"}

    penalty = rule.apply(intent_config, entities)

    assert penalty == 0


def test_negative_keyword_rule():
    rule = NegativeKeywordRule(penalty=-5)

    intent_config = {"negative_keywords": ["refund"]}
    tokens = ["i", "want", "refund"]

    penalty = rule.apply(intent_config, tokens)

    assert penalty == -5

def test_rule_engine_combined():
    rules_config = {
        "mandatory_entity_rule": {
            "penalty_if_missing": -3
        },
    }
    
    engine = RuleEngine(rules_config)
    
    intent_config = {
        "required_entities": ["order_id"],
        "negative_keywords": ["refund"],
    }

    tokens = ["refund"]
    entities = {}

    penalty = engine.apply_rules(
        intent_config,
        tokens,
        entities
    )

    assert penalty == -8
