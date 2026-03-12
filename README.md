# code_muscles
Just practicing python skills

# Assessment 004 — Advanced Python Loops, Algorithms & Data Processing

## Learning Outcomes Assessed

This assessment evaluates your ability to apply the following concepts in Python:

* Conditional statements
* Functions
* Basic loops
* Advanced loops
* Algorithmic problem solving
* Data processing using lists and dictionaries
* Regex validation
* Breaking down complex problem statements
* Running and interpreting command-line tests

---

# Assessment Structure

This assessment has **two sections**.

| Section              | Weight |
| -------------------- | ------ |
| Coding Assessment    | 60%    |
| Form-Based Questions | 40%    |

You may complete them **in any order**.

---

# Coding Score

Your coding score is determined by the number of tests you pass.

Let:

* **T** = total tests
* **P** = tests passed

```
Coding Score = (P / T) × 60%
```

Final score:

```
Final Score = Coding Score + Form Score
```

Minimum pass mark: **60%**

---

# Running Your Tests

Run all tests:

```
python3 -m pytest tests/test_loopy_hard.py -v
```

Run a specific test:

```
python3 -m pytest tests/test_loopy_hard.py::TestFunctions::test_two_sum_basic -v
```

Run with extra detail:

```
python3 -m pytest tests/test_loopy_hard.py -vv
```

---

# Project Structure

```
advanced_loops_assessment/

loopy_hard.py
tests/test_loopy_hard.py
README.md
```

---

# Coding Questions

You must complete **7 functions** in `loopy_hard.py`.

Each function is based on a **real-world scenario**. Carefully read the story, extract the requirements, and implement the algorithm.

Your code will be evaluated against **over 100 automated tests**, including:

* Edge cases
* Randomized tests
* Large inputs
* Stress tests

---

# Question 1 — market_revenue(transactions)

A local community market operates every Saturday in a busy township square. Vendors sell a variety of goods such as fruit, vegetables, snacks, and handmade products. At the end of each day, the market manager collects transaction reports from each stall.

Each report entry contains three pieces of information:

* The name of the product sold
* The quantity sold during the day
* The price per item

These records are stored as tuples in a list.

Example transaction:

```
("apple", 4, 5)
```

This means **4 apples were sold at R5 each**.

The market manager wants a quick way to calculate the **total revenue generated across all stalls** for the day.

Your task is to write a function that loops through the transaction list, calculates the revenue for each entry, and returns the **total revenue**.

If there are no transactions, the function should return **0**.

---

# Question 2 — longest_unique_word(sentence)

A data analytics company is building a tool that helps journalists analyse large collections of text such as speeches, articles, and interview transcripts.

One feature of the tool is the ability to identify **unique vocabulary** in a sentence.

For this task, a **unique word** is defined as a word that appears **exactly once** in the sentence.

Your program must:

1. Count how many times each word appears.
2. Identify all words that appear only once.
3. Return the **longest unique word**.

If two unique words have the same length, return the **first one that appears in the sentence**.

If the sentence is empty, return an empty string.

---

# Question 3 — two_sum(nums, target)

A software engineer at a fintech startup is designing a transaction analysis tool. The tool receives a list of numbers representing individual transaction amounts.

Sometimes the system needs to determine whether **two transactions combine to match a specific value** requested by auditors.

You are given:

* A list of integers
* A target value

Your task is to find **two numbers whose sum equals the target** and return their **indexes**.

Constraints:

* Each input has exactly one valid solution.
* You may not use the same element twice.

This is a classic algorithm problem often asked in technical interviews.

---

# Question 4 — peak_temperatures(temps)

The national weather service is analysing temperature data to detect short bursts of extreme heat.

Meteorologists define a **temperature spike** as a day where the temperature is strictly higher than both the previous day and the following day.

Given a list of daily temperature readings, your function must return **all temperatures that qualify as spikes**.

Important notes:

* The first and last elements cannot be spikes because they do not have two neighbours.
* Temperatures must be **strictly greater** than both neighbours.

---

# Question 5 — email_filter(emails)

A large website is importing user accounts from several outdated systems. Unfortunately, the imported dataset contains many incorrectly formatted email addresses.

Your task is to validate each email address and separate them into two groups:

* Valid email addresses
* Invalid email addresses

A valid email follows the general format:

```
username@domain.extension
```

Your function should return a dictionary with two keys:

```
{
"valid": [...],
"invalid": [...]
}
```

---

# Question 6 — stock_profit(prices)

You are given a list of stock prices where each element represents the price of a stock on a specific day.

An investor wants to know the **maximum profit** they could make with only **one buy and one sell transaction**.

Rules:

* You must buy before you sell.
* You can only buy once.
* You can only sell once.

If no profit is possible, return **0**.

---

# Question 7 — inventory_projection(stock, daily_sales)

A warehouse manager is planning inventory for an upcoming week.

They have:

* The current stock level
* A list of projected daily sales

Each day, the projected sales amount is subtracted from the inventory.

Your function must simulate this process day by day.

If the stock reaches **zero or below**, return:

```
Inventory will run out on day X.
```

If the inventory lasts through all projected days, return:

```
Inventory lasts entire period. Remaining stock: X
```

---

# Your Goal

Complete all functions inside:

```
loopy_hard.py
```

Make sure:

* Your code runs without errors
* All algorithms are correct
* **All tests pass**
