"""
Program: Word Count Analyzer
Author: Farouk Bellili
Purpose: Analyze a text file, count frequency of each word, and display an alphabetical report.
Starter Code: None
Date: 2026-03-31
"""

from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath, stop_words=None):
        self._path = Path(filepath)
        self._frequencies = {}
        self._stop_words = stop_words if stop_words else []

    def process_file(self):
        if not self._path.exists():
            print(f"Error: File '{self._path}' not found.")
            return False
        try:
            with self._path.open("r", encoding="utf-8") as file:
                for line in file:
                    # Remove punctuation
                    line = line.translate(str.maketrans("", "", string.punctuation))
                    line = line.lower()
                    words = line.split()
                    for word in words:
                        if word not in self._stop_words:
                            self._frequencies[word] = self._frequencies.get(word, 0) + 1
            return True
        except FileNotFoundError:
            return False

    def print_report(self):
        print()
        for word in sorted(self._frequencies.keys()):
            print(f"{word:<12} :: {self._frequencies[word]}")
        print()

def main():
    # Dictionary of files
    files = {
        "1": "princess_mars.txt",
        "2": "Tarzan.txt",
        "3": "treasure_island.txt",
        "4": "monte_cristo.txt"
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for key, file in files.items():
            # Display name without .txt and with title format
            print(f"{key}. {Path(file).stem.replace('_', ' ').title()}")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
            break
        elif choice in files:
            filename = files[choice]
            print(f"\nProcessing '{filename}'...\n")
            analyzer = WordAnalyzer(filename)
            if analyzer.process_file():
                analyzer.print_report()
            input("Press Enter to return to the menu...")
        else:
            print("\nInvalid choice. Please select from 1-5.")
            input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
