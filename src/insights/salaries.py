from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = [int(job.get('max_salary', 0)) for job in self.jobs_list if
                    job.get('max_salary').isdigit()]
        return max(salaries, default=0)

    def get_min_salary(self) -> int:
        salaries = [int(job.get('min_salary', float('inf'))) for job in
                    self.jobs_list if job.get('min_salary').isdigit()]
        return min(salaries, default=float('inf'))

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            min_salary = float(job['min_salary'])
            max_salary = float(job['max_salary'])

            if min_salary > max_salary:
                raise ValueError

            return min_salary <= float(salary) <= max_salary
        except (ValueError, TypeError) as e:
            raise ValueError(f"Erro ao processar salários: {e}")
        except KeyError:
            raise ValueError("""As chaves 'min_salary' e 'max_salary' são
                              obrigatórias""")

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
