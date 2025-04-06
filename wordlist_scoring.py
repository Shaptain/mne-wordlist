import nltk
import string
try:
    from nltk.corpus import words
    nltk.data.find("corpora/words")
except:
    nltk.download("words")
    from nltk.corpus import words

english_words = set(words.words())

def char_count(word):
    return sum(1 for i in word if i.isalpha())

def unique_count(word):
    return len(set(word))

def vowel_count(word):
    vowels = set("aeiou")
    return len(set(word) & vowels)

def has_rare_letters(word):
    rare = set("qzx")
    return any(char in rare for char in word)

def is_english(word):
    return word.lower() in english_words

def calculate_score(word):
    score = 0
    score += char_count(word)
    score += unique_count(word)
    
    if vowel_count(word) == 5:
        score += 2
    
    if has_rare_letters(word):
        score -= 2
    
    if is_english(word):
        score += 1
    
    return score

def main():
    with open("wordlist.txt", "r") as f:
        words = [line.strip().lower() for line in f if line.strip()]

    with open("scored_wordlist.csv", "w") as f_out:
        f_out.write("word,score\n")
        for word in words:
            word_score = calculate_score(word)
            f_out.write(f"{word},{word_score}\n")

if __name__ == "__main__":
    main()
