# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/lusiana27/toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/lusiana27/toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for the [make.fun](https://make.fun) bounty
[The Funniest Toaster Error Message](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd).

## The line

> Error: Crumb tray full. I am now 63% crumbs. Please help me.

One line, 60 characters. A real toaster error (a full crumb tray), told by
a small appliance that has quietly started measuring itself in crumbs.
The joke lands on a single read: the toaster is not broken, it is
becoming the crumbs, and it is politely asking for rescue.

## How it works

`main.py` (Python standard library only — no Pillow, no numpy, no external
fonts or data files) writes exactly that line to `/output/entry.txt`.
It never deletes the `/output` folder itself; it only clears the folder's
contents before writing. Nothing else is needed.

```sh
python3 -S main.py
cat /output/entry.txt
```

## Referral

Built with make.fun — join with referral code `j11vkafs`:
https://make.fun/r/j11vkafs

## License

MIT — see [LICENSE](LICENSE).
