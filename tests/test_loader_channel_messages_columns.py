import os
import pytest
import pandas as pd
from src.loader import SlackDataLoader
from src.config import cfg


@pytest.fixture
def sample_loader():
    return SlackDataLoader(path= cfg.path)

def test_get_channel_messages_columns(sample_loader):
    # Inserting random channel name
    channel_name = 'all-week2'

    # Get channel messages data from the loader
    channel_messages_data = sample_loader.get_channel_messages(channel_name)

    # Converting it to a DataFrame
    if isinstance(channel_messages_data, list):
        channel_messages_df = pd.DataFrame(channel_messages_data)
    else:
        channel_messages_df = channel_messages_data

    # Define the expected columns in the channel messages DataFrame
    expected_columns = ['type', 'subtype', 'ts', 'user', 'text', 'inviter']

    # Check if all expected columns are present in the DataFrame
    assert all(column in channel_messages_df.columns for column in expected_columns), "Missing columns in the channel messages DataFrame"
