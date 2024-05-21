# Informatica Opdracht

## Onderwerp site

Als onderwerp heb ik gekozen om een site te maken voor mensen die graag een hond willen uitlaten maar zelf geen hond hebben.

## Persona

| Persoonlijke informatie       | Houdt niet van| Intresses |
|----------                     |:--------:     |---------: |
| Daan Jansen                   | Vissen        | Sporten   |
| 21                            | Koud eten     | Voetbal   |
| Man                           | Studeren      | Wandelen  |
| Wageningen                    | Stil zitten   | Dieren    |


| Kansen                            | Hobby's en werk   |
|----------                         |:--------:         |
| Zoekt naar een huisdier           | Wandelen          |
| Is gevoelig voor schattige dieren | Programeur        |
| Wilt honden uitlaten              |                   |
|                                   |                   |


## Userstory

**Als** student **wil ik** graag een hond uitlaten, **zodat ik** leuke wandelingen kan maken met een schattig pluisdiertje.
<br>

**Als** arts **wil ik** graag dat iemand mijn hond uitlaat als ik lange onregelmatige diensten heb, **zodat ik** minder aan mijn hoofd heb als ik bezig ben met mijn dienst.

## Functioneel Ontwerp

Voor mijn functioneel ontwerp heb ik een django site gemaakt, hieronder heb ik kort beschreven hoe je mijn ontwerp kan openen.

1. Zorg dat je django geïnstaleerd hebt.

```bash
pip install django
```

2. Ga met de terminal naar de folder waar ```manage.py``` staat.

3. Run dan dit commando. 

```bash
python manage.py runserver
```

4. Het Functioneel Ontwerp kan je dan vinden op ```http://127.0.0.1:8000/``` 

**LET OP:** De honden zoek pagina kan je (nog) niet bereiken via de site ga daarvoor naar ```http://127.0.0.1:8000/honden```

## Gebruikers Test

Vragen:
1. Was het makkelijk om een account te maken?
2. Was het makkelijk om een hond aan te melden?
3. Was het makkelijk om jezelf als uitlater aan te melden?
4. Kan je makkelijk een hond aanvragen?
5. Zijn er onverwachte problemen?
6. Welk cijfer zou je de UI geven (tussen 1 en 10)?
7. Welk cijfer zou je de UX geven (tussen 1 en 10)?

Antwoorden:
1. Ja, het werkte goed, de pagina was een beetje leeg.
2. Ja, het is wel irritant dat je zelf terug moet klikken
3. Ja, zelfde als het bovenstaande antwoord.
4. Nee, het was heel moeilijk om het ```Honden Dashboard``` te vinden.
5. Geen grote, een paar kleine UX dingen.
6. Een 7, het is redelijk, het kleuren palet is wel mooi.
7. 5, het is niet goed genoeg best wat kleine irritante problemen.


## Aanpassingen

De inlog/aanmeld pagina's kunnen iets kleurrijker.