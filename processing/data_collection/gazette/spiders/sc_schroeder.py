from gazette.spiders.base import FecamGazetteSpider


class ScSchroederSpider(FecamGazetteSpider):
    name = "sc_schroeder"
    FECAM_QUERY = 'cod_entidade:261'
    TERRITORY_ID = "4217402"