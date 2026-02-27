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
# priority_rule MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# priority rule
# --------------------------------------------------
class PriorityRule:
    """
    Resolves ties using priority and entity count
    """

    def resolve(self, scored_intents: list) -> dict:
        """
        scored_intents format:
        [
            {
                "intent": "BookFlight",
                "score": 8,
                "priority": 3,
                "entity_count": 1,
            }
        ]
        """

        if not scored_intents:
            return None
        
        # Sort by score, then priotity, then entity count
        scored_intents = sorted(
            scored_intents,
            key=lambda x: (
                x["score"],
                x["priority"],
                x["entity_count"],
            ),
            reverse=True,
        )

        return scored_intents[0]
