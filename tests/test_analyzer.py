python
"""
Тести для Web3 аналізатора
"""

import pytest
from src.web3_analyzer import Web3Analyzer
from src.ai_integration import AIAnalyzer

def test_web3_analyzer_initialization():
    """Тест ініціалізації аналізатора"""
    analyzer = Web3Analyzer('ethereum')
    assert analyzer.network == 'ethereum'

def test_invalid_network():
    """Тест з неіснуючою мережею"""
    with pytest.raises(ValueError):
        Web3Analyzer('invalid_network')

def test_token_analysis_structure():
    """Тест структури результату аналізу"""
    analyzer = Web3Analyzer('ethereum')
    # Використовуємо валідну адресу для тесту
    result = analyzer.analyze_token('0x1234567890123456789012345678901234567890')
    
    assert 'token_address' in result
    assert 'network' in result
    assert 'basic_info' in result
