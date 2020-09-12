

def bulk_data_extractor(file, outdir, flags):
    flags = "-" + " -".join(flags) # adds '-' to first flag then joins the rest with a " -"
    if(flags == "-"):
        flags = "" # if statement to remove erroneous "-" from flags if empty
    # os.system(f"bulk-extractor -o {outdir} {flagString} {file}")
    print(f"bulk-extractor -o {outdir} {flags} {file}")
