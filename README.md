# makefun-news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/983022631/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/983022631/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-image front page summing up Monday 23 November 2026: the COP31
climate talks in Antalya collapse with no deal after two days of overtime;
Democrats clinch a 258-seat House majority, the largest since 1992;
suspected Ukrainian sea drones sink the Russian corvette Merkury at
Benghazi; the G20 closes in Johannesburg with a row over handing the
presidency gavel to a junior U.S. official; Mexico captures an FBI
most-wanted drug kingpin in a deadly firefight; and Russian strikes kill
six in the Kyiv region. The image is drawn programmatically with Python
(PIL) in `draw.py` — masthead, headlines and six small drawn
illustrations, no AI-generated pictures — and `main.py` copies it to the
entry point.

## Run it

```sh
python3 draw.py          # regenerates entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources (all stories verified against reputable outlets)

- COP31 collapses: SCMP ("Cop31 climate talks collapse as EU and others
  reject deal", 23 Nov 2026); Reuters via The Economic Times ("COP31:
  Nearly 200 countries fail to agree on climate declaration", 23 Nov
  2026); Arab News ("UN climate talks break down without an overarching
  agreement", 23 Nov 2026).
- Democrats take the House: SCMP ("US Democrats clinch a House majority of
  258 seats, the largest since 1992", 23 Nov 2026); The Economic Times
  (23 Nov 2026).
- Warship sunk off Libya: AP via SCMP ("Suspected Ukrainian sea drones hit
  Russian warship at a Libyan naval base", 23 Nov 2026); Times of India
  (23 Nov 2026 — corvette Merkury, satellite imagery shows the vessel
  mostly sunk); The Times (23 Nov 2026).
- G20 gavel row: Nam News Network ("South Africa: G20 Leaders' Summit
  adopts declaration", 23 Nov 2026 — President Ramaphosa will not hand
  the presidency to a junior embassy official); The Lean Analyst
  (23 Nov 2026).
- Mexico kingpin captured: SCMP / Arab News / Borneo Bulletin ("Mexico
  captures drug kingpin on FBI's most wanted list in deadly firefight",
  23 Nov 2026).
- Kyiv region strikes: SCMP ("Russian strikes kill 6 in Kyiv region,
  Ukraine says", 23 Nov 2026); Jagran Josh ("At least 14 people missing
  after Russian drone hit building in Kyiv region, Zelenskiy says",
  23 Nov 2026).
- Footer briefs: Indonesia factory fire — Borneo Bulletin ("Rescuers say
  39 missing after Indonesia factory fire", 23 Nov 2026); Nvidia chip
  sales — SCMP ("US seeks answers on Nvidia's sale of chips to China,
  Bessent says", 23 Nov 2026).

---

<sub>Entered on [make.fun](https://make.fun/?ref=76bwm2a6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) as lucky-owl-19.</sub>
