<div align="center">

# 📈 Mag 7 宏觀分析系統

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Ready-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)

> 🤖 基于 AI 大模型的 **美股科技七巨頭（Magnificent 7）宏觀環境分析系統**
> 
> 每日自動分析 NVDA、AAPL、MSFT、GOOGL、META、AMZN、TSLA，判斷整體市場風險偏好並推送到 Telegram

</div>

## 🎯 專案特色

### 📊 Magnificent 7 宏觀風向標

通過分析科技七巨頭的整體走勢，判斷美股宏觀環境：

| 信號 | 含義 |
|------|------|
| 🟢 **Risk-On** | Mag 7 整體走強，市場風險偏好上升 |
| 🔴 **Risk-Off** | Mag 7 整體走弱，資金轉向避險 |
| ⚪ **Neutral** | 方向不明，觀望等待 |

### 🧠 AI 驅動的決策儀表盤

- **一句話核心結論** - 直接告訴你該買/該賣/該等
- **宏觀信號解讀** - 板塊共振、權重影響、領漲股觀察
- **精確狙擊點位** - $買入價、$止損價、$目標價
- **檢查清單** - ✅⚠️❌ 快速掃描每項條件

### 🚀 適配高波動科技股

原版系統針對 A 股設計，本分支專為美股七巨頭優化：

| 項目 | 原版（A 股） | 本分支（Mag 7） |
|------|-------------|----------------|
| 乖離率閾值 | > 5% 嚴禁追高 | > 8% 謹慎追高（適配高波動） |
| 籌碼結構 | 獲利比例、集中度 | 機構情緒、分析師評級 |
| 風險排查 | 減持公告、業績預虧 | 財報風險、Fed 政策、監管調查 |
| 分析視角 | 個股交易信號 | 宏觀環境判斷 |

---

## 📈 推送效果

```
🎯 2026-02-01 Mag 7 宏觀決策儀表盤
7只股票 | 🟢買入:3 🟡觀望:3 🔴卖出:1

🌍 宏觀信號: 🟢 Risk-On | 科技股集體走強

---

� 買入 | NVIDIA (NVDA)
📌 縮量回踩MA5支撐，乖離率3.2%處於最佳買點
💰 狙擊: $950 買入 | $900 止損 | $1050 目標

🌍 宏觀信號
**市場影響權重**: 高 | **風險偏好**: � Risk-On
**板塊共振**: NVDA 帶動芯片股集體走強

✅多頭排列 ✅乖離率<8% ✅機構情緒健康

---
生成時間: 18:00
```

---

## 🚀 快速開始

### 1. Fork 專案

### 2. 配置 GitHub Secrets

進入 `Settings` → `Secrets and variables` → `Actions`

| Secret 名稱 | 說明 | 必填 |
|------------|------|:----:|
| `STOCK_LIST` | `NVDA,AAPL,MSFT,GOOGL,META,AMZN,TSLA` | ✅ |
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/) 免費獲取 | ✅ |
| `TELEGRAM_BOT_TOKEN` | @BotFather 獲取 | ✅ |
| `TELEGRAM_CHAT_ID` | @userinfobot 獲取 | ✅ |
| `TAVILY_API_KEYS` | [Tavily](https://tavily.com/) 新聞搜索 | 推薦 |

### 3. 啟用 Actions

進入 `Actions` → 點擊 `I understand my workflows, go ahead and enable them`

### 4. 手動測試

`Actions` → `每日股票分析` → `Run workflow`

### 5. 完成！

默認每個工作日 **18:00（北京時間）** 自動執行

---

## � 核心交易理念

### 動態乖離率（適配高波動股）
- **乖離率 < 3%**：最佳買點區間
- **乖離率 3-8%**：可小倉介入
- **乖離率 > 8%**：高波動股警戒區
- **乖離率 > 12%**：即使是科技巨頭也需謹慎

### 趨勢交易
- ✅ **多頭排列**：MA5 > MA10 > MA20
- � **均線發散上行** = 趨勢加速
- � **均線粘合** = 方向選擇期

### 宏觀環境判斷原則
1. **板塊共振**：當 Mag 7 中 5 只以上同向時，代表板塊共振
2. **領漲股觀察**：NVDA 常為 AI 主題領漲股，有先行指標意義
3. **權重影響**：AAPL、MSFT、NVDA 對指數影響最大

---

## 📁 專案結構

```
daily_stock_analysis/
├── main.py                 # 主程式入口
├── src/
│   ├── analyzer.py         # AI 分析器（含 Mag 7 SYSTEM_PROMPT）
│   ├── stock_analyzer.py   # 技術分析（8% 乖離率閾值）
│   ├── notification.py     # 推送（含宏觀信號顯示）
│   └── ...
├── data_provider/          # 數據源（YFinance 獲取美股）
└── .github/workflows/      # GitHub Actions
```

---

## ⚙️ 進階配置

| 環境變數 | 說明 | 預設值 |
|---------|------|--------|
| `GEMINI_MODEL` | AI 模型 | `gemini-3-flash-preview` |
| `REPORT_TYPE` | 報告類型 | `simple` |
| `ANALYSIS_DELAY` | 分析間隔（秒） | `10` |

---

## 📄 License

[MIT License](LICENSE)

基於 [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) 二次開發

## ⚠️ 免責聲明

本專案僅供學習和研究使用，不構成任何投資建議。股市有風險，投資需謹慎。