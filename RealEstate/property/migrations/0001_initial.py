import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_alter_userprofile_profile_picture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Property_Name', models.CharField(max_length=200)),
                ('Property_Description', models.TextField(blank=True, null=True)),
                ('Total_area_in_sqft', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('Price', models.IntegerField(default=0)),
                ('Property_Pictures', models.ImageField(default=None, upload_to='pics')),
                ('Road_No', models.CharField(max_length=4)),
                ('Block', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=100)),
                ('Postal_code', models.CharField(max_length=4)),
                ('District', models.CharField(max_length=100)),
                ('Property_on', models.CharField(choices=[('rent', 'Rent'), ('sell', 'Sell')], max_length=20, null=True)),
                ('Property_type', models.CharField(choices=[('commercial', 'Commercial'), ('land', 'Land'), ('residential', 'Residential')], max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='authentication.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='CommercialProperty',
            fields=[
                ('allproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='property.allproperty')),
                ('House_No', models.CharField(max_length=8)),
                ('Business_type', models.CharField(choices=[('office', 'Office'), ('community_Center', 'community_Center'), ('shop', 'Shop')], max_length=20, null=True)),
                ('Parking_spaces', models.PositiveIntegerField(default=0)),
                ('Has_elevator', models.BooleanField(default=False)),
                ('Has_security_system', models.BooleanField(default=False)),
                ('Has_conference_room', models.BooleanField(default=False)),
                ('Year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)])),
            ],
            bases=('property.allproperty',),
        ),
        migrations.CreateModel(
            name='LandProperty',
            fields=[
                ('allproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='property.allproperty')),
                ('Land_type', models.CharField(choices=[('Farmland', 'Farmland'), ('Playground', 'Playground'), ('warehouse', 'warehouse')], max_length=100, null=True)),
                ('Is_fenced', models.BooleanField(default=False)),
            ],
            bases=('property.allproperty',),
        ),
        migrations.CreateModel(
            name='ResidentialProperty',
            fields=[
                ('allproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='property.allproperty')),
                ('House_No', models.CharField(max_length=8)),
                ('Floor_count', models.PositiveIntegerField(default=1)),
                ('Bedrooms', models.PositiveIntegerField(default=1)),
                ('Bathrooms', models.PositiveIntegerField(default=1)),
                ('Garage_spaces_Per_Sqft', models.PositiveIntegerField(default=0)),
                ('Has_Pool', models.BooleanField(default=False)),
                ('Has_Garden', models.BooleanField(default=False)),
                ('Number_of_Balcony', models.PositiveIntegerField(default=1)),
                ('Year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)])),
            ],
            bases=('property.allproperty',),
        ),
    ]
