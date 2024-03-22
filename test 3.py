def max_words_in_sentence(sentences):
    max_words = 0
    
    for sentence in sentences:
        words = sentence.split() 
        word_count = len(words) 
        max_words = max(max_words, word_count) 
    
    return max_words
sentences = ["alice and bob love leetcode", "i think so too"]

max_words = max_words_in_sentence(sentences)
print(f"The maximum number of words in a single sentence is: {max_words}")
