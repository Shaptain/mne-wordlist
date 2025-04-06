# Add Wordlist Scoring to GNOME Crosswords Editor
# GNOME Crosswords: Wordlist Scoring Project

This project focuses on enhancing the GNOME Crosswords Editor by adding scoring and metadata to the wordlists it uses for generating puzzles.

Currently, the wordlists are just collections of words without any information about how complex, common, or interesting those words are. This project aims to change that by analyzing each word and assigning scores based on various linguistic traits.

## ✨ What Does This Scoring Do?

The goal is to generate more interesting, balanced, and customizable puzzles by scoring words based on features like:

- **Word length**
- **Unique character count**
- **Vowel richness**
- **(Optional) Word frequency or difficulty**

These scores can help the editor filter or prioritize words when building crossword grids.

## 🧪 Current Progress

- ✅ Built a basic Python script that scores words based on multiple traits
- ✅ Generated a sample scored wordlist (`scored_wordlist.csv`)
- ✅ Wordlist stored in text and CSV formats for easy parsing
- 🔜 Plan to integrate with GNOME Crosswords' binary wordlist format

## 🧰 Tech Stack

- Python 3
- NLTK (for linguistic processing)
- CSV and plain-text handling
- Git/GitHub for version control

## 📁 Files

- `wordlist.txt` — raw wordlist
- `wordlist_scoring.py` — script to analyze and score the words
- `scored_wordlist.csv` — output file with word scores

## 💡 Next Steps

- Add more linguistic features (e.g. syllable count, word frequency)
- Normalize scores across languages and datasets
- Integrate with GNOME Crosswords Editor wordlist format
- Optimize for larger datasets (~20 GB scale)

## 👋 About Me

Hi! I'm Safa, and enthusiastic undergrad. I am passionate about neuroscience, open-source, and Python development.  
This project is part of my learning journey and GSoC application under MNE-Python.

**GitHub**: [@Shaptain](https://github.com/Shaptain)

This is a learning project — feedback and suggestions are always welcome!
