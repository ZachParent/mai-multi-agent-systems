import sqlite3
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from dotenv import load_dotenv
import os

class UpdateEntry(BaseModel):
    """Schema for a single update entry."""
    hospital_id: str = Field(..., description="ID of the hospital to update.")
    beds_reserved: int = Field(..., description="Number of beds reserved.")
    ambulances_dispatched: int = Field(..., description="Number of ambulances dispatched.")
    paramedics_deployed: int = Field(..., description="Number of paramedics deployed.")

class HospitalUpdaterTool(BaseTool):
    name: str = "Hospital Status Updater"
    description: str = "This tool updates the status of a single hospital in the database."
    args_schema: Type[BaseModel] = UpdateEntry
    db_path: str = None

    def __init__(self):
        """
        Initialize the HospitalUpdaterTool with a default database path.
        """
        super().__init__()
        load_dotenv(os.path.join("practical", "src", ".env"))
        raw_db_path = os.getenv("DB_PATH")
        db_file = os.getenv("DB_FILE")
        normalized_path = os.path.normpath(raw_db_path)
        self.db_path = os.path.join(normalized_path, db_file)

    def _run(self, **kwargs):
        """
        Connects to a SQL database and updates the status of a single hospital.

        Args:
            hospital_id (str): ID of the hospital to update.
            beds_reserved (int): Number of beds reserved.
            ambulances_dispatched (int): Number of ambulances dispatched.
            paramedics_deployed (int): Number of paramedics deployed.
        """
        hospital_id = kwargs.get("hospital_id")
        beds_reserved = kwargs.get("beds_reserved")
        ambulances_dispatched = kwargs.get("ambulances_dispatched")
        paramedics_deployed = kwargs.get("paramedics_deployed")
        db_path = self.db_path

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE hospitals
        SET available_beds = available_beds - ?,
            available_ambulances = available_ambulances - ?,
            available_paramedics = available_paramedics - ?
        WHERE hospital_id = ?
        """, (beds_reserved, ambulances_dispatched, paramedics_deployed, hospital_id))

        conn.commit()
        conn.close()
