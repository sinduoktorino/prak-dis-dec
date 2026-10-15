class VectorClock:
    def __init__(self, num_processes, process_id):
        self.clocks = [0] * num_processes
        self.process_id = process_id

    def increment(self):
        self.clocks[self.process_id] += 1

    def send_message(self):
        self.increment()
        return list(self.clocks)

    def receive_message(self, received_clocks):
        for i in range(len(self.clocks)):
            self.clocks[i] = max(self.clocks[i], received_clocks[i])
        self.increment()

    def __str__(self):
        return f"P{self.process_id}: {self.clocks}"

    def happens_before(self, other_vector_clock):
        if self.clocks == other_vector_clock.clocks:
            return False

        all_le = True
        any_lt = False

        for i in range(len(self.clocks)):
            if self.clocks[i] > other_vector_clock.clocks[i]:
                return False
            if self.clocks[i] < other_vector_clock.clocks[i]:
                any_lt = True

        return all_le and any_lt

    def is_concurrent(self, other_vector_clock):
        return not (self.happens_before(other_vector_clock) or 
                    other_vector_clock.happens_before(self))

vc0 = VectorClock(num_processes=3, process_id=0)
vc1 = VectorClock(num_processes=3, process_id=1)
vc2 = VectorClock(num_processes=3, process_id=2)

print(vc0)
print(vc1)
print(vc2)

vc0.increment()
print(vc0)

message_from_p0 = vc0.send_message()
vc1.receive_message(message_from_p0)
print(vc0)
print(vc1)

vc2.increment()
print(vc2)

message_from_p1 = vc1.send_message()
vc2.receive_message(message_from_p1)
print(vc1)
print(vc2)

print(f"vc0 happens before vc1: {vc0.happens_before(vc1)}")
print(f"vc1 happens before vc0: {vc1.happens_before(vc0)}")
print(f"vc0 is concurrent with vc2: {vc0.is_concurrent(vc2)}")


