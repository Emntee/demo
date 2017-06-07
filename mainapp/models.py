# coding= utf-8
"""
models are defined here
"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from collections import defaultdict
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)


class Supplier(models.Model):
    """
    供应商信息
    """
    name = models.CharField(u"供应商", max_length=10)

    class Meta:
        verbose_name = "供应商条目"
        verbose_name_plural = "供应商列表"

    def __str__(self):
        return self.name


_summury_labels_for_html = [
    ("quantity", u"总量"),
    ("total", u"总价")
]


class SummuryBase(models.Model):
    """
    汇总抽象
    """
    quantity = models.FloatField(u"总量", default=0)
    total = models.FloatField(u"总价", default=0)
    unit = "m"
    record_name = None

    def sync_with_records(self):
        records = getattr(self, record_name + "_set") 
        for record in 

    def archive_as_dict(self):
        data = dict()
        for label in self.labels:
            data[label] = getattr(self, label)
        return data


_record_labels_for_html = [
    ("quantity", u"数量"),
    ("unit", u"单位"),
    ("unit_price", u"单价"),
    ("total", u"总价"),
    ("supplier", u"供应商"),
    ("date_", u"日期"),
    ("created_at", u"创建时间")
]


class RecordBase(models.Model):
    """
    单条记录基础信息部分抽象
    """
    quantity = models.FloatField(u"长度", default=0, blank=False, null=False)
    unit = models.CharField(u"单位", default="m", blank=False, null=False)
    unit_price = models.FloatField(u"单价", default=0, blank=False, null=False)
    total = models.FloatField(u"金额")
    supplier = models.ForeignKey(Supplier, verbose_name=u"供应商")
    date_ = models.DateField(u"日期")
    created_at = models.DateField(u"创建日期", auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.summury.sync_with_records()
        super(RecordBase, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.summury.sync_with_records()
        super(RecordBase, self).delete(*args, **kwargs)

    def archive_as_dict(self):
        data = dict()
        for label in self.labels:
            data[label] = getattr(self, label)
        return data


class GreignYarnSummury(SummuryBase):

    labels = _summury_labels_for_html

    class Meta:
        verbose_name = u"原纱记录汇总表"
        verbose_name_plural = u"各花色原纱记录汇总表"

    def __str__(self):
        return "{}> 原纱汇总记录".format(self.entry.texture)


class GreignYarnRecord(RecordBase):
    # 原纱
    labels = _summury_labels_for_html
    summury = models.ForeignKey(GreignYarnSummury, related_name="records")

    class Meta:
        verbose_name = u"原纱记录"
        verbose_name_plural = u"原纱记录列表"

    def __str__(self):
        return u"{}>{}>原纱记录".format(self.date_, self.summury.entry.texture)


class PaintingSummury(SummuryBase):

    labels = _summury_labels_for_html

    class Meta:
        verbose_name = u"染色记录汇总表"
        verbose_name_plural = u"各花色染色记录汇总表"

    def __str__(self):
        return "{}>染色汇总记录".format(self.entry.texture)


class PaintingRecord(RecordBase):
    # 染色
    labels = _record_labels_for_html
    summury = models.ForeignKey(PaintingSummury, related_name="records")

    class Meta:
        verbose_name = u"染色记录"
        verbose_name_plural = u"染色记录列表"

    def __str__(self):
        return u"{}>{}>染色记录".format(self.date_, self.summury.entry.texture)


class WindingSummury(SummuryBase):
    labels = _summury_labels_for_html

    class Meta:
        verbose_name = u"出轴记录汇总表"
        verbose_name_plural = u"各花色出轴记录汇总表"

    def __str__(self):
        return "{}>出轴汇总记录".format(self.entry.texture)


class WindingRecord(RecordBase):
    # 出轴
    model = models.CharField(u"机型", max_length=40, blank=True, null=True)
    labels = _record_labels_for_html.append(("model", u"机型"))
    summury = models.ForeignKey(WindingSummury, related_name="records")

    class Meta:
        verbose_name = u"出轴记录"
        verbose_name_plural = u"出轴记录列表"

    def __str__(self):
        return u"{}>{}>出轴记录".format(self.date_, self.summury.entry.texture)


class WeavingSummury(SummuryBase):
    full_page_proof_fee = models.FloatField(u"大样费", default=0)
    labels = _summury_labels_for_html.append(("full_page_proof_fee", u"大样费"))

    class Meta:
        verbose_name = u"织造记录汇总表"
        verbose_name_plural = u"各花色织造记录汇总表"

    def __str__(self):
        return "{}>织造汇总记录".format(self.entry.texture)


class WeavingRecord(RecordBase):
    # 织造-单条记录
    raw_unit_price = models.FloatField(u"单价(元/纬)")
    full_page_proof_fee = models.FloatField(u"大样费", default=0)
    labels = _record_labels_for_html.extend([("raw_unit_price", u"单价(纬)"), ("full_page_proof_fee", u"大样费")])
    summury = models.ForeignKey(WeavingSummury, related_name="records")

    class Meta:
        verbose_name = u"织造记录"
        verbose_name_plural = u"织造记录列表"

    def __str__(self):
        return u"{}>{}>织造记录".format(self.date_, self.summury.entry.texture)


class PostProcessingSummury(SummuryBase):
    labels = _summury_labels_for_html

    class Meta:
        verbose_name = u"整理记录汇总表"
        verbose_name_plural = u"各花色整理记录汇总表"

    def __str__(self):
        return "{}>整理汇总记录".format(self.entry.texture)


class PostProcessingRecord(RecordBase):
    # 整理大类>整理子类
    method = models.CharField(u"整理方式", max_length=10)
    labels = _record_labels_for_html.append(("method", u"整理方式"))
    summury = models.ForeignKey(POstProcessingSummury, related_name="records")

    class Meta:
        verbose_name = u"整理记录"
        verbose_name_plural = u"整理记录列表"

    def __str__(self):
        return u"{}>{}>整理记录".format(self.date_, self.summury.entry.texture)


class BleachingSummury(SummuryBase):
    proof_fee = models.FloatField(u"打样费",default=0)
    labels = _summury_labels_for_html.append(("proof_fee", u"打样费"))

    class Meta:
        verbose_name = u"漂白记录汇总表"
        verbose_name_plural = u"各花色漂白记录汇总表"

    def __str__(self):
        return "{}>漂白汇总记录".format(self.entry.texture)


class BleachingRecord(RecordBase):
    # 整理大类>漂白子类
    proof_fee = models.FloatField(u"打样费")
    labels = _record_labels_for_html.append(("proof_fee", u"打样费"))
    summury = models.ForeignKey(BleachingSummury, related_name="records")

    class Meta:
        verbose_name = u"漂白记录"
        verbose_name_plural = u"漂白记录列表"

    def __str__(self):
        return u"{}>{}>漂白记录".format(self.date_, self.summury.entry.texture)


class PrintingSummury(SummuryBase):
    machine_work_fee = models.FloatField(u"上机费", default=0)
    layout_fee = models.FloatField(u"版费", default=0)
    labels = _summury_labels_for_html.extend([("machine_work_fee", u"打样费"), ("layout_fee", u"版费")])

    class Meta:
        verbose_name = u"印花记录汇总表"
        verbose_name_plural = u"各花色印花记录汇总表"

    def __str__(self):
        return "{}>印花汇总记录".format(self.entry.texture)


class PrintingRecord(RecordBase):
    # 整理大类>印花子类
    machine_work_price = models.FloatField(u"上机费")
    layout_price = models.FloatField(u"版费")
    summury = models.ForeignKey(PrintingSummury, related_name="records")
    labels = _record_labels_for_html.extend([("machine_work_fee", u"打样费"), ("layout_fee", u"版费")])

    class Meta:
        verbose_name = u"印花记录"
        verbose_name_plural = u"印花记录列表"

    def __str__(self):
        return u"{}>{}>漂白记录".format(self.date_, self.summury.entry.texture)


class StoringSummury(models.Model):
    a_class_roll_sum = models.IntegerField(u"A等品卷数", default=0)
    a_class_length = models.FloatField(u"A等品长度", default=0)
    b_class_roll_sum = models.IntegerField(u"B等品卷数", default=0)
    b_class_length = models.FloatField(u"B等品长度", default=0)
    b_class_roll_sum = models.IntegerField(u"C等品卷数", default=0)
    b_class_length = models.FloatField(u"C等品长度", default=0)


class StoringRecord(models.Model):
    a_class_roll_count = models.IntegerField(u"A等品卷数")
    a_class_length = models.FloatField(u"A等品长度")
    b_class_roll_count = models.IntegerField(u"B等品卷数")
    b_class_length = models.FloatField(u"B等品长度")
    b_class_roll_count = models.IntegerField(u"C等品卷数")
    b_class_length = models.FloatField(u"C等品长度")

    reason_degrade_2_B = models.TextField(u"降等至B级原因")
    reason_degrade_2_C = models.TextField(u"降等至C级原因")

    storing_date = models.DateField(u"入库时间")
    created_at = models.DateField(auto_now_add=True)

    summury = models.ForeignKey(StoringSummury, related_name="records")

    def save(*args, **kwargs):
        summury = self.summury
        summury.a_class_roll_sum += self.a_class_roll_count
        summury.a_class_length += self.a_class_length
        summury.b_class_roll_sum += self.b_class_roll_count
        summury.b_class_length += self.b_class_length
        summury.c_class_roll_sum += self.c_class_roll_count
        summury.c_class_length += self.c_class_length

        summury.save()

        super(StoringRecord, self).save(*args, **kwargs)


class DeliveringSummury(models.Model):
    roll_sum = models.IntegerField(u"发货卷数", default=0)
    length = models.FloatField(u"发货总长度", default=0)
    sum_price = models.FloatField(u"运费总额", default=0)


class DeliveringRecord(models.Model):
    delivery_date = models.DateField(u"发货日期")
    length = models.FloatField(u"发货长度")
    roll_count = models.IntegerField(u"发货卷数")
    roll_id = models.TextField(u"卷号")
    sum_price = models.FloatField(u"运费")
    price = models.FloatField(u"运输单价")

    created_at = models.DateField(auto_now_add=True)

    summury = models.ForeignKey(DeliveringSummury, related_name="records")

    def save(*args, **kwargs):
        summury = self.summury
        summury.length += self.length
        summury.roll_sum += self.roll_count
        summury.sum_price += self.sum_price
        summury.save()
        super(DeliveringRecord, self).save(*args, **kwargs)


class Client(models.Model):
    """
    客户信息
    """
    name = models.CharField(u"客户", max_length = 10)

    def __str__(self):
        return u"客户: {}".format(self.name)


class Entry(models.Model):
    """
    basic information of one texture
    """

    texture = models.CharField(u"花号", max_length=32, unique=True)
    order_date = models.DateField(u"接单日期", null=True, blank=True)
    contract_date = models.DateField(u"合同定期", null=True, blank=True)
    specification = models.CharField(u"规格", max_length=20, null=True, blank=True)
    client = models.CharField(u"客户", max_length=40, null=True, blank=True)
    order_price = models.FloatField(u"接单单价", null=True, blank=True)
    ends_per_inch = models.FloatField(u"经密", null=True, blank=True)
    picks_per_inch = models.FloatField(u"纬密", null=True, blank=True)
    order_quantity = models.IntegerField(u"合同数量", null=True, blank=True)
    in_production = models.IntegerField(u"投产数量", null=True, blank=True)
    proc_calc_length = models.FloatField(u"经长", null=True, blank=True)
    yarn_csm_per_meter = models.FloatField(u"每米接单用纱量(kg)", null=True, blank=True)
    greige_yarn_price = models.FloatField(u"接单原纱单价", null=True, blank=True)
    painting_price = models.FloatField(u"接单染色单价", null=True, blank=True)
    winding_price = models.FloatField(u"接单出轴单价", null=True, blank=True)
    weaving_price = models.FloatField(u"接单织造单价", null=True, blank=True)
    post_proc_price = models.FloatField(u"接单整理单价", null=True, blank=True)
    delivering_price = models.FloatField(u"接单运费单价", null=True, blank=True)
    last_updated = models.DateField(u"上次改动时间", auto_now=True)

    firstly_created = models.BooleanField(default=True)
    
    greign_yarn_summury = models.OneToOneField(GreignYarnSummury, blank=True)
    painting_summury = models.OneToOneField(PaintingSummury, blank=True)
    winding_summury = models.OneToOneField(WindingSummury, blank=True)
    weaving_summury = models.OneToOneField(WeavingSummury, blank=True)
    post_processing_summury = models.OneToOneField(PostProcessingSummury, blank=True)
    bleaching_summury = models.OneToOneField(BleachingSummury, blank=True)
    printing_summury = models.OneToOneField(PrintingSummury, blank=True)
    storing_summury = models.OneToOneField(StoringSummury, blank=True)
    delivering_summury = models.OneToOneField(DeliveringSummury, blank=True)

    class Meta:
        verbose_name = "花色条目"
        verbose_name_plural = "花色条目列表"

    def __str__(self):
        return u"花色 {} 基本信息".format(self.texture)

    def save(self, *args, **kwargs):
        if self.firstly_created:
            greign_yarn_summury = GreignYarnSummury()
            greign_yarn_summury.save()
            self.greign_yarn_summury = greign_yarn_summury

            painting_summury = PaintingSummury()
            painting_summury.save()
            self.painting_summury = painting_summury

            winding_summury = WindingSummury()
            winding_summury.save()
            self.winding_summury = winding_summury

            weaving_summury = WeavingSummury()
            weaving_summury.save()
            self.weaving_summury = weaving_summury

            post_processing_summury = PostProcessingSummury()
            post_processing_summury.save()
            self.post_processing_summury = post_processing_summury

            bleaching_summury = BleachingSummury()
            bleaching_summury.save()
            self.bleaching_summury = bleaching_summury

            printing_summury = PrintingSummury()
            printing_summury.save()
            self.printing_summury = printing_summury

            storing_summury = StoringSummury()
            storing_summury.save()
            self.storing_summury = storing_summury

            delivering_summury = DeliveringSummury()
            delivering_summury.save()
            self.delivering_summury = delivering_summury

            self.firstly_created = False

        super(Entry,self).save(*args, **kwargs)
