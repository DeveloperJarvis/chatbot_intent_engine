# **Low-Level Design (LLD)** for a **Chatbot Intent Engine**

---

# 1. Objective

Design an **Intent Classification Engine** that:

- Classifies user input into predefined intents
- Uses **rule-based logic + pattern matching**
- Is lightweight, explainable, and fast
- Works without ML models (pure deterministic NLP)

---

# 2. System Overview

```
User Input
    ↓
Preprocessing Layer
    ↓
Pattern & Rule Engine
    ↓
Intent Scorer
    ↓
Intent Resolver
    ↓
Response Router
```

---

# 3. Core Components (Low-Level Design)

## 3.1 Intent Definition Module

### Purpose:

Stores all intent definitions and matching criteria.

### Data Structure:

Each intent contains:

- `intent_name`
- `patterns`
- `keywords`
- `required_entities`
- `priority`
- `confidence_threshold`
- `fallback_flag`

### Example Intent Schema (Conceptual)

Intent:

- Name: `BookFlight`
- Patterns:
  - “book a flight”
  - “reserve ticket”
  - “flight to {city}”

- Keywords:
  - book, flight, ticket, travel

- Required Entities:
  - destination

- Priority: High

---

## 3.2 Preprocessing Layer

### Responsibilities:

1. Lowercasing
2. Punctuation removal
3. Stopword filtering
4. Tokenization
5. Lemmatization/Stemming
6. Named Entity Extraction (basic rule-based)

### Output:

Normalized text + tokens + extracted entities

### Example:

Input:

> “Can you book me a flight to New York tomorrow?”

After preprocessing:

- Tokens: [book, flight, new york, tomorrow]
- Entities:
  - city: New York
  - date: tomorrow

---

## 3.3 Pattern Matching Engine

### Matching Strategies:

1. Exact phrase matching
2. Regex pattern matching
3. Keyword presence scoring
4. Slot-based pattern matching
5. Context rules (optional)

---

### 3.3.1 Exact Pattern Match

Checks:

```
if cleaned_input contains predefined phrase
```

Use case:

- “track my order”
- “cancel subscription”

Fast and deterministic.

---

### 3.3.2 Regex-Based Pattern Matching

Used for:

- Variable inputs
- Structured queries

Example patterns:

- `flight to (city)`
- `order number \d+`

Allows dynamic slot capture.

---

### 3.3.3 Keyword Scoring

For each intent:

- Count keyword matches
- Apply weight per keyword
- Compute intent score

Example:

User input:

> “I want to reserve a ticket”

Matches:

- reserve → +2
- ticket → +1

Intent score = 3

---

### 3.3.4 Slot-Based Pattern Matching

Pattern:

```
[action] + [object] + [entity]
```

Example:
“book flight to Paris”

Slots:

- action: book
- object: flight
- entity: Paris

Matching requires:

- action keyword
- object keyword
- valid entity

---

## 3.4 Rule Engine

### Rule Types:

#### 1. Mandatory Rule

Intent valid only if required entity present.

Example:

- BookFlight requires destination

If missing → downgrade confidence.

---

#### 2. Negative Rule

Exclude if conflicting keyword found.

Example:
If input contains “refund” → not BookFlight.

---

#### 3. Priority Rule

Some intents override others.

Example:

- “cancel order 123”
  Should match CancelOrder before OrderStatus.

---

#### 4. Contextual Rule (Optional)

Uses previous conversation state.

Example:
User: “yes”
System checks previous pending intent.

---

## 3.5 Intent Scoring Engine

Each intent gets a score based on:

| Factor         | Weight |
| -------------- | ------ |
| Exact match    | 5      |
| Regex match    | 4      |
| Keyword match  | 1–3    |
| Entity present | 2      |
| Negative rule  | -5     |

### Formula (Conceptual):

```
Intent Score =
  (ExactMatchWeight × count)
+ (RegexWeight × count)
+ (KeywordWeight × keyword_hits)
+ (EntityBonus)
- (PenaltyRules)
```

---

## 3.6 Intent Resolver

### Logic:

1. Rank intents by score
2. Check threshold
3. Apply tie-breaking rule:
   - Higher priority
   - More entity matches

4. If no intent passes threshold → FallbackIntent

---

## 3.7 Fallback Intent

Triggers when:

- Score below threshold
- No pattern matched

Example:

- “I like turtles”

Returns:

- “I didn’t understand that. Can you rephrase?”

---

# 4. Class Design (Conceptual Python Structure)

---

## 4.1 Intent

Attributes:

- name
- patterns
- keywords
- required_entities
- priority
- threshold

Methods:

- match_patterns()
- match_keywords()
- validate_entities()
- calculate_score()

---

## 4.2 Preprocessor

Methods:

- clean_text()
- tokenize()
- extract_entities()

---

## 4.3 RuleEngine

Methods:

- apply_mandatory_rules()
- apply_negative_rules()
- apply_priority_rules()

---

## 4.4 IntentClassifier

Methods:

- classify(input_text)
- score_intents()
- resolve_best_intent()

---

## 4.5 ChatbotEngine

Methods:

- handle_message()
- route_to_handler(intent)

---

# 5. Data Flow (Step-by-Step)

1. User sends message
2. Preprocessor normalizes text
3. Entities extracted
4. Each intent:
   - Pattern match
   - Keyword match
   - Rule validation
   - Score calculated

5. IntentResolver selects best
6. Router sends to appropriate handler

---

# 6. Performance Considerations

- Precompile regex patterns
- Use Trie structure for keyword lookup
- Cache frequent inputs
- Maintain intent index by keywords

Time Complexity:

- O(N × M)
  - N = number of intents
  - M = patterns per intent

Optimizable with inverted index.

---

# 7. Extensibility

Future upgrades:

- Hybrid ML + rule engine
- Context-aware memory
- Confidence calibration
- Multi-intent detection
- Fuzzy matching
- Semantic similarity scoring

---

# 8. Advantages of Rule-Based Intent Engine

✔ Fully explainable
✔ No training data required
✔ Deterministic behavior
✔ Fast inference
✔ Easy debugging

---

# 9. Limitations

✖ Hard to scale with many intents
✖ Poor handling of paraphrasing
✖ Manual rule maintenance
✖ No semantic understanding

---

# 10. Optional Enhancements

- Synonym expansion (WordNet)
- Spell correction
- N-gram matching
- Intent grouping
- Versioned rule sets
- Analytics dashboard

---

# 11. Example Execution Scenario

Input:

> “Can you cancel my order 456?”

Process:

- Keywords: cancel, order
- Regex: order number detected
- Exact phrase: none
- Score:
  - Keyword: 3
  - Regex: 4
  - Entity: 2
  - Total: 9

Selected Intent:
`CancelOrder`
