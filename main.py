from app_store_scraper import AppStore
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json


ziggo = AppStore(country="nl", app_name="Ziggo_SmartWifi", app_id='1480385784')
ziggo.review(how_many=2000)

ziggo_df = pd.DataFrame(np.array(ziggo.reviews),columns=['review'])
ziggo_df2 = ziggo_df.join(pd.DataFrame(ziggo_df.pop('review').tolist()))
print(ziggo_df2.head())

ziggo_df2.to_csv('ziggo_reviews.csv')

# Count the number of reviews for each rating
rating_counts = ziggo_df2['rating'].value_counts().sort_index()

# Create a bar chart of the rating counts
plt.bar(rating_counts.index, rating_counts.values)

# Set the title and axis labels
plt.title('Distribution of Ratings for Ziggo SmartWifi Reviews')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')

# Show the chart
plt.show()

ratings = ziggo_df2['rating']
plt.hist(ratings, bins=5)

# Set the title and axis labels
plt.title('Distribution of Ratings for Ziggo SmartWifi Reviews')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')

# Show the histogram
plt.show()