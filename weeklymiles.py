import argparse

parser = argparse.ArgumentParser(description='Get the rolling weekly mileage average per day.')
parser.add_argument('--avgs', type=int, nargs='+',
                    help='Get the rolling weekly average per day given a log of previous mileage')

args = parser.parse_args()

avgs = args.avgs
aggregated = [0 for _ in range(len(avgs))]
if len(avgs) >= 1:
    aggregated[0] = avgs[0]

if len(avgs) > 1:
    for i in range(1, len(avgs)):
        aggregated[i] = avgs[i] + aggregated[i-1]
        if i >= 7:
            aggregated[i] -= avgs[i-7]

print(aggregated)
