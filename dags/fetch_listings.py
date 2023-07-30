""" Fetch Property Listings DAG """
from pendulum import datetime
from airflow.decorators import dag
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from fetch_city_listings import fetch_city_listings


default_args = {
    "retries": 5,
}


@dag(
    dag_id="fetch_listings_dag_v3",
    start_date=datetime(2023, 7, 27, tz="Asia/Riyadh"),
    schedule="@daily",
    catchup=False,
    default_args=default_args
)
def fetch_listings():
    """ fetch_listings() DAG """

    clear_property_listings_table_task = SqliteOperator(
        task_id="clear_property_listings_table_task",
        sqlite_conn_id="dealapp.db",
        sql=r"DELETE FROM property_listings"
    )

    fetch_riyadh_listings_task = PythonOperator(
        task_id="fetch_riyadh_listings_task",
        python_callable=fetch_city_listings,
        op_args=["riyadh"]
    )

    fetch_jeddah_listings_task = PythonOperator(
        task_id="fetch_jeddah_listings_task",
        python_callable=fetch_city_listings,
        op_args=["jeddah"]
    )

    fetch_dammam_listings_task = PythonOperator(
        task_id="fetch_dammam_listings_task",
        python_callable=fetch_city_listings,
        op_args=["dammam"]
    )

    fetch_khobar_listings_task = PythonOperator(
        task_id="fetch_khobar_listings_task",
        python_callable=fetch_city_listings,
        op_args=["khobar"]
    )

    fetch_mekkah_listings_task = PythonOperator(
        task_id="fetch_mekkah_listings_task",
        python_callable=fetch_city_listings,
        op_args=["mekkah"]
    )

    fetch_medina_listings_task = PythonOperator(
        task_id="fetch_medina_listings_task",
        python_callable=fetch_city_listings,
        op_args=["medina"]
    )

    fetch_buraidah_listings_task = PythonOperator(
        task_id="fetch_buraidah_listings_task",
        python_callable=fetch_city_listings,
        op_args=["buraidah"]
    )

    fetch_taif_listings_task = PythonOperator(
        task_id="fetch_taif_listings_task",
        python_callable=fetch_city_listings,
        op_args=["taif"]
    )

    fetch_abha_listings_task = PythonOperator(
        task_id="fetch_abha_listings_task",
        python_callable=fetch_city_listings,
        op_args=["abha"]
    )

    fetch_ahsa_listings_task = PythonOperator(
        task_id="fetch_ahsa_listings_task",
        python_callable=fetch_city_listings,
        op_args=["ahsa"]
    )

    fetch_jubail_listings_task = PythonOperator(
        task_id="fetch_jubail_listings_task",
        python_callable=fetch_city_listings,
        op_args=["jubail"]
    )

    fetch_khamis_mushait_listings_task = PythonOperator(
        task_id="fetch_khamis_mushait_listings_task",
        python_callable=fetch_city_listings,
        op_args=["khamis mushait"]
    )

    clear_property_listings_table_task >> [
        fetch_riyadh_listings_task,
        fetch_jeddah_listings_task,
        fetch_dammam_listings_task,
        fetch_khobar_listings_task,
        fetch_mekkah_listings_task,
        fetch_medina_listings_task,
        fetch_buraidah_listings_task,
        fetch_taif_listings_task,
        fetch_abha_listings_task,
        fetch_ahsa_listings_task,
        fetch_jubail_listings_task,
        fetch_khamis_mushait_listings_task,
    ]


FETCH_LISTINGS_DAG = fetch_listings()
