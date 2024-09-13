# test_database.py
import sqlite3
import pytest
from database import Database
from habit import Habit
import datetime

@pytest.fixture
def db():
    """
    Fixture to create a temporary database for testing.
    The database resets after each test
    """
    return Database(':memory:')  # In-memory database for testing

def test_save_habit(db):
    """
    Test for saving a habit to the database.
    Checks that the habit is correctly stored and can be retrieved from the database.
    """
    # Create a new habit and save it to the database
    habit = Habit(name="Exercise", frequency="daily")
    db.save_habit(habit)
    
    # Retrieve the habit from the database
    saved_habit = db.get_habit("Exercise")

    # Check if the habit was saved and its attributes are correct
    assert saved_habit is not None
    assert saved_habit.name == "Exercise"
    assert saved_habit.frequency == "daily"

def test_delete_habit(db):
    """
    Test for deleting a habit from the database.
    Checks that a habit can be deleted from the database and cannot be retrieved once it has been deleted.
    """

    # Create and save a habit
    habit = Habit(name="Exercise", frequency="daily")
    db.save_habit(habit)

    # Delete the habit from the database
    db.delete_habit("Exercise")
    
    # Try to retrieve the deleted habit
    deleted_habit = db.get_habit("Exercise")

    # Check if the habit was deleted successfully 
    assert deleted_habit is None

def test_daily_habit_4_weeks_db(db):
    """
    Test a daily habit with 28 days of completions, saving to the database.
    Simulates 28 consecutive completions, saves them, and checks if the streak is correctly calculated.
    """
    # Create a new habit with daily frequency
    habit = Habit(name="Exercise", frequency="daily")
    
    # Simulate 28 days of completions for created habit
    for i in range(28):
        habit.habit_completed_dates.append(
            datetime.datetime.now() - datetime.timedelta(days=28 - i)
        )
    # Save the habit and the completions data to the database
    db.save_habit(habit)
    db.save_completion(habit)  # Save all the completion dates at once
    
    # Retrieve the habit and check streak
    saved_habit = db.get_habit("Exercise")
    # Print the completion dates for debugging
    print(saved_habit.habit_completed_dates)
    # Check that the streak is correct for 28 days  
    assert saved_habit.habit_streak() == 28
