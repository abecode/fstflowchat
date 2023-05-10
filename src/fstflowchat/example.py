#!/usr/bin/env python3

from typing import Callable
import fstflowchat as ffc



def intercept_decorator(condition):
    def decorator(f):
        def inner(input_):
            return condition(input_) and f(input_)
        return inner
    return decorator

# here are the implementations of the transitions/edges in the graph
# transition functions return bool True/False
# output functions return a string

def null(input_: str) -> bool:
    """this null transition will be true for any arguments, or no input

    It's not quite the same as a null transition in an FST, but it's a
    similar idea

    """
    return True

def welcome_msg(input_: str) -> str:
    return "hi, are you ready to take a quiz?"

def ready(input_: str) -> bool:
    """This will return true if the user says "yes" or "ready"
    """
    if "yes" in input_.lower():
        return True
    if "ready" in input_.lower():
        return True
    return False

def not_ready(input_: str) -> bool:
    return not ready(input_)

def ru_ready_msg(input_: str) -> str:
    return "if you're ready, say \"yes\" or \"ready\""

def ask_question(input_:str) -> str:
    question_to_ask = questions.pop(0)
    previous_questions.append(question_to_ask)
    return question_to_ask.text()

def quiz_done_or_user_exit(input_: str) -> bool:
    if quiz_done(input_):
        return True
    if user_exit(input_):
        return True
    return False

def not_quiz_done_or_user_exit(input_: str) -> bool:
    return not quiz_done_or_user_exit(input_)

@intercept_decorator(not_quiz_done_or_user_exit)
def correct_answ(input_:str) -> bool:
    global correct_count
    ##if score_answer(previous_questions[-1], input_) == "correct":
    if previous_questions[-1].score_answer(input_) == "correct":
        correct_count += 1
        return True
    return False

@intercept_decorator(not_quiz_done_or_user_exit)
def wrong_answ(input_:str) -> bool:
    global incorrect_count
    if previous_questions[-1].score_answer(input_) == "incorrect":
        incorrect_count += 1
        return True
    return False

@intercept_decorator(not_quiz_done_or_user_exit)
def partially_correct(input_: str) -> bool:
    global partial_count
    if previous_questions[-1].score_answer(input_) == "partial":
        partial_count += 1
        return True
    return False

def feedback_then_next_question(input_: str) -> str:
    return "eh, that was a so-so answer. \n" + ask_question(input_)

def feedback_drilldown_then_next_question(input_: str) -> str:
    return "wrong, pay more attention to lectures and reading\n" + ask_question(input_)

def quiz_done(input_: str) -> bool:
    if len(questions) == 0:
        return True
    return False

def user_exit(input_: str) -> bool:
    if "exit" in input_.lower():
        return True
    if "quit" in input_.lower():
        return True
    if "this sucks" in input_.lower():
        return True
    return False


def give_results(input_: str) -> str:
    return f"You got {correct_count} right, {incorrect_count} wrong, and {partial_count} partially correct"

def user_asks_q(input_: str) -> bool:
    if input_.endswith("?"):
        return True
    return False

def answer_question(input_: str) -> str:
    return "I'm sorry, I don't know how to answer that.  Let's just say bye and finish this."

def grade_last_and_give_results(input_: str) -> bool:
    """this is is for the last question in the list, only for when we
    transition from ask_questions to after_test

    """
    output_ = ""
    global correct_count, partial_count, incorrect_count
    res = previous_questions[-1].score_answer(input_)
    if res == "correct":
        correct_count += 1
    if res == "partial":
        partial_count += 1
        output_ = "eh, that was a so-so answer. \n"
    if res == "incorrect":
        incorrect_count += 1
        output_ = "wrong, pay more attention to lectures and reading\n"

    return output_ + give_results(input_)

def not_user_asks_q(input_: str) -> bool:
    return not user_asks_q(input_)

def goodbye(input_: str) -> str:
    return "goodbye, thanks for testing the dialog system!"

# set up the quiz questions
questions = ["Do you know what a database is?",
             "Is SELECT in DML or DDL?",
             "Briefly describe sixth normal form (6NF)."]
previous_questions = []

# set up the correct answer counts
correct_count = 0
partial_count = 0
incorrect_count = 0

class QuizQuestion():
    def __init__(self, question: str, score_fn: Callable[[str], str]):
        self._question = question
        self._score_fn = score_fn
    def score_answer(self, answer) -> str:
        return self._score_fn(answer)
    def text(self):
        return self._question

# set up the quiz questions
q1 = "Do you know what a database is?"
def is_affirmative(input_: str) -> bool:
  """ this is oversimplified, just a demo"""
  if "yes" in input_.lower():
    return True
  return False

def grade_q1(ans: str) -> str:
    if is_affirmative(ans):
        return "correct"
    return "incorrect"
q2 = "Is SELECT in DML or DDL?"
def grade_q2(ans: str) -> str:
    if "DDL" in ans:
        return "incorrect"
    if "DML" in ans:
        return "correct"
    else:
        return "partial"
q3 = "Briefly describe sixth normal form (6NF)."
def grade_q3(ans: str) -> str:
    return "partial"

questions = [QuizQuestion(q1, grade_q1),
             QuizQuestion(q2, grade_q2),
             QuizQuestion(q3, grade_q3)]
previous_questions = []




def main():
    graph = ffc.Graph("quiz.dot")

    # check to make sure the graph's functions have been implemented
    if not graph.check_implementation(env=globals()):
        graph.check_implementation(verbose=True, env=globals())


    # run the dialog graph
    agent = ffc.FST(graph, "start", "goodbye", globals())
    agent.run()


if __name__ == "__main__":
    main()
