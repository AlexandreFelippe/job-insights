from src.insights.jobs import ProcessJobs
from typing import List  # inicio


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industries = []
        for job in self.jobs_list:
            industry = job.get('industry')
            if industry and industry not in unique_industries:
                unique_industries.append(industry)

        return unique_industries
