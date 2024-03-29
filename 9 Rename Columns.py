# Rename Columns

# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | id          | int    |
# | first       | object |
# | last        | object |
# | age         | int    |
# +-------------+--------+
# Write a solution to rename the columns as follows:

# id to student_id
# first to first_name
# last to last_name
# age to age_in_years
# The result format is in the following example.

 

# Example 1:
# Input:
# +----+---------+----------+-----+
# | id | first   | last     | age |
# +----+---------+----------+-----+
# | 1  | Mason   | King     | 6   |
# | 2  | Ava     | Wright   | 7   |
# | 3  | Taylor  | Hall     | 16  |
# | 4  | Georgia | Thompson | 18  |
# | 5  | Thomas  | Moore    | 10  |
# +----+---------+----------+-----+
# Output:
# +------------+------------+-----------+--------------+
# | student_id | first_name | last_name | age_in_years |
# +------------+------------+-----------+--------------+
# | 1          | Mason      | King      | 6            |
# | 2          | Ava        | Wright    | 7            |
# | 3          | Taylor     | Hall      | 16           |
# | 4          | Georgia    | Thompson  | 18           |
# | 5          | Thomas     | Moore     | 10           |
# +------------+------------+-----------+--------------+
# Explanation: 
# The column names are changed accordingly

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students)
    df.rename(columns={"id":"student_id", "first":"first_name", "last":"last_name", "age":"age_in_years"}, inplace=True)
    return df

students = [
    {'id': 1, 'first': 'Mason', 'last': 'King', 'age': 6},
    {'id': 2, 'first': 'Ava', 'last': 'Wright', 'age': 7},
    {'id': 3, 'first': 'Taylor', 'last': 'Hall', 'age': 16},
    {'id': 4, 'first': 'Georgia', 'last': 'Thompson', 'age': 18},
    {'id': 5, 'first': 'Thomas', 'last': 'Moore', 'age': 10}
]

renameColumns(students)
## Author: Hemant Thapa
## Date: 11.02.2024
## Challenge: Leet Code 
