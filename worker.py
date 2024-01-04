import logging
from faktory import Worker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1_implementation.settings')


from django_jobs import reddit_data_collection_job, chan_data_collection_job, reddit_pol_collection_job, toxicity_chan_job,toxicity_reddit_job
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1_implementation.settings')

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    w = Worker("tcp://:fd0a59b4a5ed08a9@localhost:7419", queues=["django_jobs"], concurrency=4)
    w.register("reddit_data_collection_job", reddit_data_collection_job)
    # w.register("reddit_pol_collection_job", reddit_pol_collection_job)
    w.register("chan_data_collection_job", chan_data_collection_job)
    w.register("toxicity_reddit_job", toxicity_reddit_job)
    w.register("toxicity_chan_job", toxicity_chan_job)

    w.run()
