"""
Тести для Web3 аналізатора
"""

import pytest
from unittest.mock import patch, MagicMock

from src.web3_analyzer import Web3Analyzer
from src.ai_integration import AIAnalyzer
from src.report_generator import ReportGenerator


class TestWeb3Analyzer:
    """Тести для класу Web3Analyzer"""

    def test_initialization_with_valid_network(self):
        """Тест ініціалізації з валідною мережею"""
        analyzer = Web3Analyzer('ethereum')
        assert analyzer.network == 'ethereum'
        assert analyzer.config is not None

    def test_initialization_with_invalid_network(self):
        """Тест ініціалізації з неіснуючою мережею"""
        with pytest.raises(ValueError) as exc_info:
            Web3Analyzer('invalid_network')
        assert 'Непідтримувана мережа' in str(exc_info.value)

    @patch('src.web3_analyzer.Web3')
    def test_token_analysis_structure(self, mock_web3):
        """Тест структури результату аналізу токену"""
        # Налаштування mock
        mock_web3.is_address.return_value = True
        mock_web3.to_checksum_address.return_value = '0x1234567890123456789012345678901234567890'

        analyzer = Web3Analyzer('ethereum')
        result = analyzer.analyze_token('0x1234567890123456789012345678901234567890')

        # Перевірка структури
        required_keys = ['token_address', 'network', 'basic_info', 'holders_info', 'transaction_analysis']
        for key in required_keys:
            assert key in result

        assert result['network'] == 'ethereum'

    def test_get_supported_networks(self):
        """Тест отримання списку підтримуваних мереж"""
        networks = Web3Analyzer.get_supported_networks()
        assert isinstance(networks, list)
        assert 'ethereum' in networks


class TestAIAnalyzer:
    """Тести для класу AIAnalyzer"""

    @patch('src.ai_integration.openai.OpenAI')
    def test_ai_analyzer_initialization(self, mock_openai):
        """Тест ініціалізації AI аналізатора"""
        with patch('src.ai_integration.Config.XAI_API_KEY', 'test_key'):
            analyzer = AIAnalyzer()
            assert analyzer.client is not None

    def test_risk_score_calculation(self):
        """Тест розрахунку оцінки ризику"""
        analyzer = AIAnalyzer()

        # Тест високого ризику
        high_risk_data = {'holders_info': {'top_10_concentration': 80}}
        assert analyzer._calculate_risk_score(high_risk_data) == 'high'

        # Тест середнього ризику
        medium_risk_data = {'holders_info': {'top_10_concentration': 50}}
        assert analyzer._calculate_risk_score(medium_risk_data) == 'medium'

        # Тест низького ризику
        low_risk_data = {'holders_info': {'top_10_concentration': 20}}
        assert analyzer._calculate_risk_score(low_risk_data) == 'low'


class TestReportGenerator:
    """Тести для класу ReportGenerator"""

    def test_report_generator_initialization(self):
        """Тест ініціалізації генератора звітів"""
        generator = ReportGenerator()
        assert generator.timestamp is not None
        assert isinstance(generator.timestamp, str)

    @patch('builtins.open', create=True)
    def test_save_report(self, mock_open):
        """Тест збереження JSON звіту"""
        generator = ReportGenerator()
        test_data = {'test': 'data'}

        generator.save_report(test_data, 'test.json')
        mock_open.assert_called_once_with('test.json', 'w', encoding='utf-8')


# Фікстури для тестів
@pytest.fixture
def sample_analysis_data():
    """Зразкові дані для тестування"""
    return {
        'token_address': '0x1234567890123456789012345678901234567890',
        'network': 'ethereum',
        'basic_info': {
            'name': 'Test Token',
            'symbol': 'TEST',
            'decimals': 18
        },
        'holders_info': {
            'total_holders': 1000,
            'top_10_concentration': 30
        },
        'transaction_analysis': {
            'daily_volume': '1000000',
            'transaction_count_24h': 100
        }
    }


@pytest.fixture
def ai_analyzer():
    """Фікстура для AI аналізатора"""
    with patch('src.ai_integration.Config.XAI_API_KEY', 'test_key'):
        return AIAnalyzer()


if __name__ == '__main__':
    pytest.main(['-v'])
