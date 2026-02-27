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
# chatbot_engine MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from chatbot.engine.intent_classifier import IntentClassifier
from chatbot.engine.intent_resolver import IntentResolver
from chatbot.handlers import (
    BookingHandler,
    OrderHandler,
    FallbackHandler,
)
from chatbot.utils.contants import DEFAULT_FALLBACK_INTENT


# --------------------------------------------------
# chatbot engine
# --------------------------------------------------
class ChatbotEngine:
    """
    Orchestrates entire chatbot flow
    """

    def __init__(self, config):
        self.config = config
        self.classifier = IntentClassifier(config)
        self.resolver = IntentResolver()

        self.handlers = {
            "BookFlight": BookingHandler(),
            "CancelOrder": OrderHandler(),
            DEFAULT_FALLBACK_INTENT: FallbackHandler(),
        }
    
    def handle_message(self, text: str) -> str:
        scored_intents = self.classifier.classify(text)

        intent_name, entities = self.resolver.resolve(
            scored_intents,
            fallback_intent=DEFAULT_FALLBACK_INTENT,
        )

        handler = self.handlers.get(intent_name,
                                    FallbackHandler())
        
        return handler.handle(entities)
