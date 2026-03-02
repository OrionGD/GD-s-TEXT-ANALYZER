import re

class TextAnalyzer:
    def __init__(self):
        # Define stopwords (common words to ignore)
        self.stopwords = {'a', 'an', 'the', 'and', 'or', 'but', 'if', 'then', 'else', 
                          'when', 'up', 'so', 'too', 'very', 'just', 'with', 'for', 
                          'at', 'of', 'on', 'in', 'to', 'from', 'by', 'about', 'as'}
        
        # Define positive words for sentiment analysis
        self.positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful', 
                               'fantastic', 'nice', 'love', 'like', 'best', 'happy', 
                               'positive', 'awesome', 'brilliant', 'superb'}
        
        # Define negative words for sentiment analysis
        self.negative_words = {'bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike', 
                               'poor', 'worst', 'negative', 'sad', 'angry', 'annoying', 
                               'stupid', 'boring', 'dull'}

    def clean_text(self, text):
        # Remove special characters and numbers
        text = re.sub(r'\W+', ' ', text)   # Replace non-word characters with space
        text = re.sub(r'\d+', '', text)    # Remove digits
        return text.lower()

    def extract_data(self, text):
        # Extract sentences and words, removing stopwords
        sentences = [s.strip() for s in text.split('.') if s.strip()]  # Split and remove empty
        words = re.findall(r'\b\w+\b', text)
        words = [word for word in words if word not in self.stopwords]
        return sentences, words

    def sentiment_analysis(self, text):
        # Perform sentiment analysis using a simple approach
        words = text.split()
        if len(words) == 0:
            return 0.0, 0.0
        positive_count = sum(1 for word in words if word in self.positive_words)
        negative_count = sum(1 for word in words if word in self.negative_words)
        polarity = (positive_count - negative_count) / len(words)
        subjectivity = (positive_count + negative_count) / len(words)
        return polarity, subjectivity

    def keyword_identification(self, text, num_keywords=10):
        # Simple keyword identification based on word frequency
        words = re.findall(r'\b\w+\b', text)
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        keywords = [word for word, freq in sorted_words[:num_keywords]]
        return keywords

    def analyze_text(self, text):
        cleaned_text = self.clean_text(text)
        sentences, words = self.extract_data(cleaned_text)
        polarity, subjectivity = self.sentiment_analysis(cleaned_text)
        keywords = self.keyword_identification(cleaned_text)
        return {
            "sentences": sentences,
            "words": words,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "keywords": keywords
        }

def main():
    print('----- TEXT ANALYZER -----')
    text_analyzer = TextAnalyzer()
    user_input = input("Enter the text to analyze: ")
    analysis_result = text_analyzer.analyze_text(user_input)
    
    print("\nExtracted Sentences:")
    for i, sentence in enumerate(analysis_result['sentences'], 1):
        print(f"{i}. {sentence}")
    
    print("\nExtracted Words (without stopwords):")
    print(analysis_result['words'])
    
    print("\nSentiment Analysis:")
    print(f"Polarity: {analysis_result['polarity']:.3f}")
    print(f"Subjectivity: {analysis_result['subjectivity']:.3f}")
    
    print("\nIdentified Keywords:")
    print(analysis_result['keywords'])

if __name__ == "__main__":
    main()
