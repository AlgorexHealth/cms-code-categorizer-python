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
  'category' : "Anesthesia",
  'individual_codes':  [],
  'code_ranges': [("00100","02020"),( "99100","99140")]
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
  'code_ranges': [("99281","99292")]
  },
  {
  'category' : "Immunizations/Injections",
  'individual_codes':  [],
  'code_ranges': [("90281","90749"),( "96360","96379"),( "G0008","G0010")]
  },
  {
  'category' : "Inpatient Visits",
  'individual_codes': [( "99477")],
  'code_ranges': [("99217","99239"),( "99304","99340"),( "99478","99480")]
  },
  {
  'category' : "Office Visits",
  'individual_codes':  [],
  'code_ranges': [("99201","99215"),( "99341","99350")]
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
  'code_ranges': [("99381","99387"),( "99391","99429"),( "99460","99464")]
  },
  {
  'category' : "Psychiatry & Biofeedback",
  'individual_codes':  [],
  'code_ranges': [("90801","90911")]
  },
  {
  'category' : "Radiology",
  'individual_codes':  [],
  'code_ranges': [("70010","79999"),( "R0070","R0076")]
  },
  {
  'category' : "Surgery",
  'individual_codes':  [],
  'code_ranges' : [("10021","36414"),("36417","69990"),("0016T","0222T")]
  },
  {
  'category' : "Other Professional Services",
  'individual_codes':  [( "99465"),( "99499")],
  'code_ranges': [("36415","36416"),
                  ( "90935","90999"),
                  ( "91000","91299"),
                  ( "92502","92700"),
                  ( "94002", "94799"),
                  ( "95250","95251"),
                  ( "95803","96125"),
                  ( "96150","96155"),
                  ( "96401","96571"),
                  ( "96900","96999"),
                  ( "98960","99091"),
                  ( "99143","99199"),
                  ( "99354","99360"),
                  ( "99363", "99380"),
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
    'code_ranges': [("99281","99292")]
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
                    ( "92950","93352"),
                    ( "93600","93799"),
                    ( "97001","98943"),
                    ( "A4651", "A4932"),
                    ( "E1500","E1699"),
                    ( "H0001","H2037")]
  },
  {
    'category': "Radiology Services",
    'individual_codes':[ ( "70336"),( "75635"),( "76390"),( "77084")],
    'code_ranges': [ ("70010","70332"),
                    ( "70350","70390"),
                    ( "70450","70498"),
                    ( "70540","70559"),
                    ( "71010", "71130"),
                    ( "72010","72120"),
                    ( "72170","72190"),
                    ( "71250","71275"),
                    ( "71550","71555"),
                    ( "72125", "72133"),
                    ( "72141","72159"),
                    ( "72191","72198"),
                    ( "72200","73140"),
                    ( "73200","73206"),
                    ( "73218", "73225"),
                    ( "73500","73660"),
                    ( "73700","73706"),
                    ( "73718","73725"),
                    ( "74000","74022"),
                    ( "74150", "74175"),
                    ( "74181","74185"),
                    ( "74190","74775"),
                    ( "75557","75564"),
                    ( "75600","75630"),
                    ( "75650","76350"),
                    ( "76376","76380"),
                    ( "76496","76499"),
                    ( "76506","76999"),
                    ( "77001", "77003"),
                    ( "77011","77014"),
                    ( "77021","77022"),
                    ( "77031","77059"),
                    ( "77071","77083"),
                    ( "77261","77799"),
                    ( "78000","79999"),
                    ( "96401", "96571"),
                    ( "R0070","R0076")]
  },
  {
    'category': "Lab/Pathology",
    'individual_codes' : [ "36415", "36416" ],
    'code_ranges' : [  ("80047","80440"), 
              ("80500","80502"), 
              ("81000","88399"), 
              ("88720","89356"), 
              ("ATP02","ATP22"), 
              ("P2028","P9615") ]
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
  #print(','.join([pid,claim,hcpc,amount,'"{0}"'.format(category)]) )

def process_outpatient_line(line):
  cols = line.split(',')
  pid = cols[0]
  claim = cols[1]
  amount = cols[2]
  hcpc = cols[3].strip()
  category = outpatient_categorizer_by_hcpc(hcpc)
  #print(','.join([pid,claim,amount,hcpc,'"{0}"'.format(category)]))

def process_inpatient_line(line):
  cols = line.split(',')
  pid = cols[0]
  claim = cols[1]
  amount = cols[2]
  drg = cols[3].strip()
  mdc_category = inpatient_mdc_category_by_drg(drg)
  inpatient_service_category = inpatient_service_category_by_drg(drg)
  #print(','.join([pid,claim,amount,drg,'"{0}"'.format(mdc_category),'"{0}"'.format(inpatient_service_category)]))

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
