import os

from orminator import ModelWriter


class IMicrobeModelWriter(ModelWriter):
    def __init__(self, db_uri):
        super().__init__(db_uri)

    def get_model_parent_class_name(self):
        return 'db.Model'

    def import_model_base(self):
        return """\
import sqlalchemy as sa
from sqlalchemy.orm import backref
import sqlalchemy.dialects.mysql as mysql

from app import db


"""

    def write_additional_methods(self, table, table_code):
        # write a json() method
        table_code.write("    def json(self):\n        return {\n")
        for column in table.columns:
            if column.primary_key:
                # do not include primary key in JSON
                pass
            else:
                table_code.write(
                    "            '{}': self.{},\n".format(
                        column.name, self.translate_column_name_to_py(column.name)))
        table_code.write("        }")
        table_code.write("\n\n")

        # write __repr__() if we know which fields to display
        table_name_to_representative_py_attr = {
            'app_data_type': ('name', ),
            'app_tag': ('value', ),
            'assembly': ('assembly_name', ),
            'centrifuge': ('name', ),
            'combined_assembly': ('assembly_name', ),
            'domain': ('domain_name', ),
            'ftp': ('path', ),
            'investigator': ('investigator_name', ),
            'kegg_annotation': ('kegg_annotation_id', ),
            'ontology': ('label', ),
            'project': ('project_name', ),
            'project_file': ('file_', ),
            'project_group': ('group_name', ),
            'protocol': ('protocol_name', ),
            'sample': ('sample_name', ),
            'sample_attr': ('sample_attr_type', 'attr_value', ),
            'sample_attr_type': ('type_', ),
            'sample_file': ('file_', ),
            'sample_file_type': ('type_', ),
            'uproc': ('accession', )
        }

        if table.name in table_name_to_representative_py_attr:
            table_code.write(
                "    def __repr__(self):\n"
                "        return " + ' + ":" + '.join([
                    "str(self.{})".format(a)
                    for a
                    in table_name_to_representative_py_attr[table.name]]))
            table_code.write('\n\n')


def main():
    IMicrobeModelWriter(db_uri=os.environ.get('IMICROBE_DB_URI')).write_models('app/models.py')


if __name__ == '__main__':
    main()
