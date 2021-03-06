# Generated by Django 3.1.4 on 2021-01-04 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(blank=True, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('total_amount', models.CharField(max_length=30)),
                ('currency', models.CharField(choices=[('KES', 'KES'), ('USD', 'USD')], max_length=20)),
                ('payment_status', models.CharField(choices=[('Awaiting Payment', 'Awaiting Payment'), ('Payment Recieved', 'Payment Received'), ('Payment Updated', 'Payment Updated:'), ('Completed', 'Completed'), ('Partially Refunded', 'Refunded (Partially)'), ('Refunded', 'Refunded'), ('Failed', 'Failed'), ('Cancelled', 'Cancelled'), ('Expired', 'Expired')], default='A', max_length=20)),
                ('order_items', models.TextField(default='[]', null=True, verbose_name='items')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillingInfo',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='checkout.order')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='checkout.order')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=50, null=True)),
                ('amount', models.CharField(default=0, max_length=20)),
                ('currency', models.CharField(choices=[('KES', 'KES'), ('USD', 'USD')], max_length=20)),
                ('method', models.CharField(choices=[('Mpesa', 'MPESA'), ('Paypal', 'PAYPAL'), ('Voucher', 'VOUCHER')], max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
            ],
        ),
    ]
