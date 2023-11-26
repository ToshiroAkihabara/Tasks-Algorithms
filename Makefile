# pip-tools

comp:
	pip-compile

sync:
	pip-sync


# pre-commit

check:
	pre-commit run --show-diff-on-failure --color=always --all-files
