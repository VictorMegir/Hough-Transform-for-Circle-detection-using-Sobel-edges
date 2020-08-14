# Edge-Detection-and-Hough-Transform-for-Circle-detection
Implementation of Hough Transform for the purposes of circle detection using edges extracted with Sobel filter.

### Sobel Edges
We implemented the Sobel filter using Convolution with two 3x3 kernels. We create an edge map by adding the convulution results.
Our implmentation also uses thresholding to reduce noise in the edge map.

### Hough Transform
Initally, we create an accumulator space, which stores the parameters (center and range) for each circle that the Hough Transform will examine.
For each edge point (i, j) in the edge map, if that point is part of a circle then the corresponding circle recieves one vote in the accumulator space.
Return the circles with the most votes. These are the circles that the Hough Transform has detected.
