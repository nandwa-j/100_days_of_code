#mport cowsay
import sys

from sayings import hello

if len(sys.argv) == 2:
    #cowsay.cat("Hello, " + sys.argv[1])
    hello(sys.argv[1])