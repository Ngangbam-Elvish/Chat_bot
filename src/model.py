import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess import preprocess_text

class FAQChatbot:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = pd.read_csv(dataset_path)
        
        if 'question' not in self.df.columns or 'answer' not in self.df.columns:
            raise ValueError("Dataset must contain 'question' and 'answer' columns.")
        
        self.df['processed_question'] = self.df['question'].apply(preprocess_text)
        
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.df['processed_question'])
        
    def get_response(self, user_query):
        processed_query = preprocess_text(user_query)
        if not processed_query.strip():
            return "I couldn't understand that. Could you rephrase your question?"
            
        query_vector = self.vectorizer.transform([processed_query])
        similarities = cosine_similarity(query_vector, self.question_vectors)[0]
        
        best_match_idx = similarities.argmax()
        best_score = similarities[best_match_idx]
        
        if best_score < 0.2:
            return "I'm not sure I understand. Could you rephrase your question or ask something else?"
            
        return self.df.iloc[best_match_idx]['answer']