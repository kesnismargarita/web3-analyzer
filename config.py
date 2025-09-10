python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    XAI_API_KEY = os.getenv('XAI_API_KEY')
    INFURA_URL = os.getenv('INFURA_URL', 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID')
    DEFAULT_ANALYSIS_DEPTH = 'basic'
    MAX_TOKENS_TO_ANALYZE = 10
    
    # Налаштування для різних мереж
    NETWORKS = {
        'ethereum': {
            'rpc_url': INFURA_URL,
            'chain_id': 1
        },
        'polygon': {
            'rpc_url': 'https://polygon-rpc.com',
            'chain_id': 137
        }
    }
