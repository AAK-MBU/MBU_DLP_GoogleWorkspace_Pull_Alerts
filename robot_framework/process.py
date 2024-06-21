"""This module contains the main process of the robot."""
import os
from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection
from robot_framework.google.get_and_store_alerts import get_alerts_one_week, update_db_with_alerts


def process(orchestrator_connection: OrchestratorConnection) -> None:
    """Do the primary process of the robot."""
    orchestrator_connection.log_trace("Running process.")

    orchestrator_connection.log_trace("Downloading alerts from Google DLP.")
    alerts = get_alerts_one_week(orchestrator_connection)

    orchestrator_connection.log_trace("Storing alerts from Google DLP in DB.")
    update_db_with_alerts(alerts, orchestrator_connection)


if __name__ == "__main__":
    conn_string = os.getenv("OpenOrchestratorConnString")
    crypto_key = os.getenv("OpenOrchestratorKey")
    oc = OrchestratorConnection("Google DLP Workspace alerts", conn_string, crypto_key, "")
    oc.get_credential('')
    process(oc)
