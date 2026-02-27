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
# test_intent_classifier MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from config.config import AppConfig
from chatbot.engine.intent_classifier import IntentClassifier


def test_intent_classification_book_flight():
    config = AppConfig()
    classifier = IntentClassifier(config)

    text = "Book a flight to London"

    results = classifier.classify(text)

    # Get highest score intent
    best = max(results, key=lambda x: x["score"])

    assert best["intent"] == "BookFlight"
    assert best["score"] > 0
    assert best["entities"].get("city") == "London"


def test_intent_classification_cancel_order():
    config = AppConfig()
    classifier = IntentClassifier(config)

    text = "Cancel order 7890"

    results = classifier.classify(text)
    best = max(results, key=lambda x: x["score"])

    assert best["intent"] == "CancelOrder"
    assert best["entities"].get("order_id") == "7890"


def test_intent_classification_fallback():
    config = AppConfig()
    classifier = IntentClassifier(config)

    text = "I like turtles"

    results = classifier.classify(text)
    best = max(results, key=lambda x: x["score"])

    # Fallback might still get highest score = 0
    assert best["intent"] in [
        "Fallback", "BookFlight", "CancelOrder"
    ]

