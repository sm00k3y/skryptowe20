import stock_rates
import db_modify
import db_chart
from datetime import date

if __name__ == "__main__":

    half_year = round(365/2)
    stock_rates.make_chart_PLN_USD(half_year)

