from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from datetime import date

#Get today's date (for later analysis)
today = date.today()

# Configure scrapper to pull information about the app of your choice
ziggo = AppStore(country="nl", app_name="Ziggo_SmartWifi", app_id='1480385784')

# Scrap 2000 reviews.
ziggo.review(how_many=2000)

# Put data in padnas dataframe
ziggo_df = pd.DataFrame(np.array(ziggo.reviews),columns=['review'])

# Format data based on reviews in a list format.
ziggo_df_list = ziggo_df.join(pd.DataFrame(ziggo_df.pop('review').tolist()))
ziggo_df_list = ziggo_df_list.sort_values(by=['date'])
# Display top 5 entries
st.write(ziggo_df_list)

# Write dataframe to CSV file
#ziggo_df_list.to_csv('ziggo_reviews.csv')

# Count the number of reviews for each rating
rating_counts = ziggo_df_list['rating'].sort_index()

sns.histplot(ziggo_df_list['rating'], bins=5, kde=False)
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Distribution of Ratings')
st.pyplot(plt)

ratings_by_date = ziggo_df_list.groupby('date')['rating'].mean()
plt.plot(ratings_by_date.index, ratings_by_date.values)
plt.xlabel('Date')
plt.ylabel('Rating')
plt.title('Average Rating Over Time')
st.pyplot(plt)


sns.scatterplot(x='date', y='rating', data=ziggo_df_list)
plt.xlabel('Date')
plt.ylabel('Rating')
plt.title('Rating vs. Date')
st.pyplot(plt)

corr = ziggo_df_list.corr()
sns.heatmap(corr, cmap='coolwarm', annot=True)
plt.title('Correlation Between Columns')
st.pyplot(plt)

