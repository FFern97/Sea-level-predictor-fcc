import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df.['Year'], df.['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r, p, std_err = stats.linregress(df.['Year'], df.['CSIRO Adjusted Sea Level'])

    x_value = range(df.['Year'].min(), 2061)
    y_value = slope * x_value + intercept
    plt.plot(x_value, y_value)

    2050_prediction = slope * 2050 + intercept 
    # Create second line of best fit


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
