import pstats
import os
from time import sleep

cmd="python -m cProfile -o profile.stats Profiling/julia_set.py"
os.system(cmd)

#sleep(5)
p= pstats.Stats("profile.stats")
p.sort_stats("cumulative")
#p.print_stats()
#p.print_callers()
p.print_callees()