python
"""
Модуль для отримання даних з різних джерел
"""

import requests
import time
from typing import Dict, Any, List

class DataFetcher:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Web3-Analyzer/1.0'
        })
    
    def fetch_token_info(self, token_address: str, network: str = 'ethereum') -> Dict[str, Any]:
        """Отримання інформації про токен з публічних API"""
        # Тут має бути реальна логіка отримання даних
        # Поки що заглушка
        return {
            'price_usd': 1.25,
            'market_cap': 125000000,
            'volume_24h': 2500000,
            'price_change_24h': 5.2
        }
    
    def fetch_defi_data(self, protocol_address: str) -> Dict[str, Any]:
        """Отримання DeFi даних"""
        return {
            'tvl': 50000000,
            'apy': 12.5,
            'protocol_name': 'Sample DeFi'
        }
    
    def rate_limit_request(self, url: str, params: Dict = None) -> Dict[str, Any]:
        """Запит з обмеженням частоти"""
        time.sleep(0.1)  # Простий rate limiting
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {'error': 'Timeout error - server did not respond in time'}
        except requests.exceptions.ConnectionError:
            return {'error': 'Connection error - unable to reach server'}
        except requests.exceptions.HTTPError as e:
            return {'error': f'HTTP error {e.response.status_code}: {e.response.reason}'}
        except requests.exceptions.RequestException as e:
            return {'error': f'Request error: {str(e)}'}
