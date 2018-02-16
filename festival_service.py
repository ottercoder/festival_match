import festival_dao as dao
import festival_utils as utils
from festival_result_model import FestivalResultModel


def do_festivals_list_object(preference, festivals, year):
    path = 'https://www.festicket.com'
    obj_list = []
    for index in range(len(festivals)):
        print str(index) + "/" + str(len(festivals))
        path2 = path + festivals[index]
        print path2
        artists = dao.get_artists(path2, year)
        print artists
        similarity = utils.check_similarity(preference, artists)
        print similarity
        print len(similarity)
        obj_list.append(FestivalResultModel(path2, artists, similarity))
    return obj_list


def do_festivals_list(preference, festivals, year):
    path = 'https://www.festicket.com'
    for index in range(len(festivals)):
        path2 = path + festivals[index]
        print path2
        artists = dao.get_artists(path2, year)
        print artists
        similarity = utils.check_similarity(preference, artists)
        print similarity
        print len(similarity)


def do_festivals(preference, festivals, year):
    for key, value in festivals.iteritems():
        print key + " " + str(year)
        artists = dao.get_artists(value, year)
        print artists
        similarity = utils.check_similarity(preference, artists)
        print similarity
        print len(similarity)
