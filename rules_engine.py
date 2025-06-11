from experta import *

class TouristInterests(Fact):
    pass

class TouristExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recommendations = []

    @Rule(OR(TouristInterests(history='y'), TouristInterests(observation='y')))
    def historical_sites(self):
        self.recommendations.extend([
            "Visit the Taj Mahal in India – a UNESCO World Heritage Site",
            "Explore the Pyramids of Giza in Egypt",
            "Tour the Colosseum in Rome, Italy"
        ])

    @Rule(AND(TouristInterests(physical_activity='y'), TouristInterests(outdoor='y'), TouristInterests(race='y')))
    def physical_challenges(self):
        self.recommendations.extend([
            "Join the AlUla Trail Race in Saudi Arabia",
            "Run the Mumbai Marathon",
            "Hike the Inca Trail to Machu Picchu in Peru"
        ])

    @Rule(OR(TouristInterests(contemporary_art='y'), TouristInterests(observation='y')))
    def art_lovers(self):
        self.recommendations.extend([
            "Visit the AlUla Museum in Saudi Arabia",
            "Tour the Louvre Museum in Paris",
            "Check out Kala Ghoda Art Festival in Mumbai"
        ])

    @Rule(TouristInterests(relaxation='y'))
    def relaxation_spots(self):
        self.recommendations.extend([
            "Try Stargazing at Gharameel in Saudi Arabia",
            "Relax in Kerala’s backwaters, India",
            "Unwind on the beaches of Bali, Indonesia"
        ])

    @Rule(AND(TouristInterests(adventurous='y'), TouristInterests(outdoor='y')))
    def adventure_travel(self):
        self.recommendations.extend([
            "Go skydiving in Dubai",
            "Try river rafting in Rishikesh, India",
            "Experience bungee jumping in New Zealand"
        ])

    @Rule(TouristInterests(musical_performance='y'))
    def music_culture(self):
        self.recommendations.extend([
            "Enjoy classical music at Gwalior Tansen Festival",
            "Visit the Salzburg Festival in Austria",
            "Attend Sunburn Music Festival in Goa"
        ])

    @Rule(TouristInterests(filmmaking='y'))
    def movie_buffs(self):
        self.recommendations.extend([
            "Take the Bollywood Studio Tour in Mumbai",
            "Visit Universal Studios in Hollywood",
            "Explore Ramoji Film City in Hyderabad"
        ])

    @Rule(TouristInterests(shopping='y'))
    def shopaholics(self):
        self.recommendations.extend([
            "Shop at Dilli Haat in New Delhi",
            "Explore the Grand Bazaar in Istanbul",
            "Enjoy street shopping in Bangkok"
        ])

    @Rule(TouristInterests(traditional_cuisine='y'))
    def food_lovers_traditional(self):
        self.recommendations.extend([
            "Taste Hyderabadi Biryani in Hyderabad",
            "Savor street food in Delhi",
            "Try thali meals in Gujarat"
        ])

    @Rule(TouristInterests(international_cuisine='y'))
    def food_lovers_international(self):
        self.recommendations.extend([
            "Dine at Michelin-starred restaurants in Tokyo",
            "Explore Italian cuisine in Florence",
            "Enjoy Korean BBQ in Seoul"
        ])

    @Rule(TouristInterests(high_budget='y'))
    def luxury_travel(self):
        self.recommendations.extend([
            "Stay at The Leela Palace, Udaipur",
            "Fly Emirates First Class to Dubai",
            "Cruise the Mediterranean in a luxury liner"
        ])

    @Rule(TouristInterests(nature='y'))
    def nature_lovers(self):
        self.recommendations.extend([
            "Visit Munnar hills and tea estates in Kerala",
            "Explore Plitvice Lakes National Park in Croatia",
            "Experience the Blue Mountains in Australia"
        ])

    @Rule(TouristInterests(religious_spiritual='y'))
    def spiritual_journeys(self):
        self.recommendations.extend([
            "Take a pilgrimage to Varanasi, India",
            "Visit the Vatican City in Rome",
            "Explore Meiji Shrine in Tokyo"
        ])

    @Rule(TouristInterests(wildlife='y'))
    def wildlife_explorers(self):
        self.recommendations.extend([
            "Go on a jungle safari in Jim Corbett National Park",
            "See wildlife in Masai Mara, Kenya",
            "Visit Kruger National Park in South Africa"
        ])

    @Rule(TouristInterests(festivals='y'))
    def cultural_festivals(self):
        self.recommendations.extend([
            "Experience Holi in Mathura, India",
            "Celebrate Rio Carnival in Brazil",
            "Enjoy Oktoberfest in Munich, Germany"
        ])

    @Rule(TouristInterests(technology_innovation='y'))
    def tech_geeks(self):
        self.recommendations.extend([
            "Tour Bangalore's tech parks in India",
            "Visit the Silicon Valley in USA",
            "Explore Miraikan Science Museum in Tokyo"
        ])

    @Rule(TouristInterests(photography='y'))
    def shutterbugs(self):
        self.recommendations.extend([
            "Capture the sunrise at Tiger Hill, Darjeeling",
            "Photograph Iceland's northern lights",
            "Snap the cherry blossoms in Kyoto"
        ])

    @Rule(TouristInterests(architecture='y'))
    def design_lovers(self):
        self.recommendations.extend([
            "Admire stepwells in Gujarat",
            "Visit Gaudí’s architecture in Barcelona",
            "Explore Marina Bay Sands in Singapore"
        ])

    @Rule(TouristInterests(cold_climate='y'))
    def snow_seekers(self):
        self.recommendations.extend([
            "Ski in Gulmarg, Kashmir",
            "Visit the Swiss Alps",
            "See the Northern Lights in Norway"
        ])

    @Rule(TouristInterests(beach_lovers='y'))
    def beach_vacations(self):
        self.recommendations.extend([
            "Relax at Radhanagar Beach, Andaman",
            "Sunbathe in the Maldives",
            "Surf in Bondi Beach, Australia"
        ])

    @Rule(TouristInterests(budget_friendly='y'))
    def low_cost_travel(self):
        self.recommendations.extend([
            "Backpack through Himachal Pradesh",
            "Visit Vietnam for scenic budget travel",
            "Explore Lisbon, Portugal affordably"
        ])

    def run_engine(self, inputs):
        self.reset()
        self.recommendations.clear()
        self.declare(TouristInterests(**inputs))
        self.run()
        return list(set(self.recommendations))  # avoid duplicates
