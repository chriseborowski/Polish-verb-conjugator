#personal pronouns
pronouns = ["ja", "ty", "on/ona/ono", "my", "wy", "oni/one"]

#<< verb categories start here >>

#<< -A- verbs category starts here >>

#pracować category
pracowac_suffix = ["uję", "ujesz", "uje", "ujemy", "ujecie", "ują"]

def pracowac(word):
  stem = word[:-4]
  for suffix in pracowac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#brać category
brac_suffix = ["iorę", "ierzesz", "ierze", "ierzemy", "ierzecie", "iorą"]

def brac(word):
  stem = word[:-3]
  for suffix in brac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#zebrać category
zebrac_suffix = ["biorę", "bierzesz", "bierze", "bierzemy", "bierzecie", "biorą"]

def zebrac(word):
  stem = word[:-5]
  for suffix in zebrac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#stać category
stac_suffix = ["oję", "oisz", "oi", "oimy", "oicie", "oją"]

def stac(word):
  stem = word[:-2]
  for suffix in stac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#stanąć category
stanac_suffix = ["ę", "iesz", "ie", "iemy", "iecie", "ą"]

def stanac(word):
  stem = word[:-2]
  for suffix in stanac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#pisać category
pisac_suffix = ["zę", "zesz", "ze", "zemy", "zecie", "zą"]

def pisac(word):
  stem = word[:-2]
  for suffix in pisac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#kłamać category
klamac_suffix = ["ię", "iesz", "ie", "iemy", "iecie", "ą"]

def klamac(word):
  stem = word[:-2]
  for suffix in klamac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#jechać category
jechac_suffix = ["adę", "edziesz", "edzie", "edziemy", "edziecie", "adą"]

def jechac(word):
  stem = word[:-5]
  for suffix in jechac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#czytać category
czytac_suffix = ["m", "sz", "", "my", "cie", "ją"]

def czytac(word):
  stem = word[:-1]
  for suffix in czytac_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#<< -E- verbs category starts here >>

#umrzeć category
umrzec_suffix = ["ę", "zesz", "ze", "zemy", "zecie", "ą"]

def umrzec(word):
  stem = word[:-3]
  for suffix in umrzec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#jeść category
jesc_suffix = ["m", "sz", "", "my", "cie", "dzą"]

def jesc(word):
  stem = word[:-2]
  for suffix in jesc_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#patrzeć category
patrzec_suffix = ["ę", "ysz", "y", "ymy", "ycie", "ą"]

def patrzec(word):
  stem = word[:-2]
  for suffix in patrzec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#patrzeć category
rozumiec_suffix = ["m", "sz", "", "my", "cie", "ją"]

def rozumiec(word):
  stem = word[:-1]
  for suffix in rozumiec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#wieść category
wiesc_suffix = ["odę", "edziesz", "edzie", "edziemy", "edziecie", "odą"]

def wiesc(word):
  stem = word[:-3]
  for suffix in wiesc_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#wieźć category
wiezc_suffix = ["ozę", "eziesz", "ezie", "eziemy", "eziecie", "ozą"]

def wiezc(word):
  stem = word[:-3]
  for suffix in wiezc_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#zapomnieć category
zapomniec_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]

def zapomniec(word):
  stem = word[:-3]
  for suffix in zapomniec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#myśleć category
myslec_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]

def myslec(word):
  stem = word[:-2]
  for suffix in myslec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#mleć category
mlec_suffix = ["ielę", "ielesz", "iele", "ielemy", "ielecie", "ielą"]

def mlec(word):
  stem = word[:-3]
  for suffix in mlec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#chcieć category
chciec_suffix = ["ę", "esz", "e", "emy", "ecie", "ą"]

def chciec(word):
  stem = word[:-3]
  for suffix in chciec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#mieć exception
miec_suffix = ["am", "asz", "a", "amy", "acie", "ają"]

def miec(word):
  stem = word[:-3]
  for suffix in miec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#wiedzieć exception
wiedziec_suffix = ["m", "sz", "", "my", "cie", "dzą"]

def wiedziec(word):
  stem = word[:-5]
  for suffix in wiedziec_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#nieść category
niesc_suffix = ["osę", "esiesz", "esie", "esiemy", "esiecie", "osą"]

def niesc(word):
  stem = word[:-3]
  for suffix in niesc_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#pleść category
plesc_suffix = ["otę", "eciesz", "ecie", "eciemy", "eciecie", "otą"]

def plesc(word):
  stem = word[:-3]
  for suffix in plesc_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#<< -I-/-Y- category starts here >>

#tworzyć category
tworzyc_suffix = ["ę", "ysz", "y", "ymy", "ycie", "ą"]

def tworzyc(word):
  stem = word[:-2]
  for suffix in tworzyc_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#pić category
pic_suffix = ["ję", "jesz", "je", "jemy", "jecie", "ją"]

def pic(word):
  stem = word[:-1]
  for suffix in pic_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#chodzić category
chodzic_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]

def chodzic(word):
  stem = word[:-2]
  for suffix in chodzic_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#nosić category
nosic_suffix = ["zę", "isz", "i", "imy", "icie", "zą"]

def nosic(word):
  stem = word[:-2]
  for suffix in nosic_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#robić category
robic_suffix = ["ę", "sz", "", "my", "cie", "ą"]

def robic(word):
  stem = word[:-1]
  for suffix in robic_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#być exception
byc_forms = ["jestem", "jesteś", "jest", "jesteśmy", "jesteście", "są"]

def byc(word):
  for form in byc_forms:
    print(form)

#iść/-jść category

isc_suffix = ["dę", "dziesz", "dzie", "dziemy", "dziecie", "dą"]

def isc(word):
  stem = word[:-2]
  for suffix in isc_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#jeździć exception
jezdzic_suffix = ["żdżę", "ździsz", "ździ", "ździmy", "ździcie", "żdżą"]

def jezdzic(word):
  stem = word[:-5]
  for suffix in jezdzic_suffix:
    conjugated_form = stem + suffix
    print(conjugated_form)

#<< verb categories end here >>

#input form
word = input("Enter a Polish verb here (no 'się' necessary): ")

#<< checker starts here >>

if word.endswith("ać") or word.endswith("ac") or word.endswith("ąć") or word.endswith("ąc") or word.endswith("ać"):
  if word.endswith("żywać") or word.endswith("zywac") or word.endswith("żywac") or word.endswith("zywac"):
    czytac(word)
  elif word.endswith("ować") or word.endswith("owac") or word.endswith("iwać") or word.endswith("iwac") or word.endswith("ywać") or word.endswith("ywac"):
    pracowac(word) #pracować, pracuję
  elif word.endswith("ebrać") or word.endswith("ebrac"):
    zebrac(word) #zebrać, zbiorę
  elif word.endswith("brać") or word.endswith("brac"):
    brac(word) #brać, biorę
  elif word.endswith("stać") or word.endswith("stac"):
    stac(word) #stać, stoję
  elif word.endswith("nąć") or word.endswith("nąc") or word.endswith("nać") or word.endswith("nac"):
    stanac(word) #stanąć, stanę
  elif word.endswith("isać") or word.endswith("isac"):
    pisac(word) #pisać, piszę
  elif word.endswith("amać") or word.endswith("amac"):
    klamac(word) #kłamać, kłamię
  elif word.endswith("jechać") or word.endswith("jechac"):
    jechac(word) #jechać, jadę, jedziesz
  else:
    czytac(word) #czytać, czytam
elif word.endswith("eć") or word.endswith("ec") or word.endswith(
    "eść") or word.endswith("esc") or word.endswith(
    "eźć") or word.endswith("ezc"):
  if word.endswith("mrzeć") or word.endswith("mrzec"):
    umrzec(word) #umrzeć, umrę
  elif word.endswith("wiedzieć") or word.endswith("wiedziec"):
    wiedziec(word) #powiedzieć, powiem
  elif word.endswith("jeść") or word.endswith("jesc"):
    jesc(word) #jeść, jem
  elif word.endswith("czeć") or word.endswith("czec") or word.endswith(
"rzeć") or word.endswith("rzec"):
    patrzec(word) #patrzeć, patrzę
  elif word.endswith("umieć") or word.endswith("umiec"):
    rozumiec(word) #rozumieć, rozumiem
  elif word.endswith("wieść") or word.endswith("wiesc"):
    wiesc(word) #wieść, wiodę
  elif word.endswith("wieźć") or word.endswith("wiezc"):
    wiezc(word) #wieźć, wiozę
  elif word.endswith("nieść") or word.endswith("niesc"):
    niesc(word) #nieść, niosę
  elif word.endswith("pleść") or word.endswith("plesc"):
    plesc(word) #pleść, plotę
  elif word.endswith("mnieć") or word.endswith("mniec"):
    zapomniec(word) #zapomnieć, zapomnę
  elif word.endswith(("mleć")) or word.endswith("mlec"):
    mlec(word) #mleć, mielę
  elif word.endswith(("leć")) or word.endswith("lec"):
    myslec(word) #myśleć, myślę
  elif word == "chcieć" or word == "chciec":
    chciec(word) #chcieć, chcę
  elif word == "mieć" or word == "miec":
    miec(word)  #mieć, mam
  elif word == "wiedzieć" or word == "wiedziec":
    wiedziec(word)  #wiedzieć, wiem
  else:
    chciec(word)  #chcieć, chcę
elif word.endswith("ić") or word.endswith("ic") or word.endswith("yć") or word.endswith("yc") or word.endswith("iść") or word.endswith("isc") or word.endswith("iśc") or word.endswith("isć") or word.endswith("jść") or word.endswith("jsc") or word.endswith("jśc") or word.endswith("jsć"):
  if len(word) <= 3:
    if word.endswith("ić") or word.endswith("ic") or word.endswith("żyć") or word.endswith("zyc"):
      pic(word) #pić, piję
    elif word == "być" or word == "byc":
      byc(word) #być, jestem
    elif word.endswith("iść") or word.endswith("isc") or word.endswith("iśc") or word.endswith("isć"):
      isc(word) #iść, idę
  else:
    if word.endswith("żyć"):
      pic(word)
    elif word.endswith("rzyć") or word.endswith("rzyc"):
      tworzyc(word) #żyć, żyję
    elif word.endswith("odzić") or word.endswith("odzic"):
      chodzic(word) #chodzić, chodzę
    elif word.endswith("ździć") or word.endswith("zdzic") or word.endswith("ździc") or word.endswith("zdzić"):
      jezdzic(word)
    elif word.endswith("osić") or word.endswith("osic"):
      nosic(word) #nosić, noszę
    elif word.endswith("iść") or word.endswith("isc") or word.endswith("iśc") or word.endswith("isć") or word.endswith("jść") or word.endswith("jsc") or word.endswith("jśc") or word.endswith("jsć"):
      isc(word) #iść, idę (pójść, pójdę)
    else:
        robic(word) #robić, robię
else:
  print("Try again.")

#checker ends here