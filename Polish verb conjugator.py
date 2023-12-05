# personal pronouns
pronouns = ["(ja)", "(ty)", "(on/ona/ono)", "(my)", "(wy)", "(oni/one)"]

# << verb categories start here >>

# << -A- verbs category starts here >>

# pracować category
pracowac_suffix = ["uję", "ujesz", "uje", "ujemy", "ujecie", "ują"]


def pracowac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(pracowac_suffix):
        stem = word[:-4]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# stawać category
stawac_suffix = ["ję", "jesz", "je", "jemy", "jecie", "ją"]


def stawac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(stawac_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# brać category
brac_suffix = ["iorę", "ierzesz", "ierze", "ierzemy", "ierzecie", "iorą"]


def brac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(brac_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
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
    print("Present tense:\n")
    for pronoun, form in enumerate(przebrac_forms):
        print(pronouns[pronoun] + " " + form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zebrać category
zebrac_suffix = ["biorę", "bierzesz", "bierze", "bierzemy", "bierzecie", "biorą"]


def zebrac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(zebrac_suffix):
        stem = word[:-5]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# wezbrać category
wezbrac_suffix = ["zbiorę", "zbierzesz", "zbierze", "zbierzemy", "zbierzecie", "zbiorą"]


def wezbrac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(wezbrac_suffix):
        stem = word[:-6]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# żebrać category
zebrac_1_suffix = ["zę", "zesz", "ze", "zemy", "zecie", "zą"]


def zebrac_1(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(zebrac_1_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# stać category
stac_suffix = ["oję", "oisz", "oi", "oimy", "oicie", "oją"]


def stac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(stac_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# stanąć category
stanac_suffix = ["ę", "iesz", "ie", "iemy", "iecie", "ą"]
# this set of suffixes supports the ą:ę variation in the past tense
stanac_past_suffix = [
    "ąłem/-ęłam",
    "ąłeś/-ęłaś",
    "ął/-ęła/-ęło",
    "ęliśmy/-ęłyśmy",
    "ęliście/-ęłyście",
    "ęli/-ęły",
]


def stanac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(stanac_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# pisać category
pisac_suffix = ["zę", "zesz", "ze", "zemy", "zecie", "zą"]


def pisac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(pisac_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# kazać category
kazac_suffix = ["żę", "żesz", "że", "żemy", "żecie", "żą"]


def kazac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(kazac_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# kłamać category
klamac_suffix = ["ię", "iesz", "ie", "iemy", "iecie", "ią"]


def klamac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(klamac_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# jechać category
jechac_suffix = ["adę", "edziesz", "edzie", "edziemy", "edziecie", "adą"]


def jechac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(jechac_suffix):
        stem = word[:-5]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# płakać category
plakac_suffix = ["czę", "czesz", "cze", "czemy", "czecie", "czą"]


def plakac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(plakac_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# czytać category
czytac_suffix = ["m", "sz", "", "my", "cie", "ją"]
czytac_past_suffix = [
    "łem/-łam",
    "łeś/-łaś",
    "ł/-ła/-ło",
    "liśmy/-łyśmy",
    "liście/-łyście",
    "li/-ły",
]


def czytac(word):
    stem = word[:-1]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(czytac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# << -E- verbs category starts here >>

# umrzeć category
umrzec_suffix = ["ę", "zesz", "ze", "zemy", "zecie", "ą"]
umrzec_past_suffix = [
    "arłem/-arłam",
    "arłeś/-arłaś",
    "arł/-arła/-arło",
    "arliśmy/-arłyśmy",
    "arliście/-arłyście",
    "arli/-arły",
]


def umrzec(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(umrzec_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(umrzec_past_suffix):
        stem = word[:-4]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# jeść category
jesc_suffix = ["m", "sz", "", "my", "cie", "dzą"]
jesc_past_suffix = [
    "adłem/-adłam",
    "adłeś/-adłaś",
    "adł/-adła/-adło",
    "edliśmy/-adłyśmy",
    "edliście/-adłyście",
    "edli/-adły",
]


def jesc(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(jesc_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(jesc_past_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# wziąć category
wziac_suffix = ["ezmę", "eźmiesz", "eźmie", "eźmiemy", "eźmiecie", "ezmą"]


def wziac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(wziac_suffix):
        stem = word[:-4]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# -jąć category
jac_suffix = ["mę", "miesz", "mie", "miemy", "miecie", "mą"]


def jac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(jac_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zżąć exception
zzac_suffix = ["zeżnę", "zeżniesz", "zeżnie", "zeżniemy", "zeżniecie", "zeżną"]


def zzac(word):
    print("Present tense:\n")
    for pronoun, form in enumerate(zzac_suffix):
        print(pronouns[pronoun] + " " + form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# patrzeć category
patrzec_suffix = ["ę", "ysz", "y", "ymy", "ycie", "ą"]
# this set of suffixes supports the -y- conjugation in the past tense
patrzec_past_suffix = [
    "yłem/-łam",
    "yłeś/-łaś",
    "ył/-ła/-ło",
    "yliśmy/-łyśmy",
    "yliście/-łyście",
    "yli/-yły",
]


def patrzec(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(patrzec_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(patrzec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# drżeć category


def drzec(word):
    stem = word[:-2]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(patrzec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# rozumieć category
rozumiec_suffix = ["m", "sz", "", "my", "cie", "ją"]


def rozumiec(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(rozumiec_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(miec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# wieść category
wiesc_suffix = ["odę", "edziesz", "edzie", "edziemy", "edziecie", "odą"]
# this set of suffixes supports the -eść verb category in the past tense
wiesc_past_suffix = [
    "odłem/-łam",
    "odłeś/-łaś",
    "ódł/-odła/-odło",
    "edliśmy/-edłyśmy",
    "edliście/-edłyście",
    "edli/-edły",
]


def wiesc(word):
    stem = word[:-3]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(wiesc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(wiesc_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# wieźć category
wiezc_suffix = ["ozę", "eziesz", "ezie", "eziemy", "eziecie", "ozą"]
wiezc_past_suffix = [
    "ozłem/-łam",
    "ozłeś/-łaś",
    "ózł/-ozła/-ozło",
    "eźliśmy/-ozłyśmy",
    "eźliście/-ozłyście",
    "eźli/-ozły",
]


def wiezc(word):
    stem = word[:-3]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(wiezc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(wiezc_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zapomnieć category
zapomniec_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]


def zapomniec(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(zapomniec_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# myśleć category
myslec_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]


def myslec(word):
    stem = word[:-2]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(myslec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# mleć category
mlec_forms = ["mielę", "mielesz", "miele", "mielemy", "mielecie", "mielą"]
mlec_past_forms = [
    "mełłem/-am",
    "mełłeś/-aś",
    "mełł/-a/-o",
    "mełliśmy/-łyśmy",
    "mełliscie/-łyście",
    "mełli/-ły",
]


def mlec(word):
    print("Present tense:\n")
    for pronoun, form in enumerate(mlec_forms):
        print(pronouns[pronoun] + " " + form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, form in enumerate(mlec_past_forms):
        print(pronouns[pronoun] + " " + form)


# chcieć category
chciec_suffix = ["ę", "esz", "e", "emy", "ecie", "ą"]
chciec_past_suffix = [
    "ałem/-łam",
    "ałeś/-łaś",
    "ał/-ła/-ło",
    "eliśmy/-ałyśmy",
    "eliście/-ałyście",
    "eli/-ały",
]


def chciec(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(chciec_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# kraść category
krasc_suffix = ["dnę", "dniesz", "dnie", "dniemy", "dniecie", "dną"]
krasc_past_suffix = [
    "dłem/-łam",
    "dłeś/-łaś",
    "dł/-a/-o",
    "dliśmy/-łyśmy",
    "dliście/-łyście",
    "dli/-ły",
]


def krasc(word):
    stem = word[:-2]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(krasc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(krasc_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# mieć exception
miec_suffix = ["am", "asz", "a", "amy", "acie", "ają"]
# this set of suffixes supports the -E- verb category in the past tense
miec_past_suffix = [
    "ałem/-łam",
    "ałeś/-łaś",
    "ał/-ła/-ło",
    "eliśmy/-ałyśmy",
    "eliście/-ałyście",
    "eli/-ały",
]


def miec(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(miec_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(miec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# wiedzieć exception
wiedziec_suffix = ["m", "sz", "", "my", "cie", "dzą"]


def wiedziec(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(wiedziec_suffix):
        stem = word[:-5]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# nieść category
niesc_suffix = ["osę", "esiesz", "esie", "esiemy", "esiecie", "osą"]
niesc_past_suffix = [
    "osłem/-łam",
    "osłeś/-łaś",
    "ósł/-osła/-osło",
    "eśliśmy/-osłyśmy",
    "eśliście/-osłyście",
    "eśli/-osły",
]


def niesc(word):
    stem = word[:-3]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(niesc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(niesc_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# trząść exception
trzasc_suffix = ["ęsę", "ęsiesz", "ęsie", "ęsiemy", "ęsiecie", "ęsą"]
trzasc_past_suffix = [
    "ąsłem/-ęsłam",
    "ąsłeś/-ęsłaś",
    "ąsł/-ęsła/-ęsło",
    "ęśliśmy/-słyśmy",
    "ęśliście/-słyście",
    "ęśli/-sły",
]


def trzasc(word):
    stem = word[:-3]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(trzasc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(trzasc_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# pleść category
plesc_suffix = ["otę", "eciesz", "ecie", "eciemy", "eciecie", "otą"]
plesc_past_suffix = [
    "otłem/-łam",
    "otłeś/-łaś",
    "ótł/-otła/-otło",
    "etliśmy/-otłyśmy",
    "etliście/-otłyście",
    "etli/-otły",
]


def plesc(word):
    stem = word[:-3]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(plesc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(plesc_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# wleźć category
wlezc_suffix = ["zę", "ziesz", "zie", "ziemy", "ziecie", "zą"]
wlezc_past_suffix = [
    "azłem/-łam",
    "azłeś/-łaś",
    "azł/-ła/-ło",
    "eźliśmy/-azłyśmy",
    "eźliście/-azłyście",
    "eźli/-azły",
]


def wlezc(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(wlezc_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(wlezc_past_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# grząźć exception
grzazc_suffix = ["ęzę", "ęziesz", "ęzie", "ęziemy", "ęziecie", "ęzą"]
grzazc_past_suffix = [
    "ązłem/-ęzłam",
    "ązłeś/-ęzłaś",
    "ązł/-ęzła/-ęzło",
    "ęźliśmy/-ęzłyśmy",
    "ęźliście/-ęzłyście",
    "ęźli/-ęzły",
]


def grzazc(word):
    stem = word[:-3]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(grzazc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(grzazc_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# biec category
biec_suffix = ["gnę", "gniesz", "gnie", "gniemy", "gniecie", "gną"]
biec_past_suffix = [
    "głem/-am",
    "głeś/-aś",
    "gł/-a/-o",
    "gliśmy/-łyśmy",
    "gliście/-łyście",
    "gli/-ły",
]


def biec(word):
    stem = word[:-1]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(biec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(biec_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# piec category
piec_suffix = ["kę", "czesz", "cze", "czemy", "czecie", "ką"]
piec_past_suffix = [
    "kłem/-łam",
    "kłeś/-łaś",
    "kł/-ła/-ło",
    "kliśmy/-łyśmy",
    "kliście/-łyście",
    "kli/-ły",
]


def piec(word):
    stem = word[:-1]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(piec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(piec_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# piec category
wlec_suffix = ["okę", "eczesz", "ecze", "eczemy", "eczecie", "oką"]
wlec_past_suffix = [
    "okłem/-łam",
    "okłeś/-łaś",
    "ókł/-okła/-okło",
    "ekliśmy/-okłyśmy",
    "ekliście/-okłyście",
    "ekli/-okły",
]


def wlec(word):
    stem = word[:-2]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(wlec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(wlec_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# móc category
moc_suffix = ["ogę", "ożesz", "oże", "ożemy", "ożecie", "ogą"]
moc_past_suffix = [
    "ogłem/-łam",
    "ogłeś/-łaś",
    "ógł/-ogła/-ogło",
    "ogliśmy/-łyśmy",
    "ogliście/-łyście",
    "ogli/-ły",
]


def moc(word):
    stem = word[:-2]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(moc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(moc_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# strzyc category
strzyc_suffix = ["gę", "żesz", "że", "żemy", "żecie", "gą"]


def strzyc(word):
    stem = word[:-1]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(strzyc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(biec_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# << -I-/-Y- category starts here >>

# tworzyć category
tworzyc_suffix = ["ę", "ysz", "y", "ymy", "ycie", "ą"]


def tworzyc(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(tworzyc_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# pić category
pic_suffix = ["ję", "jesz", "je", "jemy", "jecie", "ją"]


def pic(word):
    stem = word[:-1]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(pic_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# piać exception
piac_suffix = ["eję", "ejesz", "eje", "ejemy", "ejecie", "eją"]


def piac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(piac_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# chodzić category
chodzic_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]


def chodzic(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(chodzic_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# cierpieć exception
cierpiec_suffix = ["ę", "sz", "", "my", "cie", "ą"]


def cierpiec(word):
    stem = word[:-2]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(cierpiec_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# nosić category
nosic_suffix = ["zę", "isz", "i", "imy", "icie", "zą"]


def nosic(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(nosic_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zlecić category
def zlecic(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(zapomniec_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# musieć category
musiec_suffix = ["zę", "isz", "i", "imy", "icie", "zą"]


def musiec(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(musiec_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# czyścić category
czyscic_suffix = ["szczę", "ścisz", "ści", "ścimy", "ścicie", "szczą"]


def czyscic(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(czyscic_suffix):
        stem = word[:-4]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# robić category
robic_suffix = ["ę", "sz", "", "my", "cie", "ą"]
robic_past_suffix = [
    "łem/-łam",
    "łeś/-łaś",
    "ł/-ła/-ło",
    "liśmy/-łyśmy",
    "liście/-łyście",
    "li/-ły",
]


def robic(word):
    stem = word[:-1]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(robic_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# być exception
byc_forms = ["jestem", "jesteś", "jest", "jesteśmy", "jesteście", "są"]


def byc(word):
    print("Present tense:\n")
    for pronoun, form in enumerate(byc_forms):
        print(pronouns[pronoun] + " " + form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# -być exception
bede_forms = ["ędę", "ędziesz", "ędzie", "ędziemy", "ędziecie", "ędą"]


def bede(word):
    print("Present tense:\n")
    stem = word[:-2]
    for pronoun, suffix in enumerate(bede_forms):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# prząść exception
przasc_suffix = ["ędę", "ędziesz", "ędzie", "ędziemy", "ędziecie", "ędą"]


def przasc(word):
    stem = word[:-3]
    for pronoun, suffix in enumerate(bede_forms):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# spać exception
spac_forms = ["śpię", "śpisz", "śpi", "śpimy", "śpicie", "śpią"]


def spac(word):
    stem = word[:-1]
    print("Present tense:\n")
    for pronoun, form in enumerate(spac_forms):
        print(pronouns[pronoun] + " " + form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# iść/-jść category

isc_suffix = ["dę", "dziesz", "dzie", "dziemy", "dziecie", "dą"]
isc_past_forms = [
    "szedłem/szłam",
    "szedłeś/szłaś",
    "szedł/szła/szło",
    "szliśmy/szłyśmy",
    "szliście/szłyście",
    "szli/szły",
]
isc_past_suffix = [
    "szedłem/-szłam",
    "szedłeś/-szłaś",
    "szedł/-szła/-szło",
    "szliśmy/-szłyśmy",
    "szliście/-szłyście",
    "szli/-szły",
]

isc_ej_past_suffix = [
    "szedłem/-eszłam",
    "szedłeś/-eszłaś",
    "szedł/-eszła/-eszło",
    "eszliśmy/-eszłyśmy",
    "eszliście/-eszłyście",
    "eszli/-eszły",
]


def isc(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(isc_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    stop_letter = "j"
    pojsc_exception = "ój"
    wejsc_exception = "ej"
    ujsc_exception = "uj"
    if stop_letter not in word:
        for pronoun, form in enumerate(isc_past_forms):
            print(pronouns[pronoun] + " " + form)
    else:
        if pojsc_exception in word:
            for pronoun, suffix in enumerate(isc_past_suffix):
                index_of_oj = word.index("ój")
                prefix = word[:index_of_oj]
                conjugated_form = prefix + "o" + suffix
                print(pronouns[pronoun] + " " + conjugated_form)
        elif wejsc_exception in word:
            for pronoun, suffix in enumerate(isc_ej_past_suffix):
                index_of_ej = word.index("ej")
                prefix = word[:index_of_ej]
                conjugated_form = prefix + suffix
                print(pronouns[pronoun] + " " + conjugated_form)
        else:
            for pronoun, suffix in enumerate(isc_past_suffix):
                index_of_j = word.index("j")
                prefix = word[:index_of_j]
                conjugated_form = prefix + suffix
                print(pronouns[pronoun] + " " + conjugated_form)


# jeździć exception
jezdzic_suffix = ["żdżę", "ździsz", "ździ", "ździmy", "ździcie", "żdżą"]


def jezdzic(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(jezdzic_suffix):
        stem = word[:-5]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# wstać exception
wstac_suffix = ["nę", "niesz", "nie", "niemy", "niecie", "ną"]


def wstac(word):
    stem = word[:-1]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(wstac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zacząć category
zaczac_suffix = ["nę", "niesz", "nie", "niemy", "niecie", "ną"]


def zaczac(word):
    stem = word[:-2]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(zaczac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zapiąć category
zapiac_suffix = ["nę", "niesz", "nie", "niemy", "niecie", "ną"]


def zapiac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(zapiac_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# -odpiąć category
odpiac_suffix = ["epnę", "epniesz", "epnie", "epniemy", "epniecie", "epną"]


def odpiac(word):
    print("Present tense:\n")
    for pronoun, suffix in enumerate(odpiac_suffix):
        stem = word[:-4]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# gryźć category
gryzc_suffix = ["zę", "ziesz", "zie", "ziemy", "ziecie", "zą"]
gryzc_past_suffix = [
    "złem/-łam",
    "złeś/-łaś",
    "zł/-ła/-ło",
    "źliśmy/-złyśmy",
    "źliście/-złyście",
    "źli/-zły",
]


def gryzc(word):
    stem = word[:-2]
    print("Present tense:\n")
    for pronoun, suffix in enumerate(gryzc_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(gryzc_past_suffix):
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
        word == "piać" or word == "piac" or word.endswith("lać") or word.endswith("lac")
    ):
        piac(word)  # piać, pieję
    elif (
        word.endswith("kazywać")
        or word.endswith("kazywac")
        or word.endswith("mazywać")
        or word.endswith("mazywac")
    ):
        pracowac(word)  # pokazywać, pokazuję
    elif (
        word.endswith("azywać")
        or word.endswith("azywac")
        or word.endswith("bywać")
        or word.endswith("bywac")
        or word.endswith("czywać")
        or word.endswith("czywac")
        or word.endswith("dzywać")
        or word.endswith("dzywac")
        or word.endswith("ezywac")
        or word.endswith("ezywać")
        or word.endswith("eżywać")
        or word.endswith("eżywac")
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
    elif word.endswith("azać") or word.endswith("azac"):
        kazac(word)  # kazać, każę
    elif word.endswith("rwać") or word.endswith("rwac"):
        stanac(word)  # urwać, urwę
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
    elif word.endswith("odpiąć") or word.endswith("odpiąc"):
        odpiac(word)  # odpiąć, odepnę
    elif (
        word.endswith("giąć")
        or word.endswith("giac")
        or word.endswith("miąć")
        or word.endswith("miąc")
        or word.endswith("piąć")
        or word.endswith("piąc")
    ):
        zapiac(word)  # zapiąć, zapnę
    elif (
        word.endswith("ziąć")
        or word.endswith("ziąc")
        or word.endswith("ziac")
        or word.endswith("ziać")
    ):
        wziac(word)  # wziąć, wezmę
    elif (
        word.endswith("cząć")
        or word.endswith("cząc")
        or word.endswith("czac")
        or word.endswith("czać")
    ):
        zaczac(word)  # zacząć, zacznę
    elif (
        word.endswith("wstać")
        or word.endswith("wstac")
        or word.endswith("astać")
        or word.endswith("astac")
        or word.endswith("dostać")
        or word.endswith("dostac")
        or word.endswith("zostać")
        or word.endswith("zostac")
    ):
        wstac(word)  # wstać, wstanę / zastać, zastanę
    elif word.endswith("stać") or word.endswith("stac"):
        stac(word)  # stać, stoję
    elif word.endswith("ynać") or word.endswith("ynac"):
        czytac(word)  # zaczynać, zaczynam
    elif word.endswith("nąć") or word.endswith("nąc"):
        stanac(word)  # stanąć, stanę
    elif word.endswith("ssać") or word.endswith("ssac"):
        stanac(word)  # ssać, ssę
    elif word.endswith("isać") or word.endswith("isac"):
        pisac(word)  # pisać, piszę
    elif word.endswith("szamać") or word.endswith("szamac"):
        czytac(word)  # szamać, szamam
    elif word.endswith("amać") or word.endswith("amac"):
        klamac(word)  # kłamać, kłamię
    elif (
        word.endswith("ebać")
        or word.endswith("ebac")
        or word.endswith("epać")
        or word.endswith("epac")
    ):
        klamac(word)  # klepać, klepię
    elif word.endswith("jechać") or word.endswith("jechac"):
        jechac(word)  # jechać, jadę, jedziesz
    elif (
        word.endswith("zżąć")
        or word.endswith("zżać")
        or word.endswith("zżąc")
        or word.endswith("zzac")
        or word.endswith("zząc")
        or word.endswith("zzać")
    ):
        zzac(word)  # zżąć, zeżnę
    elif word.endswith("jąć") or word.endswith("dąć") or word.endswith("żąć"):
        jac(word)  # pojąć, pojmę
    elif word == "gać" or word == "mać" or word == "nać":
        print("You entered a noun. Please enter a verb.")
    else:
        czytac(word)  # czytać, czytam

# This code conjugates verbs that end in -aść
elif word.endswith("aść") or word.endswith("asc"):
    krasc(word)  # kraść, kradnę

# This code conjugates verbs that end in -ąść
elif (
    word.endswith("siąść")
    or word.endswith("siasc")
    or word.endswith("siąsc")
    or word.endswith("siąśc")
    or word.endswith("siąsć")
):
    isc(word)  # posiąść, posiądę
elif word.endswith("prząść"):
    przasc(word)  # prząść, przędę
elif word.endswith("ąść") or word.endswith("ąśc") or word.endswith("ąsc"):
    trzasc(word)  # trząść, trzęsę

# This code conjugates verbs that end in -ąźć
elif word.endswith("grząźć"):
    grzazc(word)  # grząźć, grzęzę

# This code conjugates verbs that end in -eć
elif (
    word.endswith("eć")
    or word.endswith("ec")
    or word.endswith("eść")
    or word.endswith("esc")
    or word.endswith("eźć")
    or word.endswith("ezc")
):
    if (
        word.endswith("drzeć")
        or word.endswith("drzec")
        or word.endswith("mrzeć")
        or word.endswith("mrzec")
        or word.endswith("przeć")
        or word.endswith("przec")
    ):
        umrzec(word)  # umrzeć, umrę / podrzeć, podrę
    elif word.endswith("trzeć") or word.endswith("trzec"):
        patrzec(word)  # patrzeć, patrzę
    elif word.endswith("wiedzieć") or word.endswith("wiedziec"):
        wiedziec(word)  # powiedzieć, powiem
    elif word.endswith("jeść") or word.endswith("jesc"):
        jesc(word)  # jeść, jem
    elif word.endswith("rpieć") or word.endswith("rpiec"):
        cierpiec(word)  # cierpieć, cierpię
    elif word.endswith("biec") or word.endswith("ulec"):
        biec(word)  # biec, biegnę
    elif word == "kupiec":
        print("You entered a noun. Please enter a verb.")
    elif (
        word.endswith("piec")
        or word.endswith("rzec")
        or word.endswith("ciec")
        or word.endswith("siec")
    ):
        piec(word)  # piec, piekę
    elif (
        word.endswith("musieć")
        or word.endswith("musiec")
        or word.endswith("isieć")
        or word.endswith("isiec")
    ):
        musiec(word)  # musieć, muszę / wisieć, wiszę
    elif word.endswith("strzec"):
        strzyc(word)  # ustrzec, ustrzegę
    elif (
        word.endswith("czeć")
        or word.endswith("czec")
        or word.endswith("rzeć")
        or word.endswith("rzec")
        or word.endswith("szeć")
        or word.endswith("szec")
    ):
        patrzec(word)  # patrzeć, patrzę
    elif word.endswith("umieć") or word.endswith("umiec"):
        rozumiec(word)  # rozumieć, rozumiem
    elif word.endswith("wieść") or word.endswith("wiesc"):
        wiesc(word)  # wieść, wiodę
    elif word.endswith("wieźć") or word.endswith("wiezc"):
        wiezc(word)  # wieźć, wiozę
    elif word.endswith("gnieść") or word.endswith("gniesc"):
        plesc(word)  # gnieść, gniotę
    elif word.endswith("nieść") or word.endswith("niesc"):
        niesc(word)  # nieść, niosę
    elif word.endswith("pleść") or word.endswith("plesc"):
        plesc(word)  # pleść, plotę
    elif word.endswith("mnieć") or word.endswith("mniec"):
        zapomniec(word)  # zapomnieć, zapomnę
    elif word == "mleć" or word == "mlec":
        mlec(word)  # mleć, mielę
    elif word.endswith("leć"):
        myslec(word)  # myśleć, myślę
    elif word.endswith("lec"):
        wlec(word)  # wlec, wlokę
    elif word == "chcieć" or word == "chciec":
        chciec(word)  # chcieć, chcę
    elif word == "mieć" or word == "miec":
        miec(word)  # mieć, mam
    elif word == "wiedzieć" or word == "wiedziec":
        wiedziec(word)  # wiedzieć, wiem
    elif word.endswith("siedzieć") or word.endswith("siedziec"):
        zapomniec(word)  # siedzieć, siedzę
    elif word == "wleźć" or word == "wlezc":
        wlezc(word)  # wleźć, wlezę
    elif word.endswith("ecieć") or word.endswith("eciec"):
        zapomniec(word)  # lecieć, lecę
    elif (
        word.endswith("żeć")
        or word.endswith("żec")
        or word.endswith("zeć")
        or word.endswith("zec")
    ):
        drzec(word)  # drżę, drżysz
    else:
        chciec(word)  # chcieć, chcę

# This code conjugates verbs that end in -óc
elif word.endswith("moc") or word.endswith("móc"):
    moc(word)  # móc, mogę

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
        elif word.endswith("nić") or word.endswith("nic"):
            pic(word)  # gnić, gniję
        elif word == "tlić" or word == "tlic":
            myslec(word)  # tlić, tlę
        elif word == "kpić" or word == "kpic":
            robic(word)  # kpić, kpię
        elif word.endswith("pić") or word.endswith("pic"):
            pic(word)  # upić, upiję
    else:
        if (
            word.endswith("chybić")
            or word.endswith("chybic")
            or word.endswith("ubić")
            or word.endswith("ubic")
        ):
            robic(word)  # chybić, chybię
        elif (
            word.endswith("apić")
            or word.endswith("apic")
            or word.endswith("dobić")
            or word.endswith("dobic")
            or word.endswith("epić")
            or word.endswith("epic")
            or word.endswith("odbić")
            or word.endswith("odbic")
            or word.endswith("opić")
            or word.endswith("opic")
            or word.endswith("pobić")
            or word.endswith("pobic")
            or word.endswith("upić")
            or word.endswith("upic")
            or word.endswith("ybić")
            or word.endswith("ybic")
            or word.endswith("ypić")
            or word.endswith("ypic")
        ):
            pic(word)  # podbić, podbiję
        elif word == "zażyć":
            pic(word)  # zażyć, zażyję
        elif (
            word.endswith("ążyć")
            or word.endswith("azyc")
            or word.endswith("azyć")
            or word.endswith("ązyc")
            or word.endswith("ązyć")
            or word.endswith("ażyć")
            or word.endswith("ażyc")
        ):
            patrzec(word)  # dążyć, dążę
        elif word.endswith("asić") or word.endswith("asic"):
            nosic(word)  # grymasić, grymaszę
        elif (
            word.endswith("łożyć")
            or word.endswith("łożyc")
            or word.endswith("lożyć")
            or word.endswith("lozyć")
            or word.endswith("lożyc")
            or word.endswith("lozyc")
            or word.endswith("łozyc")
            or word.endswith("łozyć")
        ):
            patrzec(word)  # położyć, położę
        elif (
            word.endswith("dżyć")
            or word.endswith("dzyć")
            or word.endswith("dzyc")
            or word.endswith("dżyc")
        ):
            patrzec(word)  # dżdżyć, dżdżę / miażdżyć, miażdżę
        elif word.endswith("wić") or word.endswith("wic"):
            robic(word)  # bawić, bawię
        elif (
            word.endswith("żyć")
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
            pic(word)  # żyć, żyję
        elif word.endswith("być") or word.endswith("byc"):
            bede(word)  # zdobyć, zdobędę
        elif word.endswith("esić") or word.endswith("esic"):
            nosic(word)  # biesić, bieszę
        elif word.endswith("strzyc"):
            strzyc(word)  # strzyc, strzygę
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
        elif word.endswith("isić") or word.endswith("isic"):
            nosic(word)  # kisić, kiszę
        elif word.endswith("ścić") or word.endswith("scic"):
            czyscic(word)  # czyścić, czyszczę
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
        elif (
            word.endswith("elić")
            or word.endswith("elic")
            or word.endswith("ulić")
            or word.endswith("ulic")
            or word.endswith("alić")
            or word.endswith("alic")
            or word.endswith("odlić")
            or word.endswith("odlic")
            or word.endswith("olić")
            or word.endswith("olic")
            or word.endswith("tlić")
            or word.endswith("tlic")
            or word.endswith("ylić")
            or word.endswith("ylic")
        ):
            myslec(
                word
            )  # dzielić, dzielę / tulić, tulę / chwalić, chwalę / solić, solę / modlić, modlę
        elif word.endswith("czcić") or word.endswith("czcic"):
            nosic(word)  # czcić, czczę
        elif (
            word.endswith("cić")
            or word.endswith("cic")
            or word.endswith("dzić")
            or word.endswith("dzic")
        ):
            zlecic(word)  # płacić, płacę / budzić, budzę
        elif word.endswith("yć") or word.endswith("yc"):
            pic(word)  # ukryć, ukryję
        else:
            robic(word)  # robić, robię

# This code conjugates verbs that end in -uc/-uć
elif word.endswith("łuc"):
    piec(word)  # tłuc, tłukę
elif (
    word.endswith("nuć")
    or word.endswith("nuc")
    or word.endswith("żuć")
    or word.endswith("żuc")
    or word.endswith("zuć")
    or word.endswith("zuc")
):
    pic(word)  # żuć, żuję

# This code conjugates verbs that end in -yźć
elif word.endswith("gryźć") or word.endswith("gryzc"):
    gryzc(word)  # gryźć, gryzę

else:
    print("Try again.")

# checker ends here
