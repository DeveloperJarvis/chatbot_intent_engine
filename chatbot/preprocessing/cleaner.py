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
# cleaner MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import re
import string


# --------------------------------------------------
# text cleaner
# --------------------------------------------------
class TextCleaner:
    """
    Handles text cleaning operations
    """

    def __init__(
            self,
            lowercase: bool = True,
            remove_punctuation: bool = True,
        ):
        self.lowercase = lowercase
        self.remove_punctuation = remove_punctuation
    
    def clean(self, text: str) -> str:
        if not text:
            return ""
        
        if self.lowercase:
            text = text.lower()
        
        if self.remove_punctuation:
            text = text.translate(
                str.maketrans("", "", string.punctuation)
            )
        
        text = re.sub(r"\s+", " ", text).strip()

        return text
