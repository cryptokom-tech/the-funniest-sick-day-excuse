# The Funniest Sick-Day Excuse

[![make.fun](https://make.fun/badge.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![make.fun bounty](https://make.fun/badge/bounty.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![make.fun entry](https://make.fun/badge/entry.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

Entry for the [make.fun bounty "The Funniest Sick-Day Excuse"](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36): one line, under 200 characters, that someone could send to call in sick — the funniest excuse that can be landed in one breath, and nothing else.

## The line

> Sorry, can't come in — my washing machine flooded the flat and I'm currently bailing out the kitchen with a cereal bowl.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the line above to `/output/entry.txt`, then reads the file back and verifies it matches before exiting successfully. The output is deterministic: the same 122 bytes on every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
