# Import any dependencies needed to execute sql queries
from .sql_execution import query, db_path
import pandas as pd
import sqlite3

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase:
    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""
    
    # Define a `names` method that receives
    # no passed arguments
    @query
    def names(self):
        # Return an empty list
        return f"""
            SELECT {self.name}_id, {self.name}_name
            FROM {self.name}
        """
    
    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):
        connection = sqlite3.connect(db_path)
        
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        df = pd.read_sql_query(f"""
            SELECT event_date,
                   SUM(positive_events) AS positive_events,
                   SUM(negative_events) AS negative_events
            FROM employee_events
            WHERE {self.name}_id = ({id})
            GROUP BY event_date
            ORDER BY event_date
        """, connection)
        connection.close()
        return df
    
    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id):
        connection = sqlite3.connect(db_path)
        
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        df = pd.read_sql_query(f"""
            SELECT note_date,
                   note
            FROM notes
            WHERE {self.name}_id = ({id})
        """, connection)
        connection.close()
        return df
