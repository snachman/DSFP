import hashlib
import shutil
import bulk_extractor
import dd



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # GUI.main_window()
    dd.from_hardware("/dev/sdb", "image.dd")
    # # bulk_extractor.bulk_data_extractor("file.dd", "outputdir/", [])
    # bulk_extractor.read_bulk_data("/home/kali/Documents/")

