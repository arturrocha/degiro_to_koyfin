from functools import cached_property
from typing import List
from portfolio import Portfolio
from ticker import Ticker, build_ticker_from_degiro, add_tickers


class Converter:
    def __init__(
        self,
        input_csv: List[str],
    ):
        self._input_csv = input_csv
        self._output_csv = "koyfin.csv"

    @cached_property
    def _degiro_csv_to_list(self) -> List[str]:
        rows = []
        for _file in self._input_csv:
            with open(_file, "r") as f:
                rows.extend(f.readlines())
        return rows

    @cached_property
    def _degiro_list_no_header_and_cash(self) -> List[str]:
        tickers = [
            row.strip()
            for row in self._degiro_csv_to_list
            if "Symbol/ISIN" not in row and "CASH & CASH FUND" not in row
        ]
        return tickers

    @cached_property
    def _degiro_merged_tickers(self) -> List[Ticker]:
        tickers_with_duplicates = [
            build_ticker_from_degiro(row)
            for row in self._degiro_list_no_header_and_cash
        ]

        tickers = []
        for ticker in tickers_with_duplicates:
            done = []
            if len(tickers) > 0:
                done = [_.isin for _ in tickers]
            if ticker.isin in done:
                continue

            _list = [_ for _ in tickers_with_duplicates if _.isin == ticker.isin]
            tickers.append(add_tickers(_list))
        return tickers

    @cached_property
    def _degiro_currency(self) -> str:
        currencies = []
        for row in self._degiro_csv_to_list:
            if "Product,Symbol/ISIN,Amount,Closing" in row:
                currencies.append(row.strip()[-3:])
        assert len(set(currencies)) == 1
        return currencies[0].lower()

    @cached_property
    def _build_portfolio(self) -> Portfolio:
        return Portfolio(
            tickers=self._degiro_merged_tickers, currency=self._degiro_currency
        )

    def build(self) -> None:
        columns = ["isin", "weight"]
        df = self._build_portfolio.to_pandas()[columns]
        df["date"] = "01/01/2023"
        df.to_csv(self._output_csv, index=False)
