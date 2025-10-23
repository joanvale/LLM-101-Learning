def evaluate_quiz(form_data, correct_answers):
    results = {
        key: sorted(form_data.get(key, [])) == sorted(correct_answers[key])
        for key in correct_answers
    }
    return {
        "result": "All correct!" if all(results.values()) else "Try again!",
        "results": results
    }
