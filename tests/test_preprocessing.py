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
# test_preprocessing MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from chatbot.preprocessing import (
    TextCleaner,
    Tokenizer,
    Normalizer,
    EntityExtractor,
)


def test_text_cleaner():
    cleaner = TextCleaner()
    text = "Hello, World!"
    cleaned = cleaner.clean(text)

    assert cleaned == "hello world"


def test_tokenizer():
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("hello world")

    assert tokens == ["hello", "world"]


def test_normalizer():
    normalizer = Normalizer()
    tokens = ["booking", "flight"]

    normalized = normalizer.normalize(tokens)
    
    assert normalized == tokens


def test_entity_extractor_order():
    extractor = EntityExtractor()
    text = "Cancel order 12345"

    entities = extractor.extract(text)

    assert entities.get("order_id") == "12345"


def test_entity_extractor_city():
    extractor = EntityExtractor()
    text = "Book flight to Paris"

    entities = extractor.extract(text)

    assert entities.get("city") == "Paris"
