from datetime import datetime
import os
import sqlite3
from crewai.tools import BaseTool
from dotenv import load_dotenv
from ..data_models.public_communication import RelatedCase, RelatedCases, FireSeverity, FireType


class IncidentAnalysisTool(BaseTool):
    name: str = "Related Incidents and Case Recorder"
    description: str = (
        "This tool retrieves related incidents based on proximity, fire severity, and fire type, "
        "and records new cases into the database."
    )
    db_path: str = "incidents.db"

    def __init__(self, result_as_answer: bool):
        """
        Initialize the IncidentAnalysisTool with a default database path.

        Args:
            db_path (str): Path to the SQLite database.
            result_as_answer (bool): Directly returns tool output
        """
        super().__init__(result_as_answer=result_as_answer)
        # Load environment variables
        load_dotenv()

        # Get DB path and file from environment variables
        raw_db_path = os.getenv("DB_PATH")
        db_file = os.getenv("DB_FILE")

        # Ensure cross-platform compatibility by normalizing paths
        normalized_path = os.path.normpath(raw_db_path)
        self.db_path = os.path.join(normalized_path, db_file)
        self.result_as_answer = result_as_answer

    def _run(
        self, 
        location_x: float, 
        location_y: float, 
        fire_severity: FireSeverity, 
        fire_type: FireType,
        summary: str
    ) -> RelatedCases:
        """
        Connects to a SQL database, retrieves related incidents, and saves the new case.

        Args:
            location_x (float): X-coordinate of the location.
            location_y (float): Y-coordinate of the location.
            fire_severity (FireSeverity): Severity of the fire.
            fire_type (FireType): Type of the fire.
            summary (str): Summary of the new incident.
            db_path (str, optional): Path to the SQLite database. If not provided,
                                     uses the path stored in self.db_path.

        Returns:
            RelatedCases: An object containing lists of related cases.
        """
        db_path = self.db_path

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query 1: Sorted by distance and datetime, limit 3
        query_distance = f"""
        SELECT rowid, summary, fire_severity, fire_type, location_x, location_y
        FROM incidents
        ORDER BY ((location_x - ?) * (location_x - ?) + (location_y - ?) * (location_y - ?)) ASC, timestamp DESC
        LIMIT 3
        """
        cursor.execute(query_distance, (location_x, location_x, location_y, location_y))
        rows_distance = cursor.fetchall()

        related_by_distance = [
            RelatedCase(
                case_id=row[0],
                summary=row[1],
                fire_severity=row[2],
                fire_type=row[3],
                location_x=row[4],
                location_y=row[5]
            )
            for row in rows_distance
        ]

        # Query 2: Same fire severity and type, sorted by datetime, limit 3
        query_severity = """
        SELECT rowid, summary, fire_severity, fire_type, location_x, location_y
        FROM incidents
        WHERE fire_severity = ? AND fire_type = ?
        ORDER BY timestamp DESC
        LIMIT 3
        """
        cursor.execute(query_severity, (fire_severity, fire_type))
        rows_severity = cursor.fetchall()

        related_by_severity = [
            RelatedCase(
                case_id=row[0],
                summary=row[1],
                fire_severity=row[2],
                fire_type=row[3],
                location_x=row[4],
                location_y=row[5]
            )
            for row in rows_severity
        ]

        # Save the new incident
        new_case_timestamp = datetime.now()
        cursor.execute(
            """
            INSERT INTO incidents (summary, timestamp, fire_severity, fire_type, location_x, location_y)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (summary, new_case_timestamp.isoformat(), fire_severity, fire_type, location_x, location_y),
        )

        conn.commit()
        conn.close()
        if self.result_as_answer:
            return RelatedCases(related_cases=related_by_distance + related_by_severity).model_dump_json(indent=2)
        else:
            return RelatedCases(related_cases=related_by_distance + related_by_severity)
