import matplotlib.pyplot as plt
from datetime import timedelta
import psycopg2
from db_config import config


def execute_command(command):
    """ Executes command in the DVDRENTAL database """
    transactions = []
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(command)

        records = cur.fetchall()

        for row in range(0, len(records)):
            transactions.append(records[row])

        cur.close()

    except (Exception, psycopg2.DatabaseError) as err:
        print(err)

    finally:
        if conn is not None:
            conn.close()

    return transactions


def prepare_data(from_date, to_date):
    """ Preparing data to plot the char """
    dates = [from_date + timedelta(days=i) for i in range((to_date-from_date).days + 1)]
    usd_rates = {}
    pln_rates = {}
    pln_base = {}

    for date in dates:
        usd_rates[date] = 0
        pln_rates[date] = 0

    command = "SELECT date, rate FROM PLN_EXCHANGE_RATES WHERE date > '{}' AND date < '{}'".format(
            from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d"))

    transactions = execute_command(command)

    for tup in transactions:
        pln_base[tup[0]] = pln_base.get(tup[0], 0) + tup[1]

    command = "SELECT amount, payment_date FROM payment WHERE payment_date > '{}' AND payment_date < '{}'".format(
            from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d"))

    transactions = execute_command(command)

    for tup in transactions:
        date = tup[1].date()
        pln_rates[date] = pln_rates.get(date, 0) + (tup[0] * pln_base[date])
        usd_rates[date] = usd_rates.get(date, 0) + tup[0]

    return dates, usd_rates.values(), pln_rates.values()


def plot_char(from_date, to_date):
    """ Plotting the chart """
    dates, usd_rates, pln_rates = prepare_data(from_date, to_date)

    plt.figure(figsize=(10, 5))
    plt.title("Sum of transactions in the DVDRENTAL database in USD and PLN")
    plt.plot(dates, pln_rates, label="PLN Rates")
    plt.plot(dates, usd_rates, label="USD Rates")

    plt.xlabel('Dates')
    plt.ylabel('Sum of transaction payments')

    plt.legend()
    plt.show()

