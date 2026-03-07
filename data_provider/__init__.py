# -*- coding: utf-8 -*-
"""
===================================
数据源策略层 - 包初始化
===================================

当前项目已收敛为美股主路径。

默认仅导出：
1. BaseFetcher
2. DataFetcherManager
3. YfinanceFetcher
"""

from .base import BaseFetcher, DataFetcherManager
from .yfinance_fetcher import YfinanceFetcher

__all__ = [
    'BaseFetcher',
    'DataFetcherManager',
    'YfinanceFetcher',
]
