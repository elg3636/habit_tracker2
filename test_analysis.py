# test_analysis.py
from analysis import longest_streak, habit_longest_streak
from habit import Habit
import datetime

def test_longest_streak():
    """
    Test the function that calculates which habit has the longest streak from a list of all habits.
    Simulates two daily habits with different streak lengths to verify that the habit with the longest streak is returned.
    """
    habit1 = Habit(name="Exercise", frequency="daily")
    habit2 = Habit(name="Reading", frequency="daily")
    
    # Simulate completions for the habit Exercise with completion streak of three days
    habit1.habit_completed_dates = [
        datetime.datetime.now() - datetime.timedelta(days=2),
        datetime.datetime.now() - datetime.timedelta(days=1),
        datetime.datetime.now()
    ]
    
    # Simulate completions for the habit Reading with completion streak of 2 days
    habit2.habit_completed_dates = [
        datetime.datetime.now() - datetime.timedelta(days=5),
        datetime.datetime.now() - datetime.timedelta(days=3),
    ]
    
    habits = [habit1, habit2]

    # Assert that the habit with the longest streak is habit1 (Exercise)
    assert longest_streak(habits) == habit1

def test_habit_longest_streak():
    """
    Test the function that calculates the longest streak for a single habit.
    Simulate a daily habit and ensure that the streak length that is returned is correct.
    """
    habit = Habit(name="Exercise", frequency="daily")

    # Simulate a streak of three completions
    habit.habit_completed_dates = [
        datetime.datetime.now() - datetime.timedelta(days=2),
        datetime.datetime.now() - datetime.timedelta(days=1),
        datetime.datetime.now()
    ]
     
    # Assert that the habit streak is three days
    assert habit_longest_streak(habit) == 3

def test_longest_streak_4_weeks():
    """
    Test the function that finds the habit with the longest streak from a list,
    that includes habits with both daily and weekly frequency over a 4-week period.
    Simulate 28 daily completions for one habit, 4 weekly completions for another, 
    and missed completions for the third habit.
    """

    habit1 = Habit(name="Exercise", frequency="daily")
    habit2 = Habit(name="Meditation", frequency="daily")
    habit3 = Habit(name="Grocery Shopping", frequency="weekly")
    
    # Simulate 28 daily completions for habit1
    for i in range(28):
        habit1.habit_completed_dates.append(
            datetime.datetime.now() - datetime.timedelta(days=28 - i)
        )
    
    # Simulate 4 weekly completions for habit2
    for i in range(4):
        habit2.habit_completed_dates.append(
            datetime.datetime.now() - datetime.timedelta(weeks=4 - i)
        )

    # Simulate missed completions for habit3 (streak will be 2 only)
    for i in range(2):
        habit3.habit_completed_dates.append(
            datetime.datetime.now() - datetime.timedelta(weeks=4 - i)
        )
    
    habits = [habit1, habit2, habit3]
    
    # Check that the longest streak is 28 days (habit1)
    assert longest_streak(habits) == habit1
