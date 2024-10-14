import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Imports_Exports_Dataset.csv")

# Title of the dashboard
st.title("Imports & Exports Dashboard")

# Sidebar for filtering options
st.sidebar.header("Filters")

# Filter by country
countries = st.sidebar.multiselect("Select Countries:", options=data['Country'].unique(), default=data['Country'].unique())

# Filter by category
categories = st.sidebar.multiselect("Select Categories:", options=data['Category'].unique(), default=data['Category'].unique())

# Filter by Import/Export
imp_exp = st.sidebar.multiselect("Select Import/Export Type:", options=data['Import_Export'].unique(), default=data['Import_Export'].unique())

# Apply filters to the dataset
filtered_data = data[(data['Country'].isin(countries)) & 
                     (data['Category'].isin(categories)) &
                     (data['Import_Export'].isin(imp_exp))]

# Visualization 1: Top 10 Countries by Quantity of Imports/Exports
st.subheader("Top 10 Countries by Quantity of Imports/Exports")
top_countries = filtered_data.groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots(figsize=(10, 6))
top_countries.plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_title('Top 10 Countries by Quantity of Imports/Exports')
ax1.set_xlabel('Country')
ax1.set_ylabel('Total Quantity')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Visualization 2: Distribution of Import/Export Value by Category
st.subheader("Distribution of Import/Export Value by Category")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_data, x='Category', y='Value', ax=ax2)
ax2.set_title('Distribution of Import/Export Value by Category')
ax2.set_xlabel('Category')
ax2.set_ylabel('Value')
plt.xticks(rotation=45)
st.pyplot(fig2)

# Visualization 3: Total Weight by Shipping Method
st.subheader("Total Weight by Shipping Method")
shipping_method_weights = filtered_data.groupby('Shipping_Method')['Weight'].sum()
fig3, ax3 = plt.subplots(figsize=(8, 5))
shipping_method_weights.plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax3)
ax3.set_title('Total Weight by Shipping Method')
ax3.set_ylabel('')
st.pyplot(fig3)

# Visualization 4: Count of Transactions per Import/Export Type
st.subheader("Count of Transactions per Import/Export Type")
fig4, ax4 = plt.subplots(figsize=(6, 4))
sns.countplot(data=filtered_data, x='Import_Export', palette='viridis', ax=ax4)
ax4.set_title('Count of Transactions per Import/Export Type')
ax4.set_xlabel('Import/Export')
ax4.set_ylabel('Number of Transactions')
st.pyplot(fig4)

# Visualization 5: Average Transaction Value by Payment Terms
st.subheader("Average Transaction Value by Payment Terms")
avg_value_payment_terms = filtered_data.groupby('Payment_Terms')['Value'].mean()
fig5, ax5 = plt.subplots(figsize=(10, 6))
avg_value_payment_terms.plot(kind='bar', color='salmon', ax=ax5)
ax5.set_title('Average Transaction Value by Payment Terms')
ax5.set_xlabel('Payment Terms')
ax5.set_ylabel('Average Value')
plt.xticks(rotation=45)
st.pyplot(fig5)
