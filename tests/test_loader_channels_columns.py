import os
import pytest
import pandas as pd
from src.loader import SlackDataLoader
from src.config import cfg


@pytest.fixture
def sample_loader():
    return SlackDataLoader(path= cfg.path)

def test_get_users_columns(sample_loader):
    # Get users data from the loader
    users_data = sample_loader.get_users()

    # Converting it to a DataFrame
    if isinstance(users_data, list):
        users_df = pd.DataFrame(users_data)
    else:
        users_df = users_data

    # Define the expected columns in the users DataFrame
    expected_columns = ['id', 'team_id', 'name', 'deleted', "color", "real_name", "tz", "tz_label", "tz_offset", "profile"]

    # Check if all expected columns are present in the DataFrame
    assert all(column in users_df.columns for column in expected_columns), "Missing columns in the users DataFrame"
