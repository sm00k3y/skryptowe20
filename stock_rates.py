import requests
import matplotlib.pyplot as plt


def get_rates_avg(currency, days):      # ZADANIE 1
    url = _url('/a/{0}/last/{1}/'.format(currency, days))
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception("GET {0} STATUS CODE: ".format(resp.status_code))
    return resp.json()


def _url(path):
    return 'http://api.nbp.pl/api/exchangerates/rates/' + path


def make_chart_PLN_USD(last_days):
    eur = get_rates_avg('EUR', last_days)   # ZADANIE 2
    usd = get_rates_avg('USD', last_days)

    eur_dates = []
    eur_rates = []
    usd_rates = []
    usd_dates = []

    for rate in eur['rates']:
        eur_rates.append(rate['mid'])
        eur_dates.append(rate['effectiveDate'])

    for rate in usd['rates']:
        usd_rates.append(rate['mid'])
        usd_dates.append(rate['effectiveDate'])

    plot_chart(eur_rates, eur_dates, usd_rates, usd_dates)


def plot_chart(eur_rates, eur_dates, usd_rates, usd_dates):  # ZADANIE 3
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

