#!/usr/bin/env python3
"""Build city-level chart data from the college-town home sales CSV."""

import csv
import json
from collections import defaultdict
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "college_town_home_sales.csv"
OUTPUT = ROOT / "data" / "city_chart_data.json"


def rounded(value, places):
    quantum = Decimal("1").scaleb(-places)
    result = Decimal(str(value)).quantize(quantum, rounding=ROUND_HALF_UP)
    return int(result) if places == 0 else float(result)


def rounded_average(values, places):
    average = Decimal(sum(values)) / Decimal(len(values))
    return rounded(average, places)


def main():
    prices_by_city = defaultdict(list)
    days_by_city = defaultdict(list)
    all_prices = []
    all_days = []

    with SOURCE.open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            city_key = (row["city"], row["state"])

            price = int(row["sale_price"])
            if price >= 1000:
                prices_by_city[city_key].append(price)
                all_prices.append(price)

            if row["list_date"] and row["contract_date"]:
                list_date = date.fromisoformat(row["list_date"])
                contract_date = date.fromisoformat(row["contract_date"])
                days = (contract_date - list_date).days
                days_by_city[city_key].append(days)
                all_days.append(days)

    price_cities = [
        {
            "city": city,
            "state": state,
            "value": rounded(median(values), 0),
            "sales": len(values),
        }
        for (city, state), values in prices_by_city.items()
    ]
    price_cities.sort(key=lambda item: (-median(prices_by_city[(item["city"], item["state"])]), item["city"]))

    days_cities = [
        {
            "city": city,
            "state": state,
            "value": rounded_average(values, 2),
            "sales": len(values),
        }
        for (city, state), values in days_by_city.items()
    ]
    days_cities.sort(
        key=lambda item: (
            -sum(days_by_city[(item["city"], item["state"])]) /
            len(days_by_city[(item["city"], item["state"])]),
            item["city"],
        )
    )

    result = {
        "sale_price_rule": "sale_price >= 1000",
        "days_on_market_rule": "contract_date - list_date when both dates are present",
        "overall_median_sale_price": rounded(median(all_prices), 0),
        "overall_average_days_on_market": rounded_average(all_days, 2),
        "price_cities": price_cities,
        "days_cities": days_cities,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    print(f"Price cities: {len(price_cities)}; valid list/contract dates: {len(all_days)}")


if __name__ == "__main__":
    main()
