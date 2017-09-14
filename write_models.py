import os

import sqlalchemy as sa


mysql_to_sqlalchemy = {
    'INTEGER': 'Integer',
    'VARCHAR': 'String'
}

def write_models():
    # connect to database on server
    # e.g. mysql+pymysqldb://imicrobe:<password>@localhost/imicrobe
    db_uri = os.environ.get('IMICROBE_DB_URI')
    imicrobe_engine = sa.create_engine(db_uri)
    # reflect tables
    meta = sa.MetaData()
    meta.reflect(bind=imicrobe_engine)
    #print(meta.tables)

    with open('app/models.py', 'wt') as test_models:

        test_models.write("from app import db\n\n")

        for table in meta.sorted_tables:
            print(table)
            test_models.write("class {}(db.Model):\n".format(table.name.capitalize()))
            test_models.write("    __tablename__ = '{}'\n".format(table.name))

            for column in table.columns:
                column_name = column.name
                column_type = str(column.type).split()[0]
                column_modifiers = []

                if column.primary_key:
                    column_type = 'Integer'
                    column_modifiers.append(', primary_key=True')

                if column_name.endswith('_id'):
                    column_type = 'Integer'

                # TODO: need different names for model attribute and db column
                elif column.name == 'class':
                    column_name = 'clazz'

                if column_type.startswith('INTEGER'):
                    column_type = 'INTEGER'
                elif column_type.startswith('BIGINT'):
                    column_type = 'INTEGER'
                elif column_type.startswith('TINYINT'):
                    column_type = 'INTEGER'
                elif column_type.startswith('DOUBLE'):
                    column_type = 'Float'
                # TODO: what should LONGTEXT map to?
                elif column_type.startswith('LONGTEXT'):
                    column_type = 'Text'
                elif column_type.startswith('ENUM'):
                    column_type = 'Enum'

                test_models.write("    {name} = db.Column('{name}', db.{type}{kw})\n".format(
                    name=column_name, type=column_type, kw=''.join(column_modifiers)))

            test_models.write("\n")
            test_models.write("    def json(self):\n        return {\n")
            for column in table.columns:
                column_name = column.name
                if column.primary_key:
                    # do not include primary key in JSON
                    continue
                elif column.name == 'class':
                    column_name = 'clazz'
                test_models.write("            '{name}': self.{name},\n".format(name=column_name))

            test_models.write("        }")
            test_models.write("\n\n")

            #print(dir(table))
            print(table.columns)


if __name__ == '__main__':
    write_models()
