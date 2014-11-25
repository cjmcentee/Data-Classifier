# Description

Takes numerical data and attempts to naturally partition it into clusters.
It also describes the center and range of variation of each such cluster of points as well
as which cluster each data point was placed into.

# Requirements

Requires Python 2.7.

Uses the scipy and numpy packages for python. See: http://www.scipy.org

# Usage

Example uses for this package

Assuming the root directory is .../mixture-modeling/examples

    $ python ../scripts/MixtureModel.py -t example1d.tab -p 2 > example1d.paritioned.tab

Will parition the data in example1.tab into two groups, graph the clusters and data, and
output the relative distance of each point from each cluster and which point is
nearest to which cluster into the file example1.partitioned.tab

The output tab format is a tab separated file with the following structure:

######DATA-COLUMNS
Where N is the number of dimensions of the input data (number of columns of example1.tab),
the first N columns are the values of each coordinate point.
For 2D data, that means the first two columns will be the X and Y of the data.

######NEAREST-CLUSTER-COLUMN
The next column is the column indicating which cluster the point is nearest to.
The cluster names will be of the form 'C#', where # is a number of a cluster starting
with 0 and going up to the value input in the command line for the '-p' option.

######DISTANCE-COLUMNS
Where P is the value given at the command line for the '-p' option, the
next (and final) P columns are the distances between the point and the corresponding
cluster. (Clusters being measuring counting in the same order as they're named in
the NEAREST-CLUSTER-COLUMN.)

N can be determined in the output file by identifying the NEAREST-CLUSTER-COLUMN
with a regex match to 'C\d+'. All columns before NEAREST-CLUSTER-COLUMN are
coordinate values of the data itself, and all columns after are the distances
between the corresponding cluster and the point.


Here's three lines of example output for point data in 1 dimension and 2 clusters ('-p 2'):

```
DATA-VALUES   CLUSTER        CLUSTER-DISTANCE
-----------------------------------------------------

47.011731059    C0      59.0098561696   319.976540396
249.619188614   C1      143.597601385   117.369082841
31.4899031015   C0      74.5316841271   335.498368353
```

Notice that the columns where 'C0' is the nearest column, the first of the DISTANCE-COLUMNS
has a smaller value (is nearer to the point) than the second of the DISTANCE-COLUMNS.


# To do:

-Save the clusters to a json file and reload it to compare more points, a train-test type of
modeling.
-Add graphing support for 2D data
