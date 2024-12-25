# python3


# implement a has table using the chaining scheme


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == "check":
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print("yes" if was_found else "no")

    def write_chain(self, chain):
        if chain:
            print(" ".join(chain))
        else:
            print()

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.buckets[query.ind])
        else:
            hash_value = self._hash_func(query.s)
            if query.type == "find":
                self.write_search_result(query.s in self.buckets[hash_value])
            elif query.type == "add":
                if query.s not in self.buckets[hash_value]:
                    self.buckets[hash_value].insert(0, query.s)
            else:
                if query.s in self.buckets[hash_value]:
                    self.buckets[hash_value].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == "__main__":
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
