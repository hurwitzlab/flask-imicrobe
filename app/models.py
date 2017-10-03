from app import db

class App(db.Model):
    __tablename__ = 'app'
    app_id = db.Column('app_id', db.Integer, primary_key=True)
    app_name = db.Column('app_name', db.VARCHAR(50))
    is_active = db.Column('is_active', db.INTEGER)

    def json(self):
        return {
            'app_name': self.app_name,
            'is_active': self.is_active,
        }

class Domain(db.Model):
    __tablename__ = 'domain'
    domain_id = db.Column('domain_id', db.Integer, primary_key=True)
    domain_name = db.Column('domain_name', db.VARCHAR(50))

    def json(self):
        return {
            'domain_name': self.domain_name,
        }

class Investigator(db.Model):
    __tablename__ = 'investigator'
    investigator_id = db.Column('investigator_id', db.Integer, primary_key=True)
    investigator_name = db.Column('investigator_name', db.VARCHAR(255))
    institution = db.Column('institution', db.VARCHAR(255))
    url = db.Column('url', db.VARCHAR(255))

    def json(self):
        return {
            'investigator_name': self.investigator_name,
            'institution': self.institution,
            'url': self.url,
        }

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

class Ontology_type(db.Model):
    __tablename__ = 'ontology_type'
    ontology_type_id = db.Column('ontology_type_id', db.Integer, primary_key=True)
    type = db.Column('type', db.VARCHAR(256))
    url_template = db.Column('url_template', db.VARCHAR(256))

    def json(self):
        return {
            'type': self.type,
            'url_template': self.url_template,
        }

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

class Project_file_type(db.Model):
    __tablename__ = 'project_file_type'
    project_file_type_id = db.Column('project_file_type_id', db.Integer, primary_key=True)
    type = db.Column('type', db.VARCHAR(255))

    def json(self):
        return {
            'type': self.type,
        }

class Project_group(db.Model):
    __tablename__ = 'project_group'
    project_group_id = db.Column('project_group_id', db.Integer, primary_key=True)
    group_name = db.Column('group_name', db.VARCHAR(255))
    description = db.Column('description', db.TEXT)
    url = db.Column('url', db.VARCHAR(255))

    def json(self):
        return {
            'group_name': self.group_name,
            'description': self.description,
            'url': self.url,
        }

class Protocol(db.Model):
    __tablename__ = 'protocol'
    protocol_id = db.Column('protocol_id', db.Integer, primary_key=True)
    protocol_name = db.Column('protocol_name', db.VARCHAR(255))
    url = db.Column('url', db.VARCHAR(255))

    def json(self):
        return {
            'protocol_name': self.protocol_name,
            'url': self.url,
        }

class Pubchase(db.Model):
    __tablename__ = 'pubchase'
    pubchase_id = db.Column('pubchase_id', db.Integer, primary_key=True)
    article_id = db.Column('article_id', db.Integer)
    title = db.Column('title', db.VARCHAR(255))
    journal_title = db.Column('journal_title', db.VARCHAR(255))
    doi = db.Column('doi', db.VARCHAR(255))
    authors = db.Column('authors', db.Text)
    article_date = db.Column('article_date', db.DATE)
    created_on = db.Column('created_on', db.DATE)
    url = db.Column('url', db.Text)

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
    pubchase_rec_id = db.Column('pubchase_rec_id', db.Integer, primary_key=True)
    rec_date = db.Column('rec_date', db.DATETIME)
    checksum = db.Column('checksum', db.VARCHAR(255))

    def json(self):
        return {
            'rec_date': self.rec_date,
            'checksum': self.checksum,
        }

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
    reference_id = db.Column('reference_id', db.Integer, primary_key=True)
    file = db.Column('file', db.VARCHAR(255))
    name = db.Column('name', db.VARCHAR(100))
    revision = db.Column('revision', db.TEXT)
    length = db.Column('length', db.INTEGER)
    seq_count = db.Column('seq_count', db.INTEGER)
    build_date = db.Column('build_date', db.TEXT)
    description = db.Column('description', db.TEXT)

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

class Sample_attr_type(db.Model):
    __tablename__ = 'sample_attr_type'
    sample_attr_type_id = db.Column('sample_attr_type_id', db.Integer, primary_key=True)
    type = db.Column('type', db.VARCHAR(255))
    url_template = db.Column('url_template', db.VARCHAR(255))
    description = db.Column('description', db.Text)
    category = db.Column('category', db.VARCHAR(100))

    def json(self):
        return {
            'type': self.type,
            'url_template': self.url_template,
            'description': self.description,
            'category': self.category,
        }

class Sample_file_type(db.Model):
    __tablename__ = 'sample_file_type'
    sample_file_type_id = db.Column('sample_file_type_id', db.Integer, primary_key=True)
    type = db.Column('type', db.VARCHAR(255))

    def json(self):
        return {
            'type': self.type,
        }

class Search(db.Model):
    __tablename__ = 'search'
    search_id = db.Column('search_id', db.Integer, primary_key=True)
    table_name = db.Column('table_name', db.VARCHAR(100))
    primary_key = db.Column('primary_key', db.INTEGER)
    object_name = db.Column('object_name', db.VARCHAR(255))
    search_text = db.Column('search_text', db.Text)

    def json(self):
        return {
            'table_name': self.table_name,
            'primary_key': self.primary_key,
            'object_name': self.object_name,
            'search_text': self.search_text,
        }

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    user_name = db.Column('user_name', db.VARCHAR(50))

    def json(self):
        return {
            'user_name': self.user_name,
        }

class App_run(db.Model):
    __tablename__ = 'app_run'
    app_run_id = db.Column('app_run_id', db.Integer, primary_key=True)
    app_id = db.Column('app_id', db.Integer)
    user_id = db.Column('user_id', db.Integer)
    app_ran_at = db.Column('app_ran_at', db.DATETIME)
    params = db.Column('params', db.TEXT)

    def json(self):
        return {
            'app_id': self.app_id,
            'user_id': self.user_id,
            'app_ran_at': self.app_ran_at,
            'params': self.params,
        }

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

    def json(self):
        return {
            'project_id': self.project_id,
            'assembly_name': self.assembly_name,
            'phylum': self.phylum,
            'clazz': self.clazz,
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

class Ftp(db.Model):
    __tablename__ = 'ftp'
    ftp_id = db.Column('ftp_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    name = db.Column('name', db.VARCHAR(255))
    path = db.Column('path', db.VARCHAR(255))
    size = db.Column('size', db.VARCHAR(20))

    def json(self):
        return {
            'project_id': self.project_id,
            'name': self.name,
            'path': self.path,
            'size': self.size,
        }

class Login(db.Model):
    __tablename__ = 'login'
    login_id = db.Column('login_id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer)
    login_date = db.Column('login_date', db.DATETIME)

    def json(self):
        return {
            'user_id': self.user_id,
            'login_date': self.login_date,
        }

class Ontology(db.Model):
    __tablename__ = 'ontology'
    ontology_id = db.Column('ontology_id', db.Integer, primary_key=True)
    ontology_acc = db.Column('ontology_acc', db.VARCHAR(125))
    label = db.Column('label', db.VARCHAR(125))
    ontology_type_id = db.Column('ontology_type_id', db.Integer)

    def json(self):
        return {
            'ontology_acc': self.ontology_acc,
            'label': self.label,
            'ontology_type_id': self.ontology_type_id,
        }

class Project_file(db.Model):
    __tablename__ = 'project_file'
    project_file_id = db.Column('project_file_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    project_file_type_id = db.Column('project_file_type_id', db.Integer)
    file = db.Column('file', db.VARCHAR(255))

    def json(self):
        return {
            'project_id': self.project_id,
            'project_file_type_id': self.project_file_type_id,
            'file': self.file,
        }

class Project_page(db.Model):
    __tablename__ = 'project_page'
    project_page_id = db.Column('project_page_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    title = db.Column('title', db.VARCHAR(255))
    contents = db.Column('contents', db.TEXT)
    display_order = db.Column('display_order', db.INTEGER)
    format = db.Column('format', db.Enum)

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
    project_to_domain_id = db.Column('project_to_domain_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    domain_id = db.Column('domain_id', db.Integer)

    def json(self):
        return {
            'project_id': self.project_id,
            'domain_id': self.domain_id,
        }

class Project_to_investigator(db.Model):
    __tablename__ = 'project_to_investigator'
    project_to_investigator_id = db.Column('project_to_investigator_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    investigator_id = db.Column('investigator_id', db.Integer)

    def json(self):
        return {
            'project_id': self.project_id,
            'investigator_id': self.investigator_id,
        }

class Project_to_project_group(db.Model):
    __tablename__ = 'project_to_project_group'
    project_to_project_group_id = db.Column('project_to_project_group_id', db.Integer, primary_key=True)
    project_group_id = db.Column('project_group_id', db.Integer)
    project_id = db.Column('project_id', db.Integer)

    def json(self):
        return {
            'project_group_id': self.project_group_id,
            'project_id': self.project_id,
        }

class Project_to_protocol(db.Model):
    __tablename__ = 'project_to_protocol'
    project_to_protocol_id = db.Column('project_to_protocol_id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer)
    protocol_id = db.Column('protocol_id', db.Integer)

    def json(self):
        return {
            'project_id': self.project_id,
            'protocol_id': self.protocol_id,
        }

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

class Sample_attr_type_alias(db.Model):
    __tablename__ = 'sample_attr_type_alias'
    sample_attr_type_alias_id = db.Column('sample_attr_type_alias_id', db.Integer, primary_key=True)
    sample_attr_type_id = db.Column('sample_attr_type_id', db.Integer)
    alias = db.Column('alias', db.VARCHAR(200))

    def json(self):
        return {
            'sample_attr_type_id': self.sample_attr_type_id,
            'alias': self.alias,
        }

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

class Combined_assembly_to_sample(db.Model):
    __tablename__ = 'combined_assembly_to_sample'
    combined_assembly_to_sample_id = db.Column('combined_assembly_to_sample_id', db.Integer, primary_key=True)
    combined_assembly_id = db.Column('combined_assembly_id', db.Integer)
    sample_id = db.Column('sample_id', db.Integer)

    def json(self):
        return {
            'combined_assembly_id': self.combined_assembly_id,
            'sample_id': self.sample_id,
        }

class Sample_attr(db.Model):
    __tablename__ = 'sample_attr'
    sample_attr_id = db.Column('sample_attr_id', db.Integer, primary_key=True)
    sample_attr_type_id = db.Column('sample_attr_type_id', db.Integer)
    sample_id = db.Column('sample_id', db.Integer)
    attr_value = db.Column('attr_value', db.VARCHAR(255))
    unit = db.Column('unit', db.VARCHAR(255))

    def json(self):
        return {
            'sample_attr_type_id': self.sample_attr_type_id,
            'sample_id': self.sample_id,
            'attr_value': self.attr_value,
            'unit': self.unit,
        }

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

class Sample_to_investigator(db.Model):
    __tablename__ = 'sample_to_investigator'
    sample_to_investigator_id = db.Column('sample_to_investigator_id', db.Integer, primary_key=True)
    sample_id = db.Column('sample_id', db.Integer)
    investigator_id = db.Column('investigator_id', db.Integer)

    def json(self):
        return {
            'sample_id': self.sample_id,
            'investigator_id': self.investigator_id,
        }

class Sample_to_ontology(db.Model):
    __tablename__ = 'sample_to_ontology'
    sample_to_ontology_id = db.Column('sample_to_ontology_id', db.Integer, primary_key=True)
    sample_id = db.Column('sample_id', db.Integer)
    ontology_id = db.Column('ontology_id', db.Integer)

    def json(self):
        return {
            'sample_id': self.sample_id,
            'ontology_id': self.ontology_id,
        }

