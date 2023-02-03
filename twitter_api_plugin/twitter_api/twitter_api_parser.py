import tweepy
import json
from core.models import Graph, Node, Edge
from core.services.load import LoadService
from datetime import datetime

class TwitterApiParser(LoadService):

    api = None
    # config = {
    #         "api_key" : "YcsKjnhueVcNVLS3Uj6V8T5qM",
    #         "api_key_secret" : "4EwbQ9Rd7MikRyP3jQGM6zqinQ7NdKJCcqhPNMMyyv6s7LO7hP",
    #         "access_token" : "1059946085140054016-bcbxeLXTgQTPpPtdolK3A7H0H2ZLU2",
    #         "access_token_secret" : "Fn3JdYPNnduXxPoMOE9cWq5iyL2mWY8N6byXSALCOScuw"
    #     }   
    config = {
        "api_key" : "ZETkR67C7wrZ6TGFn3Ja35VTs",
        "api_key_secret" : "mB570POCRSuZ4jzRxqekQz3FwUqBeaeOrjtEyFWGxVwCe6DxUA",
        "access_token" : "1582707476612485125-opEeLx0RUbbJqSR1kl9z3t4yrKqB1q",
        "access_token_secret" : "9wa60GcH0eNNhsIQUTxhffljJe6lAu6lmhC7ZQx5Cwegb"
    }

    def name(self):
        return "Twitter api parser"

    def identifier(self):
        return "twitter_api_parser"

    def load(self, *args):
        self.load_credentials()
        graph = self.create_graph()
        return graph


    #Ucitavanje podataka potrebnih za validaciju sesije ka twitteru
    #Zove se prva !!!
    def load_credentials(self):
        # f = open("config.json")
        # data = json.load(f)
        api_key = self.config["api_key"]
        api_key_secret = self.config["api_key_secret"]
        access_token = self.config["access_token"]
        access_token_secret = self.config["access_token_secret"]
        self.authenticate(api_key, api_key_secret, access_token, access_token_secret)
    #----------------------------------------------------

    #Inicijalizovanje api
    def authenticate(self,api_key, api_key_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key,api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
    #----------------------------------------------------

    #Dovaljanje ljudi koje prati moj twitter koji je povezan sa api-em
    def get_users_follows(self, count = 100):
        return self.api.get_friends(count = count)
    #----------------------------------------------------

    #Dobavljanje korisnika koje prati korisnik sa prosledjenim imenom
    def get_users_follows_by_name(self, name, count = 100):
        return self.api.get_friends(screen_name = name, count = count)
    #----------------------------------------------------

    #Dobavljanje korisnika koje prati korisnik sa prosledjenim id-em
    def get_users_follows_by_id(self,id, count = 100):
        return self.api.get_friends(user_id = int(str.replace(id,"id","")), count = count)
    #----------------------------------------------------

    #Dobavljanje korisnika po imenu
    def get_user_by_name(self,name = "SMilos019"):
        return self.api.get_user(screen_name = name)
    #----------------------------------------------------

    #Kreiranje grafa sa mojim profilom kao pocetkom
    def create_graph(self, name = "SMilos019"):
        graph = Graph({})
        starting_user = self.get_user_by_name()
        starting_node = self.add_node(graph, starting_user)
        self.__fill_up_the_graph(graph, starting_node)
        return graph
    #-----------------------------------------------------

    #Ubacivanje nodova u graph
    def __fill_up_the_graph(self, graph, node, counter = 1):
        c = 4
        # print(graph)
        if counter > c:
            return counter

        follows = self.get_users_follows_by_id(node.id)
        nodes = []
        for follow in follows:
            new_node = self.add_node(graph, follow)
            nodes.append(new_node)
            self.add_edge(node, new_node)
            if(counter > c):
                return counter
            # print(graph.counter)

        for next_node in nodes:
            counter += 1
            counter = self.__fill_up_the_graph(graph, next_node, counter)

            if(counter > c):
                return counter
    #------------------------------------------------------

    #Ubacivanje usera u node a zatim noda u graph, bez grana
    def add_node(self, graph, user):
        user_data = {
            "screen_name": user.screen_name,
            "followers_count": user.followers_count,
            "created_at": user.created_at,
        }
        node = Node("id" + user.id_str,[],user_data)

        if node.id in graph.data.keys():
            return graph.data[node.id] 

        graph.add_node(node)
        return node
    #------------------------------------------------------

    #Ubacivanje drugog noda i grane
    def add_edge(self, first_node, second_node):
        edge = Edge(first_node.id, second_node.id, None)
        first_node.edges.append(edge)
    #------------------------------------------------------


if __name__ == "__main__":
    p = TwitterApiParser()
    p.load_credentials()
    graph = p.create_graph()
    print(graph)