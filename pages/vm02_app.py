from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from datetime import date


#Get today's date (for later analysis)
today = date.today()

# Configure scrapper to pull information about the app of your choice
appstore_review = AppStore(country="ie", app_name="VM Connect", app_id='1534538514')

# Scrap 2000 reviews.
appstore_review.review(how_many=2000)


# Put data in padnas dataframe
app_df = pd.DataFrame(np.array(appstore_review.reviews), columns=['review'])


# Format data based on reviews in a list format.
app_df_list = app_df.join(pd.DataFrame(app_df.pop('review').tolist()))

# Display top 5 entries
st.write(app_df_list)

# Write dataframe to CSV file
#app_df_list.to_csv('ziggo_reviews.csv')

# Count the number of reviews for each rating
rating_counts = app_df_list['rating'].value_counts().sort_index()

# Create a bar chart of the rating counts
plt.bar(rating_counts.index, rating_counts.values)

# Set the title and axis labels
plt.title('Distribution of Ratings for Ziggo SmartWifi Reviews')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')

# Show the chart
st.pyplot(plt)
