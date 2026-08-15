from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------
# Load lightweight semantic model ONCE
# --------------------------------------------------

print("Loading semantic evaluation model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Semantic model loaded!")


# --------------------------------------------------
# Semantic similarity
# --------------------------------------------------

def semantic_similarity(text1, text2):
    """
    Returns semantic similarity between two pieces of text.

    Score:
        0.0 = very different meaning
        1.0 = very similar meaning
    """

    embeddings = model.encode(
        [text1, text2],
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(similarity)


# --------------------------------------------------
# Answer evaluation
# --------------------------------------------------

def evaluate_answer(question, answer):
    """
    Evaluate how semantically relevant an answer is
    to the interview question.
    """

    if not answer or not answer.strip():

        return {
            "semantic_score": 0,
            "feedback": "No answer was detected."
        }

    similarity = semantic_similarity(
        question,
        answer
    )

    score = round(similarity * 100)

    # Basic feedback
    if score >= 80:

        feedback = (
            "Strong semantic relevance. "
            "Your answer directly addresses the question."
        )

    elif score >= 60:

        feedback = (
            "Moderate relevance. "
            "Your answer is related to the question, "
            "but could be more focused."
        )

    elif score >= 40:

        feedback = (
            "Low relevance. "
            "Try to address the main concept asked in the question."
        )

    else:

        feedback = (
            "Very low relevance. "
            "Your answer does not appear to directly address the question."
        )

    return {

        "semantic_score": score,

        "feedback": feedback

    }


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    question = "What is overfitting in machine learning?"

    answers = [

        # Correct but differently worded
        (
            "Overfitting occurs when a model memorizes "
            "the training examples and fails to generalize "
            "well to new unseen data."
        ),

        # Partially related
        (
            "Machine learning models learn patterns "
            "from training data."
        ),

        # Completely unrelated
        (
            "Python is a programming language used "
            "for building many different applications."
        )
    ]

    print("\n==============================")
    print("SEMANTIC ANSWER EVALUATION")
    print("==============================")

    for i, answer in enumerate(answers, start=1):

        result = evaluate_answer(
            question,
            answer
        )

        print(f"\nAnswer {i}")
        print("------------------------------")
        print(answer)
        print()
        print("Semantic Score:",
              result["semantic_score"])

        print("Feedback:",
              result["feedback"])