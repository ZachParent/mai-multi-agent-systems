import os
import sqlite3
import random
from datetime import timedelta, datetime
from dotenv import load_dotenv

def populate_incident_table(db_path: str, number_of_incidents=20):
    """
    Populates the database with at least 20 incidents if they do not exist.
    The summary now includes the number of injured people, and the function
    selects from 5 different summary templates to add variety.

    Args:
        db_path (str): Path to the SQLite database.
        number_of_incidents (int): Number of sample incidents to insert.
    """
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create table
        cursor.execute("""
        CREATE TABLE incidents (
            summary TEXT,
            timestamp TEXT,
            fire_severity TEXT,
            fire_type TEXT,
            location_x REAL,
            location_y REAL
        )
        """)

        # Five predefined summary templates
        summary_templates = [
            "A massive {fire_type} fire erupted, causing {injured} injuries. The severity was {severity}.",
            "The area experienced a {fire_type} fire that led to {injured} people injured. Fire severity: {severity}.",
            "A {fire_type} fire broke out, leaving {injured} individuals injured. Fire severity: {severity}.",
            "An outbreak of {fire_type} fire was reported, with {injured} injuries. Severity level: {severity}.",
            "A {fire_type} fire incident has been recorded, resulting in {injured} injuries. Severity: {severity}."
        ]

        base_time = datetime.now()
        fire_types = ["ordinary", "electrical", "gas", "chemical", "other"]
        fire_severities = ["low", "medium", "high"]

        for i in range(number_of_incidents):
            # Randomly choose fire attributes
            fire_type = random.choice(fire_types)
            fire_severity = random.choice(fire_severities)
            
            # Randomly determine number of injured people
            injured_people = random.randint(0, 20)
            
            # Pick one of the predefined summaries
            summary_template = random.choice(summary_templates)
            summary = summary_template.format(
                fire_type=fire_type, 
                injured=injured_people, 
                severity=fire_severity
            )

            # Random date within the last 30 days
            timestamp = (base_time - timedelta(days=random.randint(0, 30))).isoformat()

            # Random location
            location_x = random.uniform(-100, 100)
            location_y = random.uniform(-100, 100)

            cursor.execute("""
            INSERT INTO incidents (summary, timestamp, fire_severity, fire_type, location_x, location_y)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (summary, timestamp, fire_severity, fire_type, location_x, location_y))

        conn.commit()
        conn.close()
        print(f"INCIDENTS TABLE CREATED")

def main(reset=True):
    # Load environment variables
    load_dotenv(os.path.join("practical", "src", ".env"))

    # Get DB path and file from environment variables
    raw_db_path = os.getenv("DB_PATH")
    db_file = os.getenv("DB_FILE")

    # Ensure cross-platform compatibility by normalizing paths
    normalized_path = os.path.normpath(raw_db_path)
    db_path = os.path.join(normalized_path, db_file)

    # Check if reset is enabled and delete the existing database file
    if reset and os.path.exists(db_path):
        os.remove(db_path)
        print(f"Database file {db_path} has been deleted.")

    # Ensure the directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    populate_incident_table(db_path)

if __name__ == "__main__":
    main()