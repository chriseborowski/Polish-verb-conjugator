# Polish-verb-conjugator

This GitHub repository contains a Terminal/CLI-based automated verb conjugator for the Polish language.

![Polish verb conjugator in Python by @chriseborowski repository image](<https://github.com/chriseborowski/Polish-verb-conjugator/blob/main/Polish%20verb%20conjugator%20in%20Python%20(chriseborowski).png>)

## About

The conjugator takes a language typological approach to the problem by grouping verbs into morphologically similar categories instead of relying on statistical models or large language models (LLMs). The tool covers present-tense singular and plural forms, including irregular verb categories. Planned functionalities include exceptions (in progress), past/future tense, and a front-end interface.

Personal pronouns are included in the brackets.

## Functionalities

The latest version supports the following functionalities:

- [x] Support for the most typical, regular -A- verbs of the type: _czytać_

| [gender] |    1sg     |    2sg     |     3sg      |     1pl      |      2pl      |    3pl    |
| :------: | :--------: | :--------: | :----------: | :----------: | :-----------: | :-------: |
|          |    _ja_    |    _ty_    | _on/ona/ono_ |     _my_     |     _wy_      | _oni/one_ |
|          |  _czytam_  | _czytasz_  |   _czyta_    |  _czytamy_   |  _czytacie_   | _czytają_ |
|  [masc]  | _czytałem_ | _czytałeś_ |   _czytał_   | _czytaliśmy_ | _czytaliście_ | _czytali_ |
|  [fem]   | _czytałam_ | _czytałaś_ |  _czytała_   | _czytałyśmy_ | _czytałyście_ | _czytały_ |
|  [neut]  |            |            |  _czytało_   |              |               |           |

- [x] Support for the most typical, regular -E- verbs of the type: _chcieć_

| [gender] |    1sg     |    2sg     |     3sg      |     1pl      |      2pl      |    3pl    |
| :------: | :--------: | :--------: | :----------: | :----------: | :-----------: | :-------: |
|          |    _ja_    |    _ty_    | _on/ona/ono_ |     _my_     |     _wy_      | _oni/one_ |
|          |   _chcę_   |  _chcesz_  |    _chce_    |   _chcemy_   |   _chcecie_   |  _chcą_   |
|  [masc]  | _chciałem_ | _chciałam_ |   _chciał_   | _chcieliśmy_ | _chcieliście_ | _chcieli_ |
|  [fem]   | _chciałam_ | _chciałaś_ |  _chciała_   | _chciałyśmy_ | _chciałyście_ | _chciały_ |
|  [neut]  |            |            |  _chciało_   |              |               |           |

- [x] Support for the most typical, regular -I- verbs of the type: _robić_

| [gender] |    1sg    |    2sg    |     3sg      |     1pl     |     2pl      |    3pl    |
| :------: | :-------: | :-------: | :----------: | :---------: | :----------: | :-------: |
|          |   _ja_    |   _ty_    | _on/ona/ono_ |    _my_     |     _wy_     | _oni/one_ |
|          |  _robię_  | _robisz_  |    _robi_    |  _robimy_   |  _robicie_   |  _robią_  |
|  [masc]  | _robiłem_ | _robiłeś_ |   _robił_    | _robiliśmy_ | _robiliście_ | _robili_  |
|  [fem]   | _robiłam_ | _robiłaś_ |   _robiła_   | _robiłyśmy_ | _robiłyście_ | _robiły_  |
|  [neut]  |           |           |   _robiło_   |             |              |           |

- [x] Support for the _-iwać_ verbs of the type: _podskakiwać_

| [gender] |       1sg       |       2sg       |      3sg       |        1pl        |        2pl         |      3pl       |
| :------: | :-------------: | :-------------: | :------------: | :---------------: | :----------------: | :------------: |
|          |      _ja_       |      _ty_       |  _on/ona/ono_  |       _my_        |        _wy_        |   _oni/one_    |
|          |   _poskakuję_   | _podskakujesz_  |  _podskakuje_  |  _podskakujemy_   |  _podskakujecie_   |  _podskakują_  |
|  [masc]  | _podskakiwałem_ | _podskakiwałeś_ | _podskakiwał_  | _podskakiwaliśmy_ | _podskakiwaliście_ | _podskakiwali_ |
|  [fem]   | _podskakiwałam_ | _podskakiwałaś_ | _podskakiwała_ | _podskakiwałyśmy_ | _podskakiwałyście_ | _podskakiwały_ |
|  [neut]  |                 |                 | _podskakiwało_ |                   |                    |                |

- [x] Support for the _-ować_ verbs of the type: _pracować (pracuję, pracujesz, pracuje...)_
- [x] Support for the _-jechać_ verbs of the type: _-jechać (-jadę, -jedziesz, -jedzie...)_
- [x] Support for irregular verbs such as _mieć_, _być_, _brać_, _chcieć_, _musieć_, _móc_, _spać_, _pisać_, _jeść_, _mleć_, _strzyc_, _piać_, _ciec_, _rzec_, _ulec_, _ciąć_
- [x] Support for the _-akać_ verbs of the type: _skakać (skaczę, skaczesz, skacze...)_
- [x] Support for the _-amać_ verbs of the type: _kłamać (kłamię, kłamiesz, kłamie...)_
- [x] Support for the _-awać_ verbs of the type: _stawać (staję, stajesz, staje...)_
- [x] Support for the _-azać_ verbs of the type: _kazać (każę, każesz, każe...)_
- [x] Support for the _-azać_ verbs of the type: _kazać (każę, każesz, każe...)_
- [x] Support for the 3-letter _ąć_ verbs of the type: _dąć (dmę, dmiesz, dmie…)_
- [x] Support for the _-jąć_ verbs of the type: _pojąć (pojmę, pojmiesz, pojmie...)_
- [x] Support for the _-djąć_ verbs of the type: _zdjąć (zdejmę, zdejmiesz, zdejmie...)_
- [x] Support for the _-wziąć_ verbs of the type: _wziąć (wezmę, weźmiesz, weźmie...)_
- [x] Support for the _-mieć_ verbs of the type: _rozumieć (rozumiem, rozumiesz, rozumie...)_
- [x] Support for the _-rzeć_ verbs of the type: _umrzeć (umrzeć, umrę, umrze...)_
- [x] Support for the _-rzeć_ verbs of the type: _patrzeć (patrzę, patrzysz, patrzy...)_
- [x] Support for the past-tense forms of most typical, regular -E- verbs of the type: _chcieć (chcę, chcesz, chce...)_
- [x] Support for the past-tense forms of the most typical, regular -I- verbs of the type: _robić (robiłem/robiłam, robiłeś/robiłaś, robił/robiła/robiło...)_
- [x] Support for the past-tense forms of the _(-)jeździć_ verbs of the type: _jeździć (jeździłem/jeździłam, jeździłeś/jeździłaś, jeździł/jeździła/jeździło...)_
- [x] Support for the past-tense forms of irregular verbs such as: _być (byłem/byłam, byłeś/byłaś, był/była/było...)_, _iść_, _gryźć_, _ulec_, _ciec_, _rzec_, _żąć_, _kłóć_
- [x] Support for the past-tense forms of irregular verbs such as: _iść_ and related verbs of the type: _pójść (poszedłem/poszłam, poszedłeś/poszłaś, poszedł/poszła/poszło...)_, _wejść (wszedłem/weszłam, wszedłeś/weszłaś, wszedł/weszła/weszło...)_, _wyjść (wyszedłem/wyszłam, wyszedłeś/wyszłaś, wyszedł/wyszła/wyszło...)_
- [x] Support for the past-tense forms of the _-ować_ verbs of the type: _pracować (pracowałem/-łam, pracowałem/-łam, pracował/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-awać_ verbs of the type: _stawać (stawałem/-łam, stawałeś/-łaś, stawał/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-wić_ verbs of the type: _bawić (bawiłem/bawiłam, bawiłeś/bawiłaś, bawił/bawiła/bawiło...)_
- [x] Support for the past-tense forms of the _-brać_ verbs of the type: _brać (brałem/-łam, brałeś/-łaś, brał/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-dać_ verbs of the type: _podać (podałem/podałam, podałeś/podałaś, podał/podała/podało...)_
- [x] Support for the past-tense forms of the _(-)wstać_ verbs of the type: _wstać (wstałem/wstałam, wstałeś/wstałaś, wstał/wstała/wstało...)_
- [x] Support for the past-tense forms of the _-być_ verbs of the type: _być (byłem/byłam, byłeś/byłaś, był/była/było...)_
- [x] Support for the past-tense forms of the _-dać_ verbs of the type: _podać (podałem/podałam, podałeś/podałaś, podał/podała/podało...)_
- [x] Support for the past-tense forms of the _-kuć_/_luć_/_ruć_/_suć_ verbs of the type: _odkuć (odkułem/odkułam, odkułeś/odkułaś, odkuł/odkuła/odkuło...)_
- [x] Support for the past-tense forms of the _-szyć_ verbs of the type: _uszyć (uszyłem/uszyłam, uszyłeś/uszyłaś, uszył/uszyła/uszyło...)_
- [x] Support for the past-tense forms of the _(-)opać_ verbs of the type: _kopać (kopałem/kopałam, kopałeś/kopałaś, kopał/kopała/kopało...)_
- [x] Support for the past-tense forms of the _(-)spać_ verbs of the type: _spać (spałem/spałam, spałeś/spałeś, spał/spała/spało...)_
- [x] Support for the past-tense forms of the _-szyć_ verbs of the type: _uszyć (uszyłem/uszyłam, uszyłeś/uszyłaś, uszył/uszyła/uszyło...)_
- [x] Support for the past-tense forms of the _-nąć_ verbs of the type: _stanąć (stanąłem/stanęłam, stanąłeś/stanęłam, stanął/stanęła/stanęło...)_
- [x] Support for the past-tense forms of the _-cząć_ verbs of the type: _zacząć (zacząłem/zaczęłam, zacząłeś/zaczęłaś, zaczął/zaczęła/zaczęło...)_
- [x] Support for the past-tense forms of irregular verbs _pisać, kazać, kłamać, wlec (pisałem/-łam, pisałeś/-łaś, pisał/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-(d)jąć_ verbs of the type: _zająć (zająłem/zajęłam, zająłeś/zajęłaś, zajął/zajęła/zajęło...)_
- [x] Support for the past-tense forms of the _-ciąć_ verbs of the type: _pociąć (pociąłem/pocięłam, pociąłeś/pocięłaś, pociął/pocięła, pocięło...)_
- [x] Support for the past-tense forms of the _-giąć_ verbs of the type: _zgiąć (zgiąłem/zgięłam, zgiąłeś/zgięłaś, zgiął/zgięła/zgięło...)_
- [x] Support for the past-tense forms of the _-snąć_ verbs of the type: _zasnąć (zasnąłem/zasnęłam, zasnąłeś/zasnęłaś, zasnął/zasnęła/zasnęło...)_
- [x] Support for the past-tense forms of the _-(s)piąć_ verbs of the type: _odpiąć (odpiąłem/odpięłam, odpiąłeś/odpięłaś, odpiął/odpięła/odpięło...)_
- [x] Support for the past-tense forms of the _-wziąć_ verbs of the type: _wziąć (wziąłem/wzięłam, wziąłeś/wzięłaś, wziął/wzięła/wzięło...)_
- [x] Support for the past-tense forms of the _-zżąć_ verbs of the type: _zżąć (zżąłem/zżęłam, zżąłeś/zżęłaś, zżął/zżęła/zżęło...)_
- [x] Support for the past-tense forms of the _-mieć_ verbs of the type: _mieć (miałem/miałam, miałeś/miałaś, miał/miała/miało...)_
- [x] Support for the past-tense forms of the _-leć_ verbs of the type: _myśleć (myślałem/myślałam, myślałeś/myślałaś, myślał/myślała/myślało...)_
- [x] Support for the past-tense forms of the _-pomnieć_ verbs of the type: _zapomnieć (zapomniałem/zapomniałam, zapomniałeś/zapomniałaś, zapomniał/zapomniała/zapomniało...)_
- [x] Support for the past-tense forms of the _-trzeć_ verbs of the type: _patrzeć (patrzyłem/-łam, patrzyłeś/-łaś, patrzył/-ła/-ło...)_
- [x] Support for the past-tense forms of the _-biec_ verbs of the type: _biec (biegłem/biegłam, biegłeś/biegłaś, biegł/biegła/biegło...)_
- [x] Support for the past-tense forms of the _-pić_ verbs of the type: _wypić (wypiłem/wypiłam, wypiłeś/wypiłaś, wypił/wypiła/wypiło...)_
- [x] Support for the past-tense forms of the _-śnić_ verbs of the type: _wyśnić (wyśniłem/wyśniłam, wyśniłeś/wyśniłaś, wyśnił/wyśniła/wyśniło...)_
- [x] Support for the past-tense forms of the _-piec_ verbs of the type: _piec (piekłem/piekłam, piekłeś/piekłaś, piekł/piekła/piekło...)_
- [x] Support for the past-tense forms of the _-żeć_ verbs of the type: _leżeć (leżałem/leżałam, leżałeś/leżałaś, leżał/leżała/leżało...)_
- [x] Support for the past-tense forms of the _-ciec_/_biec_/_wlec_, _rzec_ verbs of the type: _wyrzec (wyrzekłem/wyrzekłam, wyrzekłeś/wyrzekłaś, wyrzekł/wyrzekła/wyrzekło...)_
- [x] Support for the past-tense forms of the _-aść_ verbs of the type: _kraść (kradłem/kradłam, kradłeś/kradłaś, kradł/kradła/kradło...)_
- [x] Support for the past-tense forms of the _-ąść_ verbs of the type: _trząść (trząsłem/trzęsłam, trząsłeś/trzęsłaś, trząsł/trzęsła/trzęsło...)_
- [x] Support for the past-tense forms of the _-ąźć_ verbs of the type: _grząźć (grzązłem/grzęzłam, grzązłeś/grzęzłaś, grzązł/grzęzła/grzęzło...)_
- [x] Support for the past-tense forms of the _wiedzieć_ verbs of the type: _wiedzieć (wiedziałem/wiedziałam, wiedziałeś/wiedziałaś, wiedział/wiedziała/wiedziało...)_
- [x] Support for the past-tense forms of the _-eść_ verbs of the type: _nieść (niosłem/niosłam, niosłeś/niosłaś, niósł/niosła/niosło...)_
- [x] Support for the past-tense forms of the _-(l)eść_ verbs of the type: _pleść (plotłem/plotłam, plotłeś/plotłaś, plótł/plotła/plotło...)_
- [x] Support for the past-tense forms of the _wieść_ verbs of the type: _wieść (wiodłem/wiodłam, wiodłeś/wiodłaś, wiódł/wiodła/wiodło...)_
- [x] Support for the past-tense forms of the _-cić/-dzić_ verbs of the type: _budzić (budziłem/budziłam, budziłeś/budziłaś, budził/budziła/budziło...)_
- [x] Support for the past-tense forms of the _wieźć_ verbs of the type: _wieźć (wiozłem/wiozłam, wiozłeś/wiozłaś, wiózł/wiozła/wiozło...)_
- [x] Support for the past-tense forms of the _-(l)eźć_ verbs of the type: _wleźć (wlazłem/wlazłam, wlazłeś/wlazłaś, wlazł/wlazła/wlazłoc...)_
- [x] Support for the past-tense forms of the _-móc_ verbs of the type: _pomóc (pomogłem/pomogłam, pomogłeś/pomogłaś, pomógł/pomogła/pomogło...)_
- [x] Support for the past-tense forms of the _-dzić_ verbs of the type: _chodzić (chodziłem/chodziłam, chodziłeś/chodziłaś, chodził/chodziła/chodziło...)_
- [x] Support for the past-tense forms of the _(-)czyścić_ verbs of the type: _czyścić (czyściłem/czyściłam, czyściłeś/czyściłaś, czyścił/czyściła/czyściło...)_
- [x] Support for the past-tense forms of the _-sić_ verbs of the type: _nosić (nosiłem/nosiłam, nosiłeś/nosiłaś, nosił/nosiła/nosiło...)_

## License

## Contact
