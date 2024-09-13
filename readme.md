# Habit Tracker App
## Introduction
The Habit Tracker is an application created to aid users in creating, tracking, and analyzing their habits. It allows users to add daily or weekly habits, mark them as completed, and analyze their progress.

## Features
Create Habits: Add new habits with a specified frequency (daily or weekly).
Complete Habits: Mark habits as completed.
Analyze Habits: View detailed statistics on habit streaks and progress.
Delete Habits: Remove habits from the tracker.

## Installation
### Prerequisites:
Ensure you have Python 3.x installed. You can download Python [here](https://www.python.org/downloads/).

### Steps:

1: Clone the Repository
  ```
  git clone https://github.com/elg3636/habit_tracker2.git
  ```

2: Navigate to the app directory:
  ```
  cd habit_tracker2
  ```
3: Set Up a Virtual Environment.
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate

  ```
4: Install Dependencies: Install the required Python packages using the following command:

  ```
  pip install -r requirements.txt
  ```

5: Run the App: You can start using the app by using the following code:
  ```
  python clinterface.py
  ```

## Usage
The Habit Tracker App provides various command-line comands to manage habits.

### Command-Line Interface Commands

| Command | Description |
| --- | --- |
| `add_habit <name> <frequency>` | Adds a new habit with the specified frequency (e.g., daily or weekly).|
| `habit_completed <name>` | Marks the habit as completed.|
| `delete_habit <name>` | Deletes the specified habit.|
| `analyze_habits [frequency]` | Provides an analysis of all habits or filters by frequency (optional).|
| `analyze_habit <name>` | Provides detailed analysis for the specified habit (e.g. longest streak).|

### Examples:

1. Add a Habit:
   ```
   python clinterface.py add_habit "Jog" "daily"
   ```
2. Complete a Habit:
   ```
    python clinterface.py habit_completed "Jog"
   ```
3. Analyze a specific habit:
   ```
    python clinterface.py analyze_habit "Jog"
   ```
4. Analyze all of the habits:
   ```
    python clinterface.py analyze_habits
   ```
5. Delete a Habit:
   ```
   python clinterface.py delete_habit "Jog" "daily"
   ```

### Viewing data
There are a few options to view that data in the database. 
1. In the development of the app the VS code SQLite3 extension was used:
+ Install the SQLite extension
+ Then open the `database.py` file
+ The extension should then provide an interface directly to allow the viewing of the data

2. If you are not using VS code, you can use the SQLite Command-Line tool.
+ Navigate to the project directory
+ Open the Command-Line tool using:
  ```sqlite3 habits.db```
+ Run the commands using SQL (examples below:
  + View tables:
  ```
  .tables
  ```
  + Query data from a table:
  ```
  SELECT * FROM Habits;
  SELECT * FROM Completions;
  ```

## Testing instructions

In order to ensure that the key components of the app are functioning properly, unit tests using pytest have been conducted. 
The tests cover creating and completing habits, the saving and retrieving of habits and their completions from the database and the different functions of the analysis component.

### Conducting the tests
1. Install pytest using:
   ```
   pip install pytest
   ```
2. Run the tests using:
   ```
   pytest
   ```
3. For more detailed output of each test use:
   ```
   pytest -v
   ```
4. Run specific test file run the test specifying the file name (for example:)
   ```
   pytest test_habit.py
   ```

### Testing files
Below is a summary of what each test file specfically covers:
+ `test_habit.py`: Tests habit creation, habit completion, and streaks.
+ `test_database.py`: Tests saving, retrieving, and deleting habits in the database.
+ `test_analysis.py`: Tests the analysis functions

