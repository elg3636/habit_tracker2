
import click
from database import Database
from habit import HabitOrganizer
from analysis import  get_all_habits, get_habits_ordered, longest_streak, habit_longest_streak

# Define a Click command group to group the CLI commands
@click.group()
def cli():
    pass

# Command to add a new habit
@click.command()
@click.argument('name')
@click.argument('frequency')
def add_habit(name, frequency):
    """
    Adds a new habit with the specified name and frequency.
    
    Args:
        name (str): The name of the habit.
        frequency (str): The frequency of the habit (e.g., 'daily', 'weekly').
    """
    db = Database()  # Initialize the database connection
    organizer = HabitOrganizer(db)  # Create a HabitOrganizer to manage habits
    organizer.create_habit(name, frequency)  # Create the habit
    click.echo(f"Habit '{name}' with frequency '{frequency}' added!")  # Confirm habit addition

# Command to mark a habit as completed
@click.command()
@click.argument('name')
def habit_completed(name):
    """
    Marks a habit as completed for the current date.
    
    Args:
        name (str): The name of the habit to mark as completed.
    """
    db = Database()  # Initialize the database connection
    organizer = HabitOrganizer(db)  # Create a HabitOrganizer to manage habits
    try:
        organizer.habit_completed(name)  # Mark the habit as completed
        click.echo(f"Habit '{name}' completed!")  # Confirm completion
    except ValueError as e:
        click.echo(e)  # Display an error message if the habit doesn't exist

# Command to delete a habit
@click.command()
@click.argument('name')
def delete_habit(name):
    """
    Deletes a habit from the database.
    
    Args:
        name (str): The name of the habit to delete.
    """
    db = Database()  # Initialize the database connection
    organizer = HabitOrganizer(db)  # Create a HabitOrganizer to manage habits
    try:
        organizer.delete_habit(name)  # Delete the habit
        click.echo(f"Habit '{name}' deleted!")  # Confirm deletion
    except ValueError as e:
        click.echo(e)  # Display an error message if the habit doesn't exist

# Command to analyze and display habits, optionally filtered by frequency
@click.command()
@click.argument('frequency', required=False)
def analyze_habits(frequency=None):
    """
    Analyzes and displays all habits, optionally filtering by frequency.
    
    Args:
        frequency (str, optional): The frequency to filter habits by (e.g., 'daily', 'weekly').
    """
    db = Database()  # Initialize the database connection
    organizer = HabitOrganizer(db)  # Create a HabitOrganizer to manage habits
    habits = organizer.get_all_habits()  # Retrieve all habits

    if not habits:
        click.echo("No habits available")  # Notify if no habits are found
        return

    if frequency:
        filtered_habits = get_habits_ordered(habits, frequency)  # Filter habits by frequency
        if filtered_habits:
            click.echo(f"Habits with frequency '{frequency}':")
            for habit in filtered_habits:
                click.echo(f"- {habit.name}")
        else:
            click.echo(f"No habits with frequency '{frequency}' are available")
    else:
        click.echo("All habits:")
        for habit in habits:
            click.echo(f"- {habit.name} (Streak: {habit.habit_streak()} days)")  # Display habit names and streaks

        habit_with_longest_streak = longest_streak(habits)  # Find the habit with the longest streak
        if habit_with_longest_streak:
            click.echo(f"\nThe habit with the longest streak: {habit_with_longest_streak.name} ({habit_with_longest_streak.habit_streak()} days)")
        else:
            click.echo("No habit has been completed yet.")

# Command to analyze and display a specific habit's longest streak            
@click.command()
@click.argument('name')
def analyze_habit(name):
    """
    Analyzes and displays the longest streak for a specific habit.
    
    Args:
        name (str): The name of the habit to analyze.
    """
    db = Database()  # Initialize the database connection
    organizer = HabitOrganizer(db)  # Create a HabitOrganizer to manage habits
    habit = organizer.get_habit(name)  # Retrieve the habit by name
    
    if habit:
        streak = habit_longest_streak(habit)  # Get the habit's longest streak
        click.echo(f"The longest streak for the habit '{name}' is {streak} days")  # Display the streak
    else:
        click.echo(f"The habit '{name}' cannot be found")  # Notify if the habit doesn't exist


    # Implement analysis using analytics module and display the results here

cli.add_command(add_habit)
cli.add_command(habit_completed)
cli.add_command(delete_habit)
cli.add_command(analyze_habits)
cli.add_command(analyze_habit)

# Main entry point for the CLI
if __name__ == '__main__':
    cli()