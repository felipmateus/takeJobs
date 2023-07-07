from flask_restful import Resource
from models import JobsModel
import subprocess



class Jobs(Resource):
    def get(self, search):

        DOCKER = '/app/bot/takeJobs'
        LOCAL = '/Users/felipemateusdecarvalho/Documents/developer_project/Projetos_back_end/take_job/src/bots/takeJobs'
        subprocess.run(f'scrapy crawl vagas -a search={search}', cwd=LOCAL, shell=True)
        return "OK", 200
    
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
            

