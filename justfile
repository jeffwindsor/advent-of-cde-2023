
# this list of available functions
default:
	just --list

# start ide for project
dev:
	zellij --layout	dev.kdl

# enter development shell
shell:
	nix-shell --run 'clear'

# python run file on all changes
run FILE:
	nix-shell --run 'echo {{FILE}} | entr -s "clear && python {{FILE}}"'

# pytest run on all changes
test FILE:
	nix-shell --run 'echo {{FILE}} | entr -s "clear && pytest -v {{FILE}}"'

# simple repl
repl:
	nix-shell --run 'clear && python'
