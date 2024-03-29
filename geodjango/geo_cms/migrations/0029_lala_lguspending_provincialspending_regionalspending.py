# Generated by Django 2.2.5 on 2019-09-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0028_auto_20190913_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='LguSpending',
            fields=[
                ('x', models.IntegerField(blank=True, db_column='X', null=True)),
                ('lgu', models.TextField(blank=True, db_column='LGU', primary_key=True, serialize=False)),
                ('delete', models.FloatField(blank=True, null=True)),
                ('general_administration', models.FloatField(blank=True, db_column='GENERAL.ADMINISTRATION', null=True)),
                ('elementary_school', models.FloatField(blank=True, db_column='ELEMENTARY.SCHOOL', null=True)),
                ('secondary_school', models.FloatField(blank=True, db_column='SECONDARY.SCHOOL', null=True)),
                ('university_college_education_school', models.FloatField(blank=True, db_column='UNIVERSITY.COLLEGE.EDUCATION.SCHOOL', null=True)),
                ('vocational_technical_school', models.FloatField(blank=True, db_column='VOCATIONAL...TECHNICAL.SCHOOL', null=True)),
                ('adult_education', models.FloatField(blank=True, db_column='ADULT.EDUCATION', null=True)),
                ('education_subsidiary_services', models.FloatField(blank=True, db_column='EDUCATION.SUBSIDIARY.SERVICES', null=True)),
                ('manpower_development_mangement_tool', models.FloatField(blank=True, db_column='MANPOWER.DEVELOPMENT.MANGEMENT.TOOL', null=True)),
                ('maintenance_of_sports_center_athletic_fields_playground', models.FloatField(blank=True, db_column='MAINTENANCE.OF.SPORTS.CENTER..ATHLETIC.FIELDS..PLAYGROUND', null=True)),
                ('loan_amortization_domestic_debt_service_principal_field', models.FloatField(blank=True, db_column='LOAN.AMORTIZATION.DOMESTIC.DEBT.SERVICE.PRINCIPAL.', null=True)),
                ('interest_payment_domestic_debt_service_interest_field', models.FloatField(blank=True, db_column='INTEREST.PAYMENT.DOMESTIC.DEBT.SERVICE.INTEREST.', null=True)),
                ('others', models.FloatField(blank=True, db_column='OTHERS', null=True)),
                ('year', models.IntegerField(blank=True, db_column='Year', null=True)),
            ],
            options={
                'db_table': 'lgu_spending',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvincialSpending',
            fields=[
                ('x', models.IntegerField(blank=True, db_column='X', null=True)),
                ('province', models.TextField(blank=True, db_column='Province', primary_key=True, serialize=False)),
                ('delete', models.FloatField(blank=True, null=True)),
                ('general_administration', models.FloatField(blank=True, db_column='GENERAL.ADMINISTRATION', null=True)),
                ('elementary_school', models.FloatField(blank=True, db_column='ELEMENTARY.SCHOOL', null=True)),
                ('secondary_school', models.FloatField(blank=True, db_column='SECONDARY.SCHOOL', null=True)),
                ('university_college_education_school', models.FloatField(blank=True, db_column='UNIVERSITY.COLLEGE.EDUCATION.SCHOOL', null=True)),
                ('vocational_technical_school', models.FloatField(blank=True, db_column='VOCATIONAL...TECHNICAL.SCHOOL', null=True)),
                ('adult_education', models.FloatField(blank=True, db_column='ADULT.EDUCATION', null=True)),
                ('education_subsidiary_services', models.FloatField(blank=True, db_column='EDUCATION.SUBSIDIARY.SERVICES', null=True)),
                ('manpower_development_mangement_tool', models.FloatField(blank=True, db_column='MANPOWER.DEVELOPMENT.MANGEMENT.TOOL', null=True)),
                ('maintenance_of_sports_center_athletic_fields_playground', models.FloatField(blank=True, db_column='MAINTENANCE.OF.SPORTS.CENTER..ATHLETIC.FIELDS..PLAYGROUND', null=True)),
                ('loan_amortization_domestic_debt_service_principal_field', models.FloatField(blank=True, db_column='LOAN.AMORTIZATION.DOMESTIC.DEBT.SERVICE.PRINCIPAL.', null=True)),
                ('interest_payment_domestic_debt_service_interest_field', models.FloatField(blank=True, db_column='INTEREST.PAYMENT.DOMESTIC.DEBT.SERVICE.INTEREST.', null=True)),
                ('others', models.FloatField(blank=True, db_column='OTHERS', null=True)),
                ('year', models.IntegerField(blank=True, db_column='Year', null=True)),
            ],
            options={
                'db_table': 'provincial_spending',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegionalSpending',
            fields=[
                ('x', models.IntegerField(blank=True, db_column='X', null=True)),
                ('region', models.TextField(blank=True, db_column='Region', primary_key=True, serialize=False)),
                ('delete', models.FloatField(blank=True, null=True)),
                ('general_administration', models.FloatField(blank=True, db_column='GENERAL.ADMINISTRATION', null=True)),
                ('elementary_school', models.FloatField(blank=True, db_column='ELEMENTARY.SCHOOL', null=True)),
                ('secondary_school', models.FloatField(blank=True, db_column='SECONDARY.SCHOOL', null=True)),
                ('university_college_education_school', models.FloatField(blank=True, db_column='UNIVERSITY.COLLEGE.EDUCATION.SCHOOL', null=True)),
                ('vocational_technical_school', models.FloatField(blank=True, db_column='VOCATIONAL...TECHNICAL.SCHOOL', null=True)),
                ('adult_education', models.FloatField(blank=True, db_column='ADULT.EDUCATION', null=True)),
                ('education_subsidiary_services', models.FloatField(blank=True, db_column='EDUCATION.SUBSIDIARY.SERVICES', null=True)),
                ('manpower_development_mangement_tool', models.FloatField(blank=True, db_column='MANPOWER.DEVELOPMENT.MANGEMENT.TOOL', null=True)),
                ('maintenance_of_sports_center_athletic_fields_playground', models.FloatField(blank=True, db_column='MAINTENANCE.OF.SPORTS.CENTER..ATHLETIC.FIELDS..PLAYGROUND', null=True)),
                ('loan_amortization_domestic_debt_service_principal_field', models.FloatField(blank=True, db_column='LOAN.AMORTIZATION.DOMESTIC.DEBT.SERVICE.PRINCIPAL.', null=True)),
                ('interest_payment_domestic_debt_service_interest_field', models.FloatField(blank=True, db_column='INTEREST.PAYMENT.DOMESTIC.DEBT.SERVICE.INTEREST.', null=True)),
                ('others', models.FloatField(blank=True, db_column='OTHERS', null=True)),
                ('year', models.IntegerField(blank=True, db_column='Year', null=True)),
            ],
            options={
                'db_table': 'regional_spending',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(choices=[('remoteness', 'Remoteness Index'), ('total_reci', "Total Number of Learners Receiving CCT's"), ('cct_percen', "Percentage of Students Recieving CCT's"), ('original_w', 'Water Access'), ('original_i', 'Internet Access'), ('original_e', 'Electricty Access'), ('total_enro', 'Total Number of Learners with Gender Distribution'), ('pwd_total', 'Total Number of Learners With Disability')], max_length=1)),
            ],
        ),
    ]
