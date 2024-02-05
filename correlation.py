import math

def pearson_correlation(sx, sy):
    n = len(sx)
    x, y, xy, xsq, ysq = 0, 0, 0, 0, 0
    for i in range(n):
        x += sx[i]
        y += sy[i]
        xy += sx[i]*sy[i]
        xsq += sx[i]*sx[i]
        ysq += sy[i]*sy[i]
    return (n*xy - x*y) / math.sqrt((n*xsq - x*x)*(n*ysq - y*y))

series_x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
series_y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
r = pearson_correlation(series_x, series_y)
print('{0:.3f}'.format(r))
