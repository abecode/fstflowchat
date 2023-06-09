#!/usr/bin/env python3

import random

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
    return question_to_ask

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
    if score_answer(previous_questions[-1], input_) == "correct":
        correct_count += 1
        return True
    return False

@intercept_decorator(not_quiz_done_or_user_exit)
def wrong_answ(input_:str) -> bool:
    if score_answer(previous_questions[-1], input_) == "wrong":
        return True
    return False

@intercept_decorator(not_quiz_done_or_user_exit)
def partially_correct(input_: str) -> bool:
    global partial_count
    if score_answer(previous_questions[-1], input_) == "partial":
        partial_count += 1
        return True
    return False

def feedback_then_next_question(input_: str) -> str:
    return "eh, that was a so-so answer. \n" + ask_question(input_)

def feedback_drilldown_then_next_question(input_: str) -> str:
    return "nope, pay more attention to lectures and reading\n"

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

def score_answer(question, answer):
    """ right now this is not implemented, just returns a random value"""
    res =  "correct"
    res = random.choice(["correct", "incorrect", "partial"])
    if len(questions) == 2:
        res = "correct"
    if len(questions) == 1:
        res = "partial"
    if len(questions) == 0:
        res = "incorrect"
    #print(f"question: {question}; answer: {answer}; result: {res}")
    return res

def give_results(input_: str) -> str:
    return f"You got {correct_count} right, and {partial_count} partially correct"

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
    global correct_count, partial_count
    res = score_answer(previous_questions[-1], input_)
    if res == "correct":
        correct_count += 1
    if res == "partial":
        partial_count += 1

    return give_results(input_)

def not_user_asks_q(input_: str) -> bool:
    return not user_asks_q(input_)

def goodbye(input_: str) -> str:
    return "goodbye, thanks for testing the dialog system!"

                              
            
            
if __name__ == "__main__":

    graph = ffc.Graph("quiz.dot")

    #print(graph.get_graph_functions())
    #print(graph.check_implementation(verbose=True, env=globals()))
    if not graph.check_implementation(env=globals()):
        graph.check_implementation(verbose=True, env=globals())

    # set up the quiz questions
    questions = ["Do you know what a database is?",
                 "Is SELECT in DML or DDL?",
                 "Briefly describe sixth normal form (6NF)."]
    previous_questions = []

    # set up the correct answer counts
    correct_count = 0
    partial_count = 0



            
    # run the dialog graph
    agent = ffc.FST(graph, "start", "goodbye", globals())
    agent.run()
        
    
    
        
    
    
    

    

    
