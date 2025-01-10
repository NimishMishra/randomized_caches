import concurrent.futures
import os
import time
import random


def job_function(job_id, core_id): 
    try:
        os.sched_setaffinity(0, {core_id})
        print(f"Job {job_id} pinned to core {core_id}")
    except AttributeError:
        print(f"Core pinning not supported on this platform. Job {job_id} will run without pinning.")
    
    print(f"Job {job_id} started on core {core_id}.")
    command = "/home/nimish/mirage/perf_analysis/gem5/build/X86/gem5.opt --outdir ./stats/stat_{stat} /home/nimish/mirage/perf_analysis/gem5/configs/example/spec06_config_multiprogram.py --benchmark=specrand_i --num-cpus=1 --mem-size=8GB --mem-type=DDR4_2400_8x8 --cpu-type TimingSimpleCPU --caches --l2cache --l1d_size=512B --l1i_size=32kB --l2_size=16MB --l1d_assoc=8 --l1i_assoc=8 --l2_assoc=16 --mirage_mode=scatter-cache --l2_numSkews=2 --l2_TDR=1.75 --l2_EncrLat=3 --prog-interval=300Hz > scatter_logs/log_{iden}".format(stat=job_id, iden=job_id)
    os.system(command)
    print(f"Job {job_id} finished on core {core_id} after {execution_time} seconds.")
    return job_id


def schedule_jobs_with_pinning(total_jobs, max_cores):
    completed_jobs = 0
    job_queue = list(range(total_jobs))
    active_jobs = {}
    core_pool = list(range(max_cores)) 

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_cores) as executor:
        while completed_jobs < total_jobs:
            while len(active_jobs) < max_cores and job_queue and core_pool:
                job_id = job_queue.pop(0)
                core_id = core_pool.pop(0)
                future = executor.submit(job_function, job_id, core_id)
                active_jobs[future] = core_id
                print(f"Job {job_id} submitted to core {core_id}.")

            done, _ = concurrent.futures.wait(
                active_jobs.keys(), return_when=concurrent.futures.FIRST_COMPLETED
            )
            for future in done:
                core_id = active_jobs.pop(future)
                completed_jobs += 1
                core_pool.append(core_id)
                print(f"Core {core_id} is now free.")


                if job_queue:
                    new_job_id = job_queue.pop(0)
                    core_id = core_pool.pop(0)
                    future = executor.submit(job_function, new_job_id, core_id)
                    active_jobs[future] = core_id
                    print(f"Job {new_job_id} submitted to core {core_id}.")

    print("All jobs have been completed.")


if __name__ == "__main__":
    # Takes approximate 12 hours
    total_jobs = 3840 
    max_cores = 80
    schedule_jobs_with_pinning(total_jobs, max_cores)
