import pendulum

from airflow.sdk import dag, task

from .form_processing import main_process_forms


@dag(
    dag_id="forms_processing",
    schedule="@daily",
    start_date=pendulum.datetime(2026, 1, 1, tz="Europe/Oslo"),
    catchup=False,
)
def forms_processing():

    @task
    def process():
        main_process_forms()

    process()


forms_processing()