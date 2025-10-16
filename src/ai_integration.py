python
"""
Інтеграція з xAI API для аналізу проектів
"""

import openai
from typing import Dict, Any, List
from config import Config

class AIAnalyzer:
    def __init__(self):
        if not Config.XAI_API_KEY:
            raise ValueError("XAI API ключ не знайдено в конфігурації")
        
        # Налаштування для xAI (використовуємо OpenAI сумісний інтерфейс)
        self.client = openai.OpenAI(
            api_key=Config.XAI_API_KEY,
            base_url="https://api.x.ai/v1"
        )
    
    def generate_insights(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """Генерація AI інсайтів на основі аналізу"""
        
        prompt = self._create_analysis_prompt(analysis_data)
        
        try:
            response = self.client.chat.completions.create(
                model="grok-2-1212",
                messages=[
                    {"role": "system", "content": "Ти експерт з Web3 та DeFi аналізу. Надай детальний аналіз токену."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.3
            )
            
            ai_analysis = response.choices[0].message.content
            
            return {
                'summary': ai_analysis,
                'risk_score': self._calculate_risk_score(analysis_data),
                'recommendations': self._generate_recommendations(analysis_data)
            }
            
        except Exception as e:
            return {
                'error': f"Помилка AI аналізу: {str(e)}",
                'risk_score': 'unknown',
                'recommendations': []
            }
    
    def _create_analysis_prompt(self, data: Dict[str, Any]) -> str:
        """Створення промпту для AI аналізу"""
        return f"""
        Проаналізуй наступний Web3 токен:
        
        Адреса: {data.get('token_address', 'N/A')}
        Мережа: {data.get('network', 'N/A')}
        
        Базова інформація:
        - Назва: {data.get('basic_info', {}).get('name', 'N/A')}
        - Символ: {data.get('basic_info', {}).get('symbol', 'N/A')}
        - Загальна емісія: {data.get('basic_info', {}).get('total_supply', 'N/A')}
        
        Холдери:
        - Загальна кількість: {data.get('holders_info', {}).get('total_holders', 'N/A')}
        - Концентрація топ-10: {data.get('holders_info', {}).get('top_10_concentration', 'N/A')}%
        
        Транзакції (24г):
        - Обсяг: {data.get('transaction_analysis', {}).get('daily_volume', 'N/A')}
        - Кількість транзакцій: {data.get('transaction_analysis', {}).get('transaction_count_24h', 'N/A')}
        
        Надай оцінку ризиків та рекомендації для інвестування.
        """
    
    def _calculate_risk_score(self, data: Dict[str, Any]) -> str:
        """Розрахунок оцінки ризику"""
        # Спрощена логіка оцінки ризику
        concentration = data.get('holders_info', {}).get('top_10_concentration', 0)
        
        if concentration > 70:
            return 'high'
        elif concentration > 40:
            return 'medium'
        else:
            return 'low'
    
    def _generate_recommendations(self, data: Dict[str, Any]) -> List[str]:
        """Генерація рекомендацій"""
        recommendations = []
        
        concentration = data.get('holders_info', {}).get('top_10_concentration', 0)
        if concentration > 50:
            recommendations.append("Висока концентрація холдингів може означати ризик маніпуляцій")
        
        volume = int(data.get('transaction_analysis', {}).get('daily_volume', '0'))
        if volume < 1000000:
            recommendations.append("Низький обсяг торгівлі може означати низьку ліквідність")
        
        return recommendations
