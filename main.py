
import hashlib
import shutil


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
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
