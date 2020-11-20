import stock_rates
import db_modify
import db_chart
from datetime import date

if __name__ == "__main__":

    half_year = round(365/2)
    stock_rates.make_chart_PLN_USD(half_year)

    db_modify.create_currency_table()

    from_date = date(2005, 12, 30)
    to_date = date(2008, 1, 1)

    db_modify.insert_rates(from_date, to_date)
    db_chart.plot_char(from_date, to_date)


