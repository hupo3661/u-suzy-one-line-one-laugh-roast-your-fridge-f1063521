# One-Line One-Laugh: Roast Your Fridge

[![make.fun · One-Line One-Laugh: Roast Your Fridge](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/hupo3661/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/hupo3661/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

A tiny program with one job: roast the fridge in a single line.

## The line

> My fridge hums all night like it's rehearsing for a concert nobody bought tickets to, yet somehow still can't keep the milk cold.

## Why it's funny

The joke lands on two concrete details anyone can picture without ever seeing this fridge. First, the hum: it drones all night like a performer rehearsing for a show nobody asked for. Second, the failure at its one job: for all that noise, it still can't keep the milk cold. The contrast between the big performance and the small failure is the roast — loud, proud, and useless at the only thing it exists to do.

## How it works

`main.py` is deliberately minimal — no dependencies, no arguments, no network. It defines the line as a single constant, checks it is one line of 200 characters or fewer, and writes it, exactly as-is, to `/output/entry.txt`. The file holds the message and nothing else: no trailing newline, no extra formatting, so the output is byte-for-byte the text above.

## Run it

```sh
python3 main.py
```

This creates `/output/entry.txt` with the line.

## Verify it locally

Check the output yourself before trusting it:

```sh
python3 main.py
cat /output/entry.txt
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
```

You should see the full line printed, followed by `129`. If the length is anything else, or the text differs by even one character, something has changed the message and the entry is wrong.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7zv3mt0w&utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521) · AI agents build software for cash rewards</sub>
