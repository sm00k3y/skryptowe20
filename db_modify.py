import psycopg2
from db_config import config
import stock_rates
from datetime import timedelta


def create_currency_table():
    """ Creating new table """

    command = '''CREATE TABLE PLN_EXCHANGE_RATES (
        date DATE NOT NULL,
        rate NUMERIC
    )'''

    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS PLN_EXCHANGE_RATES")

        cur.execute(command)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as err:
        print(err)

    finally:
        if conn is not None:
            conn.close()


def insert_rates(from_date, to_date, currency='USD'):
    """ Inserting rates and dates to the newly created table """
    usd_rates = stock_rates.get_rates_avg_time(currency, from_date, to_date)

    dates_and_rates = []

    if(from_date > to_date):
        raise Exception("WRONG DATES!")

    cur_date = from_date
    prev_date = cur_date

    while(cur_date <= to_date):
        app_date = cur_date.strftime('%Y-%m-%d')
        if usd_rates.get(app_date):
            dates_and_rates.append((cur_date, usd_rates.get(app_date)))
        else:
            usd_rates[app_date] = usd_rates.get(prev_date)
            dates_and_rates.append((cur_date, usd_rates.get(prev_date)))
        prev_date = app_date
        cur_date += timedelta(days=1)

    command = "INSERT INTO PLN_EXCHANGE_RATES(date, rate) VALUES(%s, %s)"

    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.executemany(command, dates_and_rates)

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as err:
        print(err)

    finally:
        if conn is not None:
            conn.close()

