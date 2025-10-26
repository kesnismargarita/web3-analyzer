python
"""
Генератор звітів для аналізу Web3 проектів
"""

import json
import csv
from datetime import datetime
from typing import Dict, Any

class ReportGenerator:
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
    
    def save_report(self, analysis_data: Dict[str, Any], filename: str):
        """Збереження звіту в JSON форматі"""
        report = {
            'generated_at': self.timestamp,
            'version': '1.0.0',
            'analysis': analysis_data
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
    
    def generate_csv_report(self, analysis_data: Dict[str, Any], filename: str):
        """Генерація CSV звіту"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Parameter', 'Value'])
            
            # Базова інформація
            basic_info = analysis_data.get('basic_info', {})
            for key, value in basic_info.items():
                writer.writerow([key, value])
    
    def generate_html_report(self, analysis_data: Dict[str, Any], filename: str):
        """Генерація HTML звіту"""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Web3 Analysis Report</title>
            <style>
                body {
                      font-family: 'Segoe UI', Arial, sans-serif;
                      margin: 20px;
                      background-color: #f5f5f5;
                }
                .header {
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        color: white;
                        padding: 20px;
                        border-radius: 8px;
                        margin-bottom: 20px;
                        }
                .section {
                        margin: 20px 0;
                        background: white;
                        padding: 15px;
                        border-radius: 8px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .data {
                    background-color: #f8f9fa;
                    padding: 15px;
                    border-radius: 4px;
                    border-left: 4px solid #667eea;
                }

            </style>
        </head>
        <body>
            <div class="header">
                <h1>Web3 Project Analysis Report</h1>
                <p>Generated: {self.timestamp}</p>
            </div>
            
            <div class="section">
                <h2>Token Information</h2>
                <div class="data">
                    <pre>{json.dumps(analysis_data, indent=2)}</pre>
                </div>
            </div>
        </body>
        </html>
        """
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
