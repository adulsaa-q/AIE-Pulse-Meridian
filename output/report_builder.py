import os
import config
from datetime import datetime

def build(insights: list[dict] )-> str:
    "รับ insights เพื่อสร้าง HTML report บันทึกลงไฟล์"
    os.makedirs(config.REPORT_OUTPUT_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{config.REPORT_OUTPUT_DIR}{config.USE_CASE}_{today}.html"

    rows = ""
    for insight in insights:
        signal = insight.get("signal_type", "")
        rows += f"""
        <div class="card">
            <h2>{insight['entity']}</h2>
            <span class="badge {signal}">{signal}</span>
            <div class="pct">{insight.get('pct_change', 'N/A')}%</div>
            <pre>{insight['insight']}</pre>
            <div class="rec">{insight.get('recommendation', '')}</div>
        </div>
        """
    html = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>AIE Report — {today}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 860px;
            margin: 48px auto;
            padding: 0 24px;
            background: #f5f5f5;
            color: #1a1a1a;
            line-height: 1.6;
        }}
        h1 {{
            font-size: 26px;
            color: #1a1a2e;
            border-bottom: 3px solid #e94560;
            padding-bottom: 12px;
            margin-bottom: 8px;
        }}
        .meta {{
            color: #666;
            font-size: 14px;
            margin-bottom: 32px;
        }}
        .card {{
            background: white;
            border-radius: 10px;
            padding: 28px 32px;
            margin-bottom: 24px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        }}
        .card h2 {{
            font-size: 18px;
            color: #1a1a2e;
            margin: 0 0 4px 0;
        }}
        .badge {{
            display: inline-block;
            font-size: 11px;
            font-weight: 600;
            padding: 3px 10px;
            border-radius: 20px;
            margin-bottom: 16px;
            letter-spacing: 0.5px;
        }}
        .ACCELERATION {{ background: #d4edda; color: #155724; }}
        .DECLINE       {{ background: #f8d7da; color: #721c24; }}
        .ANOMALY       {{ background: #fff3cd; color: #856404; }}
        .pct {{
            font-size: 22px;
            font-weight: 700;
            color: #e94560;
            margin-bottom: 16px;
        }}
        pre {{
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 6px;
            padding: 16px 20px;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 14px;
            line-height: 1.7;
            white-space: pre-wrap;
            color: #333;
            margin-bottom: 16px;
        }}
        .rec {{
            background: #e8f4fd;
            border-left: 3px solid #2196F3;
            padding: 12px 16px;
            border-radius: 0 6px 6px 0;
            font-size: 14px;
            color: #0d47a1;
        }}
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>AIE Daily Intelligence Report</h1>
        <p>📅 {today} &nbsp;|&nbsp; 🎯 {config.USE_CASE} &nbsp;|&nbsp; ⚙️ {config.STRATEGY_MODE}</p>
    </div>
    {rows}
</div>
</body>
</html>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    return filename
