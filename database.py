#database.py
import sqlite3
from habit import Habit
import datetime

class Database:
    """
    A class to handle all database operations related to habits and their completions.

    Attributes:
        conn (sqlite3.Connection): The database connection object.
    """
    def __init__(self, db_name='habits.db'):
        """
        Initializes a new Database instance and connects to the specified SQLite database.

        Args:
            db_name (str): The name of the database file. Defaults to 'habits.db'.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary tables for storing habits and completions if they don't already exist.
        """
        with self.conn:
            # Create the Habits table
            self.conn.execute('''CREATE TABLE IF NOT EXISTS Habits (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    frequency TEXT NOT NULL,
                                    created_at DATETIME NOT NULL
                                 )''')
            # Create the Completions table
            self.conn.execute('''CREATE TABLE IF NOT EXISTS Completions (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    habit_id INTEGER,
                                    completed_at DATETIME NOT NULL,
                                    FOREIGN KEY (habit_id) REFERENCES Habits(id)
                                 )''')
            
    def save_habit(self, habit):
        """
        Saves a habit to the database. If the habit already exists, updates its frequency and creation date.

        Args:
            habit (Habit): The Habit instance to be saved.
        """
        # Check if the habit already exists in the database
        existing_habit = self.conn.execute('''SELECT id FROM Habits WHERE name = ?''', (habit.name,)).fetchone()
        if existing_habit:
            with self.conn:
                self.conn.execute('''UPDATE Habits SET frequency = ?, created_at = ? WHERE id = ?''', 
                                  (habit.frequency, habit.created_at, existing_habit[0]))
         # Insert the new habit
        else:
            with self.conn:
                self.conn.execute('''INSERT INTO Habits (name, frequency, created_at)
                                 VALUES (?, ?, ?)''', (habit.name, habit.frequency, habit.created_at))
                
                
    def get_habit(self, name):
        """
        Retrieves a habit from the database by its name.

        Args:
            name (str): The name of the habit to retrieve.

        Returns:
            Habit: The Habit instance if found, or None if not found.
        """
        # Query the habit by name
        cursor = self.conn.execute('''SELECT id, name, frequency, created_at FROM Habits WHERE name = ?''', (name,))
        row = cursor.fetchone()
        if row:
            # Create a Habit instance from the retrieved data
            habit = Habit(row[1], row[2])
            habit.created_at = datetime.datetime.fromisoformat(row[3])
            # Retrieve completion dates for the habit
            completion_cursor = self.conn.execute("SELECT completed_at FROM Completions WHERE habit_id = ?", (row[0],))
            for completion_row in completion_cursor:
                habit.habit_completed_dates.append(datetime.datetime.fromisoformat(completion_row[0]))

            return habit
        return None
    
    def save_completion(self, habit):
        """
        Saves a completion record for a habit in the database.

        Args:
            habit (Habit): The Habit instance whose completion is being recorded.
        """
        # Get the habit ID from the database
        habit_id = self.conn.execute('''SELECT id FROM Habits WHERE name = ?''', (habit.name,)).fetchone()[0]
        with self.conn:
            # Insert the completion date into the Completions table
            self.conn.execute('''INSERT INTO Completions (habit_id, completed_at)
                                 VALUES (?, ?)''', (habit_id, habit.habit_completed_dates[-1]))
            
    def delete_habit(self, name):
        """
        Deletes a habit and its associated completions from the database.

        Args:
            name (str): The name of the habit to delete.

        Raises:
            ValueError: If the habit does not exist in the database.
        """
        # Get the habit ID from the database
        habit_id = self.conn.execute('''SELECT id FROM Habits WHERE name = ?''', (name,)).fetchone()
        if habit_id:
            with self.conn:
                 # Delete the habit from the Habits table
                self.conn.execute('''DELETE FROM Habits WHERE id = ?''', (habit_id[0],))
                  # Delete the associated completions from the Completions table
                self.conn.execute('''DELETE FROM Completions WHERE habit_id = ?''', (habit_id[0],))
        else:
            raise ValueError(f"Habit '{name}' does not exist")

    def get_all_habits(self):
        """
        Retrieves all habits from the database, including their completion records.

        Returns:
            list: A list of all Habit instances stored in the database.
        """
        # Query all habits from the database
        cursor = self.conn.execute("SELECT id, name, frequency, created_at FROM Habits")
        habits = []
        for row in cursor:
             # Create a Habit instance from the retrieved data
            habit = Habit(row[1], row[2])
            habit.created_at = datetime.datetime.fromisoformat(row[3])
              # Retrieve completion dates for each habit
            completion_cursor = self.conn.execute("SELECT completed_at FROM Completions WHERE habit_id = ?", (row[0],))
            for completion_row in completion_cursor:
                habit.habit_completed_dates.append(datetime.datetime.fromisoformat(completion_row[0]))
            habits.append(habit)
        return habits
        