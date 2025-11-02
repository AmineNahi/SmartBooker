"""
Module de comparaison de prix pour SmartBooker
Compare les prix entre différents prestataires pour trouver la meilleure offre
"""

class PriceComparator:
    def __init__(self):
        pass
    
    def compare_prices(self, services):
        """
        Compare les prix de plusieurs services similaires
        
        Args:
            services: Liste de dictionnaires contenant les informations des services
                    Format: [{"id": ..., "name": ..., "price": ..., "provider": ...}, ...]
                    
        Returns:
            Liste triée par prix croissant avec les meilleures offres en premier
        """
        if not services:
            return []
        
        # Trier par prix
        sorted_services = sorted(services, key=lambda x: x.get('price', float('inf')))
        
        # Calculer les économies potentielles
        if len(sorted_services) > 1:
            cheapest = sorted_services[0]['price']
            for service in sorted_services[1:]:
                service['savings'] = service['price'] - cheapest
                service['savings_percentage'] = ((service['price'] - cheapest) / service['price']) * 100
        
        return sorted_services
    
    def find_best_deal(self, services):
        """
        Trouve la meilleure offre parmi une liste de services
        
        Args:
            services: Liste de services à comparer
            
        Returns:
            Le service avec le meilleur rapport qualité-prix
        """
        compared = self.compare_prices(services)
        return compared[0] if compared else None
    
    def get_price_trend(self, historical_prices):
        """
        Analyse la tendance des prix sur une période
        
        Args:
            historical_prices: Liste de prix historiques avec dates
            
        Returns:
            Dictionnaire avec la tendance (hausse/baisse/stable) et le pourcentage
        """
        if len(historical_prices) < 2:
            return {"trend": "stable", "percentage": 0}
        
        first_price = historical_prices[0]['price']
        last_price = historical_prices[-1]['price']
        
        percentage_change = ((last_price - first_price) / first_price) * 100
        
        if percentage_change > 5:
            trend = "hausse"
        elif percentage_change < -5:
            trend = "baisse"
        else:
            trend = "stable"
        
        return {
            "trend": trend,
            "percentage": round(percentage_change, 2)
        }

