import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path


def position_weights(csv_path: Path) -> dict[str, Decimal]:
    holdings: dict[str, Decimal] = {}

    with csv_path.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        if not {"symbol", "market_value"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain symbol and market_value columns.")

        for row in reader:
            symbol = (row["symbol"] or "").strip().upper()
            try:
                value = Decimal((row["market_value"] or "").strip())
            except InvalidOperation:
                raise ValueError(
                    f"Line {reader.line_num}: market_value must be a number."
                ) from None

            if not symbol or not value.is_finite() or value < 0:
                raise ValueError(
                    f"Line {reader.line_num}: each holding needs a symbol "
                    "and a finite, nonnegative market value."
                )

            holdings[symbol] = holdings.get(symbol, Decimal(0)) + value

    total = sum(holdings.values(), Decimal(0))
    if total <= 0:
        raise ValueError("Portfolio market value must be greater than zero.")

    return {symbol: value / total for symbol, value in holdings.items()}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rank portfolio holdings and simulate price shocks."
    )
    parser.add_argument("csv_path", type=Path, help="Path to a holdings CSV.")
    parser.add_argument(
        "--shock",
        action="append",
        nargs=2,
        metavar=("SYMBOL", "PERCENT"),
        help="Simulate a price change, e.g. --shock AAA -20. May be repeated.",
    )
    args = parser.parse_args()

    try:
        weights = position_weights(args.csv_path)
    except (OSError, csv.Error, ValueError) as error:
        parser.error(str(error))

    shocks: dict[str, Decimal] = {}
    for raw_symbol, raw_percent in args.shock or []:
        symbol = raw_symbol.strip().upper()
        if symbol not in weights:
            parser.error(f"{symbol} is not in the portfolio.")
        if symbol in shocks:
            parser.error(f"Specify only one shock for {symbol}.")

        try:
            percent = Decimal(raw_percent)
        except InvalidOperation:
            parser.error("Shock percent must be a number.")

        if not percent.is_finite() or percent < -100:
            parser.error("Shock percent must be finite and at least -100.")

        shocks[symbol] = percent / Decimal(100)

    ranked = sorted(weights.items(), key=lambda item: item[1], reverse=True)
    if not shocks:
        for symbol, weight in ranked:
            print(f"{symbol}: {weight:.1%}")
        return

    contributions = {
        symbol: weight * shocks.get(symbol, Decimal(0))
        for symbol, weight in ranked
    }
    stressed_values = {
        symbol: weight + contributions[symbol] for symbol, weight in ranked
    }
    portfolio_impact = sum(contributions.values(), Decimal(0))
    stressed_total = sum(stressed_values.values(), Decimal(0))

    print(f"Portfolio impact: {portfolio_impact:+.1%}")
    print(f"{'Symbol':<10}{'Before':>10}{'After':>10}{'Impact (pp)':>14}")

    for symbol, weight in ranked:
        after = (
            f"{stressed_values[symbol] / stressed_total:.1%}"
            if stressed_total > 0
            else "N/A"
        )
        contribution_pp = contributions[symbol] * 100
        print(f"{symbol:<10}{weight:>10.1%}{after:>10}{contribution_pp:>+14.1f}")


if __name__ == "__main__":
    main()