import sqlalchemy as sa

from imicrobe_model import write_models


class FlaskModelWriter(write_models.ModelWriter):
    def get_model_parent_class_name(self):
        return 'db.Model'

    def import_model_base(self):
        return """\
import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql

from app import db


"""

    def write_additional_methods(self, table, table_code):
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

    # print(dir(table))
    # print(table.columns)

def main():
    FlaskModelWriter().write_models('app/models.py')


if __name__ == '__main__':
    main()
