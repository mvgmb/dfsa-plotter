import os
import sys
import csv
from matplotlib import pyplot


class Plotter:
    linestyles = ['-', '--', '-.', ':']
    markers = ['+', 's', 'o', '^']
    counter = 0
    x = []

    def set_x(self, x):
        self.x = x

    def add_plot(self, y, label):
        print(f'adding plot: {label}')
        pyplot.plot(
            self.x,
            y,
            label=label,
            linestyle=self.linestyles[self.counter % len(self.linestyles)],
            marker=self.markers[self.counter % len(self.markers)],
            markersize=10,
            markerfacecolor='none',
        )
        self.counter += 1


csv_filename = sys.argv[1]
out_dir = 'out/'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

outfile_name = ''
with open(csv_filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    plotter = None
    for row in reader:
        print(f'row: {row}')
        if row[0] == '__plot__':
            plotter = Plotter()
            outfile_name = row[1]
            pyplot.title(row[1])
            pyplot.xlabel(row[2])
            pyplot.ylabel(row[3])

        elif row[0] == '__end__':
            pyplot.grid()
            pyplot.legend()
            pyplot.savefig(f'{out_dir}{outfile_name}.png')
            pyplot.close()

        elif row[0] == '__x__':
            x = list(map(lambda n: float(n), row[1:len(row)]))
            print(f'x: {x}')
            plotter.set_x(x)
            pyplot.xticks(x)

        else:
            y = list(map(lambda n: float(n), row[1:len(row)]))
            print(f'y: {y}')
            plotter.add_plot(y, row[0])

        print()
