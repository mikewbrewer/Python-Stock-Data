import plotly.graph_objects as graph_object
import pandas as pd

from sys import argv
from colors import select_color




def calc_openclose(_df):
    global OPEN_CLOSE

    upper_limit = _df.shape[0]
    delta_total = 0

    for i in range(0, upper_limit):
        delta = _df['Price Open'][i] - _df['Price Close'][i]
        delta_total += delta

    delta_average = delta_total / upper_limit
    return (delta_average)



def plot_data(_argv):
    figure = graph_object.Figure()
    used_colors = []
    delta_averages = {}
    separator = ', '

    for i in range(1, len(_argv)):
        print ('reading data from ' + _argv[i] + '_data.csv')

        data_frame = pd.read_csv('CSVs/' + _argv[i] + '_data.csv')
        graph_color = select_color(used_colors)

        delta_averages[_argv[i]] = calc_openclose(data_frame)
        figure.add_trace(graph_object.Scatter(x = data_frame['Date'], y = data_frame['Price Open'], name = _argv[i], line_color = graph_color))

        used_colors.append(graph_color)

        figure.update_layout(title_text= separator.join(_argv[1:]), showlegend=True)

    print ('\n')
    print ('The following values correspond to the average delta of open vs. closing price on a given stock over time:')

    for item in delta_averages:
        print (item + ': ' + str(round(delta_averages[item], 4)))

    figure.show()



if __name__ == '__main__':
    plot_data(argv)
