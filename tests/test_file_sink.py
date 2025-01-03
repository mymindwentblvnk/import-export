import json

from hamcrest import assert_that, has_length

from import_export.file_sink import JsonlFileSink
from import_export.models import ImportEntry


class TestJsonFileSink:

    def test_save_file(self, tmpdir):
        # Given
        path = str(tmpdir) + "fake_file_path.jsonl"
        entries = [
            ImportEntry(user_id="user_id_1", first_name="first_name_1", last_name="last_name_1"),
            ImportEntry(user_id="user_id_2", first_name="first_name_2", last_name="last_name_2"),
        ]

        # When
        JsonlFileSink(path=path).save_file(entries=entries)

        # Then
        with open(path, "r") as f:
            actual_data = json.load(f)
            assert_that(actual_data, has_length(2))
