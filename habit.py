# habit.py
import datetime

class Habit:
    """
    A class to represent a habit.

    Attributes:
        name (str): The name of the habit.
        frequency (str): The frequency of the habit (e.g., 'daily', 'weekly').
        created_at (datetime): The date and time when the habit was created.
        habit_completed_dates (list): A list to store the dates when the habit was completed.
    """
    def __init__(self, name, frequency):
        """
        Initializes a new Habit instance.

        Args:
            name (str): The name of the habit.
            frequency (str): The frequency of the habit.
        """
        self.name = name
        self.frequency = frequency
        self.created_at = datetime.datetime.now()
        self.habit_completed_dates = []
        
    def complete_habit(self):
        """
        Records the completion of the habit by adding the current date and time to habit_completed_dates.
        """
        self.habit_completed_dates.append(datetime.datetime.now())

    def habit_streak(self):
        """
        Calculates the current streak of consecutive habit completions.

        Returns:
            int: The length of the current streak.
        """
        if not self.habit_completed_dates:
            return 0
        habit_streak = 1
        for i in range(1, len(self.habit_completed_dates)):
            delta = self.habit_completed_dates[i] - self.habit_completed_dates[i - 1]
            if self.frequency == 'daily':
                if delta.days == 1:
                    habit_streak += 1
                else:
                    habit_streak = 1  # Reset streak if a day is missed
            elif self.frequency == 'weekly':
                if delta.days <= 7:
                    habit_streak += 1
                else:
                    habit_streak = 1  # Reset streak if a week is missed
        return habit_streak
    
    def completion_missed(self):
        """
        Checks if a habit completion has been missed based on its frequency.
        
        Returns:
            bool: True if a completion has been missed, False otherwise.
        """
        if not self.habit_completed_dates:
            # If no completions have been logged, assume all completions are missed.
            return True

        last_completion_date = self.habit_completed_dates[-1]
        now = datetime.datetime.now()

        if self.frequency == 'daily':
            # Check if the last completion was not today or yesterday
            return now.date() != last_completion_date.date() and (now - last_completion_date).days > 1
        
        elif self.frequency == 'weekly':
            # Check if the last completion was not within the past 7 days
            return (now - last_completion_date).days > 7

        return False  # Default to no completion missed

class HabitOrganizer:
    """
    A class to manage habits, providing methods to create, complete, delete, and analyze habits.

    Attributes:
        database (Database): The database object used for storing and retrieving habit data.
    """
    def __init__(self, database):
        """
        Initializes a new HabitOrganizer instance.

        Args:
            database (Database): An instance of a Database class to interact with habit data.
        """
        self.database = database

    def create_habit(self, name, frequency):
        """
        Creates a new habit and saves it to the database.

        Args:
            name (str): The name of the habit.
            frequency (str): The frequency of the habit (e.g., 'daily', 'weekly').

        Returns:
            Habit: The created Habit instance.
        """
        habit = Habit(name, frequency)
        self.database.save_habit(habit)
        return habit
    
    def get_habit(self, name):
        """
        Retrieves a habit by name from the database.

        Args:
            name (str): The name of the habit to retrieve.

        Returns:
            Habit: The Habit instance if found, or None if not found.
        """
        return self.database.get_habit(name)
    
    def habit_completed(self, name):
        """
        Marks a habit as completed by adding the current date and time to its completion list.

        Args:
            name (str): The name of the habit to mark as completed.

        Raises:
            ValueError: If the habit does not exist in the database.
        """
        habit = self.database.get_habit(name)
        if habit:
            habit.complete_habit()
            self.database.save_completion(habit)
        else:
            raise ValueError(f"Habit '{name}' does not exist")

    def delete_habit(self, name):
         """
        Deletes a habit from the database.

        Args:
            name (str): The name of the habit to delete.

        Raises:
            ValueError: If the habit does not exist in the database.
        """
         if not self.database.get_habit(name):
            raise ValueError(f"Habit '{name}' does not exist")
         self.database.delete_habit(name)

    def get_all_habits(self):
        """
        Retrieves all habits from the database.

        Returns:
            list: A list of all Habit instances stored in the database.
        """
        return self.database.get_all_habits()

    def get_habits_ordered(self, frequency):
        """
        Retrieves all habits with the specified frequency, ordered by name.

        Args:
            frequency (str): The frequency to filter habits by.

        Returns:
            list: A sorted list of Habit instances matching the specified frequency.
        """
        return sorted([habit for habit in self.get_all_habits() if habit.frequency == frequency], key=lambda h: h.name)


    def longest_streak(self):
        """
        Determines the longest streak among all habits.

        Returns:
            int: The length of the longest streak.
        """
        return max([habit.habit_streak() for habit in self.get_all_habits()], default=0)

    def habit_longest_streak(self, habit):
        """
        Retrieves the longest streak for a specific habit.

        Args:
            habit (Habit): The Habit instance to analyze.

        Returns:
            int: The length of the longest streak for the specified habit.
        """
        return habit.habit_streak()
