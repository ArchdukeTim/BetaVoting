import csv
import sys


class Vote:
    def __init__(self, vote):
        self.vote = [int(i) for i in vote]

    def remove_vote(self, votenum):
        self.vote = [i for i in self.vote if i is not votenum]


LOST_CANDIDATES = set([])
candidates = []


def count_votes():
    while True:
        current_votes = [0] * CANDIDATES
        for vote in votes:
            current_votes[vote.vote[0] - 1] += 1

        low = max(current_votes)
        for i, val in enumerate(current_votes):
            if i + 1 not in LOST_CANDIDATES:
                if val < low:
                    low = val

        out_this_round = []
        for i, c in enumerate(current_votes):
            if c == low and i + 1 not in LOST_CANDIDATES:
                out_this_round.append(i + 1)

        if len(out_this_round) > 1:
            if len(LOST_CANDIDATES) + len(out_this_round) >= CANDIDATES:
                print("There's a tie between candidates. Please choose between ",
                      [candidate for i, candidate in enumerate(candidates) if i + 1 in out_this_round])
                exit(0)
            else:
                for i in out_this_round:
                    LOST_CANDIDATES.add(i)
        else:
            LOST_CANDIDATES.add(out_this_round[0])

        for vote in votes:
            for i in out_this_round:
                vote.remove_vote(i)

        if len(LOST_CANDIDATES) == CANDIDATES - 1:
            print('Winner: ', candidates[sum(range(1, CANDIDATES + 1)) - sum(list(LOST_CANDIDATES)) - 1])
            break


if __name__ == '__main__':
    CANDIDATES = int(sys.argv[2])
    with open(sys.argv[1], newline='') as f:
        votereader = list(csv.reader(f))
        candidates = votereader[1][-CANDIDATES:]
        candidates = [candidate.split('-')[1].strip() for candidate in candidates]
        print('Candidates:', ', '.join(candidates))
        print()
        print('Ballots')
        votereader = votereader[3:]

votereader = [vote[-6:] for vote in votereader]
for row in votereader:
    print([candidates[int(i) - 1] for i in row])
votes = [Vote(vote) for vote in votereader]

print()
count_votes()
