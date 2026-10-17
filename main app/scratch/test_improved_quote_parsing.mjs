function parseQuoteLine(clean) {
  // Line format:
  // **Author (*Work*):** *"Quote..."*
  // **Author (*Work (Subtitle)*):** *"Quote..."*
  // **Author (Work):** "Quote..."
  // **Author:** "Quote..."

  // Match the outer **...** header before the quote
  const headerQuoteMatch = clean.match(/^\*\*([\s\S]+?)\*\*:?\s*\*?["“]([\s\S]+?)["”]\*?$/) ||
                           clean.match(/^\*\*([\s\S]+?)\*\*:?\s*\*?["“]([\s\S]+)$/);

  if (headerQuoteMatch) {
    let rawHeader = headerQuoteMatch[1].trim();
    // Strip trailing colon or asterisks from header
    rawHeader = rawHeader.replace(/[:*]+$/, '').trim();

    const quoteText = (headerQuoteMatch[2] || '').replace(/["”*]+$/g, '').trim();

    // Now extract author and work from rawHeader
    // Format: "Author (*Work*)" or "Author (*Work (Subtitle)*)" or "Author (Work)" or "Author"
    const parenMatch = rawHeader.match(/^(.+?)\s*\(\*?([\s\S]+?)\*?\)$/);

    if (parenMatch) {
      const author = parenMatch[1].replace(/[:*]/g, '').trim();
      const work = parenMatch[2].replace(/[:*]/g, '').trim();
      return { author, work, quote: quoteText };
    } else {
      const author = rawHeader.replace(/[:*]/g, '').trim();
      return { author, work: '', quote: quoteText };
    }
  }

  // Fallback for lines without bold formatting
  const qm = clean.match(/["“]([^"”]+)["”]/);
  if (qm) {
    return { author: '', work: '', quote: qm[1].trim() };
  }

  return null;
}

// Test with the samples:
const samples = [
  `**Henry James (*The Art of Fiction*):** *"The successful **fictionalization** of human experience depends upon an intense and cultivated sensitivity to the nuances of life."*`,
  `**Truman Capote (*In Cold Blood (Prefatory Note)*):** *"The non-fiction novel achieves its emotional power without resort to the **fictionalization** of a single recorded fact."*`,
  `**William Osler (*The Principles and Practice of Medicine (Modern Revision)*):** *"For chronic neuropathic pain and diabetic neuropathy, low-dose **elavil** at bedtime provides significant analgesic relief independent of its antidepressant action."*`,
  `**Jack London (*The Jacket (The Star-Rover)*):** *"The prison guards called him an **ornery** convict because solitary confinement could not break his spirit."*`,
  `**Francis Bacon (*The Essays (Of Gardens)*):** *"For an **aviary**, I would not have it too close, but of turf, with living trees and bushes growing therein, where birds may sing and nest."*`,
  `**Sigmund Freud (*The Uncanny (Das Unheimliche)*):** *"The **uncanny** is that class of the terrifying which leads back to something long known to us, once very familiar."*`,
  `**Charlotte Brontë (*Jane Eyre*):** *"Here, come in, **bonny** wanderer!"*`,
  `**William Shakespeare (*Much Ado About Nothing*):** *"Then sigh not so, but let them go, and be you blithe and **bonny**, converting all your sounds of woe into Hey nonny, nonny."*`
];

console.log('Testing sample quotes with refined parseQuoteLine:');
for (const s of samples) {
  const clean = s.replace(/^>\s*-\s*(?:📜|📚|🔬|🌐|🗣️|💬)?\s*/, '').replace(/^>\s*/, '').trim();
  const res = parseQuoteLine(clean);
  console.log(`Author: "${res.author}" | Work: "${res.work}" | Quote: "${res.quote.slice(0, 45)}..."`);
}
