import pandas as pd

# Creating a dataFrame with missing values
data = {
    'Name' : ['ALice', 'Bob', None, 'David'],
    'Age' : [25,None,35,40],
    'City' : ['New York', 'Los Angeles', 'Chicago', None]
}

df = pd.DataFrame(data)
print(df)

# Dropping rows with missing values
df_dropped = df.dropna()
print(df_dropped)

# Filling missing values with a specific value
df_filled = df.fillna('Unknown')
print(df_filled)

# Filling missing values with mean (for numeric columns)
df['Age'] = df['Age'] .fillna(df['Age'].mean())
print(df)

df_renamed = df.rename(columns = {'Name': 'Full name', 'Age' : 'Years'})
print(df_renamed)

# Renaming columns by modifying the columns attribute
df.columns = ['Full Name', 'Years', 'Location']
print(df)

# Boolean Indexing
adults = df[df['Age'] > 30]
print(adults)

# Selecting specific columns
selected_columns = df[['Name', 'City']]
print(selected_columns)

# Using loc to select rows and columns by label
selected_data = df.loc[df['Age'] > 30 , ['Name', 'City']]
print(selected_data)

# using iloc to select rows and columns by position
selected_data = df.iloc[1:3, [0,2]]
print(selected_data)

# Defining a custom function
def double_age(age):
    return age*2

# Applying the custom function to a column
df['Double Age'] = df['Age'].apply(double_age)
print(df)

# Using a lambda function with apply
df['Age Plus Teen'] = df['Age'].apply(lambda x: x + 10)
print(df)
