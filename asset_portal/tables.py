import django_tables2 as tables
from django_tables2.utils import A, AttributeDict  # alias for Accessor
from django.utils.safestring import mark_safe

from models import Asset, Job, Flight


class FakeLinkColumn(tables.LinkColumn):
    def render_link(self, uri, text, attrs=None):
        """
        Render a hyperlink.
        :param   uri: URI for the hyperlink
        :param  text: value wrapped in ``<a></a>``
        :param attrs: ``<a>`` tag attributes
        """
        attrs = AttributeDict(attrs if attrs is not None else
                              self.attrs.get('a', {}))
        attrs['href'] = uri
        html = '<a {attrs}>{text}</a>'.format(
            attrs=attrs.as_html(),
            text=text
        )
        return mark_safe(html)


class AssetTable(tables.Table):
    film_title = tables.LinkColumn('asset-detail', kwargs={'slug': A('slug')}, verbose_name='Title')
    content_type = tables.TemplateColumn('''{{ value }}
                                            {% if record.dimension_properties == "3D" %}
                                                <span class="label label-info">3D</span>
                                            {% endif %}''')
    edit = tables.TemplateColumn('''
                                 <a href={% url 'asset-edit' slug=record.slug %}>
                                    <i class='fa fa-edit'></i>
                                 </a>
                                 ''', orderable=False)
    delete = tables.TemplateColumn('''
                                 <a href={% url 'asset-delete' slug=record.slug %}>
                                    <i class='fa fa-trash-o'></i>
                                 </a>
                                 ''', orderable=False)

    status = tables.TemplateColumn('''
                                    <div class="progress" style="margin-bottom: 0">
                                        <div class="progress-bar progress-bar-{% if record.status < 100 %}warning{% else %}success{% endif %}" style="width: {{ record.status }}%;">
                                            <span class="sr-only">{{ record.status }}% Complete</span>
                                            <p class="progress-bar-inner-text">{{ record.get_status_display }}</p>
                                        </div>
                                    </div>
                                    ''')

    class Meta:
        model = Asset
        fields = (
            "created", "film_title", "version_name", "release_year", "running_time", "content_type", "status",
            "edit",
            "delete",)
        attrs = {"class": "table table-striped table-bordered table-hover", "id": "assets-table"}
        order_by = '-created'
        orderable = False


class JobTable(tables.Table):
    film_title = tables.Column(accessor=A("asset.film_title"), verbose_name='Title')
    type = tables.LinkColumn('job-detail', kwargs={'slug': A('slug')}, orderable=False)
    status = tables.Column(orderable=False)
    version_name = tables.Column(accessor=A("asset.version_name"))
    paid = tables.TemplateColumn('''
                                 {% if record.paid %}
                                    <i class="text-success fa fa-check"></i>
                                 {% else %}
                                    <i class="text-danger fa fa-times"></i>
                                 {% endif %}
                                 ''')
    edit = tables.TemplateColumn('''
                                 <a
                                    {% if record.type == "Shipping" %}
                                        style="color: grey;"
                                        data-toggle="tooltip"
                                        title="Shipping Jobs can't be edited"
                                    {% else %}
                                        href={% url 'job-edit' slug=record.slug %}
                                    {% endif %}
                                    >
                                    <i class='fa fa-edit'></i>
                                 </a>
                                 ''', orderable=False)
    delete = tables.TemplateColumn('''
                                 <a
                                    {% if record.type == "Shipping" %}
                                        style="color: grey;"
                                        data-toggle="tooltip"
                                        title="Shipping Jobs can't be deleted"
                                    {% else %}
                                        href={% url 'job-delete' slug=record.slug %}
                                    {% endif %}
                                    >
                                    <i class='fa fa-trash-o'></i>
                                 </a>
                                 ''', orderable=False)

    status = tables.TemplateColumn('''
                                    <div class="progress" style="margin-bottom: 0">
                                        <div class="progress-bar progress-bar-{% if record.status < 100 %}warning{% else %}success{% endif %}" style="width: {{ record.status }}%;">
                                            <span class="sr-only">{{ record.status }}% Complete</span>
                                            <p class="progress-bar-inner-text">{{ record.get_status_display }}</p>
                                        </div>
                                    </div>
                                    ''')

    class Meta:
        model = Job
        fields = ("created", "film_title", "version_name", "type", "status", "paid", "edit", "delete",)
        attrs = {"class": "table table-striped table-bordered table-hover", "id": "jobs-table"}
        order_by = '-created'
        orderable = False


class JobInvoiceTable(tables.Table):
    film_title = tables.Column(accessor=A("asset.film_title"), verbose_name='Title')
    type = tables.LinkColumn('job-detail', kwargs={'slug': A('slug')}, orderable=False)
    status = tables.Column(orderable=False)
    paid = tables.BooleanColumn()
    pay = tables.CheckBoxColumn(accessor=A('slug'))
    fee = tables.TemplateColumn('${{ value }}')
    status = tables.TemplateColumn('''
                                    <div class="progress" style="margin-bottom: 0">
                                        <div class="progress-bar progress-bar-{% if record.status < 100 %}warning{% else %}success{% endif %}" style="width: {{ record.status }}%;">
                                            <span class="sr-only">{{ record.status }}% Complete</span>
                                            <p class="progress-bar-inner-text">{{ record.get_status_display }}</p>
                                        </div>
                                    </div>
                                    ''')

    class Meta:
        model = Job
        model.pay = False
        fields = ("pay", "created", "film_title", "type", "status", "paid", "fee")
        attrs = {"class": "table table-striped table-bordered table-hover", 'id': "jobs-table"}
        order_by = '-created'
        orderable = False


class FlightTable(tables.Table):
    created = tables.Column(accessor=A("job.created"), verbose_name="Date sent")
    exhibitor = tables.LinkColumn('flight-detail', accessor=A('screening_room.exhibitor'), kwargs={'pk': A('pk')},
                                  verbose_name="Destination / Exhibitor")
    room_number = tables.Column(accessor=A("screening_room.room_number"), verbose_name="screens")
    asset = tables.Column(accessor=A("job.asset"))

    status = tables.TemplateColumn('''
                                    <div class="progress" style="margin-bottom: 0">
                                        <div class="progress-bar progress-bar-{% if record.status < 100 %}warning{% else %}success{% endif %}" style="width: {{ record.status }}%;">
                                            <span class="sr-only">{{ record.status }}% Complete</span>
                                            <p class="progress-bar-inner-text">{{ record.get_status_display }}</p>
                                        </div>
                                    </div>
                                    ''')

    class Meta:
        model = Flight
        fields = ("created", "exhibitor", "room_number", "asset", "status",)
        attrs = {"class": "table table-striped table-bordered table-hover", 'id': "flights-table"}
        order_by = '-created'
        orderable = False

