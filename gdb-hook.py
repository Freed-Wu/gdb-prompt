r"""GDB hook
============
"""
import os
import sys

hook_names = os.getenv("HOOK_NAMES", "wakatime")

prefixs = [
    "/usr",
    "/usr/local",
    "/run/current-system/sw",
    "/data/data/com.termux/files/usr",
    "~/.local/state/nix/profile",
]

for prefix in prefixs:
    path = os.path.expanduser(
        os.path.join(
            prefix,
            f"lib/python{sys.version_info[0]}.{sys.version_info[1]}/site-packages",
        )
    )
    if os.path.isdir(path):
        sys.path.insert(0, path)

for hook_name in hook_names.split(":"):
    if hook_name == "wakatime":
        from repl_python_wakatime.hooks.wakatime import wakatime_hook as hook
    elif hook_name == "codestats":
        from repl_python_wakatime.hooks.codestats import codestats_hook as hook
    else:
        raise NotImplementedError
    hook(plugin="repl-gdb-wakatime", language="gdb", category="debugging")
