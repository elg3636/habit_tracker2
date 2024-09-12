# Habit Tracker App
## Overview
The Habit Tracker App is a command-line tool designed to help users create, track, and analyze their habits. It allows users to add daily or weekly habits, mark them as completed, and analyze their progress over time.

## Features
Create Habits: Add new habits with a specified frequency (daily or weekly).
Complete Habits: Mark habits as completed and track their streaks.
Analyze Habits: View detailed statistics on habit streaks and progress.
Delete Habits: Remove habits from the tracker.

## Installation
Prerequisites
Ensure you have Python 3.x installed. You can download Python [here](https://www.python.org/downloads/).

Steps:

1: Clone the Repository
  ```
  git clone https://github.com/elg3636/habit_tracker2.git
  ```

2: Navigate to the app directory:
  ```
  cd habit_tracker 2
  ```
3: Set Up a Virtual Environment: Create and activate a virtual environment to manage dependencies.
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate

  ```
4: Install Dependencies: Install the required Python packages using the following command:

  ```
  pip install -r requirements.txt
  ```

5: Run the App: You can start using the app by running:
  ```
  python clinterface.py
  ```

## Usage
The Habit Tracker App provides various command-line operations to manage habits.

## CLI Commands

| Command | Description |
| --- | --- |
| `add_habit <name> <frequency>` | Adds a new habit with the specified frequency (e.g., daily or weekly).|
| `habit_completed <name>` | Marks the specified habit as completed.|
| `delete_habit <name>` | Deletes the specified habit.|
| `analyze_habits [frequency]` | Provides an analysis of all habits or filters by frequency (optional).|
| `analyze_habit <name>` | Provides detailed analysis for the specified habit (e.g., longest streak).|


  



