from src.portfolio import Portfolio
from src.ticker import Ticker


def test_portfolio():
    t1 = Ticker(
        product="t1",
        isin="USt1",
        amount=12,
        closing=8.31,
        local_value_currency="usd",
        local_value=12*8.31,
        value=12*8.31*0.96,
    )
    t2 = Ticker(
        product="t2",
        isin="IEt2",
        amount=21,
        closing=81.76,
        local_value_currency="eur",
        local_value=21*81.76,
        value=21*81.76,
    )
    t3 = Ticker(
        product="t3",
        isin="IEt3",
        amount=199,
        closing=18.12,
        local_value_currency="eur",
        local_value=199*18.12,
        value=199*18.12,
    )
    portfolio = Portfolio(tickers=[t1, t2, t3], currency="eur")
    assert portfolio.currency_values == {}
