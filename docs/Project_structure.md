# 📁 Project Structure

```
chatbot-intent-engine/
│
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
│
├── config/
│   ├── intents.yaml
│   ├── rules.yaml
│   └── settings.yaml
│
├── data/
│   ├── sample_inputs.json
│   └── test_cases.json
│
├── chatbot/
│   ├── __init__.py
│   │
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── chatbot_engine.py
│   │   ├── intent_classifier.py
│   │   ├── intent_resolver.py
│   │   └── scorer.py
│   │
│   ├── intents/
│   │   ├── __init__.py
│   │   ├── base_intent.py
│   │   ├── book_flight_intent.py
│   │   ├── cancel_order_intent.py
│   │   └── fallback_intent.py
│   │
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   ├── tokenizer.py
│   │   ├── entity_extractor.py
│   │   └── normalizer.py
│   │
│   ├── patterns/
│   │   ├── __init__.py
│   │   ├── pattern_matcher.py
│   │   ├── regex_engine.py
│   │   └── keyword_matcher.py
│   │
│   ├── rules/
│   │   ├── __init__.py
│   │   ├── rule_engine.py
│   │   ├── mandatory_rule.py
│   │   ├── negative_rule.py
│   │   └── priority_rule.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   ├── constants.py
│   │   └── helpers.py
│   │
│   └── handlers/
│       ├── __init__.py
│       ├── booking_handler.py
│       ├── order_handler.py
│       └── fallback_handler.py
│
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_pattern_matching.py
│   ├── test_rule_engine.py
│   └── test_intent_classifier.py
│
└── main.py
```

---

# 📦 Folder Explanation

---

## 🔹 `config/`

Contains configurable YAML files:

- `intents.yaml` → Intent definitions (patterns, keywords, priority)
- `rules.yaml` → Rule definitions
- `settings.yaml` → Global thresholds and weights

Keeps business logic separate from code.

---

## 🔹 `data/`

- Sample inputs
- Testing datasets
- Debug logs (optional)

---

## 🔹 `chatbot/engine/`

Core orchestration logic:

- `chatbot_engine.py` → Entry point for processing messages
- `intent_classifier.py` → Scores all intents
- `intent_resolver.py` → Selects best intent
- `scorer.py` → Implements scoring formula

---

## 🔹 `chatbot/intents/`

Each intent lives independently.

- `base_intent.py` → Abstract base class
- Specific intent modules extend base class
- `fallback_intent.py` → Handles unknown queries

This makes adding new intents easy and modular.

---

## 🔹 `chatbot/preprocessing/`

Text normalization pipeline:

- Cleaner → Removes noise
- Tokenizer → Splits words
- Entity extractor → Detects city, date, numbers
- Normalizer → Lemmatization/stemming

---

## 🔹 `chatbot/patterns/`

Matching logic separated cleanly:

- Exact pattern matching
- Regex matching
- Keyword scoring

Improves maintainability.

---

## 🔹 `chatbot/rules/`

Rule evaluation system:

- Mandatory rule validation
- Negative rule filtering
- Priority override logic

Keeps classification explainable and deterministic.

---

## 🔹 `chatbot/handlers/`

Business logic execution layer.

Once intent is classified:

- Handler generates response
- Can integrate APIs later

---

## 🔹 `tests/`

Unit tests for:

- Preprocessing
- Pattern matching
- Rule engine
- Intent classification

Encouraged structure for production-ready system.

---

## 🔹 `main.py`

Entry point.

Example responsibility:

- Accept user input
- Pass to ChatbotEngine
- Print response

---

# 🏗 Design Principles Followed

- Separation of concerns
- Open/Closed principle
- Config-driven intent definitions
- Modular architecture
- Scalable folder hierarchy
- Easy unit testing
- Clear extension points

---

# 🚀 Minimal Version (For Interviews)

If interviewer wants lightweight structure:

```
chatbot/
│
├── intent_classifier.py
├── rule_engine.py
├── pattern_matcher.py
├── preprocessing.py
├── intents.py
└── main.py
```
