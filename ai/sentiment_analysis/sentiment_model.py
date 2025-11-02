"""
Module d'analyse de sentiment pour SmartBooker
Analyse les avis clients pour évaluer la fiabilité des services
"""

from textblob import TextBlob
import re

class SentimentAnalyzer:
    def __init__(self):
        self.model = None
        
    def analyze_text(self, text):
        """
        Analyse le sentiment d'un texte (avis client)
        
        Args:
            text: Texte à analyser
            
        Returns:
            Dictionnaire avec le sentiment (positif/négatif/neutre) et le score
        """
        # Nettoyer le texte
        cleaned_text = self._clean_text(text)
        
        # Analyser avec TextBlob
        blob = TextBlob(cleaned_text)
        polarity = blob.sentiment.polarity
        
        # Déterminer le sentiment
        if polarity > 0.1:
            sentiment = "positif"
        elif polarity < -0.1:
            sentiment = "négatif"
        else:
            sentiment = "neutre"
            
        return {
            "sentiment": sentiment,
            "score": polarity,
            "subjectivity": blob.sentiment.subjectivity
        }
    
    def _clean_text(self, text):
        """Nettoie le texte avant l'analyse"""
        # Supprimer les caractères spéciaux et les espaces multiples
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def analyze_batch(self, reviews):
        """
        Analyse plusieurs avis en une fois
        
        Args:
            reviews: Liste d'avis à analyser
            
        Returns:
            Liste des résultats d'analyse
        """
        return [self.analyze_text(review) for review in reviews]

