"""
    Z listy pracowników czyli elementów typu Worker(każdy pracownik posiada name oraz salary) wyznacz tych
    pracowników, których pensja mieści się w przedziale [salary_min, salary_max].
"""

from collections import namedtuple
from dataclasses import dataclass
from decimal import Decimal

# Worker = namedtuple('Worker', 'name, salary')
#
# def get_workers_with_salary_between(salary_min: float, salary_max: float, workers: list['Worker']) -> list['Worker']:
#     expected_workers = []
#     for worker in workers:
#         if worker.salary >= salary_min and worker.salary <= salary_max:
#             expected_workers.append(worker)
#     return expected_workers


@dataclass
class Worker:
    name: str
    salary: Decimal

    def has_salary_between(self, salary_min: Decimal, salary_max: Decimal) -> bool:
        return salary_min <= self.salary <= salary_max

    @staticmethod
    def get_workers_with_salary_between(salary_min: Decimal, salary_max: Decimal, workers: list['Worker']) -> list['Worker']:
        return [worker for worker in workers if worker.has_salary_between(salary_min, salary_max)]

def main() -> None:

    workers = [
        Worker(name='JAN', salary=Decimal('1200')),
        Worker(name='IZA', salary=Decimal('1400')),
        Worker(name='EWA', salary=Decimal('2300')),
        Worker(name='ALA', salary=Decimal('2100')),
        Worker(name='ELA', salary=Decimal('3200')),
        Worker(name='IGOR', salary=Decimal('3400'))
    ]

    expected_workers = Worker.get_workers_with_salary_between(Decimal('1000'), Decimal('2000'), workers)
    print(expected_workers)

if __name__ == '__main__':
    main()
