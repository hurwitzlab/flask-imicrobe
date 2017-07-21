from flask import json

from ..models import Investigator, Project


class IMicrobeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Investigator):
            return {
                #'investigator': {
                    'investigator_id': obj.investigator_id,
                    'investigator_name': obj.investigator_name,
                    'institution': obj.institution
                #}
            }

        elif isinstance(obj, Project):
            return {
                #'project': {
                    'project_id': obj.project_id,
                    'project_name': obj.project_name,
                    'project_code':  obj.project_code,
                    'pi':  obj.pi,
                    'institution': obj.institution,
                    'project_type': obj.project_type,
                    'description': obj.description,
                    'url': obj.url,
                    'read_file': obj.read_file,
                    'meta_file': obj.meta_file,
                    'assembly_file': obj.assembly_file,
                    'peptide_file': obj.peptide_file,
                    'email': obj.email,
                    'read_pep_file': obj.read_pep_file,
                    'nt_file': obj.nt_file
                #}
            }

        else:
            return json.JSONEncoder.default(obj)
