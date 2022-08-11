import pandas
from applications.device_actualizer.models import *


class Extentions:
    def bytes_to_string(self, arr: bytes):
        pass

    def handle_upload_file(self, file, url, redirect):
        print(url)
        if url.__contains__('esma_devices'):
            ds = pandas.read_excel(file, header=4)
            for record in ds.columns:
                print(ds[record].query("'Код железной дороги' == 95"))
            return redirect('applications.device_actualizer:esma_devices_all')
