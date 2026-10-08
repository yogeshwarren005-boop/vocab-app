# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
import curate_turning_b1_p1a as m

etyms = {
    'circadian': "From Latin *circa* ('about, around') + *dies* ('day').",
    'circaea': "From Latin *Circaea*, from Greek *Kirke* ('Circe, the mythical enchantress').",
    'circaetus': "From Greek *kirkos* ('hawk, circle-flying raptor') + *aetos* ('eagle').",
    'circassian': "From Russian *cherkes*, referring to the Northwest Caucasian peoples of Circassia.",
    'circe': "From Latin *Circe*, from Greek *Kirke*, the Homeric enchantress of Aeaea.",
    'circinate': "From Latin *circinatus*, past participle of *circinare* ('to make round, encircle'), from *circinus* ('compasses').",
    'circinus': "From Latin *circinus* ('pair of compasses, dividers'), from Greek *kirkinos*.",
    'circle': "From Old English *circul*, from Latin *circulus* ('small ring, circular figure'), diminutive of *circus* ('ring').",
    'circlet': "Diminutive of *circle*, from Old French *cerclet*, from Latin *circulus* ('small ring').",
    'circuit': "From Old French *circuit*, from Latin *circuitus* ('a going around'), from *circumire* ('to go around').",
    'circuitous': "From Medieval Latin *circuitosus*, from Latin *circuitus* ('a going around'), from *circuire* ('to go round').",
    'circuitry': "From *circuit* + *-ry*, denoting the collective network of electrical circuits.",
    'circular': "From Anglo-Norman and Old French *circulaire*, from Late Latin *circularis*, from Latin *circulus*.",
    'circular-knit': "Compound of *circular* + *knit*, referring to continuous circular knitting machinery.",
    'circularisation': "From *circularise* + *-ation*, noun of action from Late Latin *circularis*.",
    'circularise': "From *circular* + *-ise*, meaning to distribute circular letters or notices.",
    'circularity': "From Late Latin *circularitas*, from Latin *circularis* ('round, circular').",
    'circularization': "From *circularize* + *-ation*, noun of action denoting systematic circular distribution.",
    'circularize': "From *circular* + *-ize*, meaning to send circular notices or poll systematically.",
    'circularly': "From *circular* + *-ly*, adverb denoting circular motion or circular reasoning.",
    'circulate': "From Latin *circulatus*, past participle of *circulare* ('to form a circle, encompass').",
    'circulating': "Present participle of *circulate*, from Latin *circulare* ('to move in a circle').",
    'circulation': "From Latin *circulatio*, from *circulare* ('to encircle, move around').",
    'circulative': "From Latin *circulatus* + *-ive*, tending or serving to promote circulation.",
    'circulatory': "From French *circulatoire*, from Latin *circulatus*, relating to physical circulation.",
    'circum': "Latin preposition and productive prefix meaning 'around, about, on all sides'.",
    'circumambulate': "From Latin *circumambulare* ('to walk around'), from *circum-* ('around') + *ambulare* ('to walk').",
    'circumboreal': "From Latin *circum-* ('around') + Late Latin *borealis* ('northern'), from Greek *Boreas*.",
    'circumcise': "From Latin *circumcisus*, past participle of *circumcidere* ('to cut around'), from *caedere* ('to cut').",
    'circumcision': "From Latin *circumcisio*, from *circumcidere* ('to cut around').",
    'circumduction': "From Latin *circumductio* ('a leading around'), from *circumducere* ('to draw around').",
    'circumference': "From Old French *circumference*, from Latin *circumferentia*, from *circumferre* ('to carry around').",
    'circumferent': "From Latin *circumferens*, present participle of *circumferre* ('to lead or carry around')."
}

data = m.CURATED_TURNING_B1_P1A
for k, v in etyms.items():
    data[k]['etymology'] = v

out_path = os.path.join(os.path.dirname(__file__), 'curate_turning_b1_p1a.py')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('CURATED_TURNING_B1_P1A = ' + repr(data) + '\n')

print('Successfully updated curate_turning_b1_p1a.py with etymologies')
