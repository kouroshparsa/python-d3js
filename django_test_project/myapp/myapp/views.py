from django.shortcuts import render
from oxus.plots import *
from settings import STATIC_URL
import random
import string
HEADER = get_header(STATIC_URL)

def index(request):
    SIZE = 20
    xdata = range(SIZE)
    ydata = [i * random.randint(1, 10) for i in range(SIZE)]
    ydata2 = [x * 2 for x in ydata]

    plt1 = ScatterPlot('plot1')
    plt1.add_data(name="data1", y=ydata, x=xdata, shape='circle')

    tooltips = []
    for i in range(SIZE):
        tt = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        tooltips.append(tt)
    plt1.add_data(name="data2", y=ydata2, x=xdata, shape='cross', tooltips=tooltips, size=20)

    values = [2, 3, 5]
    labels = ['apple', 'orange', 'banana']
    plt2 = PieChart('plot2', values=values, labels=labels, is_donut=True, is_lbl_percent=True, labels_outside=True)

    values = {'food': {'fruits': ['apple', 'orange', 'banana'], 'vegetables': ['mint', 'asparagus', 'eggplant', 'avocado', 'braccoli']}}
    plt3 = TreeChart('plot3', values=values)

    plt4 = CorrelationPlot("plot4", title='Correlation', xaxis='Expected', yaxis='Actual')
    plt4.add_data('set1', exp=[1,2,3], act=[1.3,2,3.5], tooltips=['A', 'B', 'C'], color='red')
    plt4.add_data('set1', exp=[1,2,3], act=[1,2.2,2.6], tooltips=['alpha', 'beta', 'gamma'], color='green')

    page_data = {'plot1_script': plt1.get_script(),\
                 'plot2_script': plt2.get_script(),\
                 'plot3_script': plt3.get_script(),\
                 'plot4_script': plt4.get_script(),\
                 'plot_header': HEADER}

    return render(request, "index.html", page_data)

