import subprocess
from flask_restful import Resource
from models.jobs_models import JobsModel
from flask import abort




class Jobs(Resource):
    def get(self, search):

        DOCKER_PATH = '/app/bot/takeJobs'
        LOCAL_PATH = '/Users/felipemateusdecarvalho/Documents/developer_project/Projetos_back_end/takeJobs/src/bots/takeJobs'

        try:
            subprocess.run(f'scrapy crawl vagas -a search={search}', cwd=LOCAL_PATH, shell=True)
        except Exception as e:
            abort(500, message='Failed to execute job search.')  # Retorna erro 500 com mensagem personalizada

        return {'message': 'Job search completed successfully.'}, 200
    
class TakeJobs(Resource):
    def get(self, search, page, limit):

        if search != "all":
            jobs = JobsModel.find_by_title(search, page, limit)
            if jobs:
                lista_json = [job.json() for job in jobs]
                return lista_json, 200
            return {'message': 'Job not found.'}, 404
        else:
            jobs = JobsModel.select_all(page, limit)
            if jobs:
                lista_json = [job.json() for job in jobs]
                return lista_json, 200
            return {'message': 'Jobs not found.'}, 404
            

