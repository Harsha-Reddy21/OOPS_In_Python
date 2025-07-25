from collections import Counter
import re 


class TextAnalyzer:
    def __init__(self,text):
        self.original_text = text 
        self.text=text.lower()

    def get_character_frequency(self,include_spaces=False):
        if include_spaces:
            return Counter(self.text)
        return Counter(self.text.replace(" ",""))
    
    def get_word_frequency(self):
        words = re.findall(r'\b\w+\b',self.text)
        return Counter(words)

    def get_sentence_length_distribution(self):
        sentences = re.split(r'[.!?]',self.text)
        sentence_lengths = [len(sentence.split()) for sentence in sentences if sentence.strip()]
        return Counter(sentence_lengths)

    def find_common_words(self,n=10,exclude_common_word=True):
        common_words = self.get_word_frequency().most_common(n)
        if exclude_common_word:
            common_words = [word for word,count in common_words if word not in self.get_common_words()]
        return common_words

    def get_reading_statistics(self):
        words = self.get_word_frequency()
        total_words = sum(words.values())
        average_word_length = sum(len(word) for word in words.keys())/total_words
        return {
            "total_words":total_words,
            "average_word_length":average_word_length
        }

    def compare_with_text(self,other_text):
        return Counter(self.text) - Counter(other_text)



sample_text = """

Python is a versatile programming language that is widely used for web development, 
data analysis, artificial intelligence, and scientific computing.
It is known for its simple syntax and readability, making it an excellent choice for beginners.



"""

analyzer = TextAnalyzer(sample_text)
print("Character frequency:",analyzer.get_character_frequency())
print("Word frequency:",analyzer.get_word_frequency())
print("Common words:",analyzer.find_common_words())
print("Reading statistics:",analyzer.get_reading_statistics())


other_text = """
Java is a popular programming language that is widely used for web development, 
data analysis, artificial intelligence, and scientific computing.
"""

comparison=analyzer.compare_with_text(other_text)
print("Comparison with other text:",comparison)




