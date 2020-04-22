import functools as ft
import sys
import itertools as itertools

def r(first,second):
  (ls,vs,us) = first
  (l,v,u) = second
  ls.append(l)
  vs.append(v)
  us.append(u)
  return (ls,vs,us)

def arr_of_t_to_tuple_of_a(smaller):
  ret = ft.reduce(r,smaller,([],[],[]))
  return ret

def f(l,v,u):
  if l.isalpha() and u.isalpha():
    return l==v==u
  elif v.isalpha() and not l.isalpha() and not u.isalpha():
    return False
  else:
    return True

def c(l,v,u):
  if l.isalpha() and v.isalpha() and u.isalpha():
    return False
  else:
    return (l,v,u)

def look_for_alpha_mask(val,lowerupper):
  (lower,upper) = lowerupper
  # 1) first kick out values that are not within
  # the alpha lower/upper bounds. As an example:
  #  v= "10000" will be kicked out of a range of
  #     l="A1000" and u="A99999"
  does_val_fit = filter(lambda x: not x,map(f,lower,val,upper))
  if len(list(does_val_fit)) > 0:
    # and here is where we "kick out"
    return (False,(lower,val,upper))  

  # 2) secondly, remove the alphabet part and expose
  # just the numbering 
  #  As an example,  Z063PP as value possibly between
  #   Z003PP and Z903PP
  # will return the question: "Is 063 between 003 and 903?"
  smaller = filter(None,map(c,lower,val,upper))
  newlower,newval,newupper = arr_of_t_to_tuple_of_a(smaller)
  return (True,(newlower,newval,newupper))  

def normalize_val_and_ranges(val,lowerupper):
  (lower,upper) = lowerupper
  zs = itertools.zip_longest(
            reversed(lower),
            reversed(val),
            reversed(upper),fillvalue='0')
  newlower,newval,newupper = arr_of_t_to_tuple_of_a(reversed(list(zs)))
  return newval,(newlower,newupper)

# we assume that all three arguments are 5 in length
# which must be validated by calling functions
# we also assume that the lower and upper bounds are valid
#  (e.g.  ("ATP02","ATP02")  are valid while
#         ("0TP02","ATP02") are not
def is_in_range(val,lowerupper):
  (lower,upper) = lowerupper
  (nval,(nlower,nupper)) = normalize_val_and_ranges(val,(lower,upper))
  (c,(newlower,newval,newupper)) = look_for_alpha_mask(nval,(nlower,nupper))
  if not c:
    return False 
  zs = itertools.zip_longest(
            newlower,
            newval,
            newupper)
  determined_to_be_greater_than_lower_limit = False
  determined_to_be_less_than_upper_limit = False
  for (l,v,u) in zs:
    if v < l \
      and not determined_to_be_greater_than_lower_limit:
      # then we are under our bar
      return False
    if v > u \
      and not determined_to_be_less_than_upper_limit:
      # then we are over our bar
      return False
    if v > l:
      determined_to_be_greater_than_lower_limit = True
    if v < u:
      determined_to_be_less_than_upper_limit = True
  return True
   
def is_in_ranges(hcpc,ranges):
    for r in ranges :
      if is_in_range(hcpc,r):
        return True

################################################################################
# Matching Rules for DRG Inpatient Service 
#    as per:  
################################################################################
master_inpatientservice_rules_dictionary = [
	{
	'category': "Nervous system",
	'individual_codes':[],
	'code_ranges': [("020" , "103")]
	},
	{
	'category': "Eye",
	'individual_codes':[],
	'code_ranges': [("113" , "125")]
	},
	{
	'category': "Ear, Nose, Mouth & Throat",
	'individual_codes':[],
	'code_ranges': [("129" , "159")]
	},
	{
	'category': "Respiratory System",
	'individual_codes':[],
	'code_ranges': [("163" , "208")]
	},
	{
	'category': "Circulatory System",
	'individual_codes':[],
	'code_ranges': [("215" , "316")]
	},
	{
	'category': "Digestive System",
	'individual_codes':[],
	'code_ranges': [("326" , "395")]
	},
	{
	'category': "Hepatobiliary System & Pancreas",
	'individual_codes':[],
	'code_ranges': [("405" , "446")]
	},
	{
	'category': "Musculoskeletal System & Connective Tissue",
	'individual_codes':[],
	'code_ranges': [("453" , "566")]
	},
	{
	'category': "Skin, Subcutaneous Tissue & Breast",
	'individual_codes':[],
	'code_ranges': [("573" , "607")]
	},
	{
	'category': "Endocrine, Nutritional & Metabolic System",
	'individual_codes':[],
	'code_ranges': [("614" , "645")]
	},
	{
	'category': "Kidney & Urinary Tract",
	'individual_codes':[],
	'code_ranges': [("652" , "700")]
	},
	{
	'category': "Male Reproductive System",
	'individual_codes':[],
	'code_ranges': [("707" , "730")]
	},
	{
	'category': "Female Reproductive System",
	'individual_codes':[],
	'code_ranges': [("734" , "761")]
	},
	{
	'category': "Pregnancy; Childbirth",
	'individual_codes':["998"],
	'code_ranges': [("765" , "782") ]
	},
	{
	'category': "Newborns & Neonates (Perinatal Period)",
	'individual_codes':[],
	'code_ranges': [("789" , "795")]
	},
	{
	'category': "Blood, Blood Forming Organs & Immunological Disorders",
	'individual_codes':[],
	'code_ranges': [("799" , "816")]
	},
	{
	'category': "Myeloproliferative Diseases & Disorders",
	'individual_codes':[],
	'code_ranges': [("820" , "849")]
	},
	{
	'category': "Infectious & Parasitic Disease & Disorders",
	'individual_codes':[],
	'code_ranges': [("853" , "872")]
	},
	{
	'category': "Mental Diseases & Disorders",
	'individual_codes':[],
	'code_ranges': [("876" , "887")]
	},
	{
	'category': "Alcohol/Drug Use or Induced Mental Disorders",
	'individual_codes':[],
	'code_ranges': [("894" , "897")]
	},
	{
	'category': "Injuries, Poison & Toxic Effects of Drugs",
	'individual_codes':[],
	'code_ranges': [("901" , "923")]
	},
	{
	'category': "Burns",
	'individual_codes':[],
	'code_ranges': [("927" , "935")]
	},
	{
	'category': "Factors influencing Health Status",
	'individual_codes':[],
	'code_ranges': [("939" , "951")]
	},
	{
	'category': "Multiple Significant Trauma",
	'individual_codes':[],
	'code_ranges': [("955" , "965")]
	},
	{
	'category': "Human Immunodeficiency Virus Infections",
	'individual_codes':[],
	'code_ranges': [("969" , "977")]
	},
	{
	'category': "Transplants",
	'individual_codes':[],
	'code_ranges': [("001" , "013")]
	},
	{
	'category': "Extensive Procedures Unrelated to Principal Diagnosis",
	'individual_codes':["999"],
	'code_ranges': [("981" , "989") ]
	}
	]

################################################################################
# Matching Rules for DRG MDC 
#    as per:  
################################################################################
master_mdcinpatien_rules_dictionary = [
  {
  'category': "Medical",
  'individual_codes' : ["998"],
  'code_ranges' : [("52" , "103"),( "121" , "125"),( "146" , "159"),( "175" , "208"),( "280" , "316"),( "368" , "395"),( "432" , "446"),( "533" , "566"),( "592" , "607"),( "637" , "645"),( "682" , "700"),( "722" , "730"),( "754" , "761"),( "776" , "782"),( "808" , "816"),( "834" , "849"),( "862" , "872"),( "913" , "923"),( "933" , "935"),( "945" , "951"),( "963" , "965"),( "974" , "977") ]
  },
  {
  'category': "Surgical",
  'individual_codes' : ["769" , "770", "969" , "970"],
  'code_ranges' : [("1" , "13"),( "20" , "42"),( "113" , "117"),( "129" , "139"),( "163" , "168"),( "215" , "265"),( "326" , "358"),( "405" , "425"),( "453" , "517"),( "573" , "585"),( "614" , "630"),( "652" , "675"),( "707" , "718"),( "734" , "750"),( "799" , "804"),( "820" , "830"),( "853" , "858"),( "901" , "909"),( "927" , "929"),( "939" , "941"),( "955" , "959"),(  "981" , "989")]
  },
  {
  'category': "Deliveries , Newborns",
  'individual_codes' : ["774" , "775", "794" , "795"],
  'code_ranges' : [("765" , "768"),( "789" , "793")]
  },
  {
  'category': "Mental Health  Substance Abuse",
  'individual_codes' : ["876" ],
  'code_ranges' : [("880" , "887"),( "894" , "897")]
  },
]
################################################################################
# Matching Rules for HCPC Carriers 
#    as per:  
################################################################################

master_carrier_rules_dictionary = [
  {
  'category' : "Administered Drugs, including Chemo Drugs",
  'individual_codes':  [],
  'code_ranges': [("J0000","J9999")]
  },
  {
  'category' : "Allergy",
  'individual_codes':  [],
  'code_ranges': [("95004","95075"),( "95115","95199")]
  },
  {
  'category' : "Anesthesia: Head",
  'individual_codes':  [],
  'code_ranges': [("00100","00222")]
  },
    {
  'category' : "Anesthesia: Neck",
  'individual_codes':  [],
  'code_ranges': [("00300","00352")]
  },
    {
  'category' : "Anesthesia: Thorax",
  'individual_codes':  [],
  'code_ranges': [("00400","00474")]
  },
    {
  'category' : "Anesthesia: Intrathoracic",
  'individual_codes':  [],
  'code_ranges': [("00500","00580")]
  },
    {
  'category' : "Anesthesia: Spine and Spinal Cord",
  'individual_codes':  [],
  'code_ranges': [("00600","00670")]
  },
    {
  'category' : "Anesthesia: Upper Abdomen",
  'individual_codes':  [],
  'code_ranges': [("00700","00797")]
  },
    {
  'category' : "Anesthesia: Lower Abdomen",
  'individual_codes':  [],
  'code_ranges': [("00800","00882")]
  },
    {
  'category' : "Anesthesia: Perineum",
  'individual_codes':  [],
  'code_ranges': [("00902","00952")]
  },
    {
  'category' : "Anesthesia: Pelvis Except Hip",
  'individual_codes':  [],
  'code_ranges': [("01112","0110")]
  },
    {
  'category' : "Anesthesia: Upper Leg Except Knee",
  'individual_codes':  [],
  'code_ranges': [("01200","01274")]
  },
    {
  'category' : "Anesthesia: Knee and Popliteal Area",
  'individual_codes':  [],
  'code_ranges': [("01320","01444")]
  },
    {
  'category' : "Anesthesia: Lower Leg",
  'individual_codes':  [],
  'code_ranges': [("01462","01522")]
  },
    {
  'category' : "Anesthesia: Shoulder and Axillary",
  'individual_codes':  [],
  'code_ranges': [("01610", "01682")]
  },
      {
  'category' : "Anesthesia: Upper Arm and Elbow",
  'individual_codes':  [],
  'code_ranges': [("01710", "01782")]
  },
      {
  'category' : "Anesthesia: Forearm, Wrist and Hand",
  'individual_codes':  [],
  'code_ranges': [("01810", "01860")]
  },
      {
  'category' : "Anesthesia: Radiological Procedures",
  'individual_codes':  [],
  'code_ranges': [("01916", "01936")]
  },
      {
  'category' : "Anesthesia: Burn Excisions or Debridement",
  'individual_codes':  [],
  'code_ranges': [("01951", "01953")]
  },
      {
  'category' : "Anesthesia: Obstetric",
  'individual_codes':  [],
  'code_ranges': [("01958", "01969")]
  },
      {
  'category' : "Anesthesia: Other Procedures",
  'individual_codes':  [],
  'code_ranges': [("01990", "01999")]
  },
    {
  'category' : "Anesthesia: Qualifying circumstances for anesthesia",
  'individual_codes':  [],
  'code_ranges': [("99100", "99140")]
  },
    {
  'category' : "Anesthesia: Moderate (conscious) Sedation",
  'individual_codes':  [],
  'code_ranges': [("99143", "99150")]
  },
  {
  'category' : "Cardiovascular",
  'individual_codes':  [],
  'code_ranges': [("92950","93352"),( "93501","93581"),( "93600","93799"),( "93875","93990")]
  },
  {
  'category' : "Consultations",
  'individual_codes':  [],
  'code_ranges': [("99241","99255")]
  },
  {
  'category' : "Emergency Room/Critical Care",
  'individual_codes':  [],
  'code_ranges': [("99281","99292"),( "99466","99476")]
  },
    {
  'category' : "Medicine: Immune Globulins, Serum or Recombinant Prods",
  'individual_codes':  [],
  'code_ranges': [("90281","90399")]
  },
  {
  'category' : "Nursing Facility Services",
  'individual_codes':  [],
  'code_ranges': [("99304","99318")]
  },
    {
  'category' : "Domiciliary, rest home (boarding home) or custodial care services",
  'individual_codes':  [],
  'code_ranges': [("99324","99337")]
  },
    {
  'category' : "Domiciliary, rest home (assisted living facility), or home care plan oversight services	",
  'individual_codes':  [],
  'code_ranges': [("99339","99340")]
  },
    {
  'category' : "Medicine: Immunization Administration for vaccines/toxoids",
  'individual_codes':  [],
  'code_ranges': [("90465","90474")]
  },
    {
  'category' : "Medicine: Vaccines, Toxoids",
  'individual_codes':  [],
  'code_ranges': [("90476","90749")]
  },
    {
  'category' : "Medicine: Dialysis",
  'individual_codes':  [],
  'code_ranges': [("90935","90999")]
  },
    {
  'category' : "Medicine: Gastroenterology",
  'individual_codes':  [],
  'code_ranges': [("91000","91299")]
  },
    {
  'category' : "Medicine: Special Otorhinolaryngological Services",
  'individual_codes':  [],
  'code_ranges': [("92502","92700")]
  },
    {
  'category' : "Medicine: Noninvasive Vascular Diagnostic Studies",
  'individual_codes':  [],
  'code_ranges': [("93875","93990")]
  },
    {
  'category' : "Medicine: Pulmonary",
  'individual_codes':  [],
  'code_ranges': [("94002","90999")]
  },
   {
  'category' : "Medicine: Endocrinology",
  'individual_codes':  [],
  'code_ranges': [("95250","95251")]
  },
    {
  'category' : "Medicine: Neurology and Neuromuscular Procedures",
  'individual_codes':  [],
  'code_ranges': [("95803","96020")]
  },
    {
  'category' : "Medicine: Central Nervous System Assessments",
  'individual_codes':  [],
  'code_ranges': [("96101","96125")]
  },
    {
  'category' : "Medicine: Health and Behavior Assessment",
  'individual_codes':  [],
  'code_ranges': [("96150","96155")]
  },
    {
  'category' : "Medicine: hydration, therapeutic, prophylactic, diagnostic injections and infusions, and chemotherapy and other highly complex drug or highly complex biologic agent administration",
  'individual_codes':  [],
  'code_ranges': [("96360","96549")]
  },
    {
  'category' : "Medicine: Photodynamic Therapy",
  'individual_codes':  [],
  'code_ranges': [("96567","96571")]
  },
    {
  'category' : "Medicine: Special Dermatological Procedures",
  'individual_codes':  [],
  'code_ranges': [("96900","96999")]
  },
    {
  'category' : "Medicine: Medical Nutrition Therapy",
  'individual_codes':  [],
  'code_ranges': [("97802","97804")]
  },
    {
  'category' : "Medicine: Acupuncture",
  'individual_codes':  [],
  'code_ranges': [("97810","97814")]
  },
    {
  'category' : "Medicine: Osteopathic Manipulative Treatment",
  'individual_codes':  [],
  'code_ranges': [("98925","98929")]
  },
    {
  'category' : "Medicine: Chiropractic Manipulative Treatment",
  'individual_codes':  [],
  'code_ranges': [("98940","98943")]
  },
    {
  'category' : "Medicine: Education and training for patient self-managment",
  'individual_codes':  [],
  'code_ranges': [("98960","98962")]
  },
    {
  'category' : "Medicine: Non-face-to-face nonphysician services",
  'individual_codes':  [],
  'code_ranges': [("98966","98969")]
  },
    {
  'category' : "Medicine: Special Services, Procedures and Reports",
  'individual_codes':  [],
  'code_ranges': [("99000","99091")]
  },
    {
  'category' : "Medicine: Other Services and Procedures",
  'individual_codes':  [],
  'code_ranges': [("99170","99199")]
  },
  {
  'category' : "Inpatient Visits",
  'individual_codes': [( "99477")],
  'code_ranges': [("99217","99239")]
  },
  {
  'category' : "Office Visits",
  'individual_codes':  [],
  'code_ranges': [("99201","99215")]
  },
    {
  'category' : "Home Health Services",
  'individual_codes':  [],
  'code_ranges': [( "99341","99350")]
  },
   {
  'category' : "Prolonged Services",
  'individual_codes':  [],
  'code_ranges': [( "99354","99360")]
  },
   {
  'category' : "Ophthalmology",
  'individual_codes':  [],
  'code_ranges': [("92002","92499"),( "V2020","V2799")]
  },
  {
  'category' : "Pathology/Lab",
  'individual_codes':  [],
  'code_ranges': [("80047","89398"),( "P2028","P9615"),( "ATP02","ATP22")]
  },
  {
  'category' : "Physical Medicine",
  'individual_codes':  [],
  'code_ranges': [("97001","98943")]
  },
  {
  'category' : "Preventive Visits",
  'individual_codes':  [],
  'code_ranges': [("99381","99387"),( "99391","99429")]
  },
    {
  'category' : "Newborn Care Services",
  'individual_codes':  [],
  'code_ranges': [("99460","99465")]
  },
  {
  'category' : "Psychiatry & Biofeedback",
  'individual_codes':  [],
  'code_ranges': [("90801","90911")]
  },
  {
  'category' : "Radiology",
  'individual_codes':  [],
  'code_ranges': [( "R0070","R0076")]
  },
  {
  'category' : "Surgery: General",
  'individual_codes':  [],
  'code_ranges' : [("10000","10022")]
  },
    {
  'category' : "Surgery: Integumentary System",
  'individual_codes':  [],
  'code_ranges' : [("10040","19499")]
  },
    {
  'category' : "Surgery: Musculoskeletal System",
  'individual_codes':  [],
  'code_ranges' : [("20000","29999")]
  },
    {
  'category' : "Surgery: Respiratory System",
  'individual_codes':  [],
  'code_ranges' : [("30000","32999")]
  },
    {
  'category' : "Surgery: Cardiovascular System",
  'individual_codes':  [],
  'code_ranges' : [("33020","37799")]
  },
    {
  'category' : "Surgery: Hemic and Lymphatic Systems",
  'individual_codes':  [],
  'code_ranges' : [("38100","38999")]
  },
    {
  'category' : "Surgery: Mediastinum and Diaphragm",
  'individual_codes':  [],
  'code_ranges' : [("39000","39599")]
  },
    {
  'category' : "Surgery: Digestive System",
  'individual_codes':  [],
  'code_ranges' : [("40490","49999")]
  },
    {
  'category' : "Surgery: Urinary System",
  'individual_codes':  [],
  'code_ranges' : [("50010","53899")]
  },
    {
  'category' : "Surgery: Male Genital System",
  'individual_codes':  [],
  'code_ranges' : [("54000","55899")]
  },
    {
  'category' : "Surgery: Reproductive System and Intersex",
  'individual_codes':  [],
  'code_ranges' : [("55920","55980")]
  },
    {
  'category' : "Surgery: Female Genital System",
  'individual_codes':  [],
  'code_ranges' : [("56405","58999")]
  },
    {
  'category' : "Surgery: Maternity Care and Delivery",
  'individual_codes':  [],
  'code_ranges' : [("59000","55980")]
  },
    {
  'category' : "Surgery: Endocrine System",
  'individual_codes':  [],
  'code_ranges' : [("60000","60699")]
  },
    {
  'category' : "Surgery: Nervous System",
  'individual_codes':  [],
  'code_ranges' : [("61000","64999")]
  },
    {
  'category' : "Surgery: Eye and Ocular Adnexa",
  'individual_codes':  [],
  'code_ranges' : [("65091","68899")]
  },
    {
  'category' : "Surgery: Auditory System",
  'individual_codes':  [],
  'code_ranges' : [("69000","69979")]
  },
    {
  'category' : "Anatomic Pathology (postmortem)",
  'individual_codes':  [],
  'code_ranges' : [("99363","99368")]
  },
    {
  'category' : "Care plan oversight services",
  'individual_codes':  [],
  'code_ranges' : [("99374","99380")]
  },
    {
  'category' : "Complex Chronic Care Coordination Services",
  'individual_codes':  [],
  'code_ranges' : [("99487","99489")]
  },
  {
  'category' : "Other Professional Services",
  'individual_codes':  [( "99465"),( "99499")],
  'code_ranges': [("36415","36416"),
                  ( "90935","90999"),
                  ( "91000","91299"),
                  ( "95803","96125"),
                  ( "96401","96571"),
                  ( "99143","99199"),
                  ( "99441","99444"),
                  ( "99450","99456"),
                  ( "99605", "99607"),
                  ( "B4034","B9999"),
                  ( "C1300","C9899"),
                  ( "D0120","D9999"),
                  ( "G0027", "G9142"),
                  ( "H0001","H2037"),
                  ( "M0064","M0301"),
                  ( "Q0035","Q9968"),
                  ( "S0012", "S9999"),
                  ( "T1000","T5999"),
                  ( "V5008","V5299"),
                  ( "V5336","V5364"),
                  ( "W0000","ZZZZZ")]
  }
]
  


################################################################################
# Matching Rules for HCPC Outpatient
#    as per:  
################################################################################

master_outpatient_rules_dictionary = [
  {
    'category' : "Emergency Room",
    'individual_codes':  [],
    'code_ranges': [("99281","99292"), ("99466","99476")]
  },
  {
    'category': "Outpatient Surgery",
    'individual_codes':  [],
    'code_ranges': [ ("10021","36410"),
                    ( "36420","58999"),
                    ( "60000", "69990"),
                    ( "93501","93581"),
                    ( "0016T","0198T")]
  },
  {   
    'category': "Observation",
    'individual_codes':  [],
    'code_ranges': [ ("99217","99220")]
  }, 
  {     
    'category': "Ambulance",
    'individual_codes':  [],
    'code_ranges': [ ("A0021","A0999")]
  },
  { 
    'category': "DME/Prosthetics/Supplies",
    'individual_codes':  [],
    'code_ranges': [ ("A4206","A5200"),
                    ( "A5500","A5513"),
                    ( "A6000", "A9999"),
                    ( "E0100","E8002"),
                    ( "K0001","K0899"),
                    ( "L0112","L4398"),
                    ( "L5000","L9900")]
  },
  {
    'category': "Home Health",
    'individual_codes':  [],
    'code_ranges': [ ("99500","99602")]
  },
  {
    'category': "Other Outpatient Services",
    'individual_codes':  [],
    'code_ranges': [ ("59000","59899"),
                    ( "90801","90899"),
                    ( "90935", "90999"),
                    ( "92626","92633"),
                    ( "93600","93799"),
                    ( "97001","98943"),
                    ( "A4651", "A4932"),
                    ( "E1500","E1699"),
                    ( "H0001","H2037")]
  },
  {
    'category': "Radiology Services: Diagnostic Radiology",
    'individual_codes':[],
    'code_ranges': [("70000","76499")]
  },
    {
    'category': "Radiology Services: Diagnostic Ultrasound",
    'individual_codes':[],
    'code_ranges': [("76500","76999")]
  },
    {
    'category': "Radiology Services: Radiologic Guidance",
    'individual_codes':[],
    'code_ranges': [("77001","77032")]
  },
    {
    'category': "Radiology Services: Breast Mammography",
    'individual_codes':[],
    'code_ranges': [("77051","77059")]
  },
    {
    'category': "Radiology Services: Bone/Joint Studies",
    'individual_codes':[],
    'code_ranges': [("77071","77084")]
  },
    {
    'category': "Radiology Services: Radiation Oncology",
    'individual_codes':[],
    'code_ranges': [("77261","77999")]
  },
    {
    'category': "Radiology Services: Nuclear Medicine",
    'individual_codes':[],
    'code_ranges': [("78000","79999")]
  },
  {
    'category': "Lab/Pathology: Organ or Disease-oriented Panels",
    'individual_codes' : [],
    'code_ranges' : [("80000","80076")]
  },
    {
    'category': "Lab/Pathology: Drug Testing",
    'individual_codes' : [],
    'code_ranges' : [("80100","80103")]
  },
    {
    'category': "Lab/Pathology: Therapeutic Drug Assays",
    'individual_codes' : [],
    'code_ranges' : [("80150","80299")]
  },
    {
    'category': "Lab/Pathology: Evocative/Suppression Testing",
    'individual_codes' : [],
    'code_ranges' : [("80400","80440")]
  },
    {
    'category': "Lab/Pathology: Consultations",
    'individual_codes' : [],
    'code_ranges' : [("80500","80502")]
  },
    {
    'category': "Lab/Pathology: Urinalysis",
    'individual_codes' : [],
    'code_ranges' : [("81000","81099")]
  },
    {
    'category': "Lab/Pathology: Chemistry",
    'individual_codes' : [],
    'code_ranges' : [("82000","84999")]
  },
    {
    'category': "Lab/Pathology: Hematology and Coagulation",
    'individual_codes' : [],
    'code_ranges' : [("85002","85999")]
  },
    {
    'category': "Lab/Pathology: Immunology",
    'individual_codes' : [],
    'code_ranges' : [("86000","86849")]
  },
    {
    'category': "Lab/Pathology: Transfusion Medicine",
    'individual_codes' : [],
    'code_ranges' : [("86850","86849")]
  },
    {
    'category': "Lab/Pathology: Microbiology",
    'individual_codes' : [],
    'code_ranges' : [("87001","87999")]
  },
    {
    'category': "Lab/Pathology: Anatomic Pathology (postmortem)",
    'individual_codes' : [],
    'code_ranges' : [("88000","88099")]
  },
    {
    'category': "Lab/Pathology: Cytopathology",
    'individual_codes' : [],
    'code_ranges' : [("88194","88199")]
  },
    {
    'category': "Lab/Pathology: Cytogenetic Studies",
    'individual_codes' : [],
    'code_ranges' : [("88230","88299")]
  },
    {
    'category': "Lab/Pathology: Surgical Pathology",
    'individual_codes' : [],
    'code_ranges' : [("88300","88399")]
  },
    {
    'category': "Lab/Pathology: In Vivo Lab Procedures",
    'individual_codes' : [],
    'code_ranges' : [("88720","88741")]
  },
    {
    'category': "Lab/Pathology: Other Procedures",
    'individual_codes' : [],
    'code_ranges' : [("89049","89240")]
  },
    {
    'category': "Lab/Pathology: Reproductive Medicine Procedures",
    'individual_codes' : [],
    'code_ranges' : [("89250","89398")]
  }
]
################################################################################

def ccr(master):
  for d in master:
    yield d['category'],d['individual_codes'],d['code_ranges']

def inpatient_mdc_category_by_drg(drg):
  f = categorizer_by_rules(master_mdcinpatien_rules_dictionary)
  return f(drg)

def inpatient_service_category_by_drg(drg):
  f = categorizer_by_rules(master_inpatientservice_rules_dictionary)
  return f(drg)

def carrier_categorizer_by_hcpc(hcpc):
  if len(hcpc) != 5:
    return "BADHCPCCODE"
  f = categorizer_by_rules(master_carrier_rules_dictionary)
  return f(hcpc)

def outpatient_categorizer_by_hcpc(hcpc):
  #sys.stdout.write(".")
  if len(hcpc) != 5:
    return "BADHCPCCODE"
  f = categorizer_by_rules(master_outpatient_rules_dictionary)
  return f(hcpc)

def categorizer_by_rules(rules):
  category_by_code = {}
  ranges_to_category = {}
  for (category,codes,ranges) in ccr(rules):
     for c in codes:
        category_by_code[c] = category
     for (l,u) in ranges:
        category_by_code[l] = category
        category_by_code[u] = category
     for r in ranges:
        ranges_to_category[r] = category
  def actual_categorizer(code):
    if code in category_by_code:
      return category_by_code[code]
    for wrange,category in ranges_to_category.items():
      if is_in_range(code,wrange):
        return category
    return "NOTFOUND"
  return actual_categorizer


################################################################################

def process_carrier_line(line):
  cols = line.split(',')
  pid = cols[0]
  claim = cols[1]
  hcpc = cols[2]
  amount = cols[3].strip()
  category = carrier_categorizer_by_hcpc(hcpc)
  print(','.join([pid,claim,hcpc,amount,'"{0}"'.format(category)]) )

def process_outpatient_line(line):
  cols = line.split(',')
  pid = cols[0]
  claim = cols[1]
  amount = cols[2]
  hcpc = cols[3].strip()
  category = outpatient_categorizer_by_hcpc(hcpc)
  print(','.join([pid,claim,amount,hcpc,'"{0}"'.format(category)]))

def process_inpatient_line(line):
  cols = line.split(',')
  pid = cols[0]
  claim = cols[1]
  amount = cols[2]
  drg = cols[3].strip()
  mdc_category = inpatient_mdc_category_by_drg(drg)
  inpatient_service_category = inpatient_service_category_by_drg(drg)
  print(','.join([pid,claim,amount,drg,'"{0}"'.format(mdc_category),'"{0}"'.format(inpatient_service_category)]))

def run_outpatient():
  file = open('test/data/outpatient-hcpc.csv', 'r')
  for line in file:
    process_outpatient_line(line)

def run_inpatient():
  file = open('test/data/inpatient-drg.csv','r')
  for line in file:
    process_inpatient_line(line)

def run_carrier():
  file = open('test/data/carrier-hcpc.csv', 'r')
  for line in file:
    process_carrier_line(line)

#run_carrier()
#run_outpatient()
#run_inpatient()

def test():
  print(carrier_categorizer_by_hcpc("0016T"), " and should be Surgery")
  print(carrier_categorizer_by_hcpc("00100"), " and should be Anesthesia")
  print(carrier_categorizer_by_hcpc("R0076"), " and should be Radiology")
  print('look_for_alpha_mask("01",("A0","A2"))" ----- >', look_for_alpha_mask("01",("A0","A2")))
  print('look_for_alpha_mask("A1",("A0","A2")) ----- >',look_for_alpha_mask("A1",("A0","A2")) )
  print('look_for_alpha_mask("A1Z",("A0Z","A2Z")) ----- >',look_for_alpha_mask("A1Z",("A0Z","A2Z")) )
  print('look_for_alpha_mask("A100Z",("A000Z","A222Z")) ----- >',look_for_alpha_mask("A100Z",("A000Z","A222Z")))
  print('is_in_range("12",("1","201")) -->' ,is_in_range("12",("1","201")))


if __name__ == "__main__": 
  test()
