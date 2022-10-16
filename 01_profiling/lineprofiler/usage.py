import os
# pip install line_profiler
cmd="python -m kernprof -l -v Profiling/lineprofiler/to_be_profiled.py"
os.system(cmd)