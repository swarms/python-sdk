class BaseService:
    @staticmethod
    def get_ids(resources):
        return map(lambda r: r["id"], resources)

