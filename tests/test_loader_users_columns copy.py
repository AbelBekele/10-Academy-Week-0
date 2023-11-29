import os
import pytest
import pandas as pd
from src.loader import SlackDataLoader
from src.config import cfg


@pytest.fixture
def sample_loader():
    return SlackDataLoader(path= cfg.path)

def test_get_channels_columns(sample_loader):
    # Get channels data from the loader
    channels_data = sample_loader.get_channels()

    # Converting it to a DataFrame
    if isinstance(channels_data, list):
        channels_df = pd.DataFrame(channels_data)
    else:
        channels_df = channels_data

    # Define the expected columns in the channels DataFrame
    expected_columns = ['id', 'name', 'created', 'creator', 'is_general', 'is_archived', "members","topic", "purpose" ]

    # Check if all expected columns are present in the DataFrame
    assert all(column in channels_df.columns for column in expected_columns), "Missing columns in the channels DataFrame"