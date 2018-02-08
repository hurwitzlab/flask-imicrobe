from flask_admin.contrib.sqla import ModelView


class iMicrobeModelView(ModelView):
    column_display_pk = True
    form_excluded_columns = [
        'assembly_list',
        'combined_assembly_list',
        'centrifuge_list',
        'protein_list',
        'uproc_kegg_result_list',
        'uproc_pfam_result_list']  # this is just for Sample lazy!
