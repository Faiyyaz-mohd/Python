import datetime

def log_run():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Script ran at: {timestamp}\n"
    
    with open("run_log.txt", "a") as log_file:
        log_file.write(log_message)

if __name__ == "__main__":
    log_run()
    print("Logged the script run successfully!")
