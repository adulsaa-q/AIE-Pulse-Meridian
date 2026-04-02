from plugins.google_trends import collect as collect_trends
from plugins.news_rss import collect as collect_rss
from pipeline.normalizer import save, export_sample_csv
from pipeline.signal_detector import detect_signals
from engine.insight_ai import analyze
from engine.strategy import apply
from output.report_builder import build

def main():
    "รันทุก layer ตามลำดับ ตั้งแต่ดึงข้อมูลจนถึงสร้าง report"
    print(" step 1 collecting data...")
    records = collect_trends() + collect_rss()
    print(" Step 2: Saving to database...")
    save(records)
    print("🔍 Step 3: Detecting signals...")
    signals = detect_signals()
    if not signals:
        print("No signals detected today.")
        return

    print(f"Found {len(signals)} signals")

    print("Step 4: Analyzing with AI...")
    insights = analyze(signals)

    print("Step 5: Applying strategy...")
    result = apply(insights)

    print("Step 6: Building report...")
    filename = build(result)
    export_sample_csv()

    print(f"✅ Done! Report saved: {filename}")

if __name__ == "__main__":
    main()