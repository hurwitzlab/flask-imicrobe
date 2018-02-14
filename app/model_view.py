from pprint import pprint

from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView

from app import models


class iMicrobeModelView(ModelView):
    form_base_class = SecureForm
    column_display_pk = True

    form_excluded_columns = [
        'assembly_list',
        'combined_assembly_list',
        'centrifuge_list',
        'protein_list',
        'uproc_kegg_result_list',
        'uproc_pfam_result_list']  # this is just for Sample lazy!


class SampleView(iMicrobeModelView):
    form_ajax_refs = {
        'sample_attr_list': {
            'fields': (models.Sample_attr.attr_value, )
        },
        'sample_file_list': {
            'fields': (models.Sample_file.file_, )
        }
    }

    def on_model_change(self, form, model, is_created):
        print('on_model_change')
        #pprint(form.__dict__)
        #pprint(form._fields)
        #print('taxon_id: "{}"'.format(form.taxon_id))
        #print('taxon_id.__dict__: "{}"'.format(form.taxon_id.__dict__))
        #print('taxon_id.data: "{}"'.format(form.taxon_id.data))
        #print('model.taxon_id: "{}"'.format(model.taxon_id))
        # could instead look at model.taxon_id
        if form.sample_name is None:
            model.sample_name = ''
        if form.sample_type is None:
            model.sample_type = ''
        if form.taxon_id.data is None:
            model.taxon_id = ''
        #print('model.url: "{}"'.format(model.url))
        if form.url.data is None:
            model.url = ''
        #print(is_created)



class ProjectToDomainView(iMicrobeModelView):
    form_ajax_refs = {
        'project_id': {
            'fields': (models.Project.project_name, )
        },
        'domain_id': {
            'fields': (models.Domain.domain_name, )
        }
    }