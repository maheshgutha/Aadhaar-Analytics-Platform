from analysis_engine.national_analyzer import analyze_india
from analysis_engine.state_analyzer import analyze_state
from analysis_engine.insight_generator import generate_insights
from analysis_engine.visualization_engine import india_summary_plots

def run_national_analysis(df):
    report = analyze_india(df)
    insights = generate_insights({
        "service_stress_index": report["national_service_stress"],
        "anomalies_detected": report["total_anomalies"],
        "avg_enrolment_growth": report["avg_enrolment_growth"]
    })

    images = india_summary_plots(df)

    return {
        "report": report,
        "insights": insights,
        "visualizations": images
    }

def run_state_analysis(df, state):
    report = analyze_state(df, state)
    insights = generate_insights(report)
    return {"report": report, "insights": insights}
