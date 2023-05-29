
from factory import Factory
import pandas as pd
import factory


class CompanyStaff(Factory):
    class Meta:
        model = dict

    first_name = factory.Faker("first_name")
    last_name = factory.Faker('last_name')
    age = factory.Faker('random_int', min=21, max=60)
    job_title = factory.Faker('job' or None)
    salary = factory.Faker('random_int', min=-2000, max=5000 )
    work_experience = factory.Faker('random_int', min=0, max=40)


num_rows = 100

staff = CompanyStaff.create_batch(num_rows)

df = pd.DataFrame(staff)
df.to_csv('staff.csv')

print(df)
