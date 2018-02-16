import festival_dao as dao
import festival_service as service


def main():
    preference = ['Kendrick Lamar', 'Mura Masa', 'Bruno Mars', 'Milky Chance', 'Tyler, The Creator', u'M\xd8', 'Flume',
                  'Arcade Fire', 'Kings Of Leon', 'James Blake', 'Royal Blood', 'SOHN', 'Glass Animals', 'G-Eazy',
                  'Cage The Elephant', 'Breakbot', 'LCD Soundsystem', 'Nothing But Thieves', 'Red Hot Chili Peppers',
                  'Imagine Dragons', 'Chance the Rapper', 'Andersoon .Paak & The Free Nationals', 'Andersoon .Paak',
                  'The Neighbourhood', 'The National', 'Mac Miller', 'Spoon', 'Lorde', 'Justice', 'The xx',
                  'Unknown Mortal Orchestra', 'MGMT', 'SZA', 'Portugal. The Man', 'Foster The People', 'Cold War Kids',
                  'Marian Hill', 'Why?', 'Desiigner', 'ODESZA', 'BadBadNotGood', 'Fall Out Boy', 'Panic! At The Disco',
                  'Years & Years', 'Moderat', 'Prophets Of Rage', 'The Weeknd', 'Foals', 'M83', 'Tame Impala',
                  'The 1975', 'My Morning Jacket', 'Danny Brown', 'Wu-Tang Clan', 'Saint Motel', 'Childish Gambino',
                  'Die Antwoord', 'Two Door Cinema Club', 'Lee Fields & The Expressions', 'Jamiroquai', 'Radiohead',
                  'Ed Sheeran', 'Run the Jewels', 'Anderson .Paak & The Free Nationals', 'Local Natives', 'Dan Croll',
                  'Jay-Z', 'Danny Brown', 'Vince Staples', 'BADBADNOTGOOD', 'Mutemath', 'Missio', 'Phantogram',
                  'Bastille', 'Muse', 'Prophets of Rage', 'Khalid', 'Travis Scott', 'Nothing But Thieves',
                  'Cashmere Cat', 'Arctic Monkeys', 'Eels', 'Jack White', 'Black Pistol Fire', 'Jack Johnson',
                  'Loic Nottet', 'The Chemical Brothers', 'Pussy Riot', 'Macklemore', 'Massive Attack', 'Gorillaz',
                  'CHVRCHES', 'Gregory Porter', 'Portugal The Man', 'Eminem', 'Lil Wayne', 'Logic', 'Bon Iver',
                  'Bon Iver [playing 2 unique sets]','Lil Uzi Vert','Vic Mensa', 'Rise Against','Django Django' ]
    festivals = {'Sziget': 'https://www.festicket.com/festivals/sziget-festival',
                 'Opener': 'https://www.festicket.com/festivals/opener-festival',
                 'Werchter': 'https://www.festicket.com/festivals/rock-werchter',
                 'Nos Primavera': 'https://www.festicket.com/festivals/nos-primavera-sound',
                 'Flow Helsinki': 'https://www.festicket.com/festivals/flow-festival-helsinki',
                 'Reading': 'https://www.festicket.com/festivals/reading-festival',
                 'Primavera Sound': 'https://www.festicket.com/festivals/primavera-sound',
                 'Sonar Barcelona': 'https://www.festicket.com/festivals/sonar-barcelona',
                 'Melt': 'https://www.festicket.com/festivals/melt-festival/',
                 'Dour, Belgium': 'https://www.festicket.com/festivals/dour-festival/'}
    # service.do_festivals_list(preference, festivals_url, 2018)
    # do_festivals(preference, festivals, 2018)

    festivals_url = dao.get_festivals_from_file()
    list = service.do_festivals_list_object(preference, festivals_url, 2018)
    print list
    sorted_list = sorted(list, reverse=True)
    cleaned_list = []
    for index in range(len(sorted_list)):
        if (len(sorted_list[index].similarity) > 0):
            cleaned_list.append(sorted_list[index])
    for index in range(len(cleaned_list)):
        print cleaned_list[index].name
        print len(cleaned_list[index].similarity)
        print cleaned_list[index].similarity


if __name__ == '__main__':
    main()
