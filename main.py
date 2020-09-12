
import hashlib
import os
import shutil
import GUI

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

def bulk_data_extractor(file, outdir, flags):
    flags = "-" + " -".join(flags)
    if(flags == "-"):
        flags = ""
    # os.system(f"bulk-extractor -o {outdir} {flagString} {file}")
    print(f"bulk-extractor -o {outdir} {flags} {file}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # GUI.main_window()
    bulk_data_extractor("file.dd", "outputdir/", [])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
