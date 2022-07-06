"""
A bar plot is a visual tool to compare the values of various groups. It can be drawn
horizontally or vertically. We can create a bar graph using the bar() function:
"""
# Add the essential library matplotlib
import matplotlib.pyplot as plt

# create the data
movie_ratings = [1, 2, 3, 4, 5]
rating_counts = [21, 45, 72, 89, 42]

# Plot the data
plt.bar(movie_ratings, rating_counts, color='blue')

# Add X Label on X-axis
plt.xlabel("Movie Ratings")

# Add X Label on X-axis
plt.ylabel("Rating Frequency")

# Add a title to graph
plt.title("Movie Rating Distribution")

# Show the plot
plt.show()

"""
In the preceding bar chart program, the bar() function takes x-axis values, y-axis values,
and a color. In our example, we are plotting movie ratings and their frequency. Movie
ratings are on the x axis and the rating frequency is on the y axis. We can also specify the
color of the bars in the bar graph using the color parameter.
"""
