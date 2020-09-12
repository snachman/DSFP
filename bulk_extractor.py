import os

def bulk_data_extractor(file, outdir, flags):
    flags = "-" + " -".join(flags) # adds '-' to first flag then joins the rest with a " -"
    if(flags == "-"):
        flags = "" # if statement to remove erroneous "-" from flags if empty
    # os.system(f"bulk-extractor -o {outdir} {flagString} {file}")
    print(f"bulk-extractor -o {outdir} {flags} {file}")


def read_bulk_data(output_location):
    files = (os.listdir(output_location))
    for file in files:
        fullpath = (output_location + file)
        if(test_empty_files(fullpath)):
            with open(fullpath, "r") as f:
                print(f)
                print(f.read())
                f.close()


def test_empty_files(file):
    if(os.path.getsize(file) > 0):
        return True

