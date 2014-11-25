__author__ = 'coltonmcentee'

# ############################
#
# Commandline Options
#
# ############################
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-t", "--tabbed",
                  dest="tabbed_file_name",
                  help="tab delimited file where each line is a point value")

parser.add_option("-p", "--partitions",
                  dest="number_partitions",
                  help="number of paritions to split the data into")

(options, args) = parser.parse_args()

if options.number_partitions is None or int(options.number_partitions) < 1:
    print "-p (number of partitions) must be specified with a value >= 1"
    exit()

# ############################
#
# Script
#
# ############################
from matplotlib import pyplot
from GaussianMixtureModel import GaussianMixtureModel, gaussian

import Tab

#
# TODO: Add support for multidimensional data and a 2D heat map
#


#
# Script behavior
#
data = Tab.parse_as_floats(options.tabbed_file_name)

model = GaussianMixtureModel(data, int(options.number_partitions))

print model.to_tab()

# 1D data can be plotted as a histogram
if len(data[0]) == 1:
    data_points = [t[0] for t in data]
    # Plot data as histogram
    pyplot.figure(0)
    pyplot.hist(data_points, 100)

    # Plot model as gaussians
    pyplot.figure(1)
    data_min = min(data_points)
    data_max = max(data_points)
    step = max(1, int((data_max - data_min) / len(data_points)))
    x_range = range(int(data_min), int(data_max), step)

    for cluster in model.clusters:
        gaussian_plot = [gaussian(cluster.mean[0], cluster.std, float(x)) for x in x_range]
        pyplot.plot(x_range, gaussian_plot)

    pyplot.show()

# 2D data can be plotted as a contour map
elif len(data[0]) == 2:
    pyplot.figure(0)

    for cluster in model.clusters:
        data_points_x = [t[0] for t in cluster.points]
        data_points_y = [t[1] for t in cluster.points]
        pyplot.plot(data_points_x, data_points_y, '.')

    pyplot.show()
    print "# Full 2D display not implemented yet"