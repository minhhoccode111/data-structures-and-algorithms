# python3


# simulate a program that processes a list of jobs in parallel

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    next_free_worker = [(0, i) for i in range(n_workers)]
    heapq.heapify(next_free_worker)

    for job in jobs:
        next_free_time, worker = heapq.heappop(next_free_worker)
        result.append(AssignedJob(worker, next_free_time))
        heapq.heappush(next_free_worker, (next_free_time + job, worker))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
