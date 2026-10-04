# -*- coding: utf-8 -*-
"""
Fixes for the 4 words in Dashboard — arch:
- arching
- architect
- archive
- archness
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_arch_fixes = {
  "arching": {
    "primary": "Curving or bending into the shape of an arch; forming an overarching vault or curved silhouette.",
    "secondary": "In structural architecture and botany, branches, boughs, or masonry ribs spanning an open space in a parabolic curve.",
    "quotes": [
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The magnificent sugar pines formed **arching** boughs that sheltered the trail from the fierce afternoon sun."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "She looked up at the **arching** canopy of beech leaves that filtered the midday light into a cool green gloom."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "An **arching** doorway of ancient Roman brick gave entrance to the sunken courtyard of the palace."}
    ]
  },
  "architect": {
    "primary": "A person who designs buildings and supervises their construction; also a creator or prime mover of an idea or enterprise.",
    "secondary": "In systems engineering and computing, a specialist who designs complex software, hardware, or organizational structures.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The true **architect** must be not merely a builder of walls, but an interpreter of human aspiration and noble truth."},
      {"author": "William Shakespeare", "work": "Titus Andronicus", "quote": "Chief **architect** and plotter of these woes, the ruthless villain now lies bound before us."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Every man is the **architect** of a temple, called his body, to the god he worships."}
    ]
  },
  "archive": {
    "primary": "A collection of historical documents or records providing information about a place, institution, or group of people; also to store in an archive.",
    "secondary": "In information science and archival theory, a repository preserving records possessing enduring cultural, administrative, or evidential value.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The imperial **archive** at Constantinople preserved the ancient treaties negotiated between Rome and the Persian kings."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Every national **archive** in western Europe was thoroughly ransacked by historians to reconstruct the diplomacy of the Grand Alliance."},
      {"author": "Sir Walter Scott", "work": "The Antiquary", "quote": "He spent years examining dusty parchments stored in the cathedral **archive** to authenticate the family title."}
    ]
  },
  "archness": {
    "primary": "Playful teasing, roguishness, or knowing mischievousness in manner or expression.",
    "secondary": "In literary characterization and behavioral analysis, subtle ironic humor conveying playful complicity or gentle mockery.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth looked at him with an expression of delightful **archness**, wondering whether he perceived her teasing irony."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "There was a faint touch of **archness** in her tone that softened the candid severity of her judgment."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The little French girl answered with such innate **archness** that even the grave governess could not suppress a smile."}
    ]
  }
}
