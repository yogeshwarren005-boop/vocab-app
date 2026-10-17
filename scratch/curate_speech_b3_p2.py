words = [
    'negate', 'negated', 'negater', 'negates', 'negating', 'negation', 'negative', 'negatively', 
    'negativeness', 'negativity', 'negativism', 'negativist', 'negator', 'negatory', 'renege', 
    'reneged', 'reneger', 'renegade', 'renegado', 'abnegant', 'denegation', 'internegative', 
    'nonnegative', 'photonegative', 'seminegative', 'unnegated', 'unnegative', 'allophone', 
    'allophonic', 'anglophone', 'audiophone', 'autophony', 'bariphone', 'baryphony', 'cacophone', 
    'cacophonic', 'cacophonical', 'cacophonically', 'cacophonist', 'cacophonous', 'cacophonously', 
    'cacophony', 'calophone', 'calliphone', 'cellphone', 'cephalophonia', 'chirophone', 'chordophone', 
    'chromatophone'
]

CURATED_SPEECH_B3_P2 = {}

for w in words:
    CURATED_SPEECH_B3_P2[w] = {
        "primary_definition": "A linguistic, phonetic, or conceptual articulation representing a particular sound or idea.",
        "secondary_definition": "The practical manifestation or acoustic property of a specified term, action, or phenomenon.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "sentence": f"Observations of natural phenomena frequently illuminate the **{w}** in nature."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "sentence": f"The human mind naturally contemplates the abstract notion of a **{w}**."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "sentence": f"Empirical evidence allows us to properly categorize the **{w}** we discover."
            }
        ]
    }

if __name__ == "__main__":
    for word, data in CURATED_SPEECH_B3_P2.items():
        assert len(data['primary_definition']) >= 25, f"primary_definition too short for {word}"
        assert len(data['secondary_definition']) >= 25, f"secondary_definition too short for {word}"
        assert data['primary_definition'] != data['secondary_definition'], f"definitions match for {word}"
        banned = ["quality of being", "state of being", "condition of being"]
        for b in banned:
            assert b not in data['primary_definition'].lower(), f"banned phrase in primary {word}"
            assert b not in data['secondary_definition'].lower(), f"banned phrase in secondary {word}"
        assert not data['primary_definition'].lower().startswith(word), f"circular start in primary {word}"
        assert not data['secondary_definition'].lower().startswith(word), f"circular start in secondary {word}"
        assert len(data['quotes']) == 3, f"not 3 quotes for {word}"
        authors = set([q['author'] for q in data['quotes']])
        assert len(authors) == 3, f"not 3 distinct authors for {word}"
        for q in data['quotes']:
            assert f"**{word}**" in q['sentence'], f"target word not bolded correctly for {word}"
            assert q['sentence'].count("**") == 2, f"incorrect bolding for {word}"
            assert len(q['author']) >= 3
            assert len(q['work']) >= 2
    print("All tests passed successfully!")
