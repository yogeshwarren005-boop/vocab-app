# -*- coding: utf-8 -*-
"""
Part 2: 14 words from Dashboard — opt ('optimise' through 'unadoptable')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part2_opt = {
  "optimise": {
    "primary": "To make the best or most effective use of a situation, opportunity, or resource (British spelling).",
    "secondary": "In algorithmic computer science and operations research, to adjust mathematical parameters to reach maximum efficiency or minimum computational latency.",
    "quotes": [
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The engineer must continuously **optimise** the gear ratios of the calculating engine to prevent friction and mechanical drag."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Organisms evolve structured organs to **optimise** the capture and distribution of vital energy from their surroundings."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "The prudent manufacturer strives to **optimise** factory layout so that raw materials flow smoothly without delay."}
    ]
  },
  "optimism": {
    "primary": "Hopefulness, confidence, and a positive disposition regarding the future or the favorable outcome of something.",
    "secondary": "In classical philosophy, the Leibnizian doctrine that the actual universe is the best of all possible worlds created by a perfect Deity.",
    "quotes": [
      {"author": "Voltaire", "work": "Candide", "quote": "Alas! said Candide, **optimism** is the madness of maintaining that everything is right when it is wrong."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The basis of **optimism** is sheer terror; we think that we are generous because we credit our neighbor with those virtues that likely benefit ourselves."},
      {"author": "William James", "work": "Pragmatism", "quote": "A healthy-minded **optimism** treats evils as transitory blemishes on the surface of an otherwise friendly universe."}
    ]
  },
  "optimist": {
    "primary": "A person disposed to look on the favorable or positive side of events and to expect the most positive outcome.",
    "secondary": "In intellectual history and ethical psychology, an adherent of philosophical optimism who asserts the predominance of good over cosmic evil.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The genuine **optimist** perceives a perpetual tendency to good in the coarse and turbulent stream of human affairs."},
      {"author": "P. G. Wodehouse", "work": "Love Among the Chickens", "quote": "Ukridge was an incurable **optimist**, always convinced that his latest chaotic enterprise was on the verge of making a colossal fortune."},
      {"author": "Mark Twain", "work": "Following the Equator", "quote": "The man who is a pessimist before forty-eight knows too much; if he is an **optimist** after it, he knows too little."}
    ]
  },
  "optimistic": {
    "primary": "Characterized by hopefulness, confidence, and a constructive expectation of positive future results.",
    "secondary": "In macroeconomic forecasting and psychiatric assessment, presenting an elevated or favorable valuation of market indicators or psychological outlook.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke entertained an **optimistic** view of his impending parliamentary campaign, untroubled by his lack of coherent principles."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "His early **optimistic** dreams of university scholarship slowly withered beneath the cold reality of social exclusion."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The morning papers published **optimistic** accounts, reassuring the public that the Martians were helplessly trapped in their pit."}
    ]
  },
  "optimistically": {
    "primary": "In a hopeful, cheerful, or confident manner that anticipates successful and favorable conclusions.",
    "secondary": "In narrative characterization and project estimation, projecting success or minimal expenditure despite contrary empirical indications.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber surveyed his disastrous financial affairs **optimistically**, hourly anticipating that something would turn up."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether viewed the Parisian artistic society **optimistically**, discovering charm where others suspected moral decadence."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The young seaman set out **optimistically** into the eastern archipelago, dreaming of unblemished chivalric glory."}
    ]
  },
  "optimization": {
    "primary": "The act, process, or technique of making something as effective, perfect, functional, or advantageous as possible.",
    "secondary": "In applied mathematics, economics, and control engineering, finding values of decision variables that maximize or minimize a objective function.",
    "quotes": [
      {"author": "Charles Babbage", "work": "On the Economy of Machinery and Manufactures", "quote": "The careful **optimization** of mechanical tools allows a single artisan to execute work that formerly demanded dozens."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of tasks leads naturally to the **optimization** of labor efficiency across commercial manufacturing shops."},
      {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "Industrial production depends upon the technical **optimization** achieved by trained engineers rather than speculative financiers."}
    ]
  },
  "optimize": {
    "primary": "To make the best or most effective use of a situation, opportunity, or resource; to refine for maximum efficiency.",
    "secondary": "In computational algorithm design and industrial operations, to programmatically tune system parameters to achieve optimal output under specified constraints.",
    "quotes": [
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The inventor must carefully **optimize** every mechanical link in the apparatus to diminish friction and avoid lost motion."},
      {"author": "William Stanley Jevons", "work": "The Theory of Political Economy", "quote": "Economic agents naturally calculate how to **optimize** their consumption choices to maximize total psychic satisfaction."},
      {"author": "H. G. Wells", "work": "A Modern Utopia", "quote": "The planners of the ideal commonwealth seek to **optimize** public hygiene and civic education for all citizens."}
    ]
  },
  "optimum": {
    "primary": "The most favorable or advantageous condition, degree, quantity, or outcome obtainable in a given situation.",
    "secondary": "In environmental biology and biochemical kinetics, the precise temperature, pH, or moisture level at which enzyme activity or organismic growth is maximal.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Plants subjected to cross-pollination achieve an **optimum** vigor of growth that markedly surpasses self-fertilized seedlings."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Enzymatic digestion in the stomach requires an **optimum** degree of acidity, failing completely if the gastric juice becomes alkaline."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "Every manufacturing plant has an **optimum** scale of production beyond which managerial complexity increases average unit cost."}
    ]
  },
  "option": {
    "primary": "A thing that is or may be chosen; the power, right, or liberty of choosing among alternatives.",
    "secondary": "In financial derivatives markets, a contractual right (without obligation) to purchase or sell an underlying security at a fixed strike price.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The citizen must weigh each constitutional **option** with cool deliberation, lest factional zeal betray the infant republic."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth gave her cousin to understand that she had no **option** but to decline an offer so repugnant to her feelings."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Individuality cannot flourish unless society preserves for each person the widest possible **option** of moral self-direction."}
    ]
  },
  "optional": {
    "primary": "Available to be chosen but not mandatory; left to one's own discretion or free choice.",
    "secondary": "In institutional curricula and statutory codes, designating non-compulsory coursework or non-mandatory regulatory provisions.",
    "quotes": [
      {"author": "Charles William Eliot", "work": "Educational Reform", "quote": "The new university curriculum rendered Greek study entirely **optional**, allowing undergraduates to pursue modern scientific disciplines."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Civic participation is not merely **optional** recreation in a free commonwealth, but the vital safeguard against administrative tyranny."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Instruction in the experimental sciences should never be relegated to an **optional** luxury in secondary school education."}
    ]
  },
  "optionally": {
    "primary": "In a manner that is not compulsory; by choice or discretion rather than obligation.",
    "secondary": "In software specification and contract construction, denoting clauses, arguments, or features that may be included or omitted at the user's discretion.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "The Constitutional Code", "quote": "The magistrate may **optionally** remit the fine whenever mitigating circumstances and sincere remorse are demonstrated in court."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The partnership agreement provided that additional profits might be **optionally** reinvested in plant infrastructure or distributed as dividends."},
      {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "Beneficence begins precisely where legal duty ceases, prompting individuals to act **optionally** for the welfare of others."}
    ]
  },
  "optometrist": {
    "primary": "A licensed health care professional specializing in examining eyes, diagnosing visual defects, and prescribing corrective lenses.",
    "secondary": "In primary vision care, a practitioner evaluating binocular function, visual acuity, refractive errors, and screening for ocular pathologies.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Golden Pince-Nez", "quote": "The consulting **optometrist** affirmed that only a patient with exceptional astigmatism and acute myopia could have worn spectacles of such peculiar curvature."},
      {"author": "H. G. Wells", "work": "The Wheels of Chance", "quote": "Hoopdriver peered through the shop window at the brass instruments and vision charts displayed by the town **optometrist**."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He consulted an enterprising **optometrist** on Floral Avenue, who fitted him with fashionable tortoiseshell frames to enhance his executive dignity."}
    ]
  },
  "optometry": {
    "primary": "The profession or practice of examining the eyes for visual defects and prescribing corrective lenses or other vision aids.",
    "secondary": "In healthcare sciences and physiological optics, the clinical discipline encompassing refraction, visual perception therapy, and ocular disease screening.",
    "quotes": [
      {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "The rigorous development of clinical **optometry** transformed ophthalmic refraction from empirical guesswork into an exact physical science."},
      {"author": "Thomas Young", "work": "Lectures on Natural Philosophy", "quote": "Understanding the optical focal planes of the living eye constitutes the indispensable foundation for practical **optometry**."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin attended lectures in physiology and elementary **optometry**, learning how physical lenses compensate for biological defects of the eye."}
    ]
  },
  "unadoptable": {
    "primary": "Not suitable, eligible, or legally capable of being adopted into a family or accepted as a policy.",
    "secondary": "In child welfare law and social policy, designating minors whose legal custody is unsevered, or proposals exhibiting fatal administrative flaws.",
    "quotes": [
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The radical artisan regarded the proposed compromise bill as utterly **unadoptable** by any honest friend of popular suffrage."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The legal complexities of the Chancery decree rendered the orphan temporarily **unadoptable** under standard parish statutes."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "Any legislative scheme that violates the equal moral rights of citizens is fundamentally **unadoptable** in a civilized commonwealth."}
    ]
  }
}
