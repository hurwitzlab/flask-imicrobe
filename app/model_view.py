from flask_admin.contrib.sqla import ModelView


class iMicrobeModelView(ModelView):
    column_display_pk = True
    form_excluded_columns = ['uproc_list']  # this is just for Sample lazy!
