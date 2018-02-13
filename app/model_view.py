from flask_admin.contrib.sqla import ModelView

from app import models

class iMicrobeModelView(ModelView):
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