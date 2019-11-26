from random import randint

import numpy as np
import matplotlib.pyplot as plt


def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted number that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins. 
        You are not allowed to use
    """
    data_size = len(data)
    bins_size = len(bins)

    result_count = [0 for i in range(bins_size)]

    # counting the number of elements in each bin:
    for i in range(data_size):
        for j in range(bins_size):
            if j < bins_size - 1 and bins[j] <= data[i] < bins[j + 1]:
                result_count[j] += 1
                break
            elif j == bins_size - 1:
                result_count[j] += 1

    # creating the list of labels for each bin:
    result_bins = [str(bins[i]) + "-" + str(bins[i + 1]) for i in range(bins_size - 1)]
    result_bins.append(str(bins[bins_size - 1]) + "-+")

    return [result_count, result_bins]


def plot_histogram(bins_count):
    """
        Quesion 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommand using 
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    # firstly, using numerical labels for bins to save the right order
    # (otherwise, the label "100-+" will be placed right after "10-20"
    # due to the automatic sort of a list of non-numerical labels):
    x = [i for i in range(len(bins_count[0]))]
    plt.figure(figsize=(15, 10))
    plt.bar(x, height=bins_count[0], tick_label=bins_count[1])
    plt.xlabel("Bin intervals")
    plt.ylabel("Number of values")
    plt.title("Random values distribution")
    plt.show()


if __name__ == "__main__":
    
    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
