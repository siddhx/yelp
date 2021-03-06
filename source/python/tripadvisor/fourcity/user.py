__author__ = 'fpena'


class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.average_overall_rating = None
        self.criteria_weights = None
        self.cluster = None
        self.item_ratings = None
        self.item_multi_ratings = None
        self.item_reviews = None
        self.item_contexts = None

    @property
    def user_id(self):
        return self.user_id

    @user_id.setter
    def user_id(self, user_id):
        self.user_id = user_id

    @property
    def average_overall_rating(self):
        return self.average_overall_rating

    @average_overall_rating.setter
    def average_overall_rating(self, average_overall_rating):
        self.average_overall_rating = average_overall_rating

    @property
    def criteria_weights(self):
        return self.criteria_weights

    @criteria_weights.setter
    def criteria_weights(self, criteria_weights):
        self.average_overall_rating = criteria_weights

    @property
    def cluster(self):
        return self.cluster

    @cluster.setter
    def cluster(self, cluster):
        self.cluster = cluster

    @property
    def item_ratings(self):
        return self.item_ratings

    @item_ratings.setter
    def item_ratings(self, item_ratings):
        self.item_ratings = item_ratings

    @property
    def item_multi_ratings(self):
        return self.item_multi_ratings

    @item_multi_ratings.setter
    def item_multi_ratings(self, item_multi_ratings):
        self.item_multi_ratings = item_multi_ratings

    @property
    def item_reviews(self):
        return self.item_reviews

    @item_reviews.setter
    def item_reviews(self, item_reviews):
        self.item_reviews = item_reviews

    @property
    def item_contexts(self):
        return self.item_contexts

    @item_contexts.setter
    def item_contexts(self, item_contexts):
        self.item_ratings = item_contexts
