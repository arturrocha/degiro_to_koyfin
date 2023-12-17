from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Ticker:
    product: str
    isin: str
    amount: float
    closing: float
    local_value_currency: str
    local_value: float
    value: float
    weight: Optional[float] = None


def build_ticker_from_degiro(row: str) -> Ticker:
    blobs = row.split(",")
    return Ticker(
        product=blobs[0],
        isin=blobs[1],
        amount=float(blobs[2]),
        closing=float(blobs[3]),
        local_value_currency=blobs[4].split(" ")[0].lower(),
        local_value=float(blobs[4].split(" ")[1]),
        value=float(blobs[5]),
    )


def add_tickers(tickers: List[Ticker]) -> Ticker:
    return Ticker(
        product=tickers[0].product,
        isin=tickers[0].isin,
        amount=sum([_.amount for _ in tickers]),
        closing=tickers[0].closing,
        local_value_currency=tickers[0].local_value_currency,
        local_value=sum([_.local_value for _ in tickers]),
        value=sum([_.value for _ in tickers]),
    )
