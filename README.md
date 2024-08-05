# simple_log_generator
Simple script to read from sample.log file and randomly inserts line into output.log 
# How it works:
1. The script reads sample .log file
2. Randomly choses line
3. Clears the write_to_file = "/path/to/location/output.log" before generating logs
4. Writes to write_to_file = "/path/to/location/output.log"
5. The amount is taken from the user input in the boundaries 1 <= Log lines <= 10 000

# How to use:
logs_per_second = 150  # how many logs per second to write
delay = 1.0 / logs_per_second
sample_log_f = "/var/log/sample_log.log"  # Sample file containing actual logs
write_to_file = "/path/to/location/output.log"  # Output file where the logs will be randomly generated

