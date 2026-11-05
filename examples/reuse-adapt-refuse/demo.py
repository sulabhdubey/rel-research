"""Run the three-path demonstration; standard library only, no network/model calls."""
import json
from time import perf_counter, process_time
from walkthrough import sequence

if __name__ == '__main__':
    wall, cpu = perf_counter(), process_time()
    cases = sequence()
    print(json.dumps({'kind': 'constructed_demonstration', 'cases': cases,
                      'execution_wall_seconds': perf_counter()-wall,
                      'execution_cpu_seconds': process_time()-cpu,
                      'limits': 'Historical SQL is reused. Routing and rows are authored for this demonstration; no new learning trial.'}, indent=2))
