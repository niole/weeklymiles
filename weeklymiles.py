import argparse

parser = argparse.ArgumentParser(description='Get the rolling weekly mileage average per day.')
parser.add_argument('--avgs', type=int, nargs='+',
                    help='Get the rolling weekly average per day given a log of previous mileage')

parser.add_argument('--prcnt', dest='prcnt', action='store_const',
                    const=True, default=False, help='Whether or not to show the rolling percent increase over last week')

args = parser.parse_args()

print(args.prcnt)

avgs = args.avgs
aggregated = [0 for _ in range(len(avgs))]
percent_increase = [0 for _ in range(len(avgs))]
if len(avgs) >= 1:
    aggregated[0] = avgs[0]

if len(avgs) > 1:
    for i in range(1, len(avgs)):
        aggregated[i] = avgs[i] + aggregated[i-1]
        if i >= 7:
            aggregated[i] -= avgs[i-7]

        if i >= 14:
            percent_increase[i] = ((aggregated[i] - aggregated[i-7])/float(aggregated[i-7]))*100

if args.prcnt:
    print(zip(aggregated, percent_increase))
else:
    print(aggregated)
