import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r, p, std_err = linregress(x, y)

    x_value = range(x.min(), 2061)
    y_value = slope * x_value + intercept
    plt.plot(x_value, y_value, color = 'r' )

    sea_level_by_2050 = slope * 2050 + intercept

    # Create second line of best fit
    new_x = df[df['Year'] >= 2000]
    slope2, intercept2, r, p, std_err = linregress(new_x['Year'], new_x['CSIRO Adjusted Sea Level'])

    x_value2 = range(2000, 2061)
    y_value2 = slope2 * x_value2 + intercept2
    plt.plot(x_value2, y_value2, color = 'g' )

    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
