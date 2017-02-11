Galaxy Operations Python Package
================================

More informations about Genomic Interval Operations in Galaxy can be found at:
https://wiki.galaxyproject.org/Learn/IntervalOperations

This package can be installed into any Galaxy with Tool Shed: https://toolshed.g2.bx.psu.edu/view/devteam/package_galaxy_ops_1_0_0

Galaxy package itself is being maintained at https://github.com/galaxyproject/tools-devteam/tree/master/packages/package_galaxy_ops_1_0_0

## docs for Python version

Name:

galaxyOps.py - Operations on Genomic Intervals, which is written in Python

Usage:

galaxyOps.py bed_file_1 [[bed_file_2]|[-swcb...]]

Descriptions:

galaxyOps.py provides the same operation as C version galaxyOps.

Options:

-s, --subSeg: Print segments that DO NOT overlap with the 2nd bed file

-w, --subWhole: Print regions that DO NOT overlap with the 2nd bed file

-c, --complement: complement of the regions of a bed file

-b, --build=N: build of the input file ( only used for complement )

-i, --interSeg: Return only overlapping segments of 2 input bed file

-a, --interAll: Return whole regions from the 1st file, which overlap.

-m, --minSize=N: minimum size of overlapping

-o, --unionMerge: Merge any overlapping regions of 2 bed files

-l, --unionLists: Lists all the original regions of 2 bed files

-r, --restrict: Restrict region size by minSize and maxSize

-x, --maxSize=N: maximum size of the region, only for -restrict

-j, --joinLists: Join two regions from two input files side by side.

-d, --covDensity: Coverage density of the region of two queries

-p, --proximity: Find proximity regions between two queries

-U, --upstream=N: Number of bps in upstream

-D, --downstream=N: Number of bps in downstream

-W, --within: Used for proximity

-t, --cluster: Find clusters in one input file

-z, --clusterSize=N: Size of cluster

-N, --numRegion=N: Num of regions in a cluster

-S, --clusterSingle: Clustering return single region

-1, --chromCol=N: chrom column number of the 1st file (default = 0)

-2, --startCol=N: start column number of the 1st file (default = 1)

-3, --stopCol=N: stop column number of the 1st file (default = 2)

-4, --strandCol2=N: strand col num of 2nd file (proximity only, default=5)

-5, --chromCol2=N: chrom column number of the 2nd file (default = 0)

-6, --startCol2=N: start column number of the 2nd file (default = 1)

-7, --stopCol2=N: stop column number of the 2nd file (default = 2)

-C, --chrom=N: Restrict to one chromsome

Example:

`galaxyOps.py knowGenes.bed exons.bed -s > introns.bed`

Find subregions in file knowGenes.bed, that don't overlap with file exons.bed, and redirect the result to file introns.bed

## docs for C version

Galaxy Operations Help Infomation (C Version)

Name:

galaxyOps - Operations on Genomic Intervals

Usage:

galaxyOps [[database|file(s) -bed=outFile.bed]]

Descriptions:

galaxyOps provides a rapid and reliable tool to process the functional data at any scale. It not only includes standard set operations such as union, intersection, subtraction and complement, but also have operations like proximity to regions from another set of data, clustering by distance of regions within a single set of data, join, and coverage density. Operation join is similar to the operation known in the relational algebra of database systems as a "natural join". Coverage density return whole regions from first set that overlap second set, and append two more field at the end of the returned region - the overlapping number of basepairs for each returned region and the percentage of the overlapping for each region of the first set.

Options:

-bed=output.bed Put intersection into bed format

-minSize=N Minimum size to output (default 1)

-chromCol=N The column number of chrom of the first file

-startCol=N The column number of start point of the first file

-stopCol=N The column number of stop point of the first file

-strandCol=N The column number of strand, only for proximity

-chromCol2=N The column number of chrom of the second file

-startCol2=N The column number of start point of the second file

-stopCol2=N The column number of stop point of the second file

-chrom=chrN Restrict to one chromosome

-or Or tables together instead of anding them

-not Output negation of resulting bit set.

-all And tables, return all fields in the 1st list

-join Join two lists, return all fields in both lists

-covDensity Calculate the coverage density

-unionLists Union return original lists

-restrict Restrict output to minSize and/or maxSize

-maxSize=N Maximum size to output (default -1) only used with -restrict

-proximity Proximity two files, use together with -upstream, -downstream, and -within

-upstream=N Number of bps in upstream

-downstream=N Number of bps in downstream

-within Used for proximity

-subtract Subtraction, use together with -subWhole

-subWhole Subtract whole region, which is overlapped

-cluster Clustering one file, use together with -clusterSize, -numRegion, and -clusterSingle

-clusterSize=N Size of cluster

-numRegion=N Num of regions in a cluster

-clusterSingle Clustering return single region

Example:

`galaxyOps hg17 knowGenes.bed exons.bed -subtract -bed=introns.bed`
Find subregions in file knowGenes.bed, that don't overlap with file exons.bed, and put the results in bed format file introns.bed
