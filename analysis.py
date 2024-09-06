#analysis.py
def get_all_habits(habits):
    """
    Returns a list of all habits.

    Args:
        habits (list): A list of Habit objects.

    Returns:
        list: The same list of Habit objects.
    """
    return habits

def get_habits_ordered(habits, frequency):
    """
    Returns a list of habits filtered by their frequency and sorted alphabetically by name.

    Args:
        habits (list): A list of Habit objects.
        frequency (str): The frequency to filter habits by (e.g., 'daily', 'weekly').

    Returns:
        list: A sorted list of Habit objects that match the given frequency.
    """
    return sorted([habit for habit in habits if habit.frequency == frequency], key=lambda h: h.name)

def longest_streak(habits):
    """
    Returns the habit with the longest streak from a list of habits.

    Args:
        habits (list): A list of Habit objects.

    Returns:
        Habit: The Habit object with the longest streak, or None if the list is empty.
    """
    return max(habits, key=lambda habit: habit.habit_streak(), default=None)

def habit_longest_streak(habit):
    """
    Returns the longest streak for a given habit.

    Args:
        habit (Habit): A Habit object.

    Returns:
        int: The longest streak (number of consecutive completions) for the given habit.
    """
    return habit.habit_streak()


