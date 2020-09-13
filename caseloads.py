import json


def create_file(case_ID, user, location):
    data = {}
    data['case'] = [case_ID]
    data['case'].append({
        'user': user,
        'forensic_location': location
    })
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()

