#!/usr/bin/env bash
# Remember
#   pip install translate-shell
#
# It will give you same appearance as this project.
# [This tool](https://github.com/Freed-Wu/translate-shell) is originally
# written for [lftp](https://github.com/lavv17/lftp/discussions/711), but in
# fact it can be helpful for many other programs.
touch ~/.config/gdb/gdbinit
install -d ~/.config/gdb/gdb
python -m translate_shell.tools.generate_prompt \
	--format='set extended-prompt {text}' \
	--prompt-string="\n(gdb) " \
	--section WHITE BLUE ' \w' \
	--section WHITE BLACK '󰊕 \f' \
	--section BLACK YELLOW ' \t ' >>~/.config/gdb/gdb/gdbinit
echo 'source ~/.config/gdb/gdb/gdbinit' >>~/.config/gdb/gdbinit
