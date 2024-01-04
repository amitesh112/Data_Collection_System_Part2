# Reddit & 4Chan Data Collection

We are collecting data from various platforms and performing analyses.

<details>
<summary><b>🚀 Data Sources & Analysis</b></summary>

- **Reddit API:** Data is collected from Reddit's API.
  
- **4Chan API:** Data from 4Chan's API is also gathered.
  
- **PostgreSQL Database:** The collected data is stored in a PostgreSQL database.
  
- **Analysis:** We conduct both sentimental and competitive analyses on the stored data.
  
- **Backend Daemon:** A backend daemon is employed to fetch data from the APIs.

- **Scheduler:** We utilize Faktory as our scheduler.

</details>

<details>
<summary><b>🛠️ Data Collection </b></summary>

- **Directory Navigation:**  
  Navigate to the directory containing `manage.py`:  
  `cd path/to/manage.py`

- **Reddit Data Collection:**  
  `python manage.py reddit_data_collection`

- **4Chan Data Collection:**  
  `python manage.py 4chan_data_collection`

- **Job Scheduling:**  
  Initialize and run the job queue:  
  `python init_enqueue.py`
  `python worker.py`


- **Faktory Web Interface:**  
Observe the Faktory dashboard at [http://localhost:7420/](http://localhost:7420/)


<summary><b>🛠️ Moderate Hate Speech Analysis </b></summary>
