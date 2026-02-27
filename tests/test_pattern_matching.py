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
# test_pattern_matching MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from chatbot.patterns import (
    PatternMatcher,
    KeywordMatcher,
    RegexEngine,
)


def test_pattern_matcher():
    matcher = PatternMatcher()

    patterns = ["book flight", "cancel order"]
    text = "please book flight to london"

    matches = matcher.match(text, patterns)
    assert matches == 1


def test_keyword_matcher():
    matcher = KeywordMatcher()
    
    tokens = ["cancel", "order"]
    keywords = {"cancel": 3, "order": 2}

    score = matcher.match(tokens, keywords)

    assert score == 5


def test_regex_engine():
    regex_engine = RegexEngine()

    patterns = [r"cancel order (?P<order_id>\d+)"]
    text = "Cancel order 5678"

    matches, entities = regex_engine.match(text, patterns)

    assert matches == 1
    assert entities["order_id"] == "5678"
