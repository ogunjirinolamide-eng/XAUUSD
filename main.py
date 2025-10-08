from strategy.bias import BiasDetector
from strategy.entry import EntryRules
from strategy.risk import RiskManager
from core.data import MarketData
from core.scheduler import Scheduler
from config import Config


def main():
    print("🚀 Gold Momentum Bot starting up...")

    # Load config
    config = Config()

    # Initialize system components
    data = MarketData(symbol=config.SYMBOL)
    bias_detector = BiasDetector()
    entry_rules = EntryRules()
    risk_manager = RiskManager(max_daily_risk=config.MAX_DAILY_RISK, risk_per_trade=config.RISK_PER_TRADE)
    scheduler = Scheduler(interval_minutes=15)

    # Start the trading loop
    while True:
        try:
            # Fetch latest data
            candles = data.get_latest_candles(timeframe=config.TIMEFRAME_TREND_CONFIRM)
            trend_bias = bias_detector.detect_bias(candles)

            # Confirm bias and check entry conditions
            entry_signal = entry_rules.check_entry(trend_bias, data.get_latest_candles(timeframe=config.TIMEFRAME_ENTRY))

            if entry_signal:
                # Determine lot size based on risk management
                lot_size, stop_loss, take_profit = risk_manager.calculate_trade(data.current_price(), trend_bias)

                print(f"\n🟢 New trade signal detected!")
                print(f"Bias: {trend_bias}")
                print(f"Entry: {data.current_price()} | SL: {stop_loss} | TP: {take_profit}")
                print(f"Lot size: {lot_size}")
                print("Status: TRADE READY ✅")

            else:
                print(f"⚪ No valid setup found at this time ({data.timestamp_now()})")

            # Wait for next candle / interval
            scheduler.wait()

        except Exception as e:
            print(f"❌ Error in main loop: {e}")
            scheduler.wait(5)  # small delay before retry


if name == "main":
    main()
