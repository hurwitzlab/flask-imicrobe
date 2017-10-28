import collections
import io
import os
import re

import sqlalchemy as sa


mysql_to_sqlalchemy = {
    'INTEGER': 'Integer',
    'VARCHAR': 'String'
}

def write_models():
    # connect to database on server
    # e.g. mysql+pymysql://imicrobe:<password>@localhost/imicrobe
    db_uri = os.environ.get('IMICROBE_DB_URI')
    imicrobe_engine = sa.create_engine(db_uri)
    # reflect tables
    meta = sa.MetaData()
    meta.reflect(bind=imicrobe_engine)
    #print(meta.tables)

    # build a dictionary of table_name to io.StringIO
    # so we can go back to add relationships
    def string_io_factory():
        return io.StringIO()
    table_name_to_table_code = collections.defaultdict(string_io_factory)

    for table in meta.sorted_tables:
        print(table)

        table_code = table_name_to_table_code[table.name]
        table_code.write("class {}(db.Model):\n".format(table.name.capitalize()))
        table_code.write("    __tablename__ = '{}'\n".format(table.name))

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

            # this is so ugly
            if column_type.startswith('INTEGER'):
                column_type = 'INTEGER'
            elif column_type.startswith('BIGINT'):
                column_type = 'INTEGER'
            elif column_type.startswith('TINYINT'):
                column_type = 'INTEGER'
            elif column_type.startswith('DOUBLE'):
                column_type = 'Float'
            # TODO: what should LONGTEXT map to?
            # TODO: what should MEDIUMTEXT map to?
            elif column_type.startswith('LONGTEXT'):
                column_type = 'Text'
            elif column_type.startswith('MEDIUMTEXT'):
                column_type = 'Text'
            elif column_type.startswith('ENUM'):
                column_type = 'Enum'

            table_code.write("    {name} = db.Column('{name}', db.{type}{kw})\n".format(
                name=column_name, type=column_type, kw=''.join(column_modifiers)))

        table_code.write("\n")
        # TODO: make json method optional
        table_code.write("    def json(self):\n        return {\n")
        for column in table.columns:
            column_name = column.name
            if column.primary_key:
                # do not include primary key in JSON
                continue
            elif column.name == 'class':
                column_name = 'clazz'
            table_code.write("            '{name}': self.{name},\n".format(name=column_name))

        table_code.write("        }")
        table_code.write("\n\n")

        #print(dir(table))
        print(table.columns)

    # add relationships
    # look for tables with name like 'table_a_to_table_b'
    # it would be more smarter to look for tables with two foreign keys
    relationship_pattern = re.compile(
        r'^(?P<table_a>[a-zA-Z_]+)_to_(?P<table_b>[a-zA-Z_]+)$'
    )
    relationship_code = """\
    {table_2}_list = sqlalchemy.orm.relationship(
        "{class_2}",
        secondary="{relationship_table}",
        back_populates="{table_1}_list"
    )

"""

    for table_name, table_code in table_name_to_table_code.items():
        relationship_table_match = relationship_pattern.search(table_name)
        if relationship_table_match:
            print('table {} looks like a relationship table'.format(table_name))
            table_a_name = relationship_table_match.group('table_a')
            table_b_name = relationship_table_match.group('table_b')
            if table_a_name not in table_name_to_table_code:
                print('"{}" is not a table'.format(table_a_name))
            elif table_b_name not in table_name_to_table_code:
                print('"{}" is not a table'.format(table_b_name))
            else:
                print('found relationship table "{}"'.format(table_name))
                table_a_code = table_name_to_table_code[table_a_name]
                table_a_code.write(relationship_code.format(
                    table_1=table_a_name,
                    class_2=table_b_name.capitalize(),
                    relationship_table=table_name,
                    table_2=table_b_name)
                )
                table_b_code = table_name_to_table_code[table_b_name]
                table_b_code.write(relationship_code.format(
                    table_1=table_b_name,
                    class_2=table_a_name.capitalize(),
                    relationship_table=table_name,
                    table_2=table_a_name)
                )
        else:
            pass


    with open('app/models.py', 'wt') as test_models:
        test_models.write('import sqlalchemy\n\n')
        test_models.write("from app import db\n\n")
        for _, table_code in sorted(table_name_to_table_code.items()):
            test_models.write(table_code.getvalue())


if __name__ == '__main__':
    write_models()
