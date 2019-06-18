
# Jonah Golden, 2015-11-11
# Script that reads csv data, then shows and saves a plot of that data

# Import libraries
import sys
import pandas as pd
import matplotlib.pyplot as plt


def main():

    # Assign variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Load the data
    data = pd.read_csv(input_file, delimiter=',')

    # Apply the plot function to the loaded data
    data.plot()

    # Save the plot
    plt.savefig(output_file)

    # Show the plot
    plt.show()


main()
