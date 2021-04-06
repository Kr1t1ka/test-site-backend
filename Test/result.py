from .models import Steps, Result


class Result:

    def __init__(self, user_id):
        self.steps = Steps.objects.filter(user=user_id)
        self.results_arr = {i.name: 0 for i in Result.objects.all()}

    def get_res(self):
        for step in self.steps:
            facultys = step.answer.faculty.all()
            score = step.question.score
            for faculty in facultys:
                self.results_arr[faculty.name] += score

        return self.results_arr
