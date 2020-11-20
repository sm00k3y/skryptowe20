import requests
import matplotlib.pyplot as plt
from datetime import timedelta


def get_rates_avg(currency, days):      # ZADANIE 1
    """ Getting rates for the last X days """
    url = _url('/a/{0}/last/{1}/'.format(currency, days))
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception("GET STATUS CODE: {0}".format(resp.status_code))
    return resp.json()


def get_rates_avg_time(currency, from_date, to_date):
    """
    Getting rates for time frames with additional function
    If user passess more time than 365 days then program
    GETs from api more than once

    return: rates in dictionary format (rate[day] = rate in this day)
    """

    rates = {}

    # If time is longer than a year, get rates in partitions
    while (to_date - from_date).days >= 365:
        to_date_temp = from_date + timedelta(days=365)
        url = _url('/a/{0}/{1}/{2}'.format(currency, from_date.strftime("%Y-%m-%d"), to_date_temp.strftime("%Y-%m-%d")))
        resp = requests.get(url)

        if resp.status_code != 200:
            raise Exception("GET STATUS CODE: {0}".format(resp.status_code))

        for rate in resp.json()['rates']:
            rates[rate['effectiveDate']] = rate['mid']

        from_date = to_date_temp

    if from_date < to_date:
        url = _url('/a/{0}/{1}/{2}'.format(currency, from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d")))
    resp = requests.get(url)

    if resp.status_code != 200:
        raise Exception("GET STATUS CODE: {0}".format(resp.status_code))

    for rate in resp.json()['rates']:
        rates[rate['effectiveDate']] = rate['mid']

    return rates


def _url(path):
    return 'http://api.nbp.pl/api/exchangerates/rates/' + path


def make_chart_PLN_USD(last_days):
    """ Preparing data for the chart """
    eur = get_rates_avg('EUR', last_days)   # ZADANIE 2
    usd = get_rates_avg('USD', last_days)

    eur_dates = [rate['effectiveDate'] for rate in eur['rates']]
    usd_dates = [rate['effectiveDate'] for rate in usd['rates']]
    eur_rates = [rate['mid'] for rate in eur['rates']]
    usd_rates = [rate['mid'] for rate in usd['rates']]

    plot_chart(eur_rates, eur_dates, usd_rates, usd_dates)


def plot_chart(eur_rates, eur_dates, usd_rates, usd_dates):  # ZADANIE 3
    """ Plotting the chart """
    plt.figure(figsize=(15, 10))
    plt.title("Average EUR and USD rates to PLN")
    plt.plot(eur_dates, eur_rates, label="EUR Rates")
    plt.plot(usd_dates, usd_rates, label="USD Rates")

    plt.xlabel('Dates')
    plt.ylabel('Rates')

    k = 15
    x_dates = eur_dates[::k]
    plt.xticks(x_dates, rotation=45)

    plt.legend()
    plt.show()

