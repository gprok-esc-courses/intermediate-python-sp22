
class Athlete:
    def __init__(self, name, country, sport):
        self.name = name
        self.country = country
        self.sport = sport


class Athletes:
    def __init__(self):
        self.athletes = []

    def load_from_csv(self):
        file = open('athletes.csv', mode='r', encoding='utf-8')
        for line in file:
            components = line.strip().split(';')
            a = Athlete(components[0], components[1], components[2])
            self.athletes.append(a)

    def find_total(self, country, sport):
        total = 0
        for athlete in self.athletes:
            if country == 'Any' and sport == 'Any':
                total += 1
            elif country == 'Any' and athlete.sport == sport:
                total += 1
            elif sport == 'Any' and athlete.country == country:
                total += 1
            elif athlete.country == country and athlete.sport == sport:
                total += 1
        print("Total in " + sport + " sport from " + country + " country is " + str(total))

    def athlete_names(self, country, sport):
        for athlete in self.athletes:
            if country == 'Any' and sport == 'Any' or \
                    country == 'Any' and athlete.sport == sport or \
                    sport == 'Any' and athlete.country == country or \
                    athlete.country == country and athlete.sport == sport:
                print(athlete.name)


if __name__ == '__main__':
    athletes = Athletes()
    athletes.load_from_csv()
    country = input("Give country (Any for all): ")
    sport = input("Give sport (Any for all): ")
    athletes.find_total(country, sport)
    athletes.athlete_names(country, sport)


