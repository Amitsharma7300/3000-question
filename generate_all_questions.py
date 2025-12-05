#!/usr/bin/env python3
import json
import os

# Create data directory if it doesn't exist
os.makedirs('data/questions', exist_ok=True)

# ==================== LOOPS QUESTIONS ====================
loops_questions = []
loop_id = 1

# Easy Loops (200)
easy_loop_titles = [
    "Print numbers 1 to N", "Calculate sum of 1 to N", "Count vowels in string",
    "Print multiplication table", "Check palindrome number", "Find GCD of two numbers",
    "Count digits in number", "Reverse a number", "Check Armstrong number",
    "Print pattern with stars", "Simple counter loop", "Calculate average",
    "Print even numbers", "Print odd numbers", "Count specific digit"
]

for i in range(200):
    title = easy_loop_titles[i % len(easy_loop_titles)]
    loops_questions.append({
        "id": f"LOOP_E_{loop_id:04d}",
        "title": f"{title} - Question {loop_id}",
        "description": f"Write a program to {title}",
        "category": "loops",
        "difficulty": "easy",
        "coins": 10,
        "constraints": "1 <= N <= 100",
        "solution_hint": f"Use a loop to solve {title}",
        "test_cases": [
            {"input": {"n": 5}, "expected_output": "Output"},
            {"input": {"n": 3}, "expected_output": "Output"},
            {"input": {"n": 1}, "expected_output": "Output"}
        ]
    })
    loop_id += 1

# Medium Loops (150)
medium_loop_titles = [
    "Fibonacci Series up to N", "Calculate factorial", "Print pyramid pattern",
    "Find GCD using Euclidean", "Check prime number", "Generate powers of 2",
    "Find sum of digits", "Print Pascal triangle", "Count set bits",
    "Find all divisors", "Number to binary", "Binary to decimal",
    "Check perfect number", "Find Harshad number", "Generate sequence"
]

for i in range(150):
    title = medium_loop_titles[i % len(medium_loop_titles)]
    loops_questions.append({
        "id": f"LOOP_M_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Implement {title}",
        "category": "loops",
        "difficulty": "medium",
        "coins": 25,
        "constraints": "1 <= N <= 1000",
        "solution_hint": f"Use nested loops for {title}",
        "test_cases": [
            {"input": {"n": 5}, "expected_output": "0 1 1 2 3"},
            {"input": {"n": 8}, "expected_output": "0 1 1 2 3 5 8 13"},
            {"input": {"n": 3}, "expected_output": "0 1 1"}
        ]
    })

# Hard Loops (100)
hard_loop_titles = [
    "Sieve of Eratosthenes", "Generate permutations", "Find all divisors efficiently",
    "Nested loop optimization", "Complex pattern printing", "Advanced loop algorithms",
    "Prime factorization", "Modular exponentiation", "Josephus problem",
    "Collatz conjecture", "Sum of powers", "Catalan numbers",
    "Bell numbers", "Stirling numbers", "Partition function"
]

for i in range(100):
    title = hard_loop_titles[i % len(hard_loop_titles)]
    loops_questions.append({
        "id": f"LOOP_H_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Advanced: {title}",
        "category": "loops",
        "difficulty": "hard",
        "coins": 50,
        "constraints": "1 <= N <= 10000",
        "solution_hint": f"Optimize using {title}",
        "test_cases": [
            {"input": {"n": 10}, "expected_output": "2 3 5 7"},
            {"input": {"n": 20}, "expected_output": "2 3 5 7 11 13 17 19"},
            {"input": {"n": 30}, "expected_output": "2 3 5 7 11 13 17 19 23 29"}
        ]
    })

with open('data/questions/loops_questions.json', 'w') as f:
    json.dump(loops_questions, f, indent=2)
print(f"✓ Created {len(loops_questions)} loops questions")

# ==================== ARRAY QUESTIONS ====================
array_questions = []
array_id = 1

# Easy Arrays (200)
easy_array_titles = [
    "Find Maximum Element", "Find Minimum Element", "Sum of array elements",
    "Reverse an array", "Search element in array", "Count occurrences",
    "Remove duplicates", "Array rotation", "Merge two arrays",
    "Find missing number", "Check if sorted", "Array intersection",
    "Array union", "First and last element", "Element at index",
    "Array copy", "Array slice", "Array average", "Element frequency",
    "Duplicate check", "Print array", "Array to string", "String to array",
    "Even odd split", "Positive negative split"
]

for i in range(200):
    title = easy_array_titles[i % len(easy_array_titles)]
    array_questions.append({
        "id": f"ARR_E_{array_id:04d}",
        "title": f"{title} - Question {array_id}",
        "description": f"Solve: {title}",
        "category": "arrays",
        "difficulty": "easy",
        "coins": 10,
        "constraints": "1 <= N <= 1000",
        "solution_hint": f"Iterate array for {title}",
        "test_cases": [
            {"input": {"arr": [1, 5, 3, 9, 2]}, "expected_output": 9},
            {"input": {"arr": [10, 20, 5]}, "expected_output": 20},
            {"input": {"arr": [-5, -1, -10]}, "expected_output": -1}
        ]
    })
    array_id += 1

# Medium Arrays (150)
medium_array_titles = [
    "Find Pair with Sum", "Find second largest", "Rotate array by K",
    "Remove duplicates with order", "Merge sorted arrays", "Find peak element",
    "Longest increasing subsequence", "Container with most water",
    "Product of array except self", "Next permutation", "Previous permutation",
    "Three sum", "Four sum", "Majority element", "Single number",
    "Missing number", "Duplicate number", "Intersection two arrays",
    "Union two arrays", "Sort by frequency", "Top K elements",
    "Find pairs difference", "Find triplets sum", "Array partition"
]

for i in range(150):
    title = medium_array_titles[i % len(medium_array_titles)]
    array_questions.append({
        "id": f"ARR_M_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Implement: {title}",
        "category": "arrays",
        "difficulty": "medium",
        "coins": 25,
        "constraints": "1 <= N <= 10000",
        "solution_hint": f"Use optimal approach for {title}",
        "test_cases": [
            {"input": {"arr": [1, 5, 7], "target": 6}, "expected_output": True},
            {"input": {"arr": [1, 5, 3, 9], "target": 14}, "expected_output": True},
            {"input": {"arr": [1, 5, 3], "target": 15}, "expected_output": False}
        ]
    })

# Hard Arrays (100)
hard_array_titles = [
    "Maximum Subarray Sum (Kadane's)", "Longest increasing subsequence DP",
    "Median of two sorted arrays", "Trapping rain water", "Best time to buy/sell",
    "Word search in matrix", "Sliding window maximum", "Jump game",
    "Gas station", "Candy distribution", "Minimum subarray sum",
    "Longest subarray sum", "Count subarrays sum", "Max product subarray",
    "Subarray with K distinct", "Minimum window substring", "Array combination sum",
    "Permutation sequence", "Next greater element", "Largest rectangle",
    "Maximal rectangle", "Distinct subsequences", "Longest arithmetic sequence"
]

for i in range(100):
    title = hard_array_titles[i % len(hard_array_titles)]
    array_questions.append({
        "id": f"ARR_H_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Advanced: {title}",
        "category": "arrays",
        "difficulty": "hard",
        "coins": 50,
        "constraints": "1 <= N <= 100000",
        "solution_hint": f"Use advanced technique for {title}",
        "test_cases": [
            {"input": {"arr": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}, "expected_output": 6},
            {"input": {"arr": [5, -3, 5]}, "expected_output": 7},
            {"input": {"arr": [-1, -2, -3]}, "expected_output": -1}
        ]
    })

with open('data/questions/arrays_questions.json', 'w') as f:
    json.dump(array_questions, f, indent=2)
print(f"✓ Created {len(array_questions)} array questions")

# ==================== STRING QUESTIONS ====================
string_questions = []
string_id = 1

# Easy Strings (200)
easy_string_titles = [
    "Palindrome Check", "Count vowels", "Reverse string", "Convert to uppercase",
    "Find first character occurrence", "String length", "Compare strings",
    "Check substring", "Remove spaces", "Count consonants", "Toggle case",
    "Count words", "String concatenation", "Check empty string", "Remove leading/trailing spaces",
    "Simple string search", "Count specific character", "Replace character",
    "String to integer", "Integer to string", "Check alphanumeric",
    "Count digits", "Count special chars", "First and last char",
    "Char to ASCII", "ASCII to char", "String reverse words"
]

for i in range(200):
    title = easy_string_titles[i % len(easy_string_titles)]
    string_questions.append({
        "id": f"STR_E_{string_id:04d}",
        "title": f"{title} - Question {string_id}",
        "description": f"Solve: {title}",
        "category": "strings",
        "difficulty": "easy",
        "coins": 10,
        "constraints": "1 <= len(s) <= 10000",
        "solution_hint": f"Simple string operation for {title}",
        "test_cases": [
            {"input": {"s": "racecar"}, "expected_output": True},
            {"input": {"s": "hello"}, "expected_output": False},
            {"input": {"s": "aba"}, "expected_output": True}
        ]
    })
    string_id += 1

# Medium Strings (150)
medium_string_titles = [
    "Check Anagram", "Longest substring without repeating", "String compression",
    "Check rotation", "Remove duplicates", "Count character frequency",
    "Find first non-repeating", "Reverse words", "Group anagrams",
    "Valid parentheses string", "Find all occurrences", "Replace substring",
    "Split string", "Join strings", "String contains",
    "Starts with ends with", "Trim whitespace", "Case sensitive search",
    "String parsing", "URL encoding", "HTML decode",
    "Password strength", "Name validation", "Email validation",
    "Phone validation", "IP address check"
]

for i in range(150):
    title = medium_string_titles[i % len(medium_string_titles)]
    string_questions.append({
        "id": f"STR_M_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Implement: {title}",
        "category": "strings",
        "difficulty": "medium",
        "coins": 25,
        "constraints": "1 <= len(s) <= 50000",
        "solution_hint": f"Use hash map or two-pointer for {title}",
        "test_cases": [
            {"input": {"s1": "abcd", "s2": "dcba"}, "expected_output": True},
            {"input": {"s1": "listen", "s2": "silent"}, "expected_output": True},
            {"input": {"s1": "hello", "s2": "world"}, "expected_output": False}
        ]
    })

# Hard Strings (100)
hard_string_titles = [
    "Longest Palindromic Substring", "Regular expression matching",
    "Edit distance (Levenshtein)", "Shortest palindrome", "Wildcard matching",
    "Min window substring", "Word break", "Scramble string",
    "Word pattern", "Isomorphic strings", "Substring with concatenation",
    "Valid number", "Text justification", "Integer to Roman",
    "Roman to integer", "Count and say", "Missing number string",
    "Multiply strings", "Binary string operations", "Decode string",
    "Encode string", "Sliding window substring", "String interleaving",
    "Compress string advanced", "Find celebrity", "Shortest distance word"
]

for i in range(100):
    title = hard_string_titles[i % len(hard_string_titles)]
    string_questions.append({
        "id": f"STR_H_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Advanced: {title}",
        "category": "strings",
        "difficulty": "hard",
        "coins": 50,
        "constraints": "1 <= len(s) <= 10000",
        "solution_hint": f"Use DP or advanced technique for {title}",
        "test_cases": [
            {"input": {"s": "babad"}, "expected_output": "bab"},
            {"input": {"s": "cbbd"}, "expected_output": "bb"},
            {"input": {"s": "a"}, "expected_output": "a"}
        ]
    })

with open('data/questions/strings_questions.json', 'w') as f:
    json.dump(string_questions, f, indent=2)
print(f"✓ Created {len(string_questions)} string questions")

# ==================== DSA QUESTIONS ====================
dsa_questions = []
dsa_id = 1

# Easy DSA (350)
dsa_easy_titles = [
    "Linear Search", "Binary Search", "Bubble Sort", "Selection Sort",
    "Insertion Sort", "Stack Implementation", "Queue Implementation",
    "Linked List Traversal", "Tree Inorder Traversal", "Graph DFS", "BFS Traversal",
    "Single linked list insertion", "Queue using stack", "Stack overflow check",
    "Implement priority queue", "Find middle of linked list", "Detect cycle in linked list",
    "Tree height", "Find leaf nodes", "Level order traversal", "Graph adjacency matrix"
]

for i in range(350):
    title = dsa_easy_titles[i % len(dsa_easy_titles)]
    dsa_questions.append({
        "id": f"DSA_E_{dsa_id:04d}",
        "title": f"{title} - Question {dsa_id}",
        "description": f"Implement: {title}",
        "category": "dsa",
        "difficulty": "easy",
        "coins": 10,
        "constraints": "1 <= N <= 10000",
        "solution_hint": f"Standard algorithm for {title}",
        "test_cases": [
            {"input": {"arr": [1, 2, 3, 4, 5]}, "expected_output": "Success"},
            {"input": {"arr": [5, 2, 8, 1, 9]}, "expected_output": "Success"}
        ]
    })
    dsa_id += 1

# Medium DSA (350)
dsa_medium_titles = [
    "Merge Sort", "Quick Sort", "Heap Sort", "LRU Cache",
    "Balanced Parentheses", "Linked List Reversal", "LCA in BST",
    "Tree Diameter", "Number of Islands", "Topological Sort", "Union-Find",
    "Trie implementation", "Binary search tree", "AVL tree rotation",
    "Dijkstra's algorithm", "BFS shortest path", "DFS all paths",
    "N-ary tree traversal", "Symmetric tree check", "Serialize tree"
]

for i in range(350):
    title = dsa_medium_titles[i % len(dsa_medium_titles)]
    dsa_questions.append({
        "id": f"DSA_M_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Solve: {title}",
        "category": "dsa",
        "difficulty": "medium",
        "coins": 25,
        "constraints": "1 <= N <= 100000",
        "solution_hint": f"Use appropriate technique for {title}",
        "test_cases": [
            {"input": {"arr": [3, 1, 4, 1, 5, 9, 2, 6]}, "expected_output": "Solved"}
        ]
    })

# Hard DSA (350)
dsa_hard_titles = [
    "Longest Common Subsequence", "Min Cost Path", "Word Ladder",
    "Strongly Connected Components", "Maximum Flow", "Segment Tree",
    "Fenwick Tree (BIT)", "Suffix Array", "KMP Pattern Matching",
    "Rabin-Karp Hashing", "Manacher's Algorithm", "Trie with DP",
    "Graph coloring", "Traveling salesman", "Matrix chain multiplication",
    "Convex hull", "Heavy light decomposition", "Link cut tree",
    "Persistent segment tree", "Sqrt decomposition", "Centroid decomposition"
]

for i in range(350):
    title = dsa_hard_titles[i % len(dsa_hard_titles)]
    dsa_questions.append({
        "id": f"DSA_H_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Advanced: {title}",
        "category": "dsa",
        "difficulty": "hard",
        "coins": 50,
        "constraints": "1 <= N <= 1000000",
        "solution_hint": f"Advanced technique required for {title}",
        "test_cases": [
            {"input": {"s": "ABCDGH", "t": "AEDFHR"}, "expected_output": "ADH"}
        ]
    })

with open('data/questions/dsa_questions.json', 'w') as f:
    json.dump(dsa_questions, f, indent=2)
print(f"✓ Created {len(dsa_questions)} DSA questions")

# ==================== SQL QUESTIONS ====================
sql_questions = []
sql_id = 1

# Easy SQL (200)
sql_easy_titles = [
    "SELECT all records", "SELECT with WHERE", "SELECT with ORDER BY",
    "SELECT DISTINCT", "COUNT aggregate", "SUM aggregate", "AVG aggregate",
    "MAX aggregate", "MIN aggregate", "INSERT record", "Basic JOIN",
    "DELETE record", "UPDATE record", "WHERE conditions", "LIKE operator",
    "NULL checks", "NOT NULL", "Greater than", "Less than", "Equal to",
    "Sort ascending", "Sort descending", "Limit results", "Offset", "Alias column"
]

for i in range(200):
    title = sql_easy_titles[i % len(sql_easy_titles)]
    sql_questions.append({
        "id": f"SQL_E_{sql_id:04d}",
        "title": f"{title} - Question {sql_id}",
        "description": f"Write SQL query for: {title}",
        "category": "sql",
        "difficulty": "easy",
        "coins": 10,
        "constraints": "Basic SQL knowledge required",
        "solution_hint": f"Use {title} in your query",
        "test_cases": [
            {"input": {"table": "users"}, "expected_output": "Result set"}
        ]
    })
    sql_id += 1

# Medium SQL (250)
sql_medium_titles = [
    "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "GROUP BY",
    "HAVING clause", "UPDATE records", "DELETE records",
    "LIKE pattern", "IN operator", "BETWEEN operator", "Subquery",
    "DISTINCT with aggregate", "UNION operator", "CASE statement", "LIMIT clause",
    "Multiple joins", "Self join", "Nested subquery", "Aggregate with group",
    "Date operations", "String functions", "Math functions", "COALESCE", "NULLIF",
    "CAST function", "Type conversion", "Multiple conditions"
]

for i in range(250):
    title = sql_medium_titles[i % len(sql_medium_titles)]
    sql_questions.append({
        "id": f"SQL_M_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Write SQL query using: {title}",
        "category": "sql",
        "difficulty": "medium",
        "coins": 25,
        "constraints": "Intermediate SQL required",
        "solution_hint": f"Apply {title} technique",
        "test_cases": [
            {"input": {"tables": ["users", "orders"]}, "expected_output": "Joined result"}
        ]
    })

# Hard SQL (200)
sql_hard_titles = [
    "Window Functions", "CTE (Common Table Expression)", "Recursive CTE",
    "Correlated Subquery", "Self Join", "Cross Join", "EXISTS operator",
    "NOT EXISTS operator", "Full Outer Join", "Pivot Table",
    "Date Functions", "String Functions", "Index Optimization",
    "Query Execution Plan", "Transaction Control", "Stored procedures",
    "Triggers", "Views", "Materialized views", "Query tuning",
    "Execution hints", "Partition queries", "Sharding strategy",
    "Window functions advanced", "Recursive queries", "Complex joins",
    "Analytical functions", "Running total", "Ranking functions"
]

for i in range(200):
    title = sql_hard_titles[i % len(sql_hard_titles)]
    sql_questions.append({
        "id": f"SQL_H_{i+1:04d}",
        "title": f"{title} - Question {i+1}",
        "description": f"Advanced SQL: {title}",
        "category": "sql",
        "difficulty": "hard",
        "coins": 50,
        "constraints": "Advanced SQL knowledge required",
        "solution_hint": f"Use {title} for optimal solution",
        "test_cases": [
            {"input": {"query_type": "advanced"}, "expected_output": "Complex result"}
        ]
    })

with open('data/questions/sql_questions.json', 'w') as f:
    json.dump(sql_questions, f, indent=2)
print(f"✓ Created {len(sql_questions)} SQL questions")

# ==================== COMBINED INDEX ====================
all_questions = loops_questions + array_questions + string_questions + dsa_questions + sql_questions

summary = {
    "total_questions": len(all_questions),
    "categories": {
        "loops": len(loops_questions),
        "arrays": len(array_questions),
        "strings": len(string_questions),
        "dsa": len(dsa_questions),
        "sql": len(sql_questions)
    },
    "difficulty_breakdown": {
        "easy": sum(1 for q in all_questions if q['difficulty'] == 'easy'),
        "medium": sum(1 for q in all_questions if q['difficulty'] == 'medium'),
        "hard": sum(1 for q in all_questions if q['difficulty'] == 'hard')
    },
    "total_coins": sum(q['coins'] for q in all_questions)
}

with open('data/questions/all_questions.json', 'w') as f:
    json.dump(all_questions, f, indent=2)

with open('data/questions/index.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"Total Questions: {summary['total_questions']}")
print(f"Total Coins Available: {summary['total_coins']}")
print(f"\nBy Category:")
for cat, count in summary['categories'].items():
    print(f"  {cat.capitalize()}: {count} questions")
print(f"\nBy Difficulty:")
for diff, count in summary['difficulty_breakdown'].items():
    print(f"  {diff.capitalize()}: {count} questions")
print("="*60)
