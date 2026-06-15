"""Exercise 14. Substring Frequency Analysis
Practice Problem: Write a program to find how many times the substring “Emma” appears in a given string.

Exercise Purpose: Text analysis and pattern matching are core pillars of programming. This exercise introduces searching for a “needle in a haystack,” a fundamental concept for building search engines or data validation tools."""

x = input("Write a sentence: ").lower()

count_emma = x.count("emma")

print(f"Emma appeared {count_emma} times")
