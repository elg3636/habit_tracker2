# test_habit.py
import datetime
from habit import Habit

def test_habit_creation():
    """
    Test for the creation of habits
    Verification that the habit name, frequency and creation date are correctly initialized
    """
    habit = Habit(name="Exercise", frequency="daily")
    
    assert habit.name == "Exercise" # Check if the name is correctly assigned
    assert habit.frequency == "daily" # Check if the frequency is correctly assigned
    assert isinstance(habit.created_at, datetime.datetime) # Check if creation date is a datetime object
    assert habit.habit_completed_dates == [] # Verify that the completion list is initially empty

def test_habit_complete():
    """
    Test for marking a habit as complete
    Verification that the completion is recorded with the right date and time
    """
    habit = Habit(name="Exercise", frequency="daily")
    habit.complete_habit()  #Mark the habit as complete


    assert len(habit.habit_completed_dates) == 1 # Check that the habit has one completion
    assert isinstance(habit.habit_completed_dates[0], datetime.datetime) # Verify that the completion date is a datetime object


def test_habit_streak():
    """
    Test for the habit streak calculation
    """
    habit = Habit(name="Exercise", frequency="daily")
    
    # Simulate completing the habit for three days in a row
    habit.habit_completed_dates = [
        datetime.datetime.now() - datetime.timedelta(days=2),
        datetime.datetime.now() - datetime.timedelta(days=1),
        datetime.datetime.now()
    ]
    
    assert habit.habit_streak() == 3  # The streak should be 3 days

def test_daily_habit_4_weeks():
    """
    Test for a habit with daily frequency for a time period of 4 weeks (or 28days)
    """
    habit = Habit(name="Exercise", frequency="daily")
    
    # Simulate 28 days of completions
    for i in range(28):
        habit.habit_completed_dates.append(
            datetime.datetime.now() - datetime.timedelta(days=28 - i)
        )
    
    # Check that the streak is 28 days
    assert habit.habit_streak() == 28

def test_weekly_habit_4_weeks():
    """
    Test for a habit with weekly frequency for a time period of 4 weeks
    """
    habit = Habit(name="Grocery Shopping", frequency="weekly")
    
    # Simulate completion once a week during 4 weeks
    for i in range(4):
        habit.habit_completed_dates.append(
            datetime.datetime.now() - datetime.timedelta(weeks=4 - i)
        )
    
    # Check that the streak is 4 weeks
    assert habit.habit_streak() == 4
