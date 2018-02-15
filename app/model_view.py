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

    column_defaults = {
        models.Investigator: {
            models.Investigator.investigator_name: '',
            models.Investigator.institution: '',
            models.Investigator.url: '',
        },
        models.Project: {
            models.Project.project_code: '',
            models.Project.project_name: '',
            models.Project.pi: '',
            models.Project.institution: '',
            models.Project.project_type: '',
            models.Project.url: '',
            models.Project.read_file: '',
            models.Project.meta_file: '',
            models.Project.assembly_file: '',
            models.Project.peptide_file: '',
            models.Project.email: '',
            models.Project.read_pep_file: '',
            models.Project.nt_file: ''
        },
        models.Sample: {
            models.Sample.sample_name: '',
            models.Sample.sample_type: '',
            models.Sample.taxon_id: '',
            models.Sample.url: ''
        }
    }


    def _on_model_change(self, form, model, is_created):
        #print('on_model_change')
        #print('  type(model): "{}"'.format(type(model)))
        if type(model) in self.column_defaults:
            #print('  "{}" is in self.column_defaults', type(model))
            for attr, default_value in self.column_defaults[type(model)].items():
                #print('    attr: "{}" has name "{}"'.format(attr, attr.name))
                if getattr(model, attr.name) is None:
                    print('    set attr "{}" to "{}"'.format(attr, default_value))
                    setattr(model, attr.name, default_value)
                else:
                    pass
        else:
            pass


class ProjectView(iMicrobeModelView):
    column_searchable_list = ['project_code', 'project_name', 'description']
    column_filters = ['project_id', ]

    form_ajax_refs = {
        'domain_list': {
            'fields': (models.Domain.domain_name, )
        },
        'ftp_list': {
            'fields': (models.Ftp.path, )
        },
        'project_file_list': {
            'fields': (models.Project_file.file_, )
        }
     }


class SampleView(iMicrobeModelView):
    column_searchable_list = ['sample_acc', 'sample_name', 'sample_description']
    column_filters = ['sample_id', ]

    form_ajax_refs = {
        'sample_attr_list': {
            'fields': (models.Sample_attr.attr_value, )
        },
        'sample_file_list': {
            'fields': (models.Sample_file.file_, )
        }
    }
