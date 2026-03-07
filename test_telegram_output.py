from src.analyzer import AnalysisResult
from src.notification import NotificationService


def make_result(
    code: str,
    name: str,
    sentiment_score: int,
    operation_advice: str,
    dashboard: dict | None = None,
    analysis_summary: str = "",
    risk_warning: str = "",
) -> AnalysisResult:
    return AnalysisResult(
        code=code,
        name=name,
        sentiment_score=sentiment_score,
        trend_prediction="震荡",
        operation_advice=operation_advice,
        analysis_summary=analysis_summary,
        risk_warning=risk_warning,
        dashboard=dashboard or {},
    )


def test_risk_line_filters_placeholder_dates_into_background():
    notifier = NotificationService()
    result = make_result(
        code="AAPL",
        name="Apple",
        sentiment_score=50,
        operation_advice="观望",
        dashboard={
            "intelligence": {
                "risk_alerts": [
                    "中｜无具体日期｜年度报告中提及的潜在业务风险",
                    "低｜通用｜科技股普遍面临的监管风险",
                ]
            }
        },
        risk_warning="结构化结果不完整，新闻与技术面需二次确认。",
    )

    risk_line = notifier._format_risk_line(result)

    assert "无具体日期" not in risk_line
    assert "通用" not in risk_line
    assert "背景｜年度报告中提及的潜在业务风险" in risk_line
    assert "近7日未见新增硬风险" in risk_line


def test_execution_line_rejects_implausible_stop_loss():
    notifier = NotificationService()
    result = make_result(
        code="SPY",
        name="SPDR S&P 500 ETF Trust",
        sentiment_score=48,
        operation_advice="观望",
        dashboard={
            "data_perspective": {
                "price_position": {
                    "current_price": 682.2,
                    "ma5": 683.0,
                    "ma10": 684.1,
                    "ma20": 680.4,
                }
            },
            "battle_plan": {
                "sniper_points": {
                    "ideal_buy": "678",
                    "stop_loss": "20",
                    "take_profit": "692",
                }
            },
        },
    )

    execution_line = notifier._format_execution_line(result)

    assert "**进场 $678**" in execution_line
    assert "**止损 待确认**" in execution_line
    assert "**目标 $692**" in execution_line


def test_telegram_overview_groups_mag7_and_market_watch():
    notifier = NotificationService()
    nvda = make_result(
        code="NVDA",
        name="NVIDIA",
        sentiment_score=74,
        operation_advice="买入",
        dashboard={"macro_signal": {"sector_resonance": "AI/半导体共振偏强"}},
    )
    spy = make_result(
        code="SPY",
        name="SPDR S&P 500 ETF Trust",
        sentiment_score=48,
        operation_advice="观望",
        dashboard={"macro_signal": {"sector_resonance": "大盘风险偏好回落"}},
    )

    overview = notifier.generate_telegram_overview([spy, nvda], report_date="2026-03-08")

    assert "Mag7总结" in overview
    assert "大盘观察" in overview
    assert "Mag7：" in overview
    assert "1. 🟢 NVDA NVIDIA | 偏多" in overview
    assert "大盘观察：" in overview
    assert "2. ⚪ SPY SPDR S&P 500 ETF Trust | 观望" in overview


def test_market_watch_stock_block_has_group_prefix():
    notifier = NotificationService()
    result = make_result(
        code="SPY",
        name="SPDR S&P 500 ETF Trust",
        sentiment_score=48,
        operation_advice="观望",
        dashboard={
            "core_conclusion": {
                "one_sentence": "指数震荡偏弱，先等企稳",
                "position_advice": {
                    "no_position": "等回到支撑再看",
                    "has_position": "跌破支撑先降风险",
                },
            }
        },
        analysis_summary="指数短线承压，先观察支撑位。",
    )

    block = notifier.generate_telegram_single_stock_report(result)

    assert "## ⚪ 市场观察 | SPDR S&P 500 ETF Trust (SPY)" in block
