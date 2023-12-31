from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=40)),
                ("birth_date", models.DateField(auto_now=True)),
                ("has_pet", models.BooleanField(default=True)),
                ("number_pet", models.IntegerField()),
            ],
        ),
    ]
