from bs4 import BeautifulSoup
import requests, re
from dotenv import load_dotenv
import pandas as pd

load_dotenv('./.env')

def get_text_UMD(genre: str):
  url = f"https://app.testudo.umd.edu/soc/202501/{genre}"
  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    with open('./soup/prettify.md', 'w') as file:
      file.write(str(soup.prettify()))
  else:
    print(f"Error: {response.status_code}")

def get_text_UVA(genre: str):
  url = f"https://louslist.org/CC/{genre}.html"
  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    with open('./soup/prettify.md', 'w') as file:
      file.write(str(soup.prettify()))
  else:
    print(f"Error: {response.status_code}")

def get_text_VT(genre: str):
  url = f"https://catalog.vt.edu/undergraduate/course-descriptions/{genre}/"
  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    with open('./soup/prettify.md', 'w') as file:
      file.write(str(soup.prettify()))
  else:
    print(f"Error: {response.status_code}")

def get_text_PSU(genre: str):
  url = f"https://bulletins.psu.edu/university-course-descriptions/undergraduate/{genre}/"
  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    with open('./soup/prettify.md', 'w') as file:
      file.write(str(soup.prettify()))
  else:
    print(f"Error: {response.status_code}")

def create_df_umd(document_text_path: str) -> pd.DataFrame:
  with open(document_text_path, "r") as file:
    text = file.read()

  pattern = r'(<div class="course-id">\s*(.*?)\s*</div>)|(<span class="course-title">\s*(.*?)\s*</span>)|(<div class="approved-course-text">\s*(.*?)\s*</div>)'
  matches = re.findall(pattern, text, re.DOTALL)

  with open("./soup/alloutputs.md", "w") as file:
    file.write("")
  with open("./soup/alloutputs.md", "a") as file:
    for match in matches:
      for value in match:
        if value.startswith('<div class="course-id">') | (value.startswith('<div class="approved-course-text">') and "<strong>" not in value ) | value.startswith('<span class="course-title">'):
          file.write(str(value) + "\n")

  with open("./soup/alloutputs.md", "r") as outputs:
    text = outputs.read()
    newer_list = text.split('<div class="course-id">')

  course_list = []
  for course in newer_list:
    course_id = ""
    course_title = ""
    course_description = ""

    if len(course) > 0:
      id_pattern = r'(.*?)\s*</div>'
      course_id = re.search(id_pattern, course, re.DOTALL)
      title_pattern = r'<span class="course-title">(.*?)\s*</span>'
      course_title = re.search(title_pattern, course, re.DOTALL)
      description_pattern = r'<div class="approved-course-text">(.*?)\s*</div>'
      course_description = re.search(description_pattern, course, re.DOTALL)

      if course_description:
        course_list.append([course_id.group(1).strip(), course_title.group(1).strip(), course_description.group(1).strip()])

  return pd.DataFrame(course_list, columns=["Course ID", "Course Title", "Course Description"])

def create_df_uva(document_text_path: str) -> pd.DataFrame:
  with open(document_text_path, "r") as file:
    text = file.read()

  pattern = r'(<td class="CourseNum">\s*(.*?)\s*</td>)|(<td class="CourseName">\s*(.*?)\s*</td>)|(<td class="CourseDescription">\s*(.*?)\s*<br/>)'
  matches = re.findall(pattern, text, re.DOTALL)

  with open("./soup/uva_alloutputs.md", "w") as file:
    file.write("")
  with open("./soup/uva_alloutputs.md", "a") as file:
    for match in matches:
      for value in match:
        if value.startswith('<td class="CourseNum">') | value.startswith('<td class="CourseName">') | value.startswith('<td class="CourseDescription">'):
          file.write(str(value) + "\n")

  with open("./soup/uva_alloutputs.md", "r") as outputs:
    text = outputs.read()
    newer_list = text.split('<td class="CourseNum">')

  course_list = []
  for course in newer_list:
    course_id = ""
    course_title = ""
    course_description = ""

    if len(course) > 0:
      id_pattern = r'(.*?)\s*</td>'
      course_id = re.search(id_pattern, course, re.DOTALL)
      title_pattern = r'<td class="CourseName">(.*?)\s*</td>'
      course_title = re.search(title_pattern, course, re.DOTALL)
      description_pattern = r'<td class="CourseDescription">(.*?)\s*<br/>'
      course_description = re.search(description_pattern, course, re.DOTALL)

      if course_description:
        course_list.append([course_id.group(1).strip(), course_title.group(1).strip(), course_description.group(1).strip()])

  return pd.DataFrame(course_list, columns=["Course ID", "Course Title", "Course Description"])


def create_df_vt(document_text_path: str) -> pd.DataFrame:
  with open(document_text_path, "r") as file:
    text = file.read()

  pattern = r'(<span class="text col-3 detail-code margin--tiny text--semibold text--big">\s*<strong>\s*(.*?)\s*</strong>\s*</span>)|(<span class="text col-8 detail-title margin--tiny text--bold text--big">\s*<strong>\s*(.*?)\s*</strong>\s*</span>)|(<p class="courseblockextra noindent">\s*(.*?)\s*</p>)'
  matches = re.findall(pattern, text, re.DOTALL)

  with open("./soup/vt_alloutputs.md", "w") as file:
    file.write("")
  with open("./soup/vt_alloutputs.md", "a") as file:
    for match in matches:
      for value in match:
        if value.startswith('<span class="text col-3 detail-code margin--tiny text--semibold text--big">') | value.startswith('<span class="text col-8 detail-title margin--tiny text--bold text--big">') | value.startswith('<p class="courseblockextra noindent">'):
          file.write(str(value) + "\n")

  with open("./soup/vt_alloutputs.md", "r") as outputs:
    text = outputs.read()
    newer_list = text.split('<span class="text col-3 detail-code margin--tiny text--semibold text--big">')

  course_list = []
  for course in newer_list:
    course_id = ""
    course_title = ""
    course_description = ""

    if len(course) > 0:
      id_pattern = r'(.*?)\s*</strong>'
      course_id = re.search(id_pattern, course, re.DOTALL)
      title_pattern = r'<span class="text col-8 detail-title margin--tiny text--bold text--big">(.*?)\s*</span>'
      course_title = re.search(title_pattern, course, re.DOTALL)
      description_pattern = r'<p class="courseblockextra noindent">(.*?)\s*</p>'
      course_description = re.search(description_pattern, course, re.DOTALL)

      if course_description:
        course_list.append([course_id.group(1).replace("<strong>", "").replace("</strong>", "").strip(), course_title.group(1).replace("<strong>", "").replace("</strong>", "").strip(), course_description.group(1).strip()])

  return pd.DataFrame(course_list, columns=["Course ID", "Course Title", "Course Description"])


def create_df_psu(document_text_path: str) -> pd.DataFrame:
  with open(document_text_path, "r") as file:
    text = file.read()

  pattern = r'(<div class="course_title clearfix">\s*<div class="course_codetitle">\s*(.*?)\s*</div>\s*</div>)|(<div class="courseblockdesc">\s*(.*?)\s*</div>)'
  matches = re.findall(pattern, text, re.DOTALL)

  with open("./soup/psu_alloutputs.md", "w") as file:
    file.write("")
  with open("./soup/psu_alloutputs.md", "a") as file:
    for match in matches:
      for value in match:
        if value.startswith('<div class="course_title clearfix">') | value.startswith('<div class="courseblockdesc">'):
          file.write(str(value) + "\n")

  with open("./soup/psu_alloutputs.md", "r") as outputs:
    text = outputs.read()
    newer_list = text.split('<div class="course_title clearfix">')

  course_list = []
  for course in newer_list:
    course_id = ""
    course_title = ""
    course_description = ""

    if len(course) > 0:
      id_pattern = r'<div class="course_codetitle">\s*(.*?)\s*</div>'
      course_id = re.search(id_pattern, course, re.DOTALL)
      title_pattern = r'<div class="course_codetitle">\s*(.*?)\s*</div>'
      course_title = re.search(title_pattern, course, re.DOTALL)
      description_pattern = r'<div class="courseblockdesc">\s*(.*?)\s*</div>'
      course_description = re.search(description_pattern, course, re.DOTALL)

      if course_id and course_title and course_description:
        # print("description", course_description.group(1).replace("<p>", "").replace("</p>", "").replace("\n", "").strip())
        if course_description.group(1).replace("<p>", "").replace("</p>", "").replace("\n", "").strip() != "":
          # print(genre, str([course_id.group(1), course_title, course_description]))
          course_list.append([course_id.group(1).split(":", 1)[0].strip(), course_title.group(1).split(":", 1)[1].strip(), re.sub(r'<a[^>]*>.*?</a>', '', course_description.group(1), flags=re.DOTALL).replace("<p>", "").replace("</p>", "").strip()])

  return pd.DataFrame(course_list, columns=["Course ID", "Course Title", "Course Description"])

UMD_COURSE_LIST = [
  'AASP', 'AAST', 'AGNR', 'AGST', 'AMSC', 'AMST', 'ANSC', 'ANTH', 'AOSC', 'ARAB', 'ARCH', 'AREC', 'ARHU', 'ARMY', 'ARSC', 'ARTH', 'ARTT',
  'ASTR', 'BCHM', 'BIOE', 'BIOI', 'BIOL', 'BIOM', 'BIPH', 'BISI', 'BMGT', 'BSCI', 'BSCV', 'BSOS', 'BSST', 'BUAC', 'BUDT', 'BUFN', 'BULM',
  'BUMK', 'CBMG', 'CCJS', 'CHBE', 'CHEM', 'CHIN', 'CHPH', 'CHSE', 'CINE', 'CLAS', 'CLFS', 'CMLT', 'CMSC', 'COMM', 'CPBE', 'CPET',
  'CPGH', 'CPJT', 'CPMS', 'CPPL', 'CPSA', 'CPSF', 'CPSG', 'CPSN', 'CPSP', 'CPSS', 'DANC', 'DATA', 'ECON', 'EDCP', 'EDHD', 'EDHI', 'EDMS',
  'EDSP', 'EDUC', 'ENAE', 'ENBC', 'ENCE', 'ENCO', 'ENEB', 'ENEE', 'ENES', 'ENFP', 'ENGL', 'ENMA', 'ENME', 'ENPM', 'ENRE', 'ENSE', 'ENSP',
  'ENST', 'ENTM', 'ENTS', 'EPIB', 'FGSM', 'FIRE', 'FMSC', 'FREN', 'GEMS', 'GEOG', 'GEOL', 'GERS', 'GREK', 'GVPT', 'HACS', 'HBUS', 'HDCC',
  'HEBR', 'HESI', 'HESP', 'HHUM', 'HISP', 'HIST', 'HLSA', 'HLSC', 'HLTH', 'HNUH', 'HONR', 'IDEA', 'IMDM', 'IMMR', 'INAG', 'INFM', 'INST',
  'ISRL', 'ITAL', 'JAPN', 'JOUR', 'JWST', 'KNES', 'KORA', 'LACS', 'LARC', 'LATN', 'LBSC', 'LEAD', 'LGBT', 'LING', 'MATH', 'MEES', 'MIEH',
  'MITH', 'MLAW', 'MSML', 'MSQC', 'MUED', 'MUSC', 'NACS', 'NAVY', 'NEUR', 'NFSC', 'PEER', 'PERS', 'PHIL', 'PHPE', 'PHSC', 'PHYS', 'PLCY',
  'PLSC', 'PORT', 'PSYC', 'RDEV', 'RELS', 'RUSS', 'SLLC', 'SOCY', 'SPAN', 'SPHL', 'STAT', 'SURV', 'TDPS', 'THET', 'TLPL', 'TLTC', 'URSP',
  'USLT', 'VMSC', 'WEID', 'WGSS'
]

UVA_COURSE_LIST = [
  "AAS", "AMST", "Anthropology", "Art", "Astronomy", "Biology", "Chemistry", "Classics", "Drama", "EALC", "Economics",
  "English", "EnviSci", "French", "German", "History", "Mathematics", "MDST", "MESA", "Music", "Philosophy",
  "Physics", "Politics", "PHS", "Psychology", "ReliStu", "Slavic", "Sociology", "SPAN", "Statistics", "WGS",
  "ASL", "CompSci", "CreativeWriting", "EuropeanStudies", "JWST", "MSP", "MESP", "Neuroscience", "SASP",
  "APMA", "BME", "CHE", "CEE", "ENGR", "ECE", "MSE", "MAE", "STS", "SYS", "EDLF", "KINE", "SARC", "DARD",
  "DataScience", "SEAS", "LAW", "PPOL", "NURS", "MED"
]

VT_COURSE_LIST = [
  "acis", "adv", "aoe", "afst", "alce", "aaec", "als", "at", "ains", "apsc", "aps", "ahrm", "arbc", "arch", "aad", "art",
  "bds", "bchm", "biol", "bse", "bmvs", "bmsp", "bmes", "bc", "bus", "bit", "edct", "che", "chem", "chn", "cine",
  "cee", "cla", "cos", "comm", "cmst", "cmda", "cs", "cem", "cons", "cep", "crim", "cses", "dasc", "danc",
  "econ", "edco", "edci", "edep", "ece", "engr", "enge", "esm", "engl", "ent", "ensc", "fcs", "fmd", "fin",
  "fnad", "fa", "fa", "fiw", "fst", "fl", "frec", "vt", "fr", "geog", "geos", "ger", "gr", "heb", "hist", "hort", "htm",
  "hd", "hnfe", "hum", "ise", "ids", "edit", "isc", "itds", "is", "ital", "jpn", "jmc", "jud", "kor", "lar",
  "lat", "ldrs", "lahs", "mgt", "mktg", "mse", "math", "me", "mtrg", "mn", "ms", "as", "mine", "mus",
  "nano", "nr", "neur", "nseg", "psvp", "phil", "ppe", "phys", "ppws", "psci", "phs", "port", "pm", "psyc", "pr",
  "real", "rlcl", "red", "rus", "spes", "spia", "sts", "stl", "soc", "span", "stat", "suma", "sbio", "sysb",
  "edte", "ta", "tbmh", "univ", "uh", "reg", "uap", "watr", "wgs"
]

PSU_COURSE_LIST = [
  "acctg", "acs", "adted", "aersp", "afam", "afr", "agbm", "absm", "aee", "agcom", "agsc", "asm", "ag", "ageco", "agro", "air", "amst",
  "ansc", "anth", "aba", "aplng", "ayfce", "arab", "ae", "aet", "arch", "army", "art", "aed", "arth", "a-i", "artsa", "aa", "aas", "asia",
  "astro", "athtr", "besc", "bbh", "bmb", "bioet", "bmh", "be", "bisc", "biol", "bme", "be_t", "brs", "biotc", "ba", "blaw", "che", "chem",
  "cmas", "chns", "civcm", "ce", "cet", "cams", "cas", "csd", "comm", "cedev", "ced", "cied", "cmlit", "cmpmt", "cmpeh", "cmpen", "cmpet", "cmpsc",
  "cc", "cned", "crimj", "crim", "ci", "c-s", "cyber", "dance", "da", "ds", "dart", "digit", "dmd", "ece", "emsc", "earth", "econ", "educ", "edmth",
  "edldr", "edpsy", "edtec", "edthp", "ee", "eet", "emet", "eledm", "egee", "eme", "ebf", "engr", "edsgn", "egt", "emch", "esc", "et", "engl",
  "esl", "eti", "ent", "entr", "enve", "erm", "envsc", "envst", "envse", "fin", "finsv", "cap", "fdsc", "fdsys", "frnar", "frnsc", "fort",
  "for", "fr", "fsc", "game", "geog", "geosc", "ger", "glis", "gd", "greek", "hhd", "hlhed", "hhum", "hpa", "hebr", "hied", "hindi", "hist",
  "hls", "honor", "hort", "hm", "hdfs", "hrm", "hcdd", "hum", "hss", "ie", "iet", "ist", "itech", "inart", "isb", "intag", "ib", "intst", "intsp", "it",
  "japns", "jst", "kines", "kor", "ler", "lhr", "larch", "lled", "lang", "latin", "ltnst", "lpe", "ldt", "la", "lst", "ling", "mgmt", "mis", "mktg",
  "maet", "matse", "math", "mthed", "me", "met", "medvl", "meteo", "micrb", "mnpr", "mng", "mngt", "music", "brass", "jazz", "keybd", "percn",
  "strng", "voice", "wwnds", "navsc", "nuce", "nurs", "nutr", "os", "ot", "olead", "png", "phil", "photo", "pt", "phys", "plant", "ppem", "plet",
  "pol", "plsc", "pes", "port", "psych", "php", "pubpl", "qmm", "qc", "radsc", "rte", "rptm", "rhs", "rlst", "rm", "rsoc", "rus", "sset", "spsy", "sc",
  "scied", "sts", "sra", "slav", "soda", "ssed", "socw", "soc", "sweng", "soils", "span", "spled", "stat", "scm", "sur", "sust", "swa", "thea", "turf",
  "ukr", "vbsc", "wildl", "wfs", "wgss", "wmnst", "wp", "wfed", "wled"
]

umd_dfs = []
for genre in UMD_COURSE_LIST:
  get_text_UMD(genre)
  umd_dfs.append(create_df_umd('./soup/prettify.md'))

umd_final = pd.concat(umd_dfs, ignore_index=True)

uva_dfs = []
for genre in UVA_COURSE_LIST:
  get_text_UVA(genre)
  uva_dfs.append(create_df_uva('./soup/prettify.md'))

uva_final = pd.concat(uva_dfs, ignore_index=True)

vt_dfs = []
for genre in VT_COURSE_LIST:
  get_text_VT(genre)
  vt_dfs.append(create_df_vt('./soup/prettify.md'))

vt_final = pd.concat(vt_dfs, ignore_index=True)

psu_dfs = []
for genre in PSU_COURSE_LIST:
  get_text_PSU(genre)
  psu_dfs.append(create_df_psu('./soup/prettify.md'))

psu_final = pd.concat(psu_dfs, ignore_index=True)

total_df = pd.concat([umd_final, uva_final, vt_final, psu_final], ignore_index=True)
print(total_df.info())

total_df.to_csv('course_data.csv', index=False)