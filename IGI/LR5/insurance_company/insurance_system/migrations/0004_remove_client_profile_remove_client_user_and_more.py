# Generated by Django 5.0.6 on 2024-05-25 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company_info", "0005_alter_review_client_delete_employee"),
        ("insurance_system", "0003_client_user"),
        ("users", "0002_profile_employee_client"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="profile",
        ),
        migrations.RemoveField(
            model_name="client",
            name="user",
        ),
        migrations.AlterField(
            model_name="insuranceobject",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.client"
            ),
        ),
        migrations.AlterField(
            model_name="clientagent",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.client"
            ),
        ),
        migrations.AlterField(
            model_name="agent",
            name="clients",
            field=models.ManyToManyField(
                through="insurance_system.ClientAgent", to="users.client"
            ),
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
        migrations.DeleteModel(
            name="Client",
        ),
    ]
