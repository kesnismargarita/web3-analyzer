# Використання Web3 Analyzer

## Базове використання

### Аналіз токену

```bash
python main.py --token 0x1234567890123456789012345678901234567890 --network ethereum
```

### Аналіз з AI інсайтами

```bash
python main.py --token 0x1234567890123456789012345678901234567890 --ai-analysis
```

## Приклади використання

### 1. Аналіз популярного токену
```bash
python main.py --token 0xA0b86a33E6417c92D27f1e7fe66a86c53bc5b3c4 --output usdc_analysis.json
```

### 2. Аналіз з збереженням у HTML
```python
from src.web3_analyzer import Web3Analyzer
from src.report_generator import ReportGenerator

analyzer = Web3Analyzer('ethereum')
result = analyzer.analyze_token('0x...')

report_gen = ReportGenerator()
report_gen.generate_html_report(result, 'report.html')
```

## Конфігурація

Налаштуйте параметри в файлі `config.py`:

- `XAI_API_KEY` - ключ для xAI API
- `INFURA_URL` - URL для підключення до Ethereum
- `DEFAULT_ANALYSIS_DEPTH` - глибина аналізу за замовчуванням
```

### .env (приклад)
```
XAI_API_KEY=your_xai_api_key_here
INFURA_URL=https://mainnet.infura.io/v3/your_project_id
```

### .gitignore
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
env/
ENV/

# Environment variables
.env
.env.local
.env.production

# IDE
.vscode/
.idea/
*.swp
*.swo

# Reports
*.json
*.html
*.csv

# OS
.DS_Store
Thumbs.db
```
