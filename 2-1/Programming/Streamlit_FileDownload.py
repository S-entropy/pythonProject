import streamlit as st
import pandas as pd

import base64
import time
time_str = time.strftime('%Y%m%d-%H%M%S')


class FileDownloader:
    def __init__(self, data, file_name='my_file', file_ext='txt'):
        super(FileDownloader, self).__init__()
        self.data = data
        self.file_name = file_name
        self.file_ext = file_ext

    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = '{}_{}.{}'.format(self.file_name, time_str, self.file_ext)