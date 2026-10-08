import os, sys, re, json

sys.stdout.reconfigure(encoding="utf-8")

dashboards = {
    "bib": ["bib", "bibulous", "imbibe", "imbiber", "imbibing", "imbibition"],
    "coct": ["cocteau", "concoct", "concoction", "decoct", "decoction"],
    "coqu": ["coquet", "coquetry", "coquette", "coquettish", "coquettishly", "coquille"],
    "ed": [
        "abed", "aged", "agedness", "agreed", "antiquated", "complicated", "complicatedness", "deed", "ed",
        "edibility", "edible", "edibleness", "fenestrated", "indeed", "inedible", "misdeed", "nonaged", "overaged",
        "posted", "reed", "reedy", "reseed", "seabed", "seed", "seeded", "seeder", "seediness", "seedy",
        "tunicated", "unaged", "uncomplicated", "unseeded", "unveiled", "veiled"
    ],
    "lact": [
        "ablactate", "ablactation", "extragalactic", "galactic", "intergalactic", "lactaid", "lactalbumin",
        "lactarius", "lactase", "lactate", "lactating", "lactation", "lacteal", "lactescent", "lactic",
        "lactiferous", "lactifuge", "lactobacillaceae", "lactobacillus", "lactobacteriaceae", "lactoflavin",
        "lactogen", "lactogenic", "lactophrys", "lactoprotein", "lactose", "lactosuria", "lactuca", "prolactin"
    ],
    "mell": [
        "mellaril", "melliferous", "mellification", "mellifluent", "mellifluous", "mellisonant", "mellisugent",
        "mellivora", "mellon", "mellow", "mellowed", "mellowing", "mellowingly", "mellowly", "mellowness"
    ],
    "pan": [
        "companion", "companionship", "empanada", "pan", "panic", "panification", "panivorous", "pannier", "pantry"
    ],
    "pota": [
        "potable", "potage", "potash", "potassium", "potation", "potato"
    ]
}

total_words = []
for k, v in dashboards.items():
    total_words.extend(v)

print(f"Total words registered: {len(total_words)}")
assert len(total_words) == 110
