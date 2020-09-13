# DSFP
#### Damn Small Forensic Platform
#####This project is being re-factored from the beginning and has significantly changed due to Kali Linux changes and for performance (September 2020).

The need for this project comes from a missing utility for lay-people who need file recovery and basic drive insights. Even other FOSS solutions require user interface training or intermediate to advanced understanding of file structures. The results from this program should be easy enough to understand by novices.


The basic steps are as follows:
1. take a forensic image of a drive
1. hash the original and image
1. compare the two
    1. if correct, run user-defined tests against the image
    1. re-hash the image to confirm forensically sound properties
    1. log all activity
    1. produce a report

Future development will load reports as well as original media

This project is best used on Kali Linux as the tools are already installed.

Progress:
- bulk-extractor
- dd

To-Do:
- dc3dd
- extundelete
- Foremost
- iPhone Backup Analyzer
- Photorec
- Galleta
- Time
- Date
- Hex Searching