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
