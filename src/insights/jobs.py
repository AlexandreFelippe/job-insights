from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.jobs_list.append(row)

    def get_unique_job_types(self) -> List[str]:
        # A função deve retornar uma lista de valores únicos presentes na coluna job_type
        unique_job_types = list()
        for job in self.jobs_list:
            if job["job_type"] not in unique_job_types:
                unique_job_types.append(job["job_type"])

        return unique_job_types

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
