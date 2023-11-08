import sys
import csv
from datetime import datetime, timedelta

##READ FILE

def read_trace_file(trace_file_path):
    with open(trace_file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)

##CALCULATE DURATIONS
def calculate_durations(trace_events):
    event_durations = []
    ids = {}
    
    for event in trace_events:
        if event["id"] not in ids:
            start_time = event["timestamp"]
            ids[event["id"]] = start_time
            
        else:
            event_dict = {}
            start_time = datetime.strptime(ids.get(event["id"]), "%Y-%m-%d %H:%M:%S.%f")
            stop_time = datetime.strptime(event["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
            duration = (stop_time - start_time).total_seconds() * 1000
   
            event_dict["id"], event_dict["function_name"], event_dict["duration"] = event["id"], event["function_name"], duration
            event_durations.append(event_dict)

    return event_durations

##SORT FUNCTIONS BY NAME AND CALCULATE NUM OF CALLS, AVERAGE TIME AND TOTAL TIME
def sort_functions_by_name(event_durations):
    stats_temp = {}
    stats = []
    
    for event in event_durations:
        function_name = event['function_name']
        duration = event['duration']
        if function_name in stats_temp:
            stats_temp[function_name]["Num. of calls"] += 1
            stats_temp[function_name]["Total Time (ms)"] += duration
        else:
            stats_temp[function_name] = {
                "Num. of calls": 1,
                "Total Time (ms)": duration,
            }
    
    for function_name in stats_temp:
        stats_temp[function_name]["Average Time (ms)"] = stats_temp[function_name]["Total Time (ms)"] / stats_temp[function_name]["Num. of calls"]
        
    for name in stats_temp:
        stats.append([name, stats_temp[name]["Num. of calls"], stats_temp[name]["Total Time (ms)"], stats_temp[name]["Average Time (ms)"]])

    return stats


##PRINT REPORT
def print_report(stats):
    print("| Function Name  | Num. of calls | Total Time (ms) | Average Time (ms) |")
    print("|----------------|---------------|-----------------|-------------------|")
    for element in stats:
        print(f"| {element[0].ljust(15)}|{str(element[1]).center(15)}| " 
              f"{element[2]:>15.3f} | {element[3]:>17.3f} |")


##ENTRY POINT TO SCRIPT
def main(trace_file_path):
    trace_events = read_trace_file(trace_file_path)
    event_durations = calculate_durations(trace_events)
    stats = sort_functions_by_name(event_durations)
    print_report(stats)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reporting.py trace_file.log")
        sys.exit(1)
    trace_file_path = sys.argv[1]
    main(trace_file_path)

