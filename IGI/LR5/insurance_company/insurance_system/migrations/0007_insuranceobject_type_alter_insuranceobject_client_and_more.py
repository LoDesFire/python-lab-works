# Generated by Django 5.0.6 on 2024-05-27 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "insurance_system",
            "0006_remove_insurancecontract_branch_agent_salary_and_more",
        ),
        ("users", "0007_client_birth_employee_birth"),
    ]

    operations = [
        migrations.AddField(
            model_name="insuranceobject",
            name="type",
            field=models.ForeignKey(
                default=123,
                on_delete=django.db.models.deletion.CASCADE,
                to="insurance_system.insurancetype",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="insuranceobject",
            name="client",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.client",
            ),
        ),
        migrations.AlterField(
            model_name="insuranceobject",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
