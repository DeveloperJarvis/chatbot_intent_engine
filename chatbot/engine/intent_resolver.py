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
# intent_resolver MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from chatbot.rules.priority_rule import PriorityRule

# --------------------------------------------------
# intent resolver
# --------------------------------------------------
class IntentResolver:
    """
    Selects best intent using score and priority rule
    """

    def __init__(self):
        self.priority_rule = PriorityRule()
    
    def resolve(
            self,
            scored_intents: list,
            fallback_intent: str
    ):
        if not scored_intents:
            return fallback_intent, {}
        
        best = self.priority_rule.resolve(scored_intents)

        if not best or best["score"] <= 0:
            return fallback_intent, {}
        
        return best["intent"], best.get("entities", {})
