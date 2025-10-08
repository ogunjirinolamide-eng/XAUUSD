class RiskManager:
    def init(self, max_daily_risk=0.2, risk_per_trade=0.05):
        self.max_daily_risk = max_daily_risk
        self.risk_per_trade = risk_per_trade

    def calculate_trade(self, current_price, bias):
        """
        Returns (lot_size, stop_loss, take_profit)
        Uses simple fixed ratio for now.
        """
        pip_value = 1  # placeholder
        stop_loss_pips = 100
        take_profit_pips = 200

        lot_size = self.risk_per_trade * 10  # simplified logic
        stop_loss = current_price - stop_loss_pips if bias == "BULLISH" else current_price + stop_loss_pips
        take_profit = current_price + take_profit_pips if bias == "BULLISH" else current_price - take_profit_pips

        return lot_size, stop_loss, take_profit
