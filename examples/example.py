#
# The MIT License (MIT)
#
# Copyright (c) 2015 Matthew Antalek Jr
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import numpy as np
import dendroheatmap as pdh
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as ssd
import matplotlib as mpl

def random_similarity(n):

    k = 10
    cov = np.random.random((k, k))
    cov[:k/2,:k/2] *= 2
    cov[:k/2,k/2:] /= 2
    cov[k/2:,:k/2] /= 2
    cov[k/2:,k/2:] *= 2
    points = np.random.multivariate_normal(mean=[0] * k, cov=cov, size=n)
    data = ssd.squareform(ssd.pdist(points))
    linkage = sch.linkage(data)
    idxing = sch.leaves_list(linkage)
    data = data[:,idxing][idxing,:]

    dhm = pdh.DendroHeatMap(heat_map_data=data, left_dendrogram=linkage, top_dendrogram=linkage, heatmap_colors=("#ffeda0", "#feb24c", "#f03b20"), color_legend_displayed=False, left_dendrogram_displayed=False, label_color="#FF0000", dendrogram_color="#999999", heatmap_norm=mpl.colors.PowerNorm(2, data.min(), data.max()))
    dhm.analyze_clusters(0.9)
    dhm.show()

def random_distribution(n):

    #make up some data
    data = np.random.normal(scale=n, size=(n, n))
    data[0:n / 2,0:n / 2] += 75
    data[n / 2:, n / 2:] = np.random.poisson(lam=n,size=data[n / 2:, n / 2:].shape)
    #cluster the rows
    row_dist = ssd.squareform(ssd.pdist(data))
    row_Z = sch.linkage(row_dist)
    row_idxing = sch.leaves_list(row_Z)

    row_labels = ['bar{}'.format(i) for i in range(n)]

    #cluster the columns
    col_dist = ssd.squareform(ssd.pdist(data.T))
    col_Z = sch.linkage(col_dist)
    col_idxing = sch.leaves_list(col_Z)
    #make the dendrogram

    col_labels = ['foo{}'.format(i) for i in range(n)]

    data = data[:,col_idxing][row_idxing,:]

    heatmap = pdh.DendroHeatMap(heat_map_data=data,left_dendrogram=row_Z, top_dendrogram=col_Z, heatmap_colors=("#ffeda0", "#feb24c", "#f03b20"), window_size="auto", color_legend_displayed=False, label_color="#777777")
    heatmap.row_labels = row_labels
    heatmap.col_labels = col_labels
    heatmap.title = 'An example heatmap'
    heatmap.show()#heatmap.save("example.png")

def run():
    random_similarity(30)

if __name__ == '__main__':
    run()