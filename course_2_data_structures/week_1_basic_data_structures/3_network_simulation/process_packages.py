# python3

# implement a program to simulate the processing of network packages

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.current_time = 0

    def process(self, request):
        while self.finish_time and self.finish_time[0] <= request.arrived_at:
            self.finish_time.pop(0)

        self.current_time = max(self.current_time, request.arrived_at)

        if len(self.finish_time) >= self.size:
            return Response(True, -1)

        if not self.finish_time:
            start_time = request.arrived_at
        else:
            start_time = max(request.arrived_at, self.finish_time[-1])

        self.finish_time.append(start_time + request.time_to_process)
        return Response(False, start_time)


def process_requests(requests, buffer):
    return [buffer.process(request) for request in requests]


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
