def standard_deviation(x):
    if n=1:
        print("there is no standard deviation of 1 number")
    else:
        n = len(x)
        mean = sum(x) / n
        ssq = sum((x_i-mean)**2 for x_i in x)
        stdev = (ssq/n)**0.5
        return(stdev)
