from import_export.api import ApiClient
from import_export.config import Settings
from import_export.file_sink import FileSink, JsonlFileSink


class Importer:

    def __init__(self, api_client: ApiClient, file_sink: FileSink):
        self.api_client = api_client
        self.file_sink = file_sink

    def perform_import(self):
        import_entries = self.api_client.get_entries()
        self.file_sink.save_file(entries=import_entries)


def start_import():
    settings = Settings()

    api_client = ApiClient(
        url=settings.api_url,
        oauth_token_endpoint=settings.oauth_token_endpoint,
        client_id=settings.oauth_client_id,
        client_secret=settings.oauth_client_secret,
        realm_id=settings.oauth_realm_id,
    )

    json_file_sink = JsonlFileSink(path=settings.file_sink_path)

    importer = Importer(api_client=api_client, file_sink=json_file_sink)
    importer.perform_import()


if __name__ == "__main__":
    start_import()
