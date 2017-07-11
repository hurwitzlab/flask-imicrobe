from app import db


class App(db.Model):
    __tablename__ = 'app'
    app_id = db.Column('app_id', db.Integer, primary_key=True)
    app_name = db.Column('app_name', db.VARCHAR(50))
    is_active = db.Column('is_active', db.INTEGER)


class Domain(db.Model):
    __tablename__ = 'domain'
    domain_id = db.Column('domain_id', db.Integer, primary_key=True)
    domain_name = db.Column('domain_name', db.VARCHAR(50))


class Investigator(db.Model):
    __tablename__ = 'investigator'
    investigator_id = db.Column('investigator_id', db.Integer, primary_key=True)
    investigator_name = db.Column('investigator_name', db.VARCHAR(255))
    institution = db.Column('institution', db.VARCHAR(255))


class Metadata_type(db.Model):
    __tablename__ = 'metadata_type'
    metadata_type_id = db.Column('metadata_type_id', db.Integer, primary_key=True)
    category = db.Column('category', db.VARCHAR(64))
    category_type = db.Column('category_type', db.VARCHAR(32))
    qiime_tag = db.Column('qiime_tag', db.VARCHAR(128))
    mgrast_tag = db.Column('mgrast_tag', db.VARCHAR(128))
    tag = db.Column('tag', db.VARCHAR(128))
    definition = db.Column('definition', db.TEXT)
    required = db.Column('required', db.INTEGER)
    mixs = db.Column('mixs', db.INTEGER)
    type = db.Column('type', db.TEXT)
    fw_type = db.Column('fw_type', db.TEXT)
    unit = db.Column('unit', db.TEXT)


class Ontology_type(db.Model):
    __tablename__ = 'ontology_type'
    ontology_type_id = db.Column('ontology_type_id', db.Integer, primary_key=True)
    type = db.Column('type', db.VARCHAR(256))
    url_template = db.Column('url_template', db.VARCHAR(256))


class Project(db.Model):
    __tablename__ = 'project'
    project_id = db.Column('project_id', db.Integer, primary_key=True)
    project_code = db.Column('project_code', db.VARCHAR(255))
    project_name = db.Column('project_name', db.VARCHAR(255))
    pi = db.Column('pi', db.VARCHAR(255))
    institution = db.Column('institution', db.VARCHAR(255))
    project_type = db.Column('project_type', db.VARCHAR(255))
    description = db.Column('description', db.TEXT)
    url = db.Column('url', db.VARCHAR(255))
    read_file = db.Column('read_file', db.VARCHAR(100))
    meta_file = db.Column('meta_file', db.VARCHAR(100))
    assembly_file = db.Column('assembly_file', db.VARCHAR(100))
    peptide_file = db.Column('peptide_file', db.VARCHAR(100))
    email = db.Column('email', db.VARCHAR(255))
    read_pep_file = db.Column('read_pep_file', db.VARCHAR(100))
    nt_file = db.Column('nt_file', db.VARCHAR(100))


class Project_file_type(db.Model):
    __tablename__ = 'project_file_type'
    project_file_type_id = db.Column('project_file_type_id', db.Integer, primary_key=True)
    type = db.Column('type', db.VARCHAR(255))


class Project_group(db.Model):
    __tablename__ = 'project_group'
    project_group_id = db.Column('project_group_id', db.Integer, primary_key=True)
    group_name = db.Column('group_name', db.VARCHAR(255))
    description = db.Column('description', db.TEXT)
    url = db.Column('url', db.VARCHAR(255))


class Protocol(db.Model):
    __tablename__ = 'protocol'
    protocol_id = db.Column('protocol_id', db.Integer, primary_key=True)
    protocol_name = db.Column('protocol_name', db.VARCHAR(255))
    url = db.Column('url', db.VARCHAR(255))


class Pubchase(db.Model):
    __tablename__ = 'pubchase'
    pubchase_id = db.Column('pubchase_id', db.Integer, primary_key=True)
    article_id = db.Column('article_id', db.Integer)
    title = db.Column('title', db.VARCHAR(255))
    journal_title = db.Column('journal_title', db.VARCHAR(255))
    doi = db.Column('doi', db.VARCHAR(255))
    authors = db.Column('authors', db.TEXT)
    article_date = db.Column('article_date', db.DATE)
    created_on = db.Column('created_on', db.DATE)
    url = db.Column('url', db.TEXT)


class Pubchase_rec(db.Model):
    __tablename__ = 'pubchase_rec'
    pubchase_rec_id = db.Column('pubchase_rec_id', db.Integer, primary_key=True)
    rec_date = db.Column('rec_date', db.DATETIME)
    checksum = db.Column('checksum', db.VARCHAR(255))


class Query_log(db.Model):
    __tablename__ = 'query_log'
    query_log_id = db.Column('query_log_id', db.Integer, primary_key=True)
    num_found = db.Column('num_found', db.INTEGER)
    query = db.Column('query', db.TEXT)
    params = db.Column('params', db.TEXT)
    ip = db.Column('ip', db.TEXT)
    user_id = db.Column('user_id', db.Integer)
    time = db.Column('time', db.Float)
    date = db.Column('date', db.TIMESTAMP)


class Reference(db.Model):
    __tablename__ = 'reference'
    reference_id = db.Column('reference_id', db.Integer, primary_key=True)
    file = db.Column('file', db.VARCHAR(255))
    name = db.Column('name', db.VARCHAR(100))
    revision = db.Column('revision', db.TEXT)
    length = db.Column('length', db.INTEGER)
    seq_count = db.Column('seq_count', db.INTEGER)
    build_date = db.Column('build_date', db.TEXT)
    description = db.Column('description', db.TEXT)


class Sample_attr_type(db.Model):
    __tablename__ = 'sample_attr_type'
    sample_attr_type_id = db.Column('sample_attr_type_id', db.Integer, primary_key=True)
    type = db.Column('type', db.VARCHAR(255))
    url_template = db.Column('url_template', db.VARCHAR(255))
    description = db.Column('description', db.TEXT)
    category = db.Column('category', db.VARCHAR(100))


class Sample_file_type(db.Model):
    __tablename__ = 'sample_file_type'
    sample_file_type_id = db.Column('sample_file_type_id', db.Integer, primary_key=True)
    type = db.Column('type', db.VARCHAR(255))


class Search(db.Model):
    __tablename__ = 'search'
    search_id = db.Column('search_id', db.Integer, primary_key=True)
    table_name = db.Column('table_name', db.VARCHAR(100))
    primary_key = db.Column('primary_key', db.INTEGER)
    search_text = db.Column('search_text', db.Text)


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    user_name = db.Column('user_name', db.VARCHAR(50))


class App_run(db.Model):
    __tablename__ = 'app_run'
    app_run_id = db.Column('app_run_id', db.Integer, primary_key=True)
    app_id = db.Column('app_id', db.Integer)
    user_id = db.Column('user_id', db.Integer)
    app_ran_at = db.Column('app_ran_at', db.DATETIME)
    params = db.Column('params', db.TEXT)


class Combined_assembly(db.Model):
    __tablename__ = 'combined_assembly'
    combined_assembly_id = db.Column('combined_assembly_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    assembly_name = db.Column('assembly_name', db.VARCHAR(255))
    phylum = db.Column('phylum', db.VARCHAR(255))
    clazz = db.Column('clazz', db.VARCHAR(255))
    family = db.Column('family', db.VARCHAR(255))
    genus = db.Column('genus', db.VARCHAR(255))
    species = db.Column('species', db.VARCHAR(255))
    strain = db.Column('strain', db.VARCHAR(255))
    pcr_amp = db.Column('pcr_amp', db.VARCHAR(255))
    annotations_file = db.Column('annotations_file', db.VARCHAR(255))
    peptides_file = db.Column('peptides_file', db.VARCHAR(255))
    nucleotides_file = db.Column('nucleotides_file', db.VARCHAR(255))
    cds_file = db.Column('cds_file', db.VARCHAR(255))


class Ftp(db.Model):
    __tablename__ = 'ftp'
    ftp_id = db.Column('ftp_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    name = db.Column('name', db.VARCHAR(255))
    path = db.Column('path', db.VARCHAR(255))
    size = db.Column('size', db.VARCHAR(20))


class Login(db.Model):
    __tablename__ = 'login'
    login_id = db.Column('login_id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer)
    login_date = db.Column('login_date', db.DATETIME)


class Ontology(db.Model):
    __tablename__ = 'ontology'
    ontology_id = db.Column('ontology_id', db.Integer, primary_key=True)
    ontology_acc = db.Column('ontology_acc', db.VARCHAR(125))
    label = db.Column('label', db.VARCHAR(125))
    ontology_type_id = db.Column('ontology_type_id', db.Integer)


class Project_file(db.Model):
    __tablename__ = 'project_file'
    project_file_id = db.Column('project_file_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    project_file_type_id = db.Column('project_file_type_id', db.Integer)
    file = db.Column('file', db.VARCHAR(255))


class Project_page(db.Model):
    __tablename__ = 'project_page'
    project_page_id = db.Column('project_page_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    title = db.Column('title', db.VARCHAR(255))
    contents = db.Column('contents', db.TEXT)
    display_order = db.Column('display_order', db.INTEGER)
    format = db.Column('format', db.Enum)


class Project_to_domain(db.Model):
    __tablename__ = 'project_to_domain'
    project_to_domain_id = db.Column('project_to_domain_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    domain_id = db.Column('domain_id', db.Integer)


class Project_to_investigator(db.Model):
    __tablename__ = 'project_to_investigator'
    project_to_investigator_id = db.Column('project_to_investigator_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    investigator_id = db.Column('investigator_id', db.Integer)


class Project_to_project_group(db.Model):
    __tablename__ = 'project_to_project_group'
    project_to_project_group_id = db.Column('project_to_project_group_id', db.Integer, primary_key=True)
    project_group_id = db.Column('project_group_id', db.Integer)
    project_id = db.Column('project_id', db.Integer)


class Project_to_protocol(db.Model):
    __tablename__ = 'project_to_protocol'
    project_to_protocol_id = db.Column('project_to_protocol_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    protocol_id = db.Column('protocol_id', db.Integer)


class Publication(db.Model):
    __tablename__ = 'publication'
    publication_id = db.Column('publication_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    pub_code = db.Column('pub_code', db.VARCHAR(255))
    doi = db.Column('doi', db.TEXT)
    author = db.Column('author', db.TEXT)
    title = db.Column('title', db.VARCHAR(255))
    pubmed_id = db.Column('pubmed_id', db.Integer)
    journal = db.Column('journal', db.TEXT)
    pub_date = db.Column('pub_date', db.TEXT)


class Sample_attr_type_alias(db.Model):
    __tablename__ = 'sample_attr_type_alias'
    sample_attr_type_alias_id = db.Column('sample_attr_type_alias_id', db.Integer, primary_key=True)
    sample_attr_type_id = db.Column('sample_attr_type_id', db.Integer)
    alias = db.Column('alias', db.VARCHAR(200))


class Sample(db.Model):
    __tablename__ = 'sample'
    sample_id = db.Column('sample_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    combined_assembly_id = db.Column('combined_assembly_id', db.Integer)
    sample_acc = db.Column('sample_acc', db.VARCHAR(255))
    sample_name = db.Column('sample_name', db.VARCHAR(255))
    sample_type = db.Column('sample_type', db.VARCHAR(255))
    sample_description = db.Column('sample_description', db.TEXT)
    comments = db.Column('comments', db.TEXT)
    taxon_id = db.Column('taxon_id', db.Integer)
    latitude = db.Column('latitude', db.VARCHAR(255))
    longitude = db.Column('longitude', db.VARCHAR(255))
    url = db.Column('url', db.VARCHAR(255))


class Assembly(db.Model):
    __tablename__ = 'assembly'
    assembly_id = db.Column('assembly_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    assembly_code = db.Column('assembly_code', db.VARCHAR(255))
    assembly_name = db.Column('assembly_name', db.TEXT)
    organism = db.Column('organism', db.VARCHAR(255))
    pep_file = db.Column('pep_file', db.VARCHAR(255))
    nt_file = db.Column('nt_file', db.VARCHAR(255))
    cds_file = db.Column('cds_file', db.VARCHAR(255))
    description = db.Column('description', db.TEXT)
    sample_id = db.Column('sample_id', db.Integer)


class Combined_assembly_to_sample(db.Model):
    __tablename__ = 'combined_assembly_to_sample'
    combined_assembly_to_sample_id = db.Column('combined_assembly_to_sample_id', db.Integer, primary_key=True)
    combined_assembly_id = db.Column('combined_assembly_id', db.Integer)
    sample_id = db.Column('sample_id', db.Integer)


class Sample_attr(db.Model):
    __tablename__ = 'sample_attr'
    sample_attr_id = db.Column('sample_attr_id', db.Integer, primary_key=True)
    sample_attr_type_id = db.Column('sample_attr_type_id', db.Integer)
    sample_id = db.Column('sample_id', db.Integer)
    attr_value = db.Column('attr_value', db.VARCHAR(255))
    unit = db.Column('unit', db.VARCHAR(255))


class Sample_file(db.Model):
    __tablename__ = 'sample_file'
    sample_file_id = db.Column('sample_file_id', db.Integer, primary_key=True)
    sample_id = db.Column('sample_id', db.Integer)
    sample_file_type_id = db.Column('sample_file_type_id', db.Integer)
    file = db.Column('file', db.VARCHAR(200))
    num_seqs = db.Column('num_seqs', db.INTEGER)
    num_bp = db.Column('num_bp', db.INTEGER)
    avg_len = db.Column('avg_len', db.INTEGER)
    pct_gc = db.Column('pct_gc', db.Float)


class Sample_to_investigator(db.Model):
    __tablename__ = 'sample_to_investigator'
    sample_to_investigator_id = db.Column('sample_to_investigator_id', db.Integer, primary_key=True)
    sample_id = db.Column('sample_id', db.Integer)
    investigator_id = db.Column('investigator_id', db.Integer)


class Sample_to_ontology(db.Model):
    __tablename__ = 'sample_to_ontology'
    sample_to_ontology_id = db.Column('sample_to_ontology_id', db.Integer, primary_key=True)
    sample_id = db.Column('sample_id', db.Integer)
    ontology_id = db.Column('ontology_id', db.Integer)


