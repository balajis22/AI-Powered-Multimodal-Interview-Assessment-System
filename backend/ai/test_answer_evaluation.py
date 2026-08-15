from backend.ai.question_bank import get_question
from backend.ai.answer_evaluator import evaluate_answer


def test_question(role, question_index, answer):

    question_data = get_question(
        role,
        question_index
    )

    if question_data is None:
        print("Question not found.")
        return

    question = question_data["question"]
    concepts = question_data["concepts"]

    result = evaluate_answer(
        question,
        answer,
        concepts
    )

    print("\n" + "=" * 60)
    print("INTERVIEW ANSWER EVALUATION")
    print("=" * 60)

    print(f"\nRole: {role}")

    print(f"\nQuestion:")
    print(question)

    print(f"\nCandidate Answer:")
    print(answer)

    print("\n--- Evaluation ---")

    print(
        f"Semantic Relevance: "
        f"{result['semantic_score']}/100"
    )

    print(
        f"Concept Coverage: "
        f"{result['concept_coverage']}/100"
    )

    print(
        f"Final Answer Score: "
        f"{result['answer_score']}/100"
    )

    print("\nConcept Scores:")

    for concept, score in result[
        "concept_scores"
    ].items():

        print(
            f"  {score:>3}/100 - {concept}"
        )

    print("\nFeedback:")
    print(result["feedback"])


if __name__ == "__main__":

    test_question(

        role="Machine Learning Engineer",

        question_index=2,

        answer=(
            "Overfitting happens when a model performs "
            "very well on the training data but does not "
            "generalize to unseen data. We can reduce it "
            "using regularization, cross validation, or "
            "more training data."
        )
    )