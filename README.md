# 🗺️ Graph Shortest Path Finder (Python)

This repository contains a **single Python program** that builds a small graph of major African cities and computes the **shortest path from Lagos to Johannesburg** using a breadth-first search (BFS)–style approach.  

The work was completed as part of a **Data Structures & Algorithms** lab and is accompanied by a short **written analysis document** explaining the design and results.

---

## 📁 Files in This Repository

- ` path_finder_1.0.py`

- `Analysis_Report.docx`
---

## 🔍 What the Program Demonstrates

- Representation of a **graph** in Python  
- Use of an **adjacency matrix** to show connections  
- A **shortest path search** based on breadth-first traversal  
- Basic **OOP principles** (custom `Graph` class and methods)  
- Clear, readable console output

This makes it a good example of applying core algorithm and data structure concepts in a simple, practical way.

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.

2. Download or clone this repository.

3. In a terminal or command prompt, navigate to the folder where the file is stored and run:

   ```bash
   path_finder_1.0.py

---

## You should see:
The adjacency matrix printed with city names as headers
The computed shortest path from Lagos to Johannesburg, for example:

Shortest path from Lagos to Johannesburg:
['Lagos', 'Accra', 'Cairo', 'Johannesburg']

Process finished with exit code 0

---

## 🧠 High-Level Algorithm (Simple Explanation)
Each city is added as a vertex in the graph.
Direct routes between cities are added as edges.
The graph builds an adjacency matrix to show which cities are directly connected.
A shortest path method explores the graph layer by layer starting from Lagos, keeping track of visited cities and their predecessors.
When Johannesburg is reached, the program reconstructs the path by walking back through the predecessors and prints the result.

---

## 📬 Contact
Ogheneyoma Elim Ebresafe
📧 
Feel free to review the code or analysis document and reach out with feedback, suggestions, or opportunities.
