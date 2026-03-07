from src.config import Config


def test_combined_watchlist_keeps_order_and_deduplicates():
    config = Config(
        stock_list=["NVDA", "AAPL", "SPY"],
        market_watchlist=["SPY", "QQQ", "DIA"],
    )

    assert config.get_combined_watchlist() == ["NVDA", "AAPL", "SPY", "QQQ", "DIA"]


def test_is_us_focused_runtime_returns_true_for_us_only_watchlist():
    config = Config(
        stock_list=["NVDA", "AAPL", "MSFT"],
        market_watchlist=["SPY", "QQQ", "DIA"],
    )

    assert config.is_us_focused_runtime() is True


def test_is_us_focused_runtime_returns_false_when_a_share_present():
    config = Config(
        stock_list=["NVDA", "600519"],
        market_watchlist=["SPY"],
    )

    assert config.is_us_focused_runtime() is False
