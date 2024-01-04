import os
import logging
import logging.handlers
import faktory

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1_implementation.settings')

# Define a logging handler that rotates the file when it reaches a certain size
class SingleFileRotatingHandler(logging.handlers.RotatingFileHandler):
    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        if os.path.exists(self.baseFilename):
            os.remove(self.baseFilename)
        self.mode = 'a'
        self.stream = self._open()

# Configure the root logger with a formatter and handlers
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)

fileHandler = SingleFileRotatingHandler('jobs_log.log', maxBytes=5*1024*1024, backupCount=0)  # 5 MB max size
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

# Define the job functions
def toxicity_chan_job():
    logging.info("Starting toxicity_chan command")
    os.system('python manage.py toxicity_chan')
    logging.info("Finished toxicity_chan command")
    schedule_next_run('toxicity_chan_job', 600)  

def toxicity_reddit_job():
    logging.info("Starting toxicity_reddit command")
    os.system('python manage.py toxicity_reddit')
    logging.info("Finished toxicity_reddit command")
    schedule_next_run('toxicity_reddit_job', 600)

def reddit_data_collection_job():
    logging.info("Starting reddit_data_collection command")
    os.system('python manage.py reddit_data_collection')
    logging.info("Finished reddit_data_collection command")
    schedule_next_run('reddit_data_collection_job', 600)

def reddit_pol_collection_job():
    logging.info("Starting reddit_politics command")
    os.system('python manage.py reddit_politics')
    logging.info("Finished reddit_politics command")
    schedule_next_run('reddit_pol_collection_job', 600)

def chan_data_collection_job():
    logging.info("Starting 4chan_data_collection command")
    os.system('python manage.py 4chan_data_collection')
    logging.info("Finished 4chan_data_collection command")
    schedule_next_run('chan_data_collection_job',600)

# Helper function to enqueue the next run of a job
def schedule_next_run(job_name, delay_seconds):
    with faktory.connection("tcp://:fd0a59b4a5ed08a9@localhost:7419") as client:
        client.queue(job_name, queue="django_jobs", reserve_for=delay_seconds)

# The main function that enqueues all the jobs
def main():
    schedule_next_run('toxicity_chan_job', 0)
    schedule_next_run('toxicity_reddit_job', 0)
    schedule_next_run('reddit_data_collection_job', 0)
    schedule_next_run('reddit_pol_collection_job', 0)
    schedule_next_run('chan_data_collection_job', 0)

if __name__ == "__main__":
    main()
