python
#!/usr/bin/env python3
"""
Web3 Project Analyzer
Головний модуль для запуску аналізу Web3 проектів
"""

import argparse
import sys
from src.web3_analyzer import Web3Analyzer
from src.report_generator import ReportGenerator
from config import Config

import logging

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('analyzer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Аналіз Web3 проектів з AI інтеграцією')
    parser.add_argument('--token', type=str, help='Адреса токену для аналізу')
    parser.add_argument('--network', type=str, default='ethereum', help='Мережа блокчейну')
    parser.add_argument('--output', type=str, default='report.json', help='Файл для збереження звіту')
    parser.add_argument('--ai-analysis', action='store_true', help='Включити AI аналіз')
    
    args = parser.parse_args()
    
    if not args.token:
        print("Помилка: Необхідно вказати адресу токену")
        sys.exit(1)
    
    try:
        # Ініціалізація аналізатора
        analyzer = Web3Analyzer(args.network)
        
        # Базовий аналіз
        logger.info(f"Початок аналізу токену {args.token} в мережі {args.network}")

        analysis_result = analyzer.analyze_token(args.token)
        
        # AI аналіз якщо потрібно
        if args.ai_analysis:
            print("Запускаю AI аналіз...")
            from src.ai_integration import AIAnalyzer
            ai_analyzer = AIAnalyzer()
            ai_insights = ai_analyzer.generate_insights(analysis_result)
            analysis_result['ai_insights'] = ai_insights
        
        # Генерація звіту
        report_gen = ReportGenerator()
        report_gen.save_report(analysis_result, args.output)
        
        print(f"Аналіз завершено! Звіт збережено в {args.output}")
        
    except Exception as e:
        print(f"Помилка під час аналізу: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### src/__init__.py
```python
"""
Web3 Analyzer Package
"""

__version__ = "1.0.0"
__author__ = "Web3 Analytics Team"
