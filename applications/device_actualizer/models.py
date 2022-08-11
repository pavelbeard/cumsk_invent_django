from django.db import models


# Create your models here.


class Nodetable(models.Model):
    node_id = models.CharField(primary_key=True, max_length=128)
    label = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mac_address = models.TextField(blank=True, null=True)
    parent_id = models.TextField(blank=True, null=True)
    polling_agent = models.TextField(blank=True, null=True)
    get_community = models.TextField(blank=True, null=True)
    has_snmp = models.IntegerField(blank=True, null=True)
    has_web = models.IntegerField(blank=True, null=True)
    has_ftp = models.IntegerField(blank=True, null=True)
    has_telnet = models.IntegerField(db_column='has_telent', blank=True, null=True)
    has_rmon = models.IntegerField(blank=True, null=True)
    has_smtp = models.IntegerField(blank=True, null=True)
    has_tcp1 = models.IntegerField(blank=True, null=True)
    has_tcp2 = models.IntegerField(blank=True, null=True)
    has_tcp3 = models.IntegerField(blank=True, null=True)
    has_tcp4 = models.IntegerField(blank=True, null=True)
    node_group = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"snmpc_device_id_{self.node_id}"

    def get_fields(self):
        return Nodetable._meta.fields

    class Meta:
        managed = False
        db_table = 'nodetable'
        verbose_name = verbose_name_plural = 'Устройства из SNMPc'


class CiscoDs(models.Model):
    id = models.IntegerField(db_column='№',
                             primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    id_device = models.TextField(db_column='Идентификатор оборудования', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_man = models.TextField(db_column='Идентификатор в системе управления (в сети)', blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    obj_type = models.TextField(db_column='Тип объекта', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dev_type = models.TextField(db_column='Тип оборудования', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dev_model = models.TextField(db_column='Модель оборудования', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    com_code = models.TextField(db_column='Комкод', blank=True, null=True)  # Field name made lowercase.
    vendor_code = models.TextField(db_column='Код производителя', blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor = models.TextField(db_column='Производитель', blank=True, null=True)  # Field name made lowercase.
    vendor_name_eng = models.TextField(db_column='Наименование (ENG)', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    network_type = models.TextField(db_column='Сеть', blank=True, null=True)  # Field name made lowercase.
    railway_code = models.IntegerField(db_column='Код железной дороги', blank=True,
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    com_node = models.TextField(db_column='Узел связи', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    room_name = models.TextField(db_column='Название помещения', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Статус', blank=True, null=True)  # Field name made lowercase.
    comment_1 = models.TextField(db_column='Комментарий 1', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comment_2 = models.TextField(db_column='Комментарий 2', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comment_3 = models.TextField(db_column='Комментарий 3', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comment_4 = models.TextField(db_column='Комментарий 4', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comment_5 = models.TextField(db_column='Комментарий 5', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comment_6 = models.TextField(db_column='Комментарий 6', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comment_7 = models.TextField(db_column='Комментарий 7', blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return f"esma_device_id_{self.id}"

    class Meta:
        managed = False
        db_table = 'cisco_ds'
        verbose_name = verbose_name_plural = 'Устройства из ЕСМА'


class Esmacards(models.Model):
    iddevice = models.TextField(blank=True, null=True)
    idnetwork = models.TextField(blank=True, null=True)
    devicename = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    expdep = models.TextField(blank=True, null=True)
    lastpolling = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    originalid = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"ESMA card id: {self.id}"

    class Meta:
        managed = False
        db_table = 'esmacards'
        verbose_name = verbose_name_plural = 'Карточки из ЕСМА'


class Pingariumresults(models.Model):
    id = models.IntegerField(primary_key=True)
    protocol = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Device id: {self.id}"

    class Meta:
        managed = False
        db_table = 'pingariumresults'
        verbose_name = 'Запись просканированного устройства'
        verbose_name_plural = 'Записи о просканированных устройствах'


class Hardwareinfo(models.Model):
    version = models.TextField(blank=True, null=True)
    hostname = models.TextField(blank=True, null=True)
    uptime = models.TextField(blank=True, null=True)
    runningimage = models.TextField(blank=True, null=True)
    hardware = models.TextField(blank=True, null=True)
    serial = models.TextField(blank=True, null=True)
    configregister = models.TextField(blank=True, null=True)
    pingariumresult_modelid = models.ForeignKey('Pingariumresults', on_delete=models.CASCADE,
                                                db_column='pingariumresult_modelid', blank=True, null=True)

    def __str__(self):
        return f"Hardware info id: {self.id}"

    class Meta:
        managed = False
        db_table = 'hardwareinfo'
        verbose_name = 'Данные о просканированном устройстве'
        verbose_name_plural = 'Данные о просканированных устройствах'
