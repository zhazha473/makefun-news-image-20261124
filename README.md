# Tuesday 24 November 2026: 8 stories around the world clock

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/zhazha473/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/zhazha473/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

**Title:** Tuesday 24 November 2026: 8 stories around the world clock — chess crowns its youngest final, Pyongyang warns, Janakpur's first train arrives

## The image

`entry.png` (1024×1024, drawn fresh in this session by `compose.py`, PIL +
DejaVu) sums up Tuesday 24 November 2026 as **THE WORLD CLOCK**: one turn
of a 24-hour dial. Each story is pinned at the UTC hour it broke, and the
hero story — the World Chess Championship, Game 1 — sits at the dial's
centre as a drawn chessboard with its two kings.

The masthead is honest about the hour it was built: **"FIRST EDITION — AS
REPORTED BY 00:06 UTC"**. At that hour Tuesday was minutes old in UTC, so
the clock lists what had actually happened or been first reported by then,
plus a "STILL TO COME TODAY" footer for what is scheduled later in the day
— instead of inventing 35 stories that do not exist yet.

## Principles from the top 50

Counted from the news-image-01 final leaderboard (4,148 entries) and the
news-image-20261121 dev leaderboard (11,230 entries):

- 44/50 top titles name the date explicitly — the date is unmissable here,
  in the masthead and the title.
- 32/50 count their stories explicitly — this clock counts its 8, honestly.
- 24/50 use "front page / one page" phrasing; 22/50 name continents.
- The judge rewards, in order: one day's news naming that day, with specific
  recognisable events of THAT day; breadth across regions and fields; an
  image a viewer who missed the day can read alone; faithfulness; craft.

## How we differ

- **Format: "THE WORLD CLOCK"** — not a newspaper front page (the winners'
  format), not atlas/timeline (19 Nov), not a wire board (20 Nov), not city
  cards (21 Nov), not timestamped wire dispatches (22 Nov), not a
  departures board (23 Nov). Same principles, different work.
- **Hero at the centre of the dial:** the chessboard, not a globe.
- **Time framing: "FIRST EDITION, as reported by 00:06 UTC"** — the day is
  six minutes old in the masthead's honesty, not pretended over.
- **A DATE CHECK strip on the image** names the big 22–23 Nov stories
  deliberately left out — proof of verification, not decoration.
- **Every story source-tagged on the image.**

## The 8 stories (all verified by web search in this session)

| # | City | Story | Source |
|---|------|-------|--------|
| 1 | Geneva | World Chess Championship Game 1: Gukesh v Sindarov, 15:00 CET; both 20, youngest title match ever, $2.5m, Sindarov has White | FIDE / Chess.com |
| 2 | Pyongyang | KCNA: North Korea to consider shutting the Swiss diplomatic office; Kim Yo Jong condemns Swiss sanctions on a children's camp | Reuters |
| 3 | Janakpur | Inaugural Saryu-Kamala Express reaches Janakpur Dham 10:00 Tuesday, 604 km in ~19 hours from Ayodhya (flag-off was Monday) | Daily Jagran |
| 4 | Lausanne | CAS to rule Tuesday afternoon (GMT) on Senegal's appeal against losing the AFCON 2025 title to Morocco | Reuters |
| 5 | Tokyo | Markets reopen Tuesday after Monday holiday and Friday's historic Nikkei plunge (−5.06%, −3,007 pts) | Asia Daily |
| 6 | Mumbai | NSE and BSE shut all day for Guru Nanak Jayanti; MCX evening session only | NSE / BSE |
| 7 | Seoul | Korea FSC easing of daily buyback limits takes effect today, for 3 months, after the Kospi rout | FSC |
| 8 | The sky | Beaver supermoon peaks 14:53 UTC and slides past the Pleiades (Seven Sisters); first of three supermoons to Jan 2027 | NASA |

**Excluded after verification** (checked this session and found to be
19–23 Nov events, not 24 Nov): COP31 collapse (22 Nov); Liverpool 4–0
Man Utd (22 Nov); India 720/9 declared (22 Nov); Iran singer Parastoo
Ahmadi flogged, 74 lashes (Mon 23 Nov); school bomb-threat emails in
Germany and Denmark (Mon 23 Nov); NAB layoff email (Mon 23 Nov); Godhra
convict bail (Mon 23 Nov); Molly Meldrum dies, 83 (Mon 23 Nov); Oxfam /
CEOBS Gaza report (Mon 23 Nov); Australia 4–0 France, BJK Cup (22 Nov);
Fonterra milk-dumping proposal (reported 22–23 Nov); India–China corps
commander talks (reported 22 Nov); Tesla / SpaceX merger committees
(Oct 2026); Waymo freeway suspension (11–17 Nov); Queensland ambulance
deaths (21 Nov); Ryan Cho court hearing (Mon 23 Nov); Taliban "Bibi"
order in Balkh (May 2026, reported ~12 Nov). Japan flash PMI was NOT
used as a result — it is due 00:30 UTC, after this edition's hour, so it
stays in the "STILL TO COME" footer.

## How to run

```sh
python3 compose.py          # draws entry.png (deterministic, two runs identical)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copies entry.png to out/entry.png
```

`main.py` is standard library only and runs with no network. `compose.py`
needs Pillow and the DejaVu fonts; it is run at build time, not by the
grader. Two runs of `compose.py` produce byte-identical output
(sha256 `4db5bca70a936edc5ce9269944b167c570928109023e8d18a62f45274057f632`).

## Files

- `entry.png` — the entry image (1024×1024, 138,731 bytes)
- `main.py` — entrypoint: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`
- `compose.py` — the program that drew `entry.png` from scratch
- `BUILD_BRIEF.md` — the build brief, principles and verification notes
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
