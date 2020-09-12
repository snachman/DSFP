import hashlib
import shutil
import bulk_extractor


def compute_hash(file):
    m = hashlib.sha256()
    with open(file, 'rb') as f:
        buf = f.read()
        m.update(buf)
    return(m.hexdigest())


def make_copy(file, output):
    original_hash = compute_hash(file)
    shutil.copyfile(file, output)
    copy_hash = compute_hash(output)
    if original_hash == copy_hash:
        print("PASS")
        return True
    else:
        print("FAIL")
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # GUI.main_window()
    # bulk_extractor.bulk_data_extractor("file.dd", "outputdir/", [])
    bulk_extractor.read_bulk_data("/home/kali/Documents/")

