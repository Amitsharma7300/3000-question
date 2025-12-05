# 3000 Programming Questions Platform

A comprehensive collection of **3050 programming questions** across multiple topics with difficulty levels, test cases, and coin rewards.

## 📊 Overview

| Category | Questions | Easy | Medium | Hard | Total Coins |
|----------|-----------|------|--------|------|-------------|
| Loops | 450 | 200 | 150 | 100 | 9,500 |
| Arrays | 450 | 200 | 150 | 100 | 9,500 |
| Strings | 450 | 200 | 150 | 100 | 9,500 |
| DSA | 1,050 | 350 | 350 | 350 | 35,000 |
| SQL | 650 | 200 | 250 | 200 | 16,750 |
| **TOTAL** | **3,050** | **1,150** | **1,050** | **850** | **80,250** |

## 📁 Project Structure

```
3000 question/
├── data/
│   └── questions/
│       ├── loops_questions.json      # 450 loop-based questions
│       ├── arrays_questions.json     # 450 array-based questions
│       ├── strings_questions.json    # 450 string manipulation questions
│       ├── dsa_questions.json        # 1050 data structures & algorithms questions
│       ├── sql_questions.json        # 650 SQL questions
│       ├── all_questions.json        # Combined all questions (3050 total)
│       └── index.json                # Summary statistics
├── generate_all_questions.py         # Script to generate all questions
└── README.md                         # This file
```

## 🎯 Difficulty Levels & Rewards

### Easy Level
- **Coin Reward:** 10 coins per question
- **Total Questions:** 1,150
- **Total Coins:** 11,500
- **Topics:** Basic concepts, fundamental algorithms, simple implementations

### Medium Level
- **Coin Reward:** 25 coins per question
- **Total Questions:** 1,050
- **Total Coins:** 26,250
- **Topics:** Intermediate algorithms, combined data structures, optimization problems

### Hard Level
- **Coin Reward:** 50 coins per question
- **Total Questions:** 850
- **Total Coins:** 42,500
- **Topics:** Advanced algorithms, complex data structures, optimization techniques

## 📚 Question Categories

### 1. **Loops (450 Questions)**
Focus on iterative programming and loop control structures.
- Nested loops
- Fibonacci series
- Prime number checking
- Pattern printing
- Loop optimization
- **Questions ID Range:** LOOP_E_* / LOOP_M_* / LOOP_H_*

### 2. **Arrays (450 Questions)**
Array manipulation, searching, and sorting problems.
- Array traversal
- Subarray problems
- Sorting algorithms
- Searching techniques
- Two-pointer approaches
- **Questions ID Range:** ARR_E_* / ARR_M_* / ARR_H_*

### 3. **Strings (450 Questions)**
String manipulation and pattern matching.
- Palindrome checking
- Anagrams
- String searching
- Pattern matching
- String encoding/decoding
- **Questions ID Range:** STR_E_* / STR_M_* / STR_H_*

### 4. **Data Structures & Algorithms (1,050 Questions)**
Comprehensive DSA questions.
- Sorting algorithms (Bubble, Quick, Merge, Heap)
- Searching techniques (Linear, Binary)
- Tree operations (Traversal, Height, LCA)
- Graph algorithms (BFS, DFS, Dijkstra)
- Advanced topics (Segment Trees, Fenwick Trees, Tries)
- **Questions ID Range:** DSA_E_* / DSA_M_* / DSA_H_*

### 5. **SQL (650 Questions)**
Database query writing and optimization.
- SELECT queries
- JOIN operations
- Aggregation functions
- Subqueries
- Window functions
- **Questions ID Range:** SQL_E_* / SQL_M_* / SQL_H_*

## 📋 Question JSON Format

Each question follows this format:

```json
{
  "id": "LOOP_E_0001",
  "title": "Print numbers 1 to N - Question 1",
  "description": "Write a program to print numbers from 1 to N",
  "category": "loops",
  "difficulty": "easy",
  "coins": 10,
  "constraints": "1 <= N <= 100",
  "solution_hint": "Use a simple for loop from 1 to N",
  "test_cases": [
    {
      "input": {"n": 5},
      "expected_output": "Output"
    }
  ]
}
```

## 🔑 Question ID Format

- **First Part:** Category (LOOP, ARR, STR, DSA, SQL)
- **Second Part:** Difficulty (E=Easy, M=Medium, H=Hard)
- **Third Part:** Sequential number (0001-XXXX)

Example: `ARR_M_0025` = Array, Medium difficulty, 25th question

## 💾 Using the Questions

### 1. Load All Questions
```python
import json

with open('data/questions/all_questions.json', 'r') as f:
    questions = json.load(f)
print(f"Total questions: {len(questions)}")
```

### 2. Filter by Category
```python
loops_questions = [q for q in questions if q['category'] == 'loops']
print(f"Loops questions: {len(loops_questions)}")
```

### 3. Filter by Difficulty
```python
easy_questions = [q for q in questions if q['difficulty'] == 'easy']
print(f"Easy questions: {len(easy_questions)}")
```

### 4. Get Statistics
```python
with open('data/questions/index.json', 'r') as f:
    stats = json.load(f)
print(f"Total coins: {stats['total_coins']}")
```

## 🎮 Features

✅ **3050+ Questions** - Comprehensive coverage of programming topics
✅ **Multiple Difficulty Levels** - Easy, Medium, Hard
✅ **Coin Reward System** - Gamified learning experience
✅ **Test Cases** - Each question includes sample test cases
✅ **Solution Hints** - Guidance without complete solutions
✅ **Constraints** - Clear input/output constraints
✅ **Well Organized** - Categorized by topic and difficulty
✅ **JSON Format** - Easy to integrate with applications
✅ **Indexed & Searchable** - Quick access to questions

## 🔍 Question Statistics

### By Difficulty
- **Easy:** 1,150 questions (37.7%)
- **Medium:** 1,050 questions (34.4%)
- **Hard:** 850 questions (27.9%)

### By Category
- **DSA:** 1,050 questions (34.4%)
- **Loops:** 450 questions (14.8%)
- **Arrays:** 450 questions (14.8%)
- **Strings:** 450 questions (14.8%)
- **SQL:** 650 questions (21.3%)

### Total Reward
- **Total Coins Available:** 80,250 coins
- **Average Coins per Question:** 26.3

## 🚀 Getting Started

1. **Generate Questions:**
   ```bash
   python generate_all_questions.py
   ```

2. **Load Questions:**
   ```python
   import json
   with open('data/questions/all_questions.json') as f:
       questions = json.load(f)
   ```

3. **Build Your App:**
   - Create a quiz application
   - Build a learning platform
   - Develop interview prep tool
   - Create competitive programming training

## 📖 Example Usage

### Get a Random Question
```python
import json
import random

with open('data/questions/all_questions.json') as f:
    questions = json.load(f)

random_question = random.choice(questions)
print(f"Question: {random_question['title']}")
print(f"Difficulty: {random_question['difficulty']}")
print(f"Reward: {random_question['coins']} coins")
```

### Build a Quiz
```python
def run_quiz(category, difficulty, num_questions=10):
    with open('data/questions/all_questions.json') as f:
        questions = json.load(f)
    
    filtered = [q for q in questions 
                if q['category'] == category 
                and q['difficulty'] == difficulty]
    
    quiz_questions = random.sample(filtered, min(num_questions, len(filtered)))
    
    score = 0
    for q in quiz_questions:
        print(f"\n{q['title']}")
        print(f"Description: {q['description']}")
        print(f"Hint: {q['solution_hint']}")
        # Get user answer and score
    
    total_coins = sum(q['coins'] for q in quiz_questions)
    print(f"\nYou earned {score * 10} out of {total_coins} coins!")
```

## 🔗 Integration Options

- **Web Application** - REST API for questions
- **Mobile App** - JSON data for offline mode
- **Learning Platform** - LMS integration
- **Interview Prep** - Mock test generation
- **Competitive Programming** - Problem sets and rankings

## 📝 Question Attributes

Each question includes:
- **ID** - Unique identifier
- **Title** - Question name
- **Description** - Detailed problem statement
- **Category** - Topic (loops, arrays, strings, dsa, sql)
- **Difficulty** - Level (easy, medium, hard)
- **Coins** - Reward points
- **Constraints** - Input/output limits
- **Solution Hint** - Guidance for solving
- **Test Cases** - Sample input/output pairs

## 🎓 Learning Path

### Beginner
1. Start with **Easy** difficulty questions
2. Focus on **Loops** and **Arrays** first
3. Progress to **Strings**
4. Learn basic **DSA** (Sorting, Searching)

### Intermediate
1. Solve **Medium** difficulty questions
2. Study **Advanced DSA** (Trees, Graphs)
3. Learn **SQL** basics and joins
4. Practice complex array problems

### Advanced
1. Tackle **Hard** difficulty questions
2. Master **Advanced DSA** (Dynamic Programming, Graphs)
3. Learn **SQL optimization** and window functions
4. Practice algorithmic problem solving

## 📊 Data Files

### all_questions.json
- Complete collection of all 3050 questions
- File size: ~2-3 MB
- Format: JSON array of question objects

### Category-specific Files
- `loops_questions.json` - 450 questions
- `arrays_questions.json` - 450 questions
- `strings_questions.json` - 450 questions
- `dsa_questions.json` - 1050 questions
- `sql_questions.json` - 650 questions

### index.json
- Statistics and summary
- Total counts by category and difficulty
- Total coins available

## 🛠️ Customization

### Generate Custom Questions
You can modify `generate_all_questions.py` to:
- Adjust difficulty distribution
- Change coin rewards
- Add new categories
- Customize constraints

### Extend Question Set
```python
# Add your own questions
new_questions = {
    "id": "LOOP_E_0451",
    "title": "Custom Question",
    "description": "Your question description",
    # ... other fields
}
```

## ✨ Features Coming Soon

- Question explanations
- Video solutions
- Code templates
- Performance benchmarks
- Leaderboard system
- Difficulty rating from users
- Related questions suggestions

## 📄 License

This question set is provided for educational purposes. Feel free to use, modify, and distribute for learning and development.

## 🤝 Contributing

Have suggestions for improvement? Feel free to:
- Add more questions
- Improve test cases
- Add solution links
- Suggest better hints

## 📞 Support

For issues, suggestions, or questions:
- Review the JSON structure
- Check question IDs for duplicates
- Verify test case formats
- Ensure category values are lowercase

## 🎯 Key Statistics Summary

```
Total Questions: 3050
Total Coins: 80,250
Average Coins/Question: 26.3

Breakdown by Difficulty:
- Easy (10 coins): 1,150 questions = 11,500 coins
- Medium (25 coins): 1,050 questions = 26,250 coins  
- Hard (50 coins): 850 questions = 42,500 coins

Breakdown by Category:
- Loops: 450 questions
- Arrays: 450 questions
- Strings: 450 questions
- DSA: 1,050 questions
- SQL: 650 questions
```

---

**Created:** December 2024
**Total Questions:** 3,050
**Total Coins:** 80,250
**Status:** ✅ Ready for use
