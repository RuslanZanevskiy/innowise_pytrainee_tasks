# Students & Rooms data processing with python and Postgresql 

> This project processes student and room data from JSON files, populates a PostgreSQL database, executes a series of SQL queries against this data, and outputs the results in either JSON or XML format.

## Overview

This Python application performs the following key operations:
1.  **Database Schema Creation**: It dynamically creates `Rooms` and `Students` tables in a specified PostgreSQL database.
2.  **Data Population**: It reads room and student information from user-provided JSON files and populates these database tables.
3.  **SQL Query Execution**: It runs a predefined set of SQL queries to analyze the student and room data.
4.  **Output Generation**: The results of these queries are saved to files in either JSON or XML format, based on user preference.

## Prerequisites

* Python 3.10+
* PostgreSQL server (running and accessible)
* Python packages:
    * `psycopg2-binary`
    * `python-dotenv`

## Usage

Run the `main.py` script from the command line, providing paths to the students JSON file, rooms JSON file, and the desired output format (`json` or `xml`).

**Command Syntax:**
```bash
python main.py <path_to_students_json> <path_to_rooms_json> <output_format>
````

**Example:**

```bash
python main.py data/students.json data/rooms.json json
```

## SQL Queries Performed

The application executes the following SQL queries (found in the `sql/` directory):

1.  **`sql/nstudents_in_rooms.sql`**:
      * Lists each room and the count of students in it.
2.  **`sql/small_mean_age_rooms.sql`**:
      * Identifies the top 5 rooms with the smallest mean student age (in days).
3.  **`sql/big_age_diff_rooms.sql`**:
      * Identifies the top 5 rooms with the largest age difference between the oldest and youngest student.
4.  **`sql/male_female_rooms.sql`**:
      * Lists rooms that accommodate both male ('M') and female ('F') students.

The database schema itself is defined in `sql/schema.sql`.

## Logging

* Detailed logs of the application's operations, including errors, are saved to `logs.log` in the project's root directory.
