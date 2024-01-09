# personal pronouns
pronouns = ["(ja)", "(ty)", "(on/ona/ono)", "(my)", "(wy)", "(oni/one)"]

# composite future auxiliary forms
auxiliaries = ["będę", "będziesz", "będzie", "będziemy", "będziecie", "będą"]

# This list include possible perfective prefixes for verbs
perfective_prefixes = [
    "do",
    "ob",
    "od",
    "omd",
    "omie",
    "omin",
    "oml",
    "omot",
    "omów",
    "omy",
    "ople",
    "ostrzec",
    "ostrzy",
    "otwo",
    "na",
    "po",
    "pój",
    "prze",
    "przy",
    "stwo",
    "u",
    "wlać",
    "wleź",
    "wy",
    "za",
    "zbu",
    "zg",
    "zjeś",
    "zl",
    "zr",
    "zwę",
    "zwię",
    "zż",
]

# << verb categories start here >>

# << -A- verbs category starts here >>

# pracować category
pracowac_suffix = ["uję", "ujesz", "uje", "ujemy", "ujecie", "ują"]


def pracowac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(pracowac_suffix):
            stem = word[:-4]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(pracowac_suffix):
            stem = word[:-4]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# zezować category


def zezowac(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, suffix in enumerate(pracowac_suffix):
        stem = word[:-4]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        print(pronouns[pronoun] + " " + auxiliary + " " + word)


# dać category
def dac(word):
    stem = word[:-1]
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(jesc_suffix):
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
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(miec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, suffix in enumerate(miec_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-1]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(czytac_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(czytac_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


def bywac(word):
    stem = word[:-1]

    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, suffix in enumerate(czytac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        print(pronouns[pronoun] + " " + auxiliary + " " + word)


# << -E- verbs category starts here >>

# brać category
brac_suffix = ["iorę", "ierzesz", "ierze", "ierzemy", "ierzecie", "iorą"]


def brac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(brac_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(brac_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# przebrać forms
def przebrac(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(brac_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zebrać category
zebrac_suffix = ["biorę", "bierzesz", "bierze", "bierzemy", "bierzecie", "biorą"]


def zebrac(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(zebrac_suffix):
        stem = word[:-5]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# wezbrać category
wezbrac_suffix = ["zbiorę", "zbierzesz", "zbierze", "zbierzemy", "zbierzecie", "zbiorą"]


def wezbrac(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(wezbrac_suffix):
        stem = word[:-6]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# żebrać category
zebrac_1_suffix = ["zę", "zesz", "ze", "zemy", "zecie", "zą"]


def zebrac_1(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(zebrac_1_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(zebrac_1_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# stanąć category
stanac_suffix = ["ę", "iesz", "ie", "iemy", "iecie", "ą"]
# this set of suffixes supports the ą:ę variation in the past tense
stanac_past_suffix = [
    "ąłem/-ęłam",
    "ąłeś/-ęłaś",
    "ął/-ęła/-ęło",
    "ęliśmy/-łyśmy",
    "ęliście/-łyście",
    "ęli/-ły",
]


def stanac(word):
    stem = word[:-2]
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(stanac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# -snąć category
snac_suffix = ["snę", "śniesz", "śnie", "śniemy", "śniecie", "sną"]


def snac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        stop_letter_s = word.index("s")
        prefix = word[:stop_letter_s]
        for pronoun, suffix in enumerate(snac_suffix):
            conjugated_form = prefix + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        stop_letter_s = word.index("s")
        prefix = word[:stop_letter_s]
        for pronoun, suffix in enumerate(snac_suffix):
            conjugated_form = prefix + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# pisać category
pisac_suffix = ["zę", "zesz", "ze", "zemy", "zecie", "zą"]


def pisac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(pisac_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(pisac_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# kazać category
kazac_suffix = ["żę", "żesz", "że", "żemy", "żecie", "żą"]


def kazac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(kazac_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(kazac_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# kłamać category
klamac_suffix = ["ię", "iesz", "ie", "iemy", "iecie", "ią"]


def klamac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(klamac_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(klamac_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# jechać category
jechac_suffix = ["adę", "edziesz", "edzie", "edziemy", "edziecie", "adą"]


def jechac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(jechac_suffix):
            stem = word[:-5]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(jechac_suffix):
            stem = word[:-5]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# płakać category
plakac_suffix = ["czę", "czesz", "cze", "czemy", "czecie", "czą"]


def plakac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(plakac_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(plakac_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# piać exception
piac_suffix = ["eję", "ejesz", "eje", "ejemy", "ejecie", "eją"]


def piac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(piac_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(piac_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# ciąć exception
def ciac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        if len(word) > 4:
            if word[0] == "ś":
                for pronoun, suffix in enumerate(wstac_suffix):
                    stem = "zet"
                    conjugated_form = stem + suffix
                    print(pronouns[pronoun] + " " + conjugated_form)
            else:
                for pronoun, suffix in enumerate(wstac_suffix):
                    stop_letter_c = word.index("c")
                    stem = word[:stop_letter_c] + "t"
                    conjugated_form = stem + suffix
                    print(pronouns[pronoun] + " " + conjugated_form)
        else:
            for pronoun, suffix in enumerate(wstac_suffix):
                stem = "t"
                conjugated_form = stem + suffix
                print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        if len(word) > 4:
            if word[0] == "ś":
                for pronoun, suffix in enumerate(wstac_suffix):
                    stem = "zet"
                    conjugated_form = stem + suffix
                    print(pronouns[pronoun] + " " + conjugated_form)
            else:
                for pronoun, suffix in enumerate(wstac_suffix):
                    stop_letter_c = word.index("c")
                    stem = word[:stop_letter_c] + "t"
                    conjugated_form = stem + suffix
                    print(pronouns[pronoun] + " " + conjugated_form)
        else:
            for pronoun, suffix in enumerate(wstac_suffix):
                stem = "t"
                conjugated_form = stem + suffix
                print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
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
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(isc_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
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
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(isc_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# kląć category


def klac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(wstac_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(wstac_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# pić category
pic_suffix = ["ję", "jesz", "je", "jemy", "jecie", "ją"]


def pic(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-1]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(pic_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(pic_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


def mdlec(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(pic_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(pic_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# prząść exception
przasc_suffix = ["ędę", "ędziesz", "ędzie", "ędziemy", "ędziecie", "ędą"]
przasc_past_suffix = [
    "ądłem/-ędłam",
    "ądłeś/-ędłaś",
    "ądł/-ędła/-ędło",
    "ędliśmy/-łyśmy",
    "ędliście/-łyście",
    "ędli/-ły",
]


def przasc(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-3]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(przasc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(bede_forms):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(przasc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(bede_forms):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# stawać category
stawac_suffix = ["ję", "jesz", "je", "jemy", "jecie", "ją"]


def stawac(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(czytac_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, suffix in enumerate(stawac_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(umrzec_past_suffix):
            stem = word[:-4]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(umrzec_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(umrzec_past_suffix):
            stem = word[:-4]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(umrzec_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# wstać exception
wstac_suffix = ["nę", "niesz", "nie", "niemy", "niecie", "ną"]


def wstac(word):
    stem = word[:-1]
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(wstac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zacząć category
zaczac_suffix = ["nę", "niesz", "nie", "niemy", "niecie", "ną"]


def zaczac(word):
    stem = word[:-2]
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(zaczac_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# zapiąć category
zapiac_suffix = ["nę", "niesz", "nie", "niemy", "niecie", "ną"]


def zapiac(word):
    stop_letter_w = "w"
    stop_letter_s = "s"
    nonbreakable_prefix_wy = "wy"
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    if nonbreakable_prefix_wy in word:
        for pronoun, suffix in enumerate(zapiac_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    elif stop_letter_w in word:
        for pronoun, suffix in enumerate(zapiac_suffix):
            stem = word[0] + "e" + word[1:2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    elif stop_letter_s in word:
        for pronoun, suffix in enumerate(zapiac_suffix):
            stem = "zep"
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        for pronoun, suffix in enumerate(zapiac_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)


# jeść category
jesc_suffix = ["m", "sz", "", "my", "cie", "dzą"]
jesc_past_suffix = [
    "adłem/-łam",
    "adłeś/-łaś",
    "adł/-ła/-ło",
    "edliśmy/-adłyśmy",
    "edliście/-adłyście",
    "edli/-adły",
]


def jesc(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(jesc_past_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(jesc_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(jesc_past_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(jesc_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# wziąć category
wziac_suffix = ["ezmę", "eźmiesz", "eźmie", "eźmiemy", "eźmiecie", "ezmą"]


def wziac(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(wziac_suffix):
        stem = word[:-4]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# -giąć category
def giac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(zapiac_suffix):
            stem = word[:-4]
            conjugated_form = stem + "eg" + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(zapiac_suffix):
            stem = word[:-4]
            conjugated_form = stem + "eg" + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# odpiąć category
odpiac_suffix = ["epnę", "epniesz", "epnie", "epniemy", "epniecie", "epną"]


def odpiac(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(odpiac_suffix):
        stem = word[:-4]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# uląc category
ulac_suffix = ["ęknę", "ękniesz", "ęknie", "ękniemy", "ękniecie", "ękną"]
ulac_past_suffix = [
    "ąkłem/-ękłam",
    "ąkłeś/-ękłaś",
    "ąkł/-ękła/-ękło",
    "ękliśmy/-łyśmy",
    "ękliście/-łyśmy",
    "ękli/-ły",
]


def ulac(word):
    stem = word[:-2]
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(ulac_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(ulac_suffix):
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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(gryzc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(gryzc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(gryzc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("Present tense:\n")
        for pronoun, suffix in enumerate(gryzc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# -jąć category
jac_suffix = ["mę", "miesz", "mie", "miemy", "miecie", "mą"]


def jac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(jac_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(jac_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# -djąć category


def zdjac(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(stanac_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(jac_suffix):
        stem = word[:-3]
        conjugated_form = stem + "ej" + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# -żąć category


def zac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        if word == "zżąć":
            print("\nPast tense (masc/fem/neut):\n")
            for pronoun, suffix in enumerate(stanac_past_suffix):
                conjugated_form = stem + suffix
                print(pronouns[pronoun] + " " + conjugated_form)
            print("\nFuture tense:\n")
            for pronoun, suffix in enumerate(zaczac_suffix):
                conjugated_form = stem[0] + "e" + stem[1] + suffix
                print(pronouns[pronoun] + " " + conjugated_form)
        else:
            print("\nPast tense (masc/fem/neut):\n")
            for pronoun, suffix in enumerate(stanac_past_suffix):
                conjugated_form = stem + suffix
                print(pronouns[pronoun] + " " + conjugated_form)
            print("\nFuture tense:\n")
            for pronoun, suffix in enumerate(zaczac_suffix):
                conjugated_form = stem + suffix
                print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(stanac_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(zaczac_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# rozumieć category
rozumiec_suffix = ["m", "sz", "", "my", "cie", "ją"]


def rozumiec(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(miec_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(rozumiec_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(miec_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(rozumiec_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-3]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(wiesc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(wiesc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(wiesc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(wiesc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-3]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(wiezc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(wiezc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(wiezc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(wiezc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# mleć category
mlec_forms = ["ielę", "ielesz", "iele", "ielemy", "ielecie", "ielą"]
mlec_past_forms = [
    "ełłem/-am",
    "ełłeś/-aś",
    "ełł/-a/-o",
    "ełliśmy/-łyśmy",
    "ełliscie/-łyście",
    "ełli/-ły",
]


def mlec(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-3]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(mlec_past_forms):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(mlec_forms):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(mlec_past_forms):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(mlec_forms):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(chciec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(chciec_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            stem = word[:-2]
            if pronoun < 2:
                participle = stem + "ał/chciała"
                print(pronouns[pronoun] + " " + auxiliary + " " + participle)
            elif pronoun == 2:
                participle = stem + "ał/chciała/chciało"
                print(pronouns[pronoun] + " " + auxiliary + " " + participle)
            else:
                participle = stem + "eli/chciały"
                print(pronouns[pronoun] + " " + auxiliary + " " + participle)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(krasc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(krasc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(krasc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(krasc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# wiedzieć exception
wiedziec_suffix = ["m", "sz", "", "my", "cie", "dzą"]


def wiedziec(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(wiedziec_suffix):
            stem = word[:-5]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(wiedziec_suffix):
            stem = word[:-5]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-3]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(niesc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(niesc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(niesc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(niesc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-3]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(trzasc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(trzasc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(trzasc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(trzasc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# siąść category
def siasc(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(jesc_past_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(isc_suffix):
        stem = word[:-2]
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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-3]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(plesc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(plesc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(plesc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(plesc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(wlezc_past_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(wlezc_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(wlezc_past_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(wlezc_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-3]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(grzazc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(grzazc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(grzazc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(grzazc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# zaprząc category
zaprzac_past_suffix = [
    "ągłem/-ęgłam",
    "ągłeś/-ęgłaś",
    "ągł/-ęgła/-ęgło",
    "ęgliśmy/-łyśmy",
    "ęgliście/-łyście",
    "ęgli/-ły",
]


def zaprzac(word):
    stem = word[:-2]
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(zaprzac_past_suffix):
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(strzyc_suffix):
        conjugated_form = stem + "ę" + suffix
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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-1]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(biec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(biec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(biec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(biec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-1]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(piec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(piec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(piec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(piec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# wlec category
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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(wlec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(wlec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(wlec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(wlec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(moc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(moc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(moc_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(moc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            stem = word[:-2]
            if pronoun < 2:
                participle = stem + "ógł/mogła"
                print(pronouns[pronoun] + " " + auxiliary + " " + participle)
            elif pronoun == 2:
                participle = stem + "ógł/mogła/mogło"
                print(pronouns[pronoun] + " " + auxiliary + " " + participle)
            else:
                participle = stem + "ogli/mogły"
                print(pronouns[pronoun] + " " + auxiliary + " " + participle)


# kłóć exception
kloc_suffix = ["olę", "olesz", "ole", "olemy", "olecie", "olą"]


def kloc(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(kloc_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(kloc_suffix):
            stem = word[:-3]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# strzyc category
strzyc_suffix = ["gę", "żesz", "że", "żemy", "żecie", "gą"]


def strzyc(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-1]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(biec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(strzyc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(biec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(strzyc_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# << -I-/-Y- verbs category starts here >>

# drżeć category


def drzec(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(patrzec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(patrzec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# myśleć category
myslec_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]


def myslec(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(myslec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(myslec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(patrzec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(patrzec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(patrzec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(patrzec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# stać category
stac_suffix = ["oję", "oisz", "oi", "oimy", "oicie", "oją"]


def stac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(stac_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(czytac_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(stac_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# tworzyć category
tworzyc_suffix = ["ę", "ysz", "y", "ymy", "ycie", "ą"]


def tworzyc(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(tworzyc_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(tworzyc_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# zapomnieć category
zapomniec_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]


def zapomniec(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, suffix in enumerate(zapomniec_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)


# chodzić category
chodzic_suffix = ["ę", "isz", "i", "imy", "icie", "ą"]


def chodzic(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, suffix in enumerate(chodzic_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        print(pronouns[pronoun] + " " + auxiliary + " " + word)


# cierpieć exception
cierpiec_suffix = ["ę", "sz", "", "my", "cie", "ą"]


def cierpiec(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-2]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(cierpiec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(chciec_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(cierpiec_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# nosić category


def nosic(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, suffix in enumerate(sic_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        print(pronouns[pronoun] + " " + auxiliary + " " + word)


# -sić category
sic_suffix = ["zę", "isz", "i", "imy", "icie", "zą"]


def sic(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(sic_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(sic_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# zlecić category
def zlecic(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(zapomniec_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(zapomniec_suffix):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# musieć category
musiec_suffix = ["zę", "isz", "i", "imy", "icie", "zą"]


def musiec(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(chciec_past_suffix):
        stem = word[:-2]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, suffix in enumerate(musiec_suffix):
        stem = word[:-3]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        stem = word[:-2]
        if pronoun < 2:
            participle = stem + "ał/musiała"
            print(pronouns[pronoun] + " " + auxiliary + " " + participle)
        elif pronoun == 2:
            participle = stem + "ał/musiała/musiało"
            print(pronouns[pronoun] + " " + auxiliary + " " + participle)
        else:
            participle = stem + "eli/musiały"
            print(pronouns[pronoun] + " " + auxiliary + " " + participle)


# czyścić category
czyscic_suffix = ["szczę", "ścisz", "ści", "ścimy", "ścicie", "szczą"]


def czyscic(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(czyscic_suffix):
            stem = word[:-4]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(czyscic_suffix):
            stem = word[:-4]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


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
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-1]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(robic_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nPresent tense:\n")
        for pronoun, suffix in enumerate(robic_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# być exception
byc_forms = ["jestem", "jesteś", "jest", "jesteśmy", "jesteście", "są"]


def byc(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, form in enumerate(byc_forms):
        print(pronouns[pronoun] + " " + form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        print(pronouns[pronoun] + " " + auxiliary)


# -być exception
bede_forms = ["ędę", "ędziesz", "ędzie", "ędziemy", "ędziecie", "ędą"]


def bede(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            stem = word[:-1]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, suffix in enumerate(bede_forms):
            stem = word[:-2]
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)


# spać exception
spac_forms = ["śpię", "śpisz", "śpi", "śpimy", "śpicie", "śpią"]


def spac(word):
    is_perfective = False
    for prefix in perfective_prefixes:
        if word.startswith(prefix):
            is_perfective = True
            break

    stem = word[:-1]

    if is_perfective:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("\nFuture tense:\n")
        for pronoun, form in enumerate(spac_forms):
            index_of_s = word.index("s")
            stem = word[:index_of_s]
            print(pronouns[pronoun] + " " + stem + form)
    else:
        print("\nPast tense (masc/fem/neut):\n")
        for pronoun, suffix in enumerate(robic_past_suffix):
            conjugated_form = stem + suffix
            print(pronouns[pronoun] + " " + conjugated_form)
        print("Present tense:\n")
        for pronoun, form in enumerate(spac_forms):
            print(pronouns[pronoun] + " " + form)
        print("\nFuture tense:\n")
        for pronoun, auxiliary in enumerate(auxiliaries):
            print(pronouns[pronoun] + " " + auxiliary + " " + word)


# jeździć exception
jezdzic_suffix = ["żdżę", "ździsz", "ździ", "ździmy", "ździcie", "żdżą"]


def jezdzic(word):
    print("\nPast tense (masc/fem/neut):\n")
    for pronoun, suffix in enumerate(robic_past_suffix):
        stem = word[:-1]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nPresent tense:\n")
    for pronoun, suffix in enumerate(jezdzic_suffix):
        stem = word[:-5]
        conjugated_form = stem + suffix
        print(pronouns[pronoun] + " " + conjugated_form)
    print("\nFuture tense:\n")
    for pronoun, auxiliary in enumerate(auxiliaries):
        print(pronouns[pronoun] + " " + auxiliary + " " + word)


# << verb categories end here >>

# input form
word = input("Enter a Polish verb here (no 'się' necessary): ")

# << checker starts here >>

# This code conjugates verbs that end in -ać or -ąc or -ąć
if (
    word.endswith("ać")
    or word.endswith("ac")
    or word.endswith("ąć")
    or word.endswith("ąc")
    or word.endswith("ać")
):
    if word == "bać" or word == "bac":
        stac(word)  # bać (się), boję (się)
    elif word.endswith("spać") or word.endswith("spac"):
        spac(word)  # spać, śpię
    elif word.endswith("wierać") or word.endswith("wierac"):
        bywac(word)  # zawierać, zawieram
    elif word.endswith("prać") or word.endswith("prac"):
        brac(word)  # prać, piorę
    elif word == "orać" or word == "orac":
        zebrac_1(word)  # orać, orzę
    elif (
        word.endswith("piać")
        or word.endswith("piac")
        or word.endswith("lać")
        or word.endswith("lac")
    ):
        piac(word)  # piać, pieję
    elif word.endswith("dać") or word.endswith("dac"):
        dac(word)  # dać, dam
    elif (
        word.endswith("kazywać")
        or word.endswith("kazywac")
        or word.endswith("mazywać")
        or word.endswith("mazywac")
    ):
        zezowac(word)  # pokazywać, pokazuję
    elif word.endswith("bywać") or word.endswith("bywac"):
        bywac(word)  # bywać, bywam
    elif (
        word.endswith("azywać")
        or word.endswith("azywac")
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
    elif word.endswith("ezować") or word.endswith("ezowac"):
        zezowac(word)  # zezować, zezuję
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
        przebrac(word)  # przebrać, przebiorę
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
    elif word.endswith("giąć") or word.endswith("giąc"):
        giac(word)  # zgiąć, zegnę
    elif (
        word.endswith("miąć")
        or word.endswith("miąc")
        or word.endswith("piąć")
        or word.endswith("piąc")
    ):
        zapiac(word)  # zapiąć, zapnę
    elif word.endswith("ciąć") or word.endswith("ciąc") or word.endswith("ciać"):
        ciac(word)  # ciąć, tnę
    elif word.endswith("rząc") or word.endswith("rzac"):
        zaprzac(word)  # zaprząc, zaprzęgę
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
    elif word.endswith("ląć"):
        klac(word)  # kląć, klnę
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
    elif (
        word.endswith("agać")
        or word.endswith("agac")
        or word.endswith("ijać")
        or word.endswith("ijac")
        or word.endswith("inać")
        or word.endswith("inac")
        or word.endswith("szać")
        or word.endswith("szac")
        or word.endswith("ynać")
        or word.endswith("ynac")
    ):
        bywac(word)  # zaczynać, zaczynam
    elif word.endswith("snąć") or word.endswith("snąc"):
        snac(word)  # zasnąć, zasnę
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
        or word.endswith("opać")
        or word.endswith("opac")
    ):
        klamac(word)  # klepać, klepię
    elif word.endswith("jechać") or word.endswith("jechac"):
        jechac(word)  # jechać, jadę, jedziesz
    elif (
        word.endswith("żąć")
        or word.endswith("żać")
        or word.endswith("żąc")
        or word.endswith("zac")
        or word.endswith("ząc")
        or word.endswith("zać")
    ):
        zac(word)  # użąć, użnę
    elif (
        word.endswith("bjąć")
        or word.endswith("bjąc")
        or word.endswith("bjać")
        or word.endswith("djąć")
        or word.endswith("djać")
        or word.endswith("djąc")
        or word.endswith("djac")
    ):
        zdjac(word)  # zdjąć, zdejmę
    elif word.endswith("jąć") or word.endswith("dąć") or word.endswith("żąć"):
        jac(word)  # pojąć, pojmę
    elif word == "gać" or word == "mać" or word == "nać":
        print("You entered a noun. Please enter a verb.")
    elif word.endswith("ąc"):
        ulac(word)  # uląc, ulęknę
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
    siasc(word)  # posiąść, posiądę
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
        or word.endswith("wrzeć")
        or word.endswith("wrzec")
    ):
        umrzec(word)  # umrzeć, umrę / podrzeć, podrę
    elif word.endswith("trzeć"):
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
    elif word.endswith("piec") or word.endswith("ciec") or word.endswith("siec"):
        piec(word)  # piec, piekę
    elif (
        word.endswith("musieć")
        or word.endswith("musiec")
        or word.endswith("isieć")
        or word.endswith("isiec")
    ):
        musiec(word)  # musieć, muszę / wisieć, wiszę
    elif word.endswith("trzec"):
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
    elif word.endswith("mieść") or word.endswith("mieśc") or word.endswith("miesć"):
        plesc(word)  # mieść, miotę
    elif word.endswith("mnieć") or word.endswith("mniec"):
        zapomniec(word)  # zapomnieć, zapomnę
    elif word.endswith("dleć") or word.endswith("dlec"):
        mdlec(word)  # mdleć, mdleję
    elif word.endswith("mleć") or word.endswith("mlec"):
        mlec(word)  # mleć, mielę
    elif word.endswith("śleć"):
        myslec(word)  # myśleć, myślę
    elif word.endswith("wlec"):
        wlec(word)  # wlec, wlokę
    elif word == "chcieć" or word == "chciec":
        chciec(word)  # chcieć, chcę
    elif word == "mieć" or word == "miec":
        miec(word)  # mieć, mam
    elif word == "wiedzieć" or word == "wiedziec":
        wiedziec(word)  # wiedzieć, wiem
    elif word.endswith("siedzieć") or word.endswith("siedziec"):
        zapomniec(word)  # siedzieć, siedzę
    elif word.endswith("leźć") or word.endswith("lezc"):
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

# This code conjugates verbs that end in -óć
elif word.endswith("łóć") or word.endswith("łóc"):
    kloc(word)  # kłóć, kolę

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
    if len(word) == 3:
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
        else:
            pic(word)
    elif len(word) <= 4:
        if word.endswith("szyć") or word.endswith("szyc"):
            pic(word)  # szyć, szyję
        elif (
            word.endswith("śnić")
            or word.endswith("snić")
            or word.endswith("śnic")
            or word.endswith("snic")
        ):
            robic(word)  # śnić, śnię
        elif word.endswith("nić") or word.endswith("nic"):
            pic(word)  # gnić, gniję
        elif word == "tlić" or word == "tlic":
            myslec(word)  # tlić, tlę
        elif word == "kpić" or word == "kpic":
            robic(word)  # kpić, kpię
        elif word.endswith("być") or word.endswith("byc"):
            bede(word)  # ubyć, ubędę
        elif (
            word.endswith("pić")
            or word.endswith("pic")
            or word.endswith("myć")
            or word.endswith("myc")
        ):
            pic(word)  # upić, upiję
        elif word.endswith("jść") or word.endswith("jśc") or word.endswith("jsc"):
            isc(word)  # ujść, ujdę
        else:
            pic(
                word
            )  # any 4-letter verbs not covered by the above category use this function
    else:
        if (
            word.endswith("chybić")
            or word.endswith("chybic")
            or word.endswith("ubić")
            or word.endswith("ubic")
            or word.endswith("rybić")
            or word.endswith("rybic")
        ):
            robic(word)  # chybić, chybię
        elif word.endswith("ęszyć") or word.endswith("ęszyc"):
            tworzyc(word)  # węszyć, węszę
        elif word.endswith("kszyć"):
            patrzec(word)  # powiększyć, powiększę
        elif word.endswith("szyć") or word.endswith("szyc"):
            pic(word)  # szyć, szyję
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
        elif (
            word.endswith("asić")
            or word.endswith("asic")
            or word.endswith("esić")
            or word.endswith("esic")
            or word.endswith("isić")
            or word.endswith("isic")
            or word.endswith("usić")
            or word.endswith("usic")
        ):
            sic(word)  # wymusić, wymuszę
        elif word.endswith("nosić") or word.endswith("nosic"):
            nosic(word)  # nosić, noszę
        elif word.endswith("strzyc"):
            strzyc(word)  # strzyc, strzygę
        elif (
            word.endswith("rzyć")
            or word.endswith("rzyc")
            or word.endswith("czyć")
            or word.endswith("czyc")
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
            sic(word)  # czcić, czczę
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
    word.endswith("kuć")
    or word.endswith("kuc")
    or word.endswith("luć")
    or word.endswith("luc")
    or word.endswith("łuć")
    or word.endswith("nuć")
    or word.endswith("nuc")
    or word.endswith("ruć")
    or word.endswith("ruc")
    or word.endswith("suć")
    or word.endswith("suc")
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

# The conjugator ends here
