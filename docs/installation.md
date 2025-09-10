# Інсталяція Web3 Analyzer

## Системні вимоги

- Python 3.8 або новіший
- pip (менеджер пакетів Python)

## Кроки інсталяції

1. Клонуйте репозиторій:
```bash
git clone https://github.com/your-username/web3-analyzer.git
cd web3-analyzer
```

2. Створіть віртуальне середовище:
```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
```

3. Встановіть залежності:
```bash
pip install -r requirements.txt
```

4. Створіть файл .env та додайте ваші API ключі:
```
XAI_API_KEY=your_xai_api_key_here
INFURA_URL=https://mainnet.infura.io/v3/your_project_id
```

## Перевірка інсталяції

Запустіть тести:
```bash
python -m pytest tests/
```
