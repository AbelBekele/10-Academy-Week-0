from __future__ import print_function
import argparse
import os

default_path = os.path.join("data", "Anonymized_B6SlackExport_25Nov23", "anonymized")
default_channel_path = os.path.join(default_path, 'channels.json')
default_userfile_path = os.path.join(default_path, 'users.json')

parser = argparse.ArgumentParser(description='cmdArgs')

# Add arguments to the parser
parser.add_argument('--output', type=str, default='slack_data.csv',
                    help='filename to write analysis output in CSV format')
parser.add_argument('--path', required=False, type=str, default=default_path,
                    help='directory where slack data reside')
parser.add_argument('--channel', type=str, default=default_channel_path,
                    help='which channel we parsing')
parser.add_argument('--userfile', type=str, default=default_userfile_path,
                    help='users profile information')

# Parse command-line arguments
cfg, unknown_args = parser.parse_known_args()

# Print the values of the arguments
print(f'Output File: {cfg.output}')
print(f'Path: {cfg.path}')
print(f'Channel: {cfg.channel}')
print(f'Userfile: {cfg.userfile}')
