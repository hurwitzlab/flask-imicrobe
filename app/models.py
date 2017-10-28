import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql

from app import db


class App(db.Model):
    __tablename__ = 'app'

    app_id = sa.Column('app_id', mysql.INTEGER(unsigned=True), primary_key=True)

    app_name = sa.Column('app_name', mysql.VARCHAR(50))  # column.type was 'VARCHAR(50)'

    is_active = sa.Column('is_active', mysql.TINYINT(4))  # column.type was 'TINYINT(4)'


    app_data_type_list = sa.orm.relationship(
        "App_data_type",
        secondary="app_to_app_data_type",
        back_populates="app_list"
    )

    app_tag_list = sa.orm.relationship(
        "App_tag",
        secondary="app_to_app_tag",
        back_populates="app_list"
    )

    def json(self):
        return {
            'app_name': self.app_name,
            'is_active': self.is_active,
        }


class App_data_type(db.Model):
    __tablename__ = 'app_data_type'

    app_data_type_id = sa.Column('app_data_type_id', mysql.INTEGER(unsigned=True), primary_key=True)

    name = sa.Column('name', mysql.VARCHAR(50))  # column.type was 'VARCHAR(50)'

    alias = sa.Column('alias', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    app_list = sa.orm.relationship(
        "App",
        secondary="app_to_app_data_type",
        back_populates="app_data_type_list"
    )

    def json(self):
        return {
            'name': self.name,
            'alias': self.alias,
        }


class App_run(db.Model):
    __tablename__ = 'app_run'

    __table_args__ = (
        sa.ForeignKeyConstraint(['app_id'], ['app.app_id']),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'])
    )

    app_run_id = sa.Column('app_run_id', mysql.INTEGER(unsigned=True), primary_key=True)

    app_id = sa.Column('app_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    user_id = sa.Column('user_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    app_ran_at = sa.Column('app_ran_at', sa.DateTime)  # column.type was 'DATETIME'

    params = sa.Column('params', mysql.TEXT())  # column.type was 'TEXT'


    def json(self):
        return {
            'app_id': self.app_id,
            'user_id': self.user_id,
            'app_ran_at': self.app_ran_at,
            'params': self.params,
        }


class App_tag(db.Model):
    __tablename__ = 'app_tag'

    app_tag_id = sa.Column('app_tag_id', mysql.INTEGER(unsigned=True), primary_key=True)

    value = sa.Column('value', mysql.VARCHAR(50))  # column.type was 'VARCHAR(50)'


    app_list = sa.orm.relationship(
        "App",
        secondary="app_to_app_tag",
        back_populates="app_tag_list"
    )

    def json(self):
        return {
            'value': self.value,
        }


class App_to_app_data_type(db.Model):
    __tablename__ = 'app_to_app_data_type'

    __table_args__ = (
        sa.ForeignKeyConstraint(['app_id'], ['app.app_id']),
        sa.ForeignKeyConstraint(['app_data_type_id'], ['app_data_type.app_data_type_id'])
    )

    app_to_app_data_type_id = sa.Column('app_to_app_data_type_id', mysql.INTEGER(unsigned=True), primary_key=True)

    app_id = sa.Column('app_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    app_data_type_id = sa.Column('app_data_type_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'app_id': self.app_id,
            'app_data_type_id': self.app_data_type_id,
        }


class App_to_app_tag(db.Model):
    __tablename__ = 'app_to_app_tag'

    __table_args__ = (
        sa.ForeignKeyConstraint(['app_id'], ['app.app_id']),
        sa.ForeignKeyConstraint(['app_tag_id'], ['app_tag.app_tag_id'])
    )

    app_to_app_tag_id = sa.Column('app_to_app_tag_id', mysql.INTEGER(unsigned=True), primary_key=True)

    app_id = sa.Column('app_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    app_tag_id = sa.Column('app_tag_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'app_id': self.app_id,
            'app_tag_id': self.app_tag_id,
        }


class Assembly(db.Model):
    __tablename__ = 'assembly'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id']),
        sa.ForeignKeyConstraint(['sample_id'], ['sample.sample_id'])
    )

    assembly_id = sa.Column('assembly_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    assembly_code = sa.Column('assembly_code', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    assembly_name = sa.Column('assembly_name', mysql.TEXT())  # column.type was 'TEXT'

    organism = sa.Column('organism', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    pep_file = sa.Column('pep_file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    nt_file = sa.Column('nt_file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    cds_file = sa.Column('cds_file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    description = sa.Column('description', mysql.TEXT())  # column.type was 'TEXT'

    sample_id = sa.Column('sample_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'project_id': self.project_id,
            'assembly_code': self.assembly_code,
            'assembly_name': self.assembly_name,
            'organism': self.organism,
            'pep_file': self.pep_file,
            'nt_file': self.nt_file,
            'cds_file': self.cds_file,
            'description': self.description,
            'sample_id': self.sample_id,
        }


class Combined_assembly(db.Model):
    __tablename__ = 'combined_assembly'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id']),
    )

    combined_assembly_id = sa.Column('combined_assembly_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    assembly_name = sa.Column('assembly_name', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    phylum = sa.Column('phylum', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    class_ = sa.Column('class', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    family = sa.Column('family', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    genus = sa.Column('genus', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    species = sa.Column('species', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    strain = sa.Column('strain', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    pcr_amp = sa.Column('pcr_amp', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    annotations_file = sa.Column('annotations_file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    peptides_file = sa.Column('peptides_file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    nucleotides_file = sa.Column('nucleotides_file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    cds_file = sa.Column('cds_file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    sample_list = sa.orm.relationship(
        "Sample",
        secondary="combined_assembly_to_sample",
        back_populates="combined_assembly_list"
    )

    def json(self):
        return {
            'project_id': self.project_id,
            'assembly_name': self.assembly_name,
            'phylum': self.phylum,
            'class': self.class_,
            'family': self.family,
            'genus': self.genus,
            'species': self.species,
            'strain': self.strain,
            'pcr_amp': self.pcr_amp,
            'annotations_file': self.annotations_file,
            'peptides_file': self.peptides_file,
            'nucleotides_file': self.nucleotides_file,
            'cds_file': self.cds_file,
        }


class Combined_assembly_to_sample(db.Model):
    __tablename__ = 'combined_assembly_to_sample'

    __table_args__ = (
        sa.ForeignKeyConstraint(['combined_assembly_id'], ['combined_assembly.combined_assembly_id']),
        sa.ForeignKeyConstraint(['sample_id'], ['sample.sample_id'])
    )

    combined_assembly_to_sample_id = sa.Column('combined_assembly_to_sample_id', mysql.INTEGER(unsigned=True), primary_key=True)

    combined_assembly_id = sa.Column('combined_assembly_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    sample_id = sa.Column('sample_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'combined_assembly_id': self.combined_assembly_id,
            'sample_id': self.sample_id,
        }


class Domain(db.Model):
    __tablename__ = 'domain'

    domain_id = sa.Column('domain_id', mysql.INTEGER(unsigned=True), primary_key=True)

    domain_name = sa.Column('domain_name', mysql.VARCHAR(50))  # column.type was 'VARCHAR(50)'


    project_list = sa.orm.relationship(
        "Project",
        secondary="project_to_domain",
        back_populates="domain_list"
    )

    def json(self):
        return {
            'domain_name': self.domain_name,
        }


class Ftp(db.Model):
    __tablename__ = 'ftp'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id']),
    )

    ftp_id = sa.Column('ftp_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    name = sa.Column('name', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    path = sa.Column('path', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    size = sa.Column('size', mysql.VARCHAR(20))  # column.type was 'VARCHAR(20)'


    def json(self):
        return {
            'project_id': self.project_id,
            'name': self.name,
            'path': self.path,
            'size': self.size,
        }


class Investigator(db.Model):
    __tablename__ = 'investigator'

    investigator_id = sa.Column('investigator_id', mysql.INTEGER(unsigned=True), primary_key=True)

    investigator_name = sa.Column('investigator_name', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    institution = sa.Column('institution', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    url = sa.Column('url', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    project_list = sa.orm.relationship(
        "Project",
        secondary="project_to_investigator",
        back_populates="investigator_list"
    )

    sample_list = sa.orm.relationship(
        "Sample",
        secondary="sample_to_investigator",
        back_populates="investigator_list"
    )

    def json(self):
        return {
            'investigator_name': self.investigator_name,
            'institution': self.institution,
            'url': self.url,
        }


class Login(db.Model):
    __tablename__ = 'login'

    __table_args__ = (
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id']),
    )

    login_id = sa.Column('login_id', mysql.INTEGER(unsigned=True), primary_key=True)

    user_id = sa.Column('user_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    login_date = sa.Column('login_date', sa.DateTime)  # column.type was 'DATETIME'


    def json(self):
        return {
            'user_id': self.user_id,
            'login_date': self.login_date,
        }


class Metadata_type(db.Model):
    __tablename__ = 'metadata_type'

    metadata_type_id = sa.Column('metadata_type_id', mysql.INTEGER(unsigned=True), primary_key=True)

    category = sa.Column('category', mysql.VARCHAR(64))  # column.type was 'VARCHAR(64)'

    category_type = sa.Column('category_type', mysql.VARCHAR(32))  # column.type was 'VARCHAR(32)'

    qiime_tag = sa.Column('qiime_tag', mysql.VARCHAR(128))  # column.type was 'VARCHAR(128)'

    mgrast_tag = sa.Column('mgrast_tag', mysql.VARCHAR(128))  # column.type was 'VARCHAR(128)'

    tag = sa.Column('tag', mysql.VARCHAR(128))  # column.type was 'VARCHAR(128)'

    definition = sa.Column('definition', mysql.TEXT())  # column.type was 'TEXT'

    required = sa.Column('required', mysql.TINYINT(4))  # column.type was 'TINYINT(4)'

    mixs = sa.Column('mixs', mysql.TINYINT(4))  # column.type was 'TINYINT(4)'

    type = sa.Column('type', mysql.TEXT())  # column.type was 'TEXT'

    fw_type = sa.Column('fw_type', mysql.TEXT())  # column.type was 'TEXT'

    unit = sa.Column('unit', mysql.TEXT())  # column.type was 'TEXT'


    def json(self):
        return {
            'category': self.category,
            'category_type': self.category_type,
            'qiime_tag': self.qiime_tag,
            'mgrast_tag': self.mgrast_tag,
            'tag': self.tag,
            'definition': self.definition,
            'required': self.required,
            'mixs': self.mixs,
            'type': self.type,
            'fw_type': self.fw_type,
            'unit': self.unit,
        }


class Ontology(db.Model):
    __tablename__ = 'ontology'

    __table_args__ = (
        sa.ForeignKeyConstraint(['ontology_type_id'], ['ontology_type.ontology_type_id']),
    )

    ontology_id = sa.Column('ontology_id', mysql.INTEGER(unsigned=True), primary_key=True)

    ontology_acc = sa.Column('ontology_acc', mysql.VARCHAR(125))  # column.type was 'VARCHAR(125)'

    label = sa.Column('label', mysql.VARCHAR(125))  # column.type was 'VARCHAR(125)'

    ontology_type_id = sa.Column('ontology_type_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    sample_list = sa.orm.relationship(
        "Sample",
        secondary="sample_to_ontology",
        back_populates="ontology_list"
    )

    def json(self):
        return {
            'ontology_acc': self.ontology_acc,
            'label': self.label,
            'ontology_type_id': self.ontology_type_id,
        }


class Ontology_type(db.Model):
    __tablename__ = 'ontology_type'

    ontology_type_id = sa.Column('ontology_type_id', mysql.INTEGER(unsigned=True), primary_key=True)

    type = sa.Column('type', mysql.VARCHAR(256))  # column.type was 'VARCHAR(256)'

    url_template = sa.Column('url_template', mysql.VARCHAR(256))  # column.type was 'VARCHAR(256)'


    def json(self):
        return {
            'type': self.type,
            'url_template': self.url_template,
        }


class Project(db.Model):
    __tablename__ = 'project'

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_code = sa.Column('project_code', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    project_name = sa.Column('project_name', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    pi = sa.Column('pi', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    institution = sa.Column('institution', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    project_type = sa.Column('project_type', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    description = sa.Column('description', mysql.TEXT())  # column.type was 'TEXT'

    url = sa.Column('url', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    read_file = sa.Column('read_file', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'

    meta_file = sa.Column('meta_file', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'

    assembly_file = sa.Column('assembly_file', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'

    peptide_file = sa.Column('peptide_file', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'

    email = sa.Column('email', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    read_pep_file = sa.Column('read_pep_file', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'

    nt_file = sa.Column('nt_file', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'


    domain_list = sa.orm.relationship(
        "Domain",
        secondary="project_to_domain",
        back_populates="project_list"
    )

    investigator_list = sa.orm.relationship(
        "Investigator",
        secondary="project_to_investigator",
        back_populates="project_list"
    )

    project_group_list = sa.orm.relationship(
        "Project_group",
        secondary="project_to_project_group",
        back_populates="project_list"
    )

    protocol_list = sa.orm.relationship(
        "Protocol",
        secondary="project_to_protocol",
        back_populates="project_list"
    )

    def json(self):
        return {
            'project_code': self.project_code,
            'project_name': self.project_name,
            'pi': self.pi,
            'institution': self.institution,
            'project_type': self.project_type,
            'description': self.description,
            'url': self.url,
            'read_file': self.read_file,
            'meta_file': self.meta_file,
            'assembly_file': self.assembly_file,
            'peptide_file': self.peptide_file,
            'email': self.email,
            'read_pep_file': self.read_pep_file,
            'nt_file': self.nt_file,
        }


class Project_file(db.Model):
    __tablename__ = 'project_file'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_file_type_id'], ['project_file_type.project_file_type_id']),
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id'])
    )

    project_file_id = sa.Column('project_file_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    project_file_type_id = sa.Column('project_file_type_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    file = sa.Column('file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    def json(self):
        return {
            'project_id': self.project_id,
            'project_file_type_id': self.project_file_type_id,
            'file': self.file,
        }


class Project_file_type(db.Model):
    __tablename__ = 'project_file_type'

    project_file_type_id = sa.Column('project_file_type_id', mysql.INTEGER(unsigned=True), primary_key=True)

    type = sa.Column('type', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    def json(self):
        return {
            'type': self.type,
        }


class Project_group(db.Model):
    __tablename__ = 'project_group'

    project_group_id = sa.Column('project_group_id', mysql.INTEGER(unsigned=True), primary_key=True)

    group_name = sa.Column('group_name', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    description = sa.Column('description', mysql.TEXT())  # column.type was 'TEXT'

    url = sa.Column('url', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    project_list = sa.orm.relationship(
        "Project",
        secondary="project_to_project_group",
        back_populates="project_group_list"
    )

    def json(self):
        return {
            'group_name': self.group_name,
            'description': self.description,
            'url': self.url,
        }


class Project_page(db.Model):
    __tablename__ = 'project_page'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id']),
    )

    project_page_id = sa.Column('project_page_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    title = sa.Column('title', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    contents = sa.Column('contents', mysql.TEXT())  # column.type was 'TEXT'

    display_order = sa.Column('display_order', mysql.INTEGER())  # column.type was 'INTEGER(11)'

    format = sa.Column('format', mysql.ENUM('html','markdown'))  # column.type was 'ENUM('html','markdown')'


    def json(self):
        return {
            'project_id': self.project_id,
            'title': self.title,
            'contents': self.contents,
            'display_order': self.display_order,
            'format': self.format,
        }


class Project_to_domain(db.Model):
    __tablename__ = 'project_to_domain'

    __table_args__ = (
        sa.ForeignKeyConstraint(['domain_id'], ['domain.domain_id']),
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id'])
    )

    project_to_domain_id = sa.Column('project_to_domain_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    domain_id = sa.Column('domain_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'project_id': self.project_id,
            'domain_id': self.domain_id,
        }


class Project_to_investigator(db.Model):
    __tablename__ = 'project_to_investigator'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id']),
        sa.ForeignKeyConstraint(['investigator_id'], ['investigator.investigator_id'])
    )

    project_to_investigator_id = sa.Column('project_to_investigator_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    investigator_id = sa.Column('investigator_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'project_id': self.project_id,
            'investigator_id': self.investigator_id,
        }


class Project_to_project_group(db.Model):
    __tablename__ = 'project_to_project_group'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_group_id'], ['project_group.project_group_id']),
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id'])
    )

    project_to_project_group_id = sa.Column('project_to_project_group_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_group_id = sa.Column('project_group_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'project_group_id': self.project_group_id,
            'project_id': self.project_id,
        }


class Project_to_protocol(db.Model):
    __tablename__ = 'project_to_protocol'

    __table_args__ = (
        sa.ForeignKeyConstraint(['protocol_id'], ['protocol.protocol_id']),
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id'])
    )

    project_to_protocol_id = sa.Column('project_to_protocol_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    protocol_id = sa.Column('protocol_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'project_id': self.project_id,
            'protocol_id': self.protocol_id,
        }


class Protocol(db.Model):
    __tablename__ = 'protocol'

    protocol_id = sa.Column('protocol_id', mysql.INTEGER(unsigned=True), primary_key=True)

    protocol_name = sa.Column('protocol_name', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    url = sa.Column('url', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    project_list = sa.orm.relationship(
        "Project",
        secondary="project_to_protocol",
        back_populates="protocol_list"
    )

    def json(self):
        return {
            'protocol_name': self.protocol_name,
            'url': self.url,
        }


class Pubchase(db.Model):
    __tablename__ = 'pubchase'

    pubchase_id = sa.Column('pubchase_id', mysql.INTEGER(unsigned=True), primary_key=True)

    article_id = sa.Column('article_id', mysql.INTEGER())  # column.type was 'INTEGER(11)'

    title = sa.Column('title', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    journal_title = sa.Column('journal_title', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    doi = sa.Column('doi', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    authors = sa.Column('authors', mysql.MEDIUMTEXT())  # column.type was 'MEDIUMTEXT'

    article_date = sa.Column('article_date', sa.Date)  # column.type was 'DATE'

    created_on = sa.Column('created_on', sa.Date)  # column.type was 'DATE'

    url = sa.Column('url', mysql.MEDIUMTEXT())  # column.type was 'MEDIUMTEXT'


    def json(self):
        return {
            'article_id': self.article_id,
            'title': self.title,
            'journal_title': self.journal_title,
            'doi': self.doi,
            'authors': self.authors,
            'article_date': self.article_date,
            'created_on': self.created_on,
            'url': self.url,
        }


class Pubchase_rec(db.Model):
    __tablename__ = 'pubchase_rec'

    pubchase_rec_id = sa.Column('pubchase_rec_id', mysql.INTEGER(unsigned=True), primary_key=True)

    rec_date = sa.Column('rec_date', sa.DateTime)  # column.type was 'DATETIME'

    checksum = sa.Column('checksum', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    def json(self):
        return {
            'rec_date': self.rec_date,
            'checksum': self.checksum,
        }


class Publication(db.Model):
    __tablename__ = 'publication'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id']),
    )

    publication_id = sa.Column('publication_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    pub_code = sa.Column('pub_code', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    doi = sa.Column('doi', mysql.TEXT())  # column.type was 'TEXT'

    author = sa.Column('author', mysql.TEXT())  # column.type was 'TEXT'

    title = sa.Column('title', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    pubmed_id = sa.Column('pubmed_id', mysql.INTEGER())  # column.type was 'INTEGER(11)'

    journal = sa.Column('journal', mysql.TEXT())  # column.type was 'TEXT'

    pub_date = sa.Column('pub_date', mysql.TEXT())  # column.type was 'TEXT'


    def json(self):
        return {
            'project_id': self.project_id,
            'pub_code': self.pub_code,
            'doi': self.doi,
            'author': self.author,
            'title': self.title,
            'pubmed_id': self.pubmed_id,
            'journal': self.journal,
            'pub_date': self.pub_date,
        }


class Query_log(db.Model):
    __tablename__ = 'query_log'

    query_log_id = sa.Column('query_log_id', mysql.INTEGER(unsigned=True), primary_key=True)

    num_found = sa.Column('num_found', mysql.INTEGER())  # column.type was 'INTEGER(11)'

    query = sa.Column('query', mysql.TEXT())  # column.type was 'TEXT'

    params = sa.Column('params', mysql.TEXT())  # column.type was 'TEXT'

    ip = sa.Column('ip', mysql.TEXT())  # column.type was 'TEXT'

    user_id = sa.Column('user_id', mysql.TEXT())  # column.type was 'TEXT'

    time = sa.Column('time', sa.Float)  # column.type was 'DOUBLE'

    date = sa.Column('date', mysql.TIMESTAMP)  # column.type was 'TIMESTAMP'


    def json(self):
        return {
            'num_found': self.num_found,
            'query': self.query,
            'params': self.params,
            'ip': self.ip,
            'user_id': self.user_id,
            'time': self.time,
            'date': self.date,
        }


class Reference(db.Model):
    __tablename__ = 'reference'

    reference_id = sa.Column('reference_id', mysql.INTEGER(unsigned=True), primary_key=True)

    file = sa.Column('file', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    name = sa.Column('name', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'

    revision = sa.Column('revision', mysql.TEXT())  # column.type was 'TEXT'

    length = sa.Column('length', mysql.BIGINT(unsigned=True))  # column.type was 'BIGINT(20) UNSIGNED'

    seq_count = sa.Column('seq_count', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    build_date = sa.Column('build_date', mysql.TEXT())  # column.type was 'TEXT'

    description = sa.Column('description', mysql.TEXT())  # column.type was 'TEXT'


    def json(self):
        return {
            'file': self.file,
            'name': self.name,
            'revision': self.revision,
            'length': self.length,
            'seq_count': self.seq_count,
            'build_date': self.build_date,
            'description': self.description,
        }


class Sample(db.Model):
    __tablename__ = 'sample'

    __table_args__ = (
        sa.ForeignKeyConstraint(['project_id'], ['project.project_id']),
        sa.ForeignKeyConstraint(['combined_assembly_id'], ['combined_assembly.combined_assembly_id'])
    )

    sample_id = sa.Column('sample_id', mysql.INTEGER(unsigned=True), primary_key=True)

    project_id = sa.Column('project_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    combined_assembly_id = sa.Column('combined_assembly_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    sample_acc = sa.Column('sample_acc', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    sample_name = sa.Column('sample_name', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    sample_type = sa.Column('sample_type', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    sample_description = sa.Column('sample_description', mysql.TEXT())  # column.type was 'TEXT'

    comments = sa.Column('comments', mysql.TEXT())  # column.type was 'TEXT'

    taxon_id = sa.Column('taxon_id', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    latitude = sa.Column('latitude', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    longitude = sa.Column('longitude', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    url = sa.Column('url', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    combined_assembly_list = sa.orm.relationship(
        "Combined_assembly",
        secondary="combined_assembly_to_sample",
        back_populates="sample_list"
    )

    investigator_list = sa.orm.relationship(
        "Investigator",
        secondary="sample_to_investigator",
        back_populates="sample_list"
    )

    ontology_list = sa.orm.relationship(
        "Ontology",
        secondary="sample_to_ontology",
        back_populates="sample_list"
    )

    uproc_list = sa.orm.relationship(
        "Uproc",
        secondary="sample_to_uproc",
        back_populates="sample_list"
    )

    def json(self):
        return {
            'project_id': self.project_id,
            'combined_assembly_id': self.combined_assembly_id,
            'sample_acc': self.sample_acc,
            'sample_name': self.sample_name,
            'sample_type': self.sample_type,
            'sample_description': self.sample_description,
            'comments': self.comments,
            'taxon_id': self.taxon_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'url': self.url,
        }


class Sample_attr(db.Model):
    __tablename__ = 'sample_attr'

    __table_args__ = (
        sa.ForeignKeyConstraint(['sample_attr_type_id'], ['sample_attr_type.sample_attr_type_id']),
        sa.ForeignKeyConstraint(['sample_id'], ['sample.sample_id'])
    )

    sample_attr_id = sa.Column('sample_attr_id', mysql.INTEGER(unsigned=True), primary_key=True)

    sample_attr_type_id = sa.Column('sample_attr_type_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    sample_id = sa.Column('sample_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    attr_value = sa.Column('attr_value', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    unit = sa.Column('unit', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    def json(self):
        return {
            'sample_attr_type_id': self.sample_attr_type_id,
            'sample_id': self.sample_id,
            'attr_value': self.attr_value,
            'unit': self.unit,
        }


class Sample_attr_type(db.Model):
    __tablename__ = 'sample_attr_type'

    sample_attr_type_id = sa.Column('sample_attr_type_id', mysql.INTEGER(unsigned=True), primary_key=True)

    type = sa.Column('type', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    url_template = sa.Column('url_template', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    description = sa.Column('description', mysql.MEDIUMTEXT())  # column.type was 'MEDIUMTEXT'

    category = sa.Column('category', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'


    def json(self):
        return {
            'type': self.type,
            'url_template': self.url_template,
            'description': self.description,
            'category': self.category,
        }


class Sample_attr_type_alias(db.Model):
    __tablename__ = 'sample_attr_type_alias'

    __table_args__ = (
        sa.ForeignKeyConstraint(['sample_attr_type_id'], ['sample_attr_type.sample_attr_type_id']),
    )

    sample_attr_type_alias_id = sa.Column('sample_attr_type_alias_id', mysql.INTEGER(unsigned=True), primary_key=True)

    sample_attr_type_id = sa.Column('sample_attr_type_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    alias = sa.Column('alias', mysql.VARCHAR(200))  # column.type was 'VARCHAR(200)'


    def json(self):
        return {
            'sample_attr_type_id': self.sample_attr_type_id,
            'alias': self.alias,
        }


class Sample_file(db.Model):
    __tablename__ = 'sample_file'

    __table_args__ = (
        sa.ForeignKeyConstraint(['sample_file_type_id'], ['sample_file_type.sample_file_type_id']),
        sa.ForeignKeyConstraint(['sample_id'], ['sample.sample_id'])
    )

    sample_file_id = sa.Column('sample_file_id', mysql.INTEGER(unsigned=True), primary_key=True)

    sample_id = sa.Column('sample_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    sample_file_type_id = sa.Column('sample_file_type_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    file = sa.Column('file', mysql.VARCHAR(200))  # column.type was 'VARCHAR(200)'

    num_seqs = sa.Column('num_seqs', mysql.INTEGER())  # column.type was 'INTEGER(11)'

    num_bp = sa.Column('num_bp', mysql.BIGINT(unsigned=True))  # column.type was 'BIGINT(20) UNSIGNED'

    avg_len = sa.Column('avg_len', mysql.INTEGER())  # column.type was 'INTEGER(11)'

    pct_gc = sa.Column('pct_gc', sa.Float)  # column.type was 'DOUBLE'


    def json(self):
        return {
            'sample_id': self.sample_id,
            'sample_file_type_id': self.sample_file_type_id,
            'file': self.file,
            'num_seqs': self.num_seqs,
            'num_bp': self.num_bp,
            'avg_len': self.avg_len,
            'pct_gc': self.pct_gc,
        }


class Sample_file_type(db.Model):
    __tablename__ = 'sample_file_type'

    sample_file_type_id = sa.Column('sample_file_type_id', mysql.INTEGER(unsigned=True), primary_key=True)

    type = sa.Column('type', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'


    def json(self):
        return {
            'type': self.type,
        }


class Sample_to_investigator(db.Model):
    __tablename__ = 'sample_to_investigator'

    __table_args__ = (
        sa.ForeignKeyConstraint(['sample_id'], ['sample.sample_id']),
        sa.ForeignKeyConstraint(['investigator_id'], ['investigator.investigator_id'])
    )

    sample_to_investigator_id = sa.Column('sample_to_investigator_id', mysql.INTEGER(unsigned=True), primary_key=True)

    sample_id = sa.Column('sample_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    investigator_id = sa.Column('investigator_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'sample_id': self.sample_id,
            'investigator_id': self.investigator_id,
        }


class Sample_to_ontology(db.Model):
    __tablename__ = 'sample_to_ontology'

    __table_args__ = (
        sa.ForeignKeyConstraint(['ontology_id'], ['ontology.ontology_id']),
        sa.ForeignKeyConstraint(['sample_id'], ['sample.sample_id'])
    )

    sample_to_ontology_id = sa.Column('sample_to_ontology_id', mysql.INTEGER(unsigned=True), primary_key=True)

    sample_id = sa.Column('sample_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    ontology_id = sa.Column('ontology_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'


    def json(self):
        return {
            'sample_id': self.sample_id,
            'ontology_id': self.ontology_id,
        }


class Sample_to_uproc(db.Model):
    __tablename__ = 'sample_to_uproc'

    __table_args__ = (
        sa.ForeignKeyConstraint(['sample_id'], ['sample.sample_id']),
        sa.ForeignKeyConstraint(['uproc_id'], ['uproc.uproc_id'])
    )

    sample_to_uproc_id = sa.Column('sample_to_uproc_id', mysql.INTEGER(unsigned=True), primary_key=True)

    sample_id = sa.Column('sample_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    uproc_id = sa.Column('uproc_id', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    read_count = sa.Column('read_count', mysql.INTEGER())  # column.type was 'INTEGER(11)'


    def json(self):
        return {
            'sample_id': self.sample_id,
            'uproc_id': self.uproc_id,
            'read_count': self.read_count,
        }


class Search(db.Model):
    __tablename__ = 'search'

    search_id = sa.Column('search_id', mysql.INTEGER(unsigned=True), primary_key=True)

    table_name = sa.Column('table_name', mysql.VARCHAR(100))  # column.type was 'VARCHAR(100)'

    primary_key = sa.Column('primary_key', mysql.INTEGER(unsigned=True))  # column.type was 'INTEGER(10) UNSIGNED'

    object_name = sa.Column('object_name', mysql.VARCHAR(255))  # column.type was 'VARCHAR(255)'

    search_text = sa.Column('search_text', mysql.LONGTEXT())  # column.type was 'LONGTEXT'


    def json(self):
        return {
            'table_name': self.table_name,
            'primary_key': self.primary_key,
            'object_name': self.object_name,
            'search_text': self.search_text,
        }


class Uproc(db.Model):
    __tablename__ = 'uproc'

    uproc_id = sa.Column('uproc_id', mysql.INTEGER(unsigned=True), primary_key=True)

    accession = sa.Column('accession', mysql.VARCHAR(16))  # column.type was 'VARCHAR(16)'

    identifier = sa.Column('identifier', mysql.VARCHAR(16))  # column.type was 'VARCHAR(16)'

    name = sa.Column('name', mysql.VARCHAR(80))  # column.type was 'VARCHAR(80)'

    description = sa.Column('description', mysql.TEXT())  # column.type was 'TEXT'


    sample_list = sa.orm.relationship(
        "Sample",
        secondary="sample_to_uproc",
        back_populates="uproc_list"
    )

    def json(self):
        return {
            'accession': self.accession,
            'identifier': self.identifier,
            'name': self.name,
            'description': self.description,
        }


class User(db.Model):
    __tablename__ = 'user'

    user_id = sa.Column('user_id', mysql.INTEGER(unsigned=True), primary_key=True)

    user_name = sa.Column('user_name', mysql.VARCHAR(50))  # column.type was 'VARCHAR(50)'


    def json(self):
        return {
            'user_name': self.user_name,
        }


