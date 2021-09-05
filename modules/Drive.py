class Drive:
    def __init__(self, service):
        self.service = service

    def ls(self, folder_id):
        """
        #TODO
        """
        files = []
        page_token = None
        while True:
            response = (
                self.service.files()
                .list(
                    q=f"'{folder_id}' in parents",
                    spaces="drive",
                    fields="nextPageToken, files(id, name, mimeType, createdTime, modifiedTime, owners)",
                    pageToken=page_token,
                )
                .execute()
            )
            files.extend(response.get("files", []))
            page_token = response.get("nextPageToken", None)
            if page_token is None:
                break
        return files

    def move(self, file_id, destination_folder_id):
        """
        #TODO
        """
        file = self.service.files().get(fileId=file_id, fields="parents").execute()
        previous_parents = ",".join(file.get("parents"))
        file = (
            drive_service.files()
            .update(
                fileId=file_id,
                addParents=destination_folder_id,
                removeParents=previous_parents,
                fields="id, parents",
            )
            .execute()
        )
        return file

    def upload_csv(self, source_path, destination_name, destination_folder_id):
        """
        #TODO
        """
        metadata = {"name": destination_name, "mimeType": "text/csv"}
        file = (
            self.service.files().create(body=metadata, media_body=source_path).execute()
        )  # Upload
        file = self.move(file.get("id"), destination_folder_id)  # Move to destiny
        return file
