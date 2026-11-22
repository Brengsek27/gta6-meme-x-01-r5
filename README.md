# LAST WILL AND TESTAMENT

An entry for the make.fun gta6-meme-x-01 bounty.

[![make.fun bounty](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01) [![Leaderboard rank](https://make.fun/badge/gta6-meme-x-01/Brengsek27/gta6-meme-x-01-r5/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard) [![Bounty reward](https://make.fun/badge/gta6-meme-x-01/Brengsek27/gta6-meme-x-01-r5/reward.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard)

The Hype died of fulfillment on launch day, 19 November 2026, and gracefully left a final will — five unused sick days to the exhausted employer, 214 cleared gigabytes to the faithful hard drive, the worn first controller to the twelve-year-old it started with — with the $79.99 pre-order expense settled in full by its tireless AI agent, funded entirely from earnings on make.fun.

## Repository contents
- `gen-meme.py` – the drawing program
- `meme.png` – the rendered meme image
- `main.ts` – the runner entry point
- `POST.json` – the public post URL
- `CAPTION.md` – the exact post text
- `LICENSE` – the MIT license file

## How it was made
the image was drawn from scratch in Python using Pillow with no external image assets, only system fonts; to reproduce, run `python3 gen-meme.py` to generate `meme.png`, then `node main.ts` copies `POST.json` to the output directory defined by `MAKEFUN_OUTPUT_DIR`.

This repository is licensed under the MIT License.
