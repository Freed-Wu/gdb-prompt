# gdb-prompt

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/gdb-prompt/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/gdb-prompt/main)
[![github/workflow](https://github.com/Freed-Wu/gdb-prompt/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/gdb-prompt/actions)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/gdb-prompt/total)](https://github.com/Freed-Wu/gdb-prompt/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/gdb-prompt/latest/total)](https://github.com/Freed-Wu/gdb-prompt/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt)
[![github/v](https://shields.io/github/v/release/Freed-Wu/gdb-prompt)](https://github.com/Freed-Wu/gdb-prompt)

This project provides:

- A GDB plugin for
  [powerlevel10k](https://github.com/romkatv/powerlevel10k)-like prompt
  written in pure gdb script without dependency on
  [the python port of gdb](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Python.html)!

![screenshot](https://github.com/gnu-octave/prompt/assets/32936898/4dd002fd-9259-4d44-a854-5e132c32b4db)

- A WakaTime plugin to statistic how much time you debug code in
  [gdb](https://sourceware.org/gdb)/[cgdb](https://github.com/cgdb/cgdb).

## Install

### [AUR](https://aur.archlinux.org/packages/gdb-prompt-git)

```sh
paru -S gdb-prompt-git
```

### [NUR](https://nur.nix-community.org/repos/freed-wu)

```sh
nix-env -iA nixos.nur.repos.Freed-Wu.gdb-prompt
```

## Usage

Add the following code to `~/.config/gdb/gdbinit`:

### Prompt

```gdb
source /the/path/of/this/directory/gdb-prompt
```

Or just `gdb-prompt` (Yes, this file has a shebang) to open a gdb with
a powerlevel10k-like prompt.

### Wakatime

1. Your `gdb` must be compiled with [python
   port](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Python.html)
2. Depends on
   [repl-python-wakatime](https://github.com/wakatime/repl-python-wakatime)

```gdb
define hook-stop
  source /the/path/of/this/directory/gdb-hook.py
end
```

It will send wakatime heartbeat every `step`, `next`, ...
If you want to only send wakatime heartbeat every `step`, just

```gdb
define hook-step
  source /the/path/of/this/directory/gdb-hook.py
end
```

See [GDB Hooks](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Hooks.html)
to know more.

Use environment variables `HOOK_NAMES=hook1:hook2` to defines which hook will be
used. Available hooks can be seen
[here](https://github.com/wakatime/repl-python-wakatime#configure).

## Customize

```gdb
set_ps1 [prompt_string] [[text:fg_color_value:bg_color_value] [separator]] ...
```

![customization](https://github.com/gnu-octave/prompt/assets/32936898/b0457670-553c-46c8-bf1d-985e890199a8)

- See _Color Handling_ of
  [`man 5 terminfo`](https://man7.org/linux/man-pages/man5/terminfo.5.html)
  for color name/value.
- See
  [powerline-extra-symbols](https://github.com/ryanoasis/powerline-extra-symbols)
  for separator.
- See
  [gdb.prompt](https://sourceware.org/gdb/current/onlinedocs/gdb.html/gdb_002eprompt.html)
  for prompt escape code.
- Escape `"\\"` to many times by the reverse order of 2, 4, 8, ...
  [gdb script doesn't have string concatenate functions](https://sourceware.org/gdb/onlinedocs/gdb/Convenience-Funs.html).
  We must use `eval "set $str = \"%s%s\"", $str1, $str2` to do it, which `eval`
  will convert `"\\\\"` to `"\\"`.

## Alternatives

If you hate gdb script and want a more common language, you can [try python](scripts/generate-gdb-prompt.sh).
