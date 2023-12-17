from dataclasses import dataclass
from src.ticker import Ticker, build_ticker_from_degiro, add_tickers


@dataclass
class MockTicker:
    product = "ticker name"
    isin = "US123123XX"
    amount = 123
    closing = 12.2
    local_value_currency = "usd"
    local_value = 12.2
    value = 11.3
    weight = 0.03

    def get_ticker(self) -> Ticker:
        return Ticker(
            product=self.product,
            isin=self.isin,
            amount=self.amount,
            closing=self.closing,
            local_value_currency=self.local_value_currency,
            local_value=self.local_value,
            value=self.value,
            weight=self.weight,
        )


def test_ticker():
    ticker = MockTicker().get_ticker()
    assert ticker.product == "ticker name"
    assert ticker.isin == "US123123XX"


def test_build_ticker_from_degiro():
    data = "LOMA NEGRA CIA IND-SPON ADR,US54150E1047,84,6.65,USD 558.60,508.10"
    ticker = build_ticker_from_degiro(data)
    assert ticker.product == "LOMA NEGRA CIA IND-SPON ADR"
    assert ticker.isin == "US54150E1047"
    assert ticker.amount == 84
    assert ticker.closing == 6.65
    assert ticker.local_value_currency == "usd"
    assert ticker.local_value == 558.60
    assert ticker.value == 508.10


def test_add_ticker():
    t1 = MockTicker().get_ticker()
    t2 = MockTicker().get_ticker()
    res = add_tickers(tickers=[t1, t2])
    assert res.product == "ticker name"
    assert res.isin == "US123123XX"
    assert res.value == t1.value + t2.value
    assert res.local_value_currency == t2.local_value_currency
    assert res.local_value == t1.local_value * 2
