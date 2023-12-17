from functools import cached_property
from typing import List, Dict

import pandas as pd

from ticker import Ticker


class Portfolio:
    def __init__(
        self,
        tickers: List[Ticker],
        currency: str,
    ):
        self._tickers = tickers
        self.currency = currency
        self.build_weights()

    @cached_property
    def total_value(self) -> float:
        return sum([_.value for _ in self._tickers])

    @cached_property
    def _currencies(self) -> List[str]:
        return list(set([_.local_value_currency for _ in self._tickers]))

    @cached_property
    def currency_values(self) -> Dict[str, float]:
        values = {}
        for currency in self._currencies:
            values[currency] = sum(
                [
                    _.local_value
                    for _ in self._tickers
                    if _.local_value_currency == currency
                ]
            )
        return values

    def build_weights(self) -> None:
        for ticker in self._tickers:
            ticker.weight = round(ticker.value / self.total_value, 2)

    def summary(self) -> None:
        print(f"currency = {self.currency}")
        print(f"total_value = {self.total_value}")
        print(f"_currencies = {self._currencies}")
        print(f"currency_values = {self.currency_values}")
        print(self._tickers[0])

    def to_pandas(self) -> pd.DataFrame:
        _list = []
        for ticker in self._tickers:
            _list.append(
                {
                    "product": ticker.product,
                    "isin": ticker.isin,
                    "amount": ticker.amount,
                    "closing": ticker.closing,
                    "local_value_currency": ticker.local_value_currency,
                    "local_value": ticker.local_value,
                    "value": ticker.value,
                    "weight": ticker.weight,
                }
            )
        return pd.DataFrame(_list)
