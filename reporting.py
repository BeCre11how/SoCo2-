import sys
import csv
from datetime import datetime

def read_trace_file(trace_file_path):
    """ Reads the trace file and returns a list of events. """
    with open(trace_file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)

def calculate_durations(trace_events):
    """ Calculates the durations of each function call. """
    start_times = {}
    durations = {}

    for event in trace_events:
        function_id = event['id']
        function_name = event['function_name']
        timestamp = datetime.strptime(event['timestamp'], '%Y-%m-%d %H:%M:%S.%f')

        if event['event'] == 'start':
            start_times[function_id] = timestamp
        elif event['event'] == 'stop' and function_id in start_times:
            duration = (timestamp - start_times[function_id]).total_seconds() * 1000  # convert to milliseconds
            if function_name not in durations:
                durations[function_name] = []
            durations[function_name].append(duration)

    return durations

def calculate_statistics(durations):
    """ Calculates the number of calls, total time, and average time per function. """
    stats = {}
    for function_name, times in durations.items():
        total_time = sum(times)
        num_calls = len(times)
        avg_time = total_time / num_calls
        stats[function_name] = {
            'num_calls': num_calls,
            'total_time': total_time,
            'avg_time': avg_time
        }
    return stats

def print_report(stats):
    """ Prints out the report in a table format. """
    print("| Function Name  | Num. of calls | Total Time (ms) | Average Time (ms) |")
    print("|----------------|---------------|-----------------|-------------------|")
    for function_name, data in stats.items():
        print(f"| {function_name.ljust(15)}| {str(data['num_calls']).center(15)} | "
              f"{data['total_time']:>15.3f} | {data['avg_time']:>17.3f} |")

def main(trace_file_path):
    trace_events = read_trace_file(trace_file_path)
    durations = calculate_durations(trace_events)
    stats = calculate_statistics(durations)
    print_report(stats)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reporting.py trace_file.log")
        sys.exit(1)
    trace_file_path = sys.argv[1]
    main(trace_file_path)

