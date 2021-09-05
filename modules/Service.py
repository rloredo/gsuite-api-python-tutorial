from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


class Service:
    def __init__(self, service_credentials_path, app):
        """
        #TODO
        """
        self.service = self._get_service(service_credentials_path, app)

    def _get_service(self, service_credentials_path, app):
        """
        #TODO
        """
        if app == "sheets":
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                service_credentials_path, ["https://www.googleapis.com/auth/drive"]
            )
            return discovery.build("sheets", "v4", credentials=credentials)
        if app == "docs":
            pass  # TODO
        if app == "slides":
            pass  # TODO
        if app == "drive":
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                service_credentials_path, ["https://www.googleapis.com/auth/drive"]
            )
            return discovery.build("drive", "v3", credentials=credentials)
        if app == "calendar":
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                service_credentials_path,
                ["https://www.googleapis.com/auth/calendar.readonly"],
            )
            return discovery.build("calendar", "v3", credentials=credentials)
        else:
            raise ValueError(
                "Incorrect app name passed. Use: sheets, docs, slides, drive or calendar"
            )
