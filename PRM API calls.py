import urllib2, json

url = "https://prm.gs.ucdavis.edu/api/person?loginIds=eerichmo&loginIds=tibbitts"   # Does a login search
request = urllib2.Request(url)
request.add_header('X-Auth-Token', '{auth-token}')
response = urllib2.urlopen(request)

results = json.loads(response.read())

for person in results['records']:
  print person['name'] + ',' + person['studentId'] + ',' + person['loginId'] + ',' + person['primaryTitle'] + ',' + person['homeDepartmentName']

# Other Example Calls

# Search by emails
# url = "https://prm.gs.ucdavis.edu/api/person?emails=eerichmond@ucdavis.edu&emails=smtibbitts@ucdavis.edu"

# Search by PIDMs or Student IDs or Employee IDs
# url = "https://prm.gs.ucdavis.edu/api/person?pidms=12345&studentIds=987654321&employeeIds=123456789"

# Search by name (first or last). "eli rich" or "rich, eli" with narrow down to first and last
# url = "https://prm.gs.ucdavis.edu/api/person?greedySearch=eli"

# Find the program coordinators in all graduate programs
# url = "https://prm.gs.ucdavis.edu/api/GS/program/member?roleCodes=PROGRAM_COORDINATOR&programTypes=GRADUATE_GROUP&programTypes=GRADUATE_PROGRAM&programTypes=PROFESSIONAL_PROGRAM&programTypes=DESIGNATED_EMPHASIS"

# Find the students and program coordinators in anthropology
# url = "https://prm.gs.ucdavis.edu/api/program/GANT/member?roleCodes=STUDENT&roleCodes=PROGRAM_COORDINATOR"

# Return the major professors in all graduate programs
# url = "https://prm.gs.ucdavis.edu/api/GS/program/member/mentor?roleCodes=MAJOR_PROFESSOR_MENTOR

# Find a single person plus their roles (not a result set like the URLs above)
# url = "https://prm.gs.ucdavis.edu/api/person/eerichmo"