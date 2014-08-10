from abc import ABCMeta, abstractmethod
from tripadvisor.fourcity import extractor
from utils import dictionary_utils


__author__ = 'fpena'


class BaseRecommender(object):

    __metaclass__ = ABCMeta

    def __init__(self, name, similarity_matrix_builder, num_neighbors=None):
        self._name = name
        self._num_neighbors = num_neighbors
        self._similarity_matrix_builder = similarity_matrix_builder
        self.reviews = None
        self.user_ids = None
        self.user_dictionary = None
        self.user_similarity_matrix = None

    def load(self, reviews):
        self.reviews = reviews
        self.user_dictionary =\
            extractor.initialize_users(
                self.reviews,
                self._similarity_matrix_builder._is_multi_criteria)
        self.user_ids = extractor.get_groupby_list(self.reviews, 'user_id')
        if self._similarity_matrix_builder._similarity_metric is not None:
            self.user_similarity_matrix =\
                self._similarity_matrix_builder.build_similarity_matrix(
                    self.user_dictionary, self.user_ids)

    def clear(self):
        self.reviews = None
        self.user_ids = None
        self.user_dictionary = None
        self.user_similarity_matrix = None

    def get_most_similar_users(self, user_id):

        if self._num_neighbors is None:
            most_similar_users = list(self.user_ids)
            most_similar_users.remove(user_id)
            return most_similar_users

        # Sort the users by similarity
        similarity_matrix = self.user_similarity_matrix[user_id].copy()
        similarity_matrix.pop(user_id, None)

        most_similar_users = dictionary_utils.sort_dictionary_keys(
            similarity_matrix)[:self._num_neighbors]

        return most_similar_users


    @abstractmethod
    def predict_rating(self, user, item):
        pass

    @property
    def name(self):
        return self._name
