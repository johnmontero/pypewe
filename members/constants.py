from members import strings

GENDER_MALE = 'male'
GENDER_FEMALE = 'female'

GENDER_TUPLE = (
  (GENDER_MALE, strings.GENDER_MALE),
  (GENDER_FEMALE, strings.GENDER_FEMALE)
)

GENDER_DICT = dict(GENDER_TUPLE)
GENDER_CHOICES = set([k for k,v in GENDER_TUPLE])

OCCUPATION_STUDENT = 'student'
OCCUPATION_STUDENT_OTHER = 'student_other'
OCCUPATION_DESIGNER = 'designer'
OCCUPATION_DEVELOPER = 'developer'
OCCUPATION_SYSADMIN = 'sysadmin'
OCCUPATION_DEVOP = 'devop'
OCCUPATION_PROFESSOR = 'professor'
OCCUPATION_PM = 'pm'
OCCUPATION_DBA = 'dba'
OCCUPATION_ENTREPRENEUR = 'entrepreneur'
OCCUPATION_CTO = 'cto'
OCCUPATION_CEO = 'ceo'
OCCUPATION_CONSULTANT = 'consultant'
OCCUPATION_OTHER_TECHNICAL = 'technical'
OCCUPATION_OTHER_UNIVERSITY = 'university'
OCCUPATION_OTHER = 'other'

OCCUPATION_TUPLE = (
  (OCCUPATION_STUDENT, strings.OCCUPATION_STUDENT),
  (OCCUPATION_STUDENT_OTHER, strings.OCCUPATION_STUDENT_OTHER),
  (OCCUPATION_DESIGNER, strings.OCCUPATION_DESIGNER),
  (OCCUPATION_DEVELOPER, strings.OCCUPATION_DEVELOPER),
  (OCCUPATION_SYSADMIN, strings.OCCUPATION_SYSADMIN),
  (OCCUPATION_DEVOP, strings.OCCUPATION_DEVOP),
  (OCCUPATION_PROFESSOR, strings.OCCUPATION_PROFESSOR),
  (OCCUPATION_PM, strings.OCCUPATION_PM),
  (OCCUPATION_DBA, strings.OCCUPATION_DBA),
  (OCCUPATION_ENTREPRENEUR, strings.OCCUPATION_ENTREPRENEUR),
  (OCCUPATION_CTO, strings.OCCUPATION_CTO),
  (OCCUPATION_CEO, strings.OCCUPATION_CEO),
  (OCCUPATION_CONSULTANT, strings.OCCUPATION_CONSULTANT),
  (OCCUPATION_OTHER_TECHNICAL, strings.OCCUPATION_OTHER_TECHNICAL),
  (OCCUPATION_OTHER_UNIVERSITY, strings.OCCUPATION_OTHER_UNIVERSITY),
  (OCCUPATION_OTHER, strings.OCCUPATION_OTHER),
)

OCCUPATION_DICT = dict(OCCUPATION_TUPLE)
OCCUPATION_CHOICES = set([k for k,v in OCCUPATION_TUPLE])
