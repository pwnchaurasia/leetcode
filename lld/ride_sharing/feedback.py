
class Feedback:
    feedback = {}
    def __init__(self, rating_for, rating_from, rating, review):
        self.rating_for = rating_for
        self.rating_from = rating_from
        self.rating = rating
        self.review = review

    def add_feedback(self):
        self.feedback[self.rating_for] = self.feedback.get(self.rating_for, [])
        feedback_data = {
            "rating_from": self.rating_from,
            "rating": self.rating,
            "review": self.review
        }
        self.feedback[self.rating_for].append(feedback_data)

    def all_feedback(self):
        return self.feedback[self.rating_for]

    def __repr__(self):
        return f" user: {self.rating_from} gave {self.rating} to  {self.rating_for}"
