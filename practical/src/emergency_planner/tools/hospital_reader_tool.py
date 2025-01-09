import sqlite3
from crewai.tools import BaseTool
from ..data_models import HospitalLoc
from typing import List
from dotenv import load_dotenv
import os

class HospitalReaderTool(BaseTool):
    name: str = "Hospital Information Reader"
    description: str = "This tool retrieves information of all hospitals from the database."
    db_path: str = None

    def __init__(self):
        """
        Initialize the HospitalReaderTool with a default database path.

        Args:
            db_path (str): Path to the SQLite database.
        """
        super().__init__()
        # Load environment variables
        load_dotenv()

        # Get DB path and file from environment variables
        raw_db_path = os.getenv("DB_PATH")
        db_file = os.getenv("DB_FILE")

        # Ensure cross-platform compatibility by normalizing paths
        normalized_path = os.path.normpath(raw_db_path)
        self.db_path = os.path.join(normalized_path, db_file)

    def _run(self) -> List[HospitalLoc]:
        """
        Connects to a SQL database and retrieves information of all hospitals.

        Returns:
            Hospitals: An object containing a list of all hospitals.
        """
        db_path = self.db_path

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to fetch all hospitals
        query = """
        SELECT hospital_id, location_x, location_y, available_beds, available_ambulances, available_paramedics
        FROM hospitals
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        hospitals = [
            HospitalLoc(
                hospital_id=row[0],
                location=(row[1], row[2]),
                available_beds=row[3],
                available_ambulances=row[4],
                available_paramedics=row[5]
            )
            for row in rows
        ]

        conn.close()

        return hospitals
