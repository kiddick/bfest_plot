import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def load_data():
    days, bfests = np.loadtxt(
        "data.txt",
        unpack=True,
        converters={0: mdates.strpdate2num('%d.%m.%y')}
    )
    today = datetime.datetime.now().strftime('%d.%m.%y')
    days = np.append(days, mdates.strpdate2num('%d.%m.%y')(today))
    with open('data.txt') as data:
        labels = [el.split()[0] for el in data.readlines()]
    return days, bfests, today, labels


def imaginate(days, bfests, today, labels):
    plt.plot_date(
        x=days,
        y=np.append(bfests, bfests[-1]),
        fmt='o--',
        mew=0,
        ms=10,
        color='red',
        markevery=range(len(days - 1))
    )
    plt.plot_date(
        x=days[-1], y=bfests[-1], fmt='o--', mew=0, ms=12, color='green')
    plt.title('Bfests')
    plt.xticks(days, labels + [today])
    plt.grid(True)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.gcf().set_size_inches(15, 5)
    plt.gca().set_xlim([days[0] - 20, days[-1] + 20])
    plt.savefig(pic_name())


def pic_name():
    return '{}.png'.format(datetime.datetime.now().strftime('%d_%m_%y'))

if __name__ == '__main__':
    imaginate(*load_data())
    print 'ready: {}'.format(pic_name())
