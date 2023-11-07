from django.db import migrations


def forwards_func(apps, _):
    service_model = apps.get_model("Apps", "Service")
    services = ["facebook", "youtube", "zalo"]
    for service in services:
        service_model.objects.create(name=service)


def reverse_func(_, __):
    ...


class Migration(migrations.Migration):
    dependencies = [
        ('Apps', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
