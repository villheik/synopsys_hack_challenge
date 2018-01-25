from synopsys.pesti import processor
import sys

# Synopsys Finland Pesti Challenge 2018

# Loop through input in STDIN.
# Each line should have format <processpipeline> <string to process>.
#
# Prepare:
# $ pip3 install -r requirements.txt
# $ python3 -m unittest discover -v
#
# Example:
# $ echo -n 'IMTH SYNOPSYS-HAS-COOL-JOBS-OPEN-CHECK-THE-WEB' | python3 process.py
# 363861623235616665653538326662386434333162333435

if sys.version_info[0] != 3:
    print("This script requires Python 3")
    exit()

# For each line
for line in sys.stdin:
    # Split pipeline and challenge string separated by whitespace
    pipeline, input = line.rstrip().split(" ")

    # Process the challenge and print out the response
    print(processor.process(pipeline, input))

