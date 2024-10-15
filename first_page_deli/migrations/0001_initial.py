# Generated by Django 4.2.15 on 2024-10-15 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('plu', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BYOPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaCheese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheese_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaCrust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crust_type', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaMeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meat_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sauce_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PizzaToppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='CheeseBoard',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='Dips',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='EntertainmentEnd',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            options={
                'verbose_name': 'Entertainment End',
                'verbose_name_plural': 'Entertainment End',
            },
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='HotCase',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            options={
                'verbose_name': 'Hot Case Item',
                'verbose_name_plural': 'Hot Case Items',
            },
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='PackedMeatI',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='PackedMeatII',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='PizzaAndSalads',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='SaladsEnd',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='SandwichEndI',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            options={
                'verbose_name': 'Sandwich End - I',
                'verbose_name_plural': 'Sandwich End - I',
            },
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='SandwichEndII',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            options={
                'verbose_name': 'Sandwich End - II',
                'verbose_name_plural': 'Sandwich End - II',
            },
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='ServiceCaseSalads',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='SoupsAndMeals',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
            ],
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ManyToManyField(blank=True, to='first_page_deli.category')),
                ('cheese', models.ManyToManyField(to='first_page_deli.pizzacheese')),
                ('crust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_page_deli.pizzacrust')),
                ('meat', models.ManyToManyField(blank=True, to='first_page_deli.pizzameat')),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_page_deli.pizzasauce')),
                ('size', models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='first_page_deli.pizzasize')),
                ('toppings', models.ManyToManyField(to='first_page_deli.pizzatoppings')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.PositiveIntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_ordered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_page_deli.pizza')),
            ],
        ),
        migrations.AddField(
            model_name='basemodel',
            name='category',
            field=models.ManyToManyField(blank=True, to='first_page_deli.category'),
        ),
        migrations.CreateModel(
            name='ServiceCaseMeats',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_page_deli.basemodel')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_case_meats', to='first_page_deli.brand')),
            ],
            options={
                'verbose_name': 'Service Case Meat',
                'verbose_name_plural': 'Service Case Meats',
            },
            bases=('first_page_deli.basemodel',),
        ),
        migrations.CreateModel(
            name='OnSaleSalads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_sale_salads', models.ManyToManyField(blank=True, to='first_page_deli.servicecasesalads')),
            ],
        ),
        migrations.CreateModel(
            name='OnSaleMeats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_sale_meats', models.ManyToManyField(blank=True, to='first_page_deli.servicecasemeats')),
            ],
        ),
    ]