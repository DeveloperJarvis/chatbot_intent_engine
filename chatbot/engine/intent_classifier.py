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
# intent_classifier MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from chatbot.preprocessing import (
    TextCleaner,
    Tokenizer,
    Normalizer,
    EntityExtractor,
)
from chatbot.patterns import (
    PatternMatcher,
    KeywordMatcher,
    RegexEngine,
)
from chatbot.rules.rule_engine import RuleEngine
from chatbot.engine.scorer import IntentScorer


# --------------------------------------------------
# intent classifier
# --------------------------------------------------
class IntentClassifier:
    """
    Core classification engine
    """

    def __init__(self, config):
        self.config = config
        self.intents_config = config.get_intents()
        self.rules_config = config.get_rules()

        self.cleaner = TextCleaner()
        self.tokenizer = Tokenizer()
        self.normalizer = Normalizer()
        self.entity_extractor = EntityExtractor()

        self.pattern_matcher = PatternMatcher()
        self.keyword_matcher = KeywordMatcher()
        self.regex_engine = RegexEngine()

        self.rule_engine = RuleEngine(self.rules_config)
        self.scorer = IntentScorer(self.rules_config)
    
    def classify(self, text: str):
        original_text = text
        cleaned = self.cleaner.clean(text)
        tokens = self.tokenizer.tokenize(cleaned)
        tokens = self.normalizer.normalize(tokens)
        entities = self.entity_extractor.extract(original_text)

        scored_intents = []

        for intent_name, intent_config in self.intents_config.items():

            exact_matches = self.pattern_matcher.match(
                cleaned, intent_config.get("patterns", [])
            )

            regex_matches, regex_entities = self.regex_engine.match(
                original_text, intent_config.get("regex_patterns", [])
            )

            keyword_score = self.keyword_matcher.match(
                tokens, intent_config.get("keywords", {})
            )

            combined_entities = {**entities, **regex_entities}

            penalties = self.rule_engine.apply_rules(
                intent_config, tokens, combined_entities
            )

            score = self.scorer.calculate(
                exact_matches,
                regex_matches,
                keyword_score,
                len(combined_entities),
                penalties,
            )

            scored_intents.append(
                {
                    "intent": intent_name,
                    "score": score,
                    "priority": intent_config.get("priority", 0),
                    "entity_count": len(combined_entities),
                    "entities": combined_entities,
                }
            )

        return scored_intents
