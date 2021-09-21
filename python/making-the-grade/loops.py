def round_scores(student_scores):

    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    return [round(score) for score in student_scores]

def count_failed_students(student_scores):

    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    number_of_failed_student = 0
    for scores in student_scores:
        if scores <= 40:
            number_of_failed_student += 1
    return number_of_failed_student

def above_threshold(student_scores, threshold):
    
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    best_performing_student= []
    for scores in student_scores:
        if scores >= threshold:
            best_performing_student.append(scores)
    return best_performing_student

    # OR
    # By using List comprehension
    # best_performing_student = [scores for scores in student_scores if scores >= threshold]
    # return best_performing_student

def letter_grades(highest):

    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    result = []
    lowest_grade = 40
    starting_grade = 41
    even_increment = (highest- lowest_grade)/4
    while highest >= starting_grade:
        result.append(int(starting_grade))
        starting_grade += even_increment
    return result

def student_ranking(student_scores, student_names):

    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    ranking_list = []
    rank = 0
    
    for index , names in enumerate(student_names):
        rank = rank + 1
        ranking_list.append(f"{rank}. {names}: {student_scores[index]}")
    return ranking_list

def perfect_score(student_info):

    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for student in student_info:
        if student[1] == 100:
            return student
    return "No perfect score."

    #OR
    #using count
    # for student in student_info:
    #     if student.count(100)> 0:
    #         return student
    # return "No perfect score."
