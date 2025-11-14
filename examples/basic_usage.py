#!/usr/bin/env python3
"""
Приклади базового використання Web3 Analyzer
"""

import sys
import os

# Додаємо батьківську директорію в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.web3_analyzer import Web3Analyzer
from src.ai_integration import AIAnalyzer
from src.report_generator import ReportGenerator

def example_basic_analysis():
    """Приклад базового аналізу токену"""
    print("🔍 Приклад базового аналізу токену")

    # Ініціалізація аналізатора
    analyzer = Web3Analyzer('ethereum')

    # Аналіз токену (використовуємо тестову адресу)
    token_address = '0x1234567890123456789012345678901234567890'
    result = analyzer.analyze_token(token_address)

    print(f"✅ Аналіз завершено для токену: {result['token_address']}")
    print(f"📊 Мережа: {result['network']}")

    return result

def example_ai_analysis():
    """Приклад AI аналізу"""
    print("\n🤖 Приклад AI аналізу")

    # Отримуємо базовий аналіз
    basic_result = example_basic_analysis()

    # AI аналіз
    ai_analyzer = AIAnalyzer()
    try:
        ai_insights = ai_analyzer.generate_insights(basic_result)
        print(f"🎯 Оцінка ризику: {ai_insights.get('risk_score', 'unknown')}")
        print(f"💡 Кількість рекомендацій: {len(ai_insights.get('recommendations', []))}")
    except Exception as e:
        print(f"⚠️ Помилка AI аналізу: {e}")

def example_report_generation():
    """Приклад генерації звітів"""
    print("\n📊 Приклад генерації звітів")

    # Отримуємо результат аналізу
    result = example_basic_analysis()

    # Генеруємо звіти
    report_gen = ReportGenerator()

    # JSON звіт
    report_gen.save_report(result, 'example_report.json')
    print("✅ JSON звіт збережено: example_report.json")

    # CSV звіт
    report_gen.generate_csv_report(result, 'example_report.csv')
    print("✅ CSV звіт збережено: example_report.csv")

    # HTML звіт
    report_gen.generate_html_report(result, 'example_report.html')
    print("✅ HTML звіт збережено: example_report.html")

if __name__ == "__main__":
    print("🚀 Запуск прикладів Web3 Analyzer\n")

    # Запускаємо приклади
    example_basic_analysis()
    example_ai_analysis()
    example_report_generation()

    print("\n✨ Усі приклади виконано!")
