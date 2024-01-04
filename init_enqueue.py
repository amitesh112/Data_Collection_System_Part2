import faktory
import time

def enqueue_job(client, job_name):
    client.queue(job_name, queue="django_jobs", reserve_for=60*60)

if __name__ == "__main__":
    # while True:
    with faktory.connection("tcp://:fd0a59b4a5ed08a9@localhost:7419") as client:
        enqueue_job(client, "reddit_data_collection_job")
        enqueue_job(client, "chan_data_collection_job")
        # enqueue_job(client, "reddit_pol_collection_job")
        enqueue_job(client, "toxicity_reddit_job")
        enqueue_job(client, "toxicity_chan_job")
        # time.sleep(1800)  # 1800 seconds = 30 minutes
        # time.sleep(600) 
