# personal pronouns
pronouns = ["(ja)", "(ty)", "(on/ona/ono)", "(my)", "(wy)", "(oni/one)"]

# << verb categories start here >>

# << -A- verbs category starts here >>

# pracować category
pracowac_suffix = ["uję", "ujesz", "uje", "ujemy", "ujecie", "ują"]

def pracowac(word):
    stem = word[:-4]
    for pronoun, suffix in enumerate(pracowac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# stawać category
stawac_suffix = ["ję", "jesz", "je", "jemy", "jecie", "ją"]

def stawac(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(stawac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# brać category
brac_suffix = ["iorę", "ierzesz", "ierze", "ierzemy", "ierzecie", "iorą"]

def brac(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(brac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# przebrać forms
przebrac_forms = [
    "przebiorę",
    "przebierzesz",
    "przebierze",
    "przebierzemy",
    "przebierzecie",
    "przebiorą",
]

def przebrac(word):
    for pronoun, form in enumerate(przebrac_forms):
        print(pronouns[pronoun] + " " + form)

# zebrać category
zebrac_suffix = ["biorę", "bierzesz", "bierze", "bierzemy", "bierzecie", "biorą"]

def zebrac(word):
    stem = word[:-5]
    for pronoun, suffix in enumerate(zebrac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# wezbrać category
wezbrac_suffix = ["zbiorę", "zbierzesz", "zbierze", "zbierzemy", "zbierzecie", "zbiorą"]

def wezbrac(word):
    stem = word[:-6]
    for pronoun, suffix in enumerate(wezbrac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# żebrać category
zebrac_1_suffix = ["zę", "zesz", "ze", "zemy", "zecie", "zą"]

def zebrac_1(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(zebrac_1_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# stać category
stac_suffix = ["oję", "oisz", "oi", "oimy", "oicie", "oją"]

def stac(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(stac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# stanąć category
stanac_suffix = ["ę", "iesz", "ie", "iemy", "iecie", "ą"]

def stanac(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(stanac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# pisać category
pisac_suffix = ["zę", "zesz", "ze", "zemy", "zecie", "zą"]

def pisac(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(pisac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# kłamać category
klamac_suffix = ["ię", "iesz", "ie", "iemy", "iecie", "ą"]

def klamac(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(klamac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# jechać category
jechac_suffix = ["adę", "edziesz", "edzie", "edziemy", "edziecie", "adą"]

def jechac(word):
    stem = word[:-5]
    for pronoun, suffix in enumerate(jechac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# płakać category
plakac_suffix = ["czę", "czesz", "cze", "czemy", "czecie", "czą"]

def plakac(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(plakac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# czytać category
czytac_suffix = ["m", "sz", "", "my", "cie", "ją"]

def czytac(word):
    stem = word[:-1]
    for pronoun, suffix in enumerate(czytac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# << -E- verbs category starts here >>

# umrzeć category
umrzec_suffix = ["ę", "zesz", "ze", "zemy", "zecie", "ą"]

def umrzec(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(umrzec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# jeść category
jesc_suffix = ["m", "sz", "", "my", "cie", "dzą"]

def jesc(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(jesc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# patrzeć category
patrzec_suffix = ["ę", "ysz", "y", "ymy", "ycie", "ą"]

def patrzec(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(patrzec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# rozumieć category
rozumiec_suffix = ["m", "sz", "", "my", "cie", "ją"]

def rozumiec(word):
    stem = word[:-1]
    for pronoun, suffix in enumerate(rozumiec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# wieść category
wiesc_suffix = ["odę", "edziesz", "edzie", "edziemy", "edziecie", "odą"]

def wiesc(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(wiesc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# wieźć category
wiezc_suffix = ["ozę", "eziesz", "ezie", "eziemy", "eziecie", "ozą"]

def wiezc(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(wiezc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# zapomnieć category
zapomniec_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]

def zapomniec(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(zapomniec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# myśleć category
myslec_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]

def myslec(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(myslec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# mleć category
mlec_forms = ["mielę", "mielesz", "miele", "mielemy", "mielecie", "mielą"]

def mlec(word):
    for pronoun, form in enumerate(mlec_forms):
        print(pronouns[pronoun] + " " + form)

# chcieć category
chciec_suffix = ["ę", "esz", "e", "emy", "ecie", "ą"]

def chciec(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(chciec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# mieć exception
miec_suffix = ["am", "asz", "a", "amy", "acie", "ają"]

def miec(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(miec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# wiedzieć exception
wiedziec_suffix = ["m", "sz", "", "my", "cie", "dzą"]

def wiedziec(word):
    stem = word[:-5]
    for pronoun, suffix in enumerate(wiedziec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# nieść category
niesc_suffix = ["osę", "esiesz", "esie", "esiemy", "esiecie", "osą"]

def niesc(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(niesc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# pleść category
plesc_suffix = ["otę", "eciesz", "ecie", "eciemy", "eciecie", "otą"]

def plesc(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(plesc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# wleźć category
wlezc_suffix = ["zę", "ziesz", "zie", "ziemy", "ziecie", "zą"]

def wlezc(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(wlezc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# << -I-/-Y- category starts here >>

# tworzyć category
tworzyc_suffix = ["ę", "ysz", "y", "ymy", "ycie", "ą"]

def tworzyc(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(tworzyc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# pić category
pic_suffix = ["ję", "jesz", "je", "jemy", "jecie", "ją"]

def pic(word):
    stem = word[:-1]
    for pronoun, suffix in enumerate(pic_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# chodzić category
chodzic_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]

def chodzic(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(chodzic_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# nosić category
nosic_suffix = ["zę", "isz", "i", "imy", "icie", "zą"]

def nosic(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(nosic_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# musieć category
musiec_suffix = ["zę", "isz", "i", "imy", "icie", "zą"]

def musiec(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(musiec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# mielić category
mielic_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]

def mielic(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(mielic_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# robić category
robic_suffix = ["ę", "sz", "", "my", "cie", "ą"]

def robic(word):
    stem = word[:-1]
    for pronoun, suffix in enumerate(robic_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# być exception
byc_forms = ["jestem", "jesteś", "jest", "jesteśmy", "jesteście", "są"]

def byc(word):
    for pronoun, form in enumerate(byc_forms):
        print(pronouns[pronoun] + " " + form)

# spać exception
spac_forms = ["śpię", "śpisz", "śpi", "śpimy", "śpicie", "śpią"]

def spac(word):
    for pronoun, form in enumerate(spac_forms):
        print(pronouns[pronoun] + " " + form)
    
# iść/-jść category

isc_suffix = ["dę", "dziesz", "dzie", "dziemy", "dziecie", "dą"]

def isc(word):
    stem = word[:-2]
    for pronoun, suffix in enumerate(isc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# jeździć exception
jezdzic_suffix = ["żdżę", "ździsz", "ździ", "ździmy", "ździcie", "żdżą"]

def jezdzic(word):
    stem = word[:-5]
    for pronoun, suffix in enumerate(jezdzic_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

wstac_suffix = ["nę", "niesz", "nie", "niemy", "niecie", "ną"]

def wstac(word):
    stem = word[:-1]
    for pronoun, suffix in enumerate(wstac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)

# << verb categories end here >>

# input form
word = input("Enter a Polish verb here (no 'się' necessary): ")

# << checker starts here >>

# This code conjugates verbs that end in -ać or -ąć
if (
    word.endswith("ać")
    or word.endswith("ac")
    or word.endswith("ąć")
    or word.endswith("ąc")
    or word.endswith("ać")
):
    if word == "bać" or word == "bac":
        stac(word)  # bać (się), boję (się)
    elif word == "spać" or word == "spac":
        spac(word)  # spać, śpię
    elif word.endswith("prać") or word.endswith("prac"):
        brac(word)  # prać, piorę
    elif word == "orać" or word == "orac":
        zebrac_1(word)  # orać, orzę
    elif (
        word.endswith("azywać")
        or word.endswith("azywac")
        or word.endswith("bywać")
        or word.endswith("bywac")
        or word.endswith("czywać")
        or word.endswith("czywac")
        or word.endswith("dzywać")
        or word.endswith("dzywac")
        or word.endswith("rywać")
        or word.endswith("rywac")
        or word.endswith("szywać")
        or word.endswith("szywac")
        or word.endswith("yzywać")
        or word.endswith("yzywac")
        or word.endswith("żywać")
        or word.endswith("żywac")
    ):
        czytac(word)
    elif (
        word.endswith("ować")
        or word.endswith("owac")
        or word.endswith("iwać")
        or word.endswith("iwac")
        or word.endswith("ywać")
        or word.endswith("ywac")
    ):
        pracowac(word)  # pracować, pracuję
    elif word.endswith("awać") or word.endswith("awac"):
        stawac(word)  # stawać, staję
    elif word.endswith("akać") or word.endswith("akac"):
        plakac(word)  # płakać, płaczę
    elif word == "przebrać" or word == "przebrac":
        przebrac(word)
    elif word.endswith("żebrać") or word.endswith("żebrac"):
        zebrac_1(word)  # żebrać, żebrzę
    elif word.endswith("zabrać") or word.endswith("zabrac"):
        brac(word)
    elif word.endswith("abrać") or word.endswith("abrac"):
        pisac(word)  # babrać, babrzę
    elif word.endswith("ebrać") or word.endswith("ebrac"):
        zebrac(word)  # zebrać, zbiorę
    elif word.endswith("ezbrać") or word.endswith("ezbrac"):
        wezbrac(word)  # wezbrać, wzbiorę
    elif word.endswith("brać") or word.endswith("brac"):
        brac(word)  # brać, biorę
    elif word.endswith("wstać") or word.endswith("wstac") or word.endswith("astać") or word.endswith("astac"):
        wstac(word)  #wstać, wstanę / zastać, zastanę
    elif word.endswith("stać") or word.endswith("stac"):
        stac(word)  # stać, stoję
    elif (
        word.endswith("nąć")
        or word.endswith("nąc")
        or word.endswith("nać")
        or word.endswith("nac")
    ):
        stanac(word)  # stanąć, stanę
    elif word.endswith("isać") or word.endswith("isac"):
        pisac(word)  # pisać, piszę
    elif word.endswith("amać") or word.endswith("amac"):
        klamac(word)  # kłamać, kłamię
    elif word.endswith("jechać") or word.endswith("jechac"):
        jechac(word)  # jechać, jadę, jedziesz
    else:
        czytac(word)  # czytać, czytam

# This code conjugates verbs that end in -eć
elif (
    word.endswith("eć")
    or word.endswith("ec")
    or word.endswith("eść")
    or word.endswith("esc")
    or word.endswith("eźć")
    or word.endswith("ezc")
):
    if word.endswith("mrzeć") or word.endswith("mrzec"):
        umrzec(word)  # umrzeć, umrę
    elif word.endswith("wiedzieć") or word.endswith("wiedziec"):
        wiedziec(word)  # powiedzieć, powiem
    elif word.endswith("jeść") or word.endswith("jesc"):
        jesc(word)  # jeść, jem
    elif word.endswith("musieć") or word.endswith("musiec") or word.endswith("isieć") or word.endswith("isiec"):
        musiec(word)  # musieć, muszę / wisieć, wiszę
    elif (
        word.endswith("czeć")
        or word.endswith("czec")
        or word.endswith("rzeć")
        or word.endswith("rzec")
    ):
        patrzec(word)  # patrzeć, patrzę
    elif word.endswith("umieć") or word.endswith("umiec"):
        rozumiec(word)  # rozumieć, rozumiem
    elif word.endswith("wieść") or word.endswith("wiesc"):
        wiesc(word)  # wieść, wiodę
    elif word.endswith("wieźć") or word.endswith("wiezc"):
        wiezc(word)  # wieźć, wiozę
    elif word.endswith("nieść") or word.endswith("niesc"):
        niesc(word)  # nieść, niosę
    elif word.endswith("pleść") or word.endswith("plesc"):
        plesc(word)  # pleść, plotę
    elif word.endswith("mnieć") or word.endswith("mniec"):
        zapomniec(word)  # zapomnieć, zapomnę
    elif word == "mleć" or word == "mlec":
        mlec(word)  # mleć, mielę
    elif word.endswith(("leć")) or word.endswith("lec"):
        myslec(word)  # myśleć, myślę
    elif word == "chcieć" or word == "chciec":
        chciec(word)  # chcieć, chcę
    elif word == "mieć" or word == "miec":
        miec(word)  # mieć, mam
    elif word == "wiedzieć" or word == "wiedziec":
        wiedziec(word)  # wiedzieć, wiem
    elif word == "wleźć" or word == "wlezc":
        wlezc(word)  # wleźć, wlezę
    else:
        chciec(word)  # chcieć, chcę

# This code conjugates verbs that end in -ić or -yć
elif (
    word.endswith("ić")
    or word.endswith("ic")
    or word.endswith("yć")
    or word.endswith("yc")
    or word.endswith("iść")
    or word.endswith("isc")
    or word.endswith("iśc")
    or word.endswith("isć")
    or word.endswith("jść")
    or word.endswith("jsc")
    or word.endswith("jśc")
    or word.endswith("jsć")
):
    if len(word) <= 3:
        if (
            word.endswith("ić")
            or word.endswith("ic")
            or word.endswith("żyć")
            or word.endswith("zyc")
            or word.endswith("myć")
            or word.endswith("myc")
            or word.endswith("ryć")
            or word.endswith("ryc")
            or word.endswith("tyc")
            or word.endswith("tyć")
            or word.endswith("wyć")
            or word.endswith("wyc")
        ):
            pic(word)  # pić, piję
        elif word == "być" or word == "byc":
            byc(word)  # być, jestem
        elif (
            word.endswith("iść")
            or word.endswith("isc")
            or word.endswith("iśc")
            or word.endswith("isć")
        ):
            isc(word)  # iść, idę
    elif len(word) <= 4:
        if word.endswith("szyć") or word.endswith("szyc"):
            pic(word)  # szyć, szyję
    else:
        if word.endswith("żyć"):
            pic(word)  # żyć, żyję
        elif (
            word.endswith("rzyć")
            or word.endswith("rzyc")
            or word.endswith("czyć")
            or word.endswith("czyc")
            or word.endswith("szyć")
            or word.endswith("szyc")
        ):
            tworzyc(word)
        elif word.endswith("odzić") or word.endswith("odzic"):
            chodzic(word)  # chodzić, chodzę
        elif (
            word.endswith("ździć")
            or word.endswith("zdzic")
            or word.endswith("ździc")
            or word.endswith("zdzić")
        ):
            jezdzic(word)
        elif word.endswith("osić") or word.endswith("osic"):
            nosic(word)  # nosić, noszę
        elif (
            word.endswith("iść")
            or word.endswith("isc")
            or word.endswith("iśc")
            or word.endswith("isć")
            or word.endswith("jść")
            or word.endswith("jsc")
            or word.endswith("jśc")
            or word.endswith("jsć")
        ):
            isc(word)  # iść, idę (pójść, pójdę)
        elif word.endswith("elić") or word.endswith("elic"):
            mielic(word)
        else:
            robic(word)  # robić, robię
else:
    print("Try again.")

# checker ends here
