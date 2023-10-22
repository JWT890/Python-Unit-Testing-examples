"""

Jon William Taylor
Date: September 17, 2021
Assignment: Statistical processing
Semester: Fall 2021
IS 310-01 Advanced Computer Programming in Business

About this program:
This program will calculate and show the min, max, range, median, average and mode of the weekly gas prices for Boston, Chicago, and Cleveland over a year's worth of data

Input: Will take the data for the cities and calculate them

Output: Will show the results in a table format

"""
print(__doc__)
### import statements here

### Define the sub functions, if any here

### the main function
def gas_prices():
    print("Boston")
    def boston_max(x):
        boston_max = x[0]
        for check in x: #checks for the max gas price for Boston
            boston_max = check #finds the max gas price
        return boston_max #returns the gas price
    boston = [2.643, 2.63, 2.632, 2.634, 2.635, 2.633, 2.636, 2.649, 2.654, 2.652, 2.654, 2.657, 2.663, 2.682, 2.669, 2.663, 2.674, 2.739, 2.761, 2.777, 2.791, 2.79, 2.806, 2.802, 2.814, 2.799, 2.791, 2.771, 2.788, 2.831, 2.859, 2.882, 2.893, 2.913, 2.923, 2.881, 2.808, 2.724, 2.654, 2.638, 2.61, 2.543, 2.491, 2.484, 2.477, 2.44, 2.458, 2.48, 2.506, 2.521, 2.518, 2.539]
    print("Max", boston_max(boston)) #prints the max gas price for Boston
    def boston_min(x):
        boston_min = x[0]
        for check in x: #checks for the minimum gas price for Boston
            if check > boston_min: #finds the minimum gas price
                boston_min = check #finds the minimum gas price
        return boston_min #returns the gas price
    boston =  [2.643, 2.63, 2.632, 2.634, 2.635, 2.633, 2.636, 2.649, 2.654, 2.652, 2.654, 2.657, 2.663, 2.682, 2.669, 2.663, 2.674, 2.739, 2.761, 2.777, 2.791, 2.79, 2.806, 2.802, 2.814, 2.799, 2.791, 2.771, 2.788, 2.831, 2.859, 2.882, 2.893, 2.913, 2.923, 2.881, 2.808, 2.724, 2.654, 2.638, 2.61, 2.543, 2.491, 2.484, 2.477, 2.44, 2.458, 2.48, 2.506, 2.521, 2.518, 2.539]
    print("Min", boston_min(boston)) #prints the minimum gas price for Boston

    def boston_range(boston):
        return max(boston) - min(boston) #returns the range between the maximum and minimum gas prices for Boston
    boston = [2.643, 2.63, 2.632, 2.634, 2.635, 2.633, 2.636, 2.649, 2.654, 2.652, 2.654, 2.657, 2.663, 2.682, 2.669, 2.663, 2.674, 2.739, 2.761, 2.777, 2.791, 2.79, 2.806, 2.802, 2.814, 2.799, 2.791, 2.771, 2.788, 2.831, 2.859, 2.882, 2.893, 2.913, 2.923, 2.881, 2.808, 2.724, 2.654, 2.638, 2.61, 2.543, 2.491, 2.484, 2.477, 2.44, 2.458, 2.48, 2.506, 2.521, 2.518, 2.539]
    dispersion = max(boston) - min(boston) #the value that is between the two
    print("Range: {}".format(dispersion)) #prints the range of the gas price

    def boston_mean(boston):
        return sum(boston) / len(boston) #finds the average gas price value for Boston
    boston = [2.643, 2.63, 2.632, 2.634, 2.635, 2.633, 2.636, 2.649, 2.654, 2.652, 2.654, 2.657, 2.663, 2.682, 2.669, 2.663, 2.674, 2.739, 2.761, 2.777, 2.791, 2.79, 2.806, 2.802, 2.814, 2.799, 2.791, 2.771, 2.788, 2.831, 2.859, 2.882, 2.893, 2.913, 2.923, 2.881, 2.808, 2.724, 2.654, 2.638, 2.61, 2.543, 2.491, 2.484, 2.477, 2.44, 2.458, 2.48, 2.506, 2.521, 2.518, 2.539]
    mean = boston_mean(boston) #the representation for the data set above it
    print('Mean: {}'.format(mean)) #prints the mean value for Boston

    def boston_median(boston):
        copy_a_list = boston[:] #looks at the available list for Boston
        copy_a_list.sort() #sorts the list for the median value
        if len(copy_a_list) % 2 == 0: #checks for the median of the list
            right_mid = len(copy_a_list) // 2 #checks the first portion of the list
            left_mid = right_mid - 1 #checks for the second portion of the list
            median = (copy_a_list[left_mid] + copy_a_list[right_mid]) / 2 #finds the median value of the gas prices
        else:
            mid = len(copy_a_list) // 2 #checks the length of the list
            median = copy_a_list[mid] #checks the middle of the list of values
        return median #returns the median value of the list

    boston = [2.643, 2.63, 2.632, 2.634, 2.635, 2.633, 2.636, 2.649, 2.654, 2.652, 2.654, 2.657, 2.663, 2.682, 2.669, 2.663, 2.674, 2.739, 2.761, 2.777, 2.791, 2.79, 2.806, 2.802, 2.814, 2.799, 2.791, 2.771, 2.788, 2.831, 2.859, 2.882, 2.893, 2.913, 2.923, 2.881, 2.808, 2.724, 2.654, 2.638, 2.61, 2.543, 2.491, 2.484, 2.477, 2.44, 2.458, 2.48, 2.506, 2.521, 2.518, 2.539]
    print('Median: {}'.format(boston_median(boston))) #prints the median value of the gas prices for Boston

    def get_boston_frequency(boston):
        print("Price", "\t", "Mode") #splits the price and frequency
        sorted_list = boston[:]#sorts the given list to find frequency
        sorted_list.sort() #sorts the list to find frequency of gas prices

        previous = sorted_list[0] #starting point for finding frequency
        group_count = 0 #starting value for the frequency
        for current in sorted_list:
            if current == previous:
                group_count += 1 #for each value that is repeated, the counter goes up
                previous = current
            else:
                print(previous, "\t", group_count) #splits the values
                previous = current
                group_count = 1 #lists each value by appearance
        print(current, "\t", group_count)
    boston = [2.643, 2.63, 2.632, 2.634, 2.635, 2.633, 2.636, 2.649, 2.654, 2.652, 2.654, 2.657, 2.663, 2.682, 2.669, 2.663, 2.674, 2.739, 2.761, 2.777, 2.791, 2.79, 2.806, 2.802, 2.814, 2.799, 2.791, 2.771, 2.788, 2.831, 2.859, 2.882, 2.893, 2.913, 2.923, 2.881, 2.808, 2.724, 2.654, 2.638, 2.61, 2.543, 2.491, 2.484, 2.477, 2.44, 2.458, 2.48, 2.506, 2.521, 2.518, 2.539]
    get_boston_frequency(boston) #prints the frequency of the Boston gas prices

    print("Chicago")
    def chicago_max(x):
        chicago_max = x[0]
        for check in x: #checks for the max gas price of Chicago
            if check > chicago_max: #finds the max gas price
                chicago_max = check #locates the max price
        return chicago_max #returns the max value for Chicago
    chicago = [2.731, 2.726, 2.726, 2.757, 2.683, 2.739, 2.804, 2.742, 2.726, 2.793, 2.839, 2.939, 2.931, 2.858, 2.986, 2.867, 2.792, 2.879, 2.923, 2.889, 2.905, 3.083, 3.193, 3.214, 3.385, 3.194, 3.156, 3.052, 2.967, 3.093, 3.265, 3.259, 3.263, 3.336, 3.267, 3.222, 3.183, 3.09, 3.098, 3.002, 2.88, 2.8, 2.665, 2.578, 2.609, 2.477, 2.41, 2.345, 2.255, 2.303, 2.268, 2.237]
    print("Max", chicago_max(chicago)) #prints the max gas price for Chicago

    def chicago_min(x):
        chicago_min = x[0]
        for check in x: #checks for the minimum gas price of Chicago
            if check < chicago_min: #looks for the minimum gas price for Chicago
                chicago_min = check #locates the minimum pirce
        return chicago_min #returns the minimum value for Chicago

    chicago = [2.731, 2.726, 2.726, 2.757, 2.683, 2.739, 2.804, 2.742, 2.726, 2.793, 2.839, 2.939, 2.931, 2.858, 2.986, 2.867, 2.792, 2.879, 2.923, 2.889, 2.905, 3.083, 3.193, 3.214, 3.385, 3.194, 3.156, 3.052, 2.967, 3.093, 3.265, 3.259, 3.263, 3.336, 3.267, 3.222, 3.183, 3.09, 3.098, 3.002, 2.88, 2.8, 2.665, 2.578, 2.609, 2.477, 2.41, 2.345, 2.255, 2.303, 2.268, 2.237]
    print("Min", chicago_min(chicago)) #prints the minimum gas price value for Chicago

    def chicago_range(chicago):
        return max(chicago) - min(chicago) #returns the value in between max and min for Chicago
    chicago = [2.731, 2.726, 2.726, 2.757, 2.683, 2.739, 2.804, 2.742, 2.726, 2.793, 2.839, 2.939, 2.931, 2.858, 2.986, 2.867, 2.792, 2.879, 2.923, 2.889, 2.905, 3.083, 3.193, 3.214, 3.385, 3.194, 3.156, 3.052, 2.967, 3.093, 3.265, 3.259, 3.263, 3.336, 3.267, 3.222, 3.183, 3.09, 3.098, 3.002, 2.88, 2.8, 2.665, 2.578, 2.609, 2.477, 2.41, 2.345, 2.255, 2.303, 2.268, 2.237]
    dispersion = max(chicago) - min(chicago) #calculates the difference between the two
    print("Range: {}".format(dispersion)) #prints the result for range for Chicago

    def chicago_mean(chicago):
        return sum(chicago) / len(boston) #finds the average gas price price for Chicago
    chicago = [2.731, 2.726, 2.726, 2.757, 2.683, 2.739, 2.804, 2.742, 2.726, 2.793, 2.839, 2.939, 2.931, 2.858, 2.986, 2.867, 2.792, 2.879, 2.923, 2.889, 2.905, 3.083, 3.193, 3.214, 3.385, 3.194, 3.156, 3.052, 2.967, 3.093, 3.265, 3.259, 3.263, 3.336, 3.267, 3.222, 3.183, 3.09, 3.098, 3.002, 2.88, 2.8, 2.665, 2.578, 2.609, 2.477, 2.41, 2.345, 2.255, 2.303, 2.268, 2.237]
    mean = chicago_mean(chicago) #the representation of the value above it
    print("Mean: {}".format(mean)) #prints the mean value for Chicago

    def chicago_median(chicago):
        copy_a_list = chicago[:] #looks at the available list for Chicago
        copy_a_list.sort() #sorts the list for the median value
        if len(copy_a_list) % 2 == 0: #checks for the median of the list
            right_mid = len(copy_a_list) // 2 #checks the first portion of the list
            left_mid = right_mid - 1 #checks the second portion of the list
            median = (copy_a_list[left_mid] + copy_a_list[right_mid]) / 2 #finds the median value of the prices
        else:
            mid = len(copy_a_list) // 2 #checks the length of the list
            median = copy_a_list[mid] #locates the median value for Chicago
        return median #returns the median Chicago value
    chicago = [2.731, 2.726, 2.726, 2.757, 2.683, 2.739, 2.804, 2.742, 2.726, 2.793, 2.839, 2.939, 2.931, 2.858, 2.986, 2.867, 2.792, 2.879, 2.923, 2.889, 2.905, 3.083, 3.193, 3.214, 3.385, 3.194, 3.156, 3.052, 2.967, 3.093, 3.265, 3.259, 3.263, 3.336, 3.267, 3.222, 3.183, 3.09, 3.098, 3.002, 2.88, 2.8, 2.665, 2.578, 2.609, 2.477, 2.41, 2.345, 2.255, 2.303, 2.268, 2.237]
    print("Median: {}".format(chicago_median(chicago))) #prints the median value for Chicago

    def get_chicago_frequency(chicago):
        print("Price","\t", "Mode") #splits the price and frequency
        sorted_list = chicago[:] #sorts the given list to find the frequency
        sorted_list.sort() #sorts the list to find the frequency of gas prices

        previous = sorted_list[0]
        group_count = 0
        for current in sorted_list:
            if current == previous:
                group_count += 1 #for each value that is repeated, the counter goes up
                previous = current
            else:
                print(previous, "\t", group_count) #splits the values
                previous = current
                group_count = 1 #lists each value by appearance
        print(current, "\t", group_count)
    chicago = [2.731, 2.726, 2.726, 2.757, 2.683, 2.739, 2.804, 2.742, 2.726, 2.793, 2.839, 2.939, 2.931, 2.858, 2.986, 2.867, 2.792, 2.879, 2.923, 2.889, 2.905, 3.083, 3.193, 3.214, 3.385, 3.194, 3.156, 3.052, 2.967, 3.093, 3.265, 3.259, 3.263, 3.336, 3.267, 3.222, 3.183, 3.09, 3.098, 3.002, 2.88, 2.8, 2.665, 2.578, 2.609, 2.477, 2.41, 2.345, 2.255, 2.303, 2.268, 2.237]
    get_chicago_frequency(chicago) #prints the frequency of the Chicago gas prices

    print("Cleveland")
    def cleveland_max(x):
        cleveland_max = x[0]
        for check in x: #checks for the max gas price of Cleveland
            if check > cleveland_max: #finds the max gas price
                cleveland_max = check #locates the max price
        return cleveland_max #returns the max gas price
    cleveland = [2.692, 2.567, 2.632, 2.585, 2.652, 2.554, 2.605, 2.486, 2.532, 2.495, 2.581, 2.679, 2.613, 2.647, 2.772, 2.656, 2.615, 2.622, 2.584, 2.661, 2.636, 2.781, 2.762, 2.839, 2.838, 2.733, 2.718, 2.624, 2.495, 2.566, 2.841, 2.646, 2.805, 2.702, 2.801, 2.732, 2.755, 2.677, 2.693, 2.65, 2.566, 2.502, 2.497, 2.412, 2.419, 2.296, 2.234, 2.18, 2.114, 2.059, 2.046, 2.011]
    print("Max", cleveland_max(cleveland)) #prints the maximum value for Cleveland

    def cleveland_min(x):
        cleveland_max = x[0]
        for check in x: #checks for the minimum gas price for Cleveland
            if check < cleveland_max: #finds the min gas price
                cleveland_max = check #locates the min price
        return cleveland_max #returns the min gas price
    cleveland = [2.692, 2.567, 2.632, 2.585, 2.652, 2.554, 2.605, 2.486, 2.532, 2.495, 2.581, 2.679, 2.613, 2.647, 2.772, 2.656, 2.615, 2.622, 2.584, 2.661, 2.636, 2.781, 2.762, 2.839, 2.838, 2.733, 2.718, 2.624, 2.495, 2.566, 2.841, 2.646, 2.805, 2.702, 2.801, 2.732, 2.755, 2.677, 2.693, 2.65, 2.566, 2.502, 2.497, 2.412, 2.419, 2.296, 2.234, 2.18, 2.114, 2.059, 2.046, 2.011]
    print("Min", cleveland_min(cleveland)) #prints the min value for Cleveland

    def cleveland_range(cleveland):
        return max(cleveland) - min(cleveland) #returns the range value in between max and min for Cleveland
    cleveland = [2.692, 2.567, 2.632, 2.585, 2.652, 2.554, 2.605, 2.486, 2.532, 2.495, 2.581, 2.679, 2.613, 2.647, 2.772, 2.656, 2.615, 2.622, 2.584, 2.661, 2.636, 2.781, 2.762, 2.839, 2.838, 2.733, 2.718, 2.624, 2.495, 2.566, 2.841, 2.646, 2.805, 2.702, 2.801, 2.732, 2.755, 2.677, 2.693, 2.65, 2.566, 2.502, 2.497, 2.412, 2.419, 2.296, 2.234, 2.18, 2.114, 2.059, 2.046, 2.011]
    dispersion = max(cleveland) - min(cleveland) #calculates the difference between the two
    print("Range: {}".format(dispersion)) #prints the range value for Cleveland

    def cleveland_mean(cleveland):
        return sum(cleveland) / len(cleveland) #finds the average gas price for Cleveland
    cleveland = [2.692, 2.567, 2.632, 2.585, 2.652, 2.554, 2.605, 2.486, 2.532, 2.495, 2.581, 2.679, 2.613, 2.647, 2.772, 2.656, 2.615, 2.622, 2.584, 2.661, 2.636, 2.781, 2.762, 2.839, 2.838, 2.733, 2.718, 2.624, 2.495, 2.566, 2.841, 2.646, 2.805, 2.702, 2.801, 2.732, 2.755, 2.677, 2.693, 2.65, 2.566, 2.502, 2.497, 2.412, 2.419, 2.296, 2.234, 2.18, 2.114, 2.059, 2.046, 2.011]
    mean = cleveland_mean(cleveland) #the representation of the value above it
    print("Mean: {}".format(mean)) #prints the mean value for Cleveland

    def cleveland_median(cleveland):
        copy_a_list = cleveland[:] #looks at the available list for Cleveland
        copy_a_list.sort() #sorts the list for the median value
        if len(copy_a_list) % 2 == 0:
            right_mid = len(copy_a_list) // 2 #checks the first portion of the list
            left_mid = right_mid - 1 #checks the second portion of the list
            median = (copy_a_list[left_mid] +copy_a_list[right_mid]) / 2 #finds the median price value
        else:
            mid = len(copy_a_list) // 2 #checks the length of the list
            median = copy_a_list[mid] #locates the median value
        return median #returns the value

    cleveland = [2.692, 2.567, 2.632, 2.585, 2.652, 2.554, 2.605, 2.486, 2.532, 2.495, 2.581, 2.679, 2.613, 2.647, 2.772, 2.656, 2.615, 2.622, 2.584, 2.661, 2.636, 2.781, 2.762, 2.839, 2.838, 2.733, 2.718, 2.624, 2.495, 2.566, 2.841, 2.646, 2.805, 2.702, 2.801, 2.732, 2.755, 2.677, 2.693, 2.65, 2.566, 2.502, 2.497, 2.412, 2.419, 2.296, 2.234, 2.18, 2.114, 2.059, 2.046, 2.011]
    print("Median: {}".format(cleveland_median(cleveland))) #prints the median value of the list

    def get_cleveland_frequency(cleveland):
        print("Price","\t", "Frequency") #splits the price and frequency
        sorted_list = cleveland[:] #sorts the given list for the frequency
        sorted_list.sort() #sorts the values for the frequency

        previous = sorted_list[0]
        group_count = 0
        for current in sorted_list:
            if current == previous:
                group_count += 1 #for each value that is repeated, the counter goes up
                previous = current
            else:
                print(previous, "\t", group_count) #splits the values
                previous = current
                group_count = 1 #lists each value by appearance
        print(current,"\t", group_count)

    cleveland = [2.692, 2.567, 2.632, 2.585, 2.652, 2.554, 2.605, 2.486, 2.532, 2.495, 2.581, 2.679, 2.613, 2.647, 2.772, 2.656, 2.615, 2.622, 2.584, 2.661, 2.636, 2.781, 2.762, 2.839, 2.838, 2.733, 2.718, 2.624, 2.495, 2.566, 2.841, 2.646, 2.805, 2.702, 2.801, 2.732, 2.755, 2.677, 2.693, 2.65, 2.566, 2.502, 2.497, 2.412, 2.419, 2.296, 2.234, 2.18, 2.114, 2.059, 2.046, 2.011]
    get_cleveland_frequency(cleveland) #prints the frequency of the Cleveland prices


def main():
    gas_prices() #prints the function since it contains sub functions


if __name__ == '__main__':
    main()
