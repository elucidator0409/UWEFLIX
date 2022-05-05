# Generated by Django 4.0.4 on 2022-05-04 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_paymentintent_seat_payment_moviebooked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviebooked',
            name='booked_seats',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='movie',
        ),
        migrations.DeleteModel(
            name='PaymentIntent',
        ),
        migrations.AddField(
            model_name='seat',
            name='no',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_type',
            field=models.CharField(choices=[('', 'Select'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], default='', max_length=8),
        ),
        migrations.AddField(
            model_name='seat',
            name='show',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='booking.show'),
        ),
        migrations.AlterField(
            model_name='bookedseat',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.seat'),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('no', 'show')},
        ),
        migrations.DeleteModel(
            name='MovieBooked',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Seats',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='occupant_email',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='occupant_first_name',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='occupant_last_name',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='purchase_time',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='seat_no',
        ),
    ]