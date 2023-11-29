# Polish-verb-conjugator

This GitHub repository contains a Terminal/CLI-based automated verb conjugator for the Polish language.

![Polish verb conjugator in Python by @chriseborowski repository image](<https://github.com/chriseborowski/Polish-verb-conjugator/blob/main/Polish%20verb%20conjugator%20in%20Python%20(chriseborowski).png>)

## About

The conjugator takes a language typological approach to the problem by grouping verbs into morphologically similar categories instead of relying on statistical models or large language models (LLMs). The tool covers present-tense singular and plural forms, including irregular verb categories. Planned functionalities include exceptions (in progress), past/future tense, and a front-end interface.

Personal pronouns are included in the brackets.

## Functionalities

The latest version supports the following functionalities:

- [x] Support for the most typical, regular -A- verbs of the type: _czytać (czytam, czytasz, czyta...)_
- [x] Support for the most typical, regular -E- verbs of the type: _chcieć (chcę, chcesz, chce...)_
- [x] Support for the most typical, regular -I- verbs of the type: _robić (robię, robisz, robi...)_
- [x] Support for the _-iwać_ verbs of the type: _podskakiwać (podskakuję, podskakujesz, podskakuje...)_
- [x] Support for the _-ować_ verbs of the type: _pracować (pracuję, pracujesz, pracuje...)_
- [x] Support for the _-jechać_ verbs of the type: _-jechać (-jadę, -jedziesz, -jedzie...)_
- [x] Support for irregular verbs such as _mieć_, _być_, _brać_, _chcieć_, _musieć_, _móc_, _spać_, _pisać_, _jeść_, _mleć_, _strzyc_, _piać_
- [x] Support for the _-akać_ verbs of the type: _skakać (skaczę, skaczesz, skacze...)_
- [x] Support for the _-amać_ verbs of the type: _kłamać (kłamię, kłamiesz, kłamie...)_
- [x] Support for the _-awać_ verbs of the type: _stawać (staję, stajesz, staje...)_
- [x] Support for the _-azać_ verbs of the type: _kazać (każę, każesz, każe...)_
- [x] Support for the _-azać_ verbs of the type: _kazać (każę, każesz, każe...)_
- [x] Support for the 3-letter _ąć_ verbs of the type: _dąć (dmę, dmiesz, dmie…)_
- [x] Support for the _-jąć_ verbs of the type: _pojąć (pojmę, pojmiesz, pojmie...)_
- [x] Support for the _-wziąć_ verbs of the type: _wziąć (wezmę, weźmiesz, weźmie...)_
- [x] Support for the _-mieć_ verbs of the type: _rozumieć (rozumiem, rozumiesz, rozumie...)_
- [x] Support for the _-rzeć_ verbs of the type: _umrzeć (umrzeć, umrę, umrze...)_
- [x] Support for the _-rzeć_ verbs of the type: _patrzeć (patrzę, patrzysz, patrzy...)_
- [x] Support for the past-tense forms of the most typical, regular -A- verbs of the type: _czytać (czytam, czytasz, czyta...)_
- [x] Support for the past-tense forms of most typical, regular -E- verbs of the type: _chcieć (chcę, chcesz, chce...)_
- [x] Support for the past-tense forms of the most typical, regular -I- verbs of the type: _robić (robię, robisz, robi...)_
- [x] Support for the past-tense forms of irregular verbs such as: _być (byłem/byłam, byłeś/byłaś, był/była/było...)_
- [x] Support for the past-tense forms of the _-ować_ verbs of the type: _pracować (pracowałem/-łam, pracowałem/-łam, pracował/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-awać_ verbs of the type: _stawać (stawałem/-łam, stawałeś/-łaś, stawał/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-brać_ verbs of the type: _brać (brałem/-łam, brałeś/-łaś, brał/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-być_ verbs of the type: _być (byłem/byłam, byłeś/byłaś, był/była/było...)_
- [x] Support for the past-tense forms of the _(-)spać_ verbs of the type: _spać (spałem/spałam, spałeś/spałeś, spał/spała/spało...)_
- [x] Support for the past-tense forms of the _-nąć_ verbs of the type: _stanąć (stanąłem/stanęłam, stanąłeś/stanęłam, stanął/stanęła/stanęło...)_
- [x] Support for the past-tense forms of irregular verbs _pisać, kazać, kłamać (pisałem/-łam, pisałeś/-łaś, pisał/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-jąć_ verbs of the type: _zająć (zająłem/zajęłam, zająłeś/zajęłaś, zajął/zajęła/zajęło...)_
- [x] Support for the past-tense forms of the _-wziąć_ verbs of the type: _wziąć (wziąłem/wzięłam, wziąłeś/wzięłaś, wziął/wzięła/wzięło...)_
- [x] Support for the past-tense forms of the _-zżąć_ verbs of the type: _zżąć (zżąłem/zżęłam, zżąłeś/zżęłaś, zżął/zżęła/zżęło...)_
- [x] Support for the past-tense forms of the _-mieć_ verbs of the type: _mieć (miałem/miałam, miałeś/miałaś, miał/miała/miało...)_
- [x] Support for the past-tense forms of the _-leć_ verbs of the type: _myśleć (myślałem/myślałam, myślałeś/myślałaś, myślał/myślała/myślało...)_
- [x] Support for the past-tense forms of the _-pomnieć_ verbs of the type: _zapomnieć (zapomniałem/zapomniałam, zapomniałeś/zapomniałaś, zapomniał/zapomniała/zapomniało...)_
- [x] Support for the past-tense forms of the _-trzeć_ verbs of the type: _patrzeć (patrzyłem/-łam, patrzyłeś/-łaś, patrzył/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-biec_ verbs of the type: _biec (biegłem/biegłam, biegłeś/biegłaś, biegł/biegła/biegło...)_
- [x] Support for the past-tense forms of the _-piec_ verbs of the type: _piec (piekłem/piekłam, piekłeś/piekłaś, piekł/piekła/piekło...)_
- [x] Support for the past-tense forms of the _-aść_ verbs of the type: _kraść (kradłem/kradłam, kradłeś/kradłaś, kradł/kradła/kradło...)_
- [x] Support for the past-tense forms of the _-ąść_ verbs of the type: _trząść (trząsłem/trzęsłam, trząsłeś/trzęsłaś, trząsł/trzęsła/trzęsło...)_
- [x] Support for the past-tense forms of the _-ąźć_ verbs of the type: _grząźć (grzązłem/grzęzłam, grzązłeś/grzęzłaś, grzązł/grzęzła/grzęzło...)_
- [x] Support for the past-tense forms of the _wiedzieć_ verbs of the type: _wiedzieć (wiedziałem/wiedziałam, wiedziałeś/wiedziałaś, wiedział/wiedziała/wiedziało...)_
- [x] Support for the past-tense forms of the _-eść_ verbs of the type: _nieść (niosłem/niosłam, niosłeś/niosłaś, niósł/niosła/niosło...)_
- [x] Support for the past-tense forms of the _-(l)eść_ verbs of the type: _pleść (plotłem/plotłam, plotłeś/plotłaś, plótł/plotła/plotło...)_
- [x] Support for the past-tense forms of the _wieść_ verbs of the type: _wieść (wiodłem/wiodłam, wiodłeś/wiodłaś, wiódł/wiodła/wiodło...)_
- [x] Support for the past-tense forms of the _wieźć_ verbs of the type: _wieźć (wiozłem/wiozłam, wiozłeś/wiozłaś, wiózł/wiozła/wiozło...)_
- [x] Support for the past-tense forms of the _-(l)eźć_ verbs of the type: _wleźć (wlazłem/wlazłam, wlazłeś/wlazłaś, wlazł/wlazła/wlazłoc...)_
- [x] Support for the past-tense forms of the _-móc_ verbs of the type: _pomóc (pomogłem/pomogłam, pomogłeś/pomogłaś, pomógł/pomogła/pomogło...)_
- [x] Support for the past-tense forms of the _-dzić_ verbs of the type: _chodzić (chodziłem/chodziłam, chodziłeś/chodziłaś, chodził/chodziła/chodziło...)_
- [x] Support for the past-tense forms of the _(-)czyścić_ verbs of the type: _czyścić (czyściłem/czyściłam, czyściłeś/czyściłaś, czyścił/czyściła/czyściło...)_
- [x] Support for the past-tense forms of the _-sić_ verbs of the type: _nosić (nosiłem/nosiłam, nosiłeś/nosiłaś, nosił/nosiła/nosiło...)_

## License

## Contact
