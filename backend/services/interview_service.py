import threading
from time import time

from backend.vision.interview_analyzer import analyze_interview
from backend.audio.speech_analyzer import analyze_speech
from backend.ai.answer_evaluator import evaluate_answer
from backend.ai.question_bank import get_question
from backend.scoring.scoring_engine import InterviewScorer


class InterviewService:

    def __init__(self):

        self.vision_result = None
        self.speech_result = None
        self.answer_result = None

    # --------------------------------------------------
    # THREAD FUNCTIONS
    # --------------------------------------------------

    def run_vision(self, duration, start_event):

        self.vision_result = analyze_interview(
            duration,
            start_event
        )

    def run_speech(self, duration, start_event):

        self.speech_result = analyze_speech(
            duration,
            start_event
        )

    # --------------------------------------------------
    # MAIN INTERVIEW
    # --------------------------------------------------

    def run(
        self,
        duration,
        role="Machine Learning Engineer",
        question_number=1
    ):
        """
        Runs the complete interview pipeline.

        Includes:
        - Computer Vision
        - Speech Analysis
        - Semantic Answer Evaluation
        - Interview Scoring
        """

        # --------------------------------------------------
        # Get Interview Question
        # --------------------------------------------------

        question_data = get_question(
            role,
            question_number
        )

        question = question_data["question"]

        expected_concepts = question_data["concepts"]
        start_event = threading.Event()
        # --------------------------------------------------
        # Run Vision + Speech
        # --------------------------------------------------

        vision_thread = threading.Thread(
            target=self.run_vision,
            args=(duration, start_event)
        )

        speech_thread = threading.Thread(
            target=self.run_speech,
            args=(duration, start_event)
        )
        print("Preparing camera and microphone...")

        vision_thread.start()
        speech_thread.start()

        print("Camera and microphone ready.")

        print("Interview starts in 3 seconds...")

        import time

        time.sleep(3)

        print("GO! Interview started.")

        start_event.set()

        

        

        vision_thread.join()

        print("Vision finished")

        speech_thread.join()

        print("Speech finished")

        # --------------------------------------------------
        # Evaluate Candidate Answer
        # --------------------------------------------------

        transcript = self.speech_result[
            "transcript"
        ]

        self.answer_result = evaluate_answer(
            question,
            transcript,
            expected_concepts
        )

        # --------------------------------------------------
        # Traditional Interview Scoring
        # --------------------------------------------------

        scorer = InterviewScorer()

        scorer.emotion_score(
            self.vision_result["emotion"]
        )

        scorer.eye_score(
            self.vision_result["eye"]
        )

        scorer.head_score(
            self.vision_result["head"]
        )

        scorer.speech_score(
            self.speech_result["speech_score"]
        )

        scorer.background_score(
            self.speech_result[
                "background_natural"
            ]
        )

        total = scorer.total()

        # --------------------------------------------------
        # Recommendations
        # --------------------------------------------------

        recommendations = []

        if (
            self.vision_result["eye"]
            != "Looking Center"
        ):

            recommendations.append(
                "Maintain better eye contact."
            )

        if (
            self.vision_result["head"]
            != "Center"
        ):

            recommendations.append(
                "Keep your head facing the interviewer."
            )

        if (
            self.speech_result["total_fillers"]
            > 3
        ):

            recommendations.append(
                "Reduce filler words."
            )

        if self.speech_result["wpm"] < 90:

            recommendations.append(
                "Speak slightly faster."
            )

        if self.speech_result["wpm"] > 170:

            recommendations.append(
                "Slow down your speaking pace."
            )

        # Add answer feedback
        if self.answer_result["answer_score"] < 60:

            recommendations.append(
                self.answer_result["feedback"]
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Excellent interview performance!"
            )

        # --------------------------------------------------
        # Return Complete Result
        # --------------------------------------------------

        return {

            # Question
            "question": question,

            # Vision
            "emotion": self.vision_result[
                "emotion"
            ],

            "eye_contact": self.vision_result[
                "eye"
            ],

            "head_pose": self.vision_result[
                "head"
            ],

            # Speech
            "speech_score": self.speech_result[
                "speech_score"
            ],

            "transcript": transcript,

            "background": self.speech_result[
                "background"
            ],

            "wpm": self.speech_result[
                "wpm"
            ],

            "fillers": self.speech_result[
                "total_fillers"
            ],

            # Answer Evaluation
            "semantic_score": self.answer_result[
                "semantic_score"
            ],

            "concept_coverage": self.answer_result[
                "concept_coverage"
            ],

            "answer_score": self.answer_result[
                "answer_score"
            ],

            "answer_feedback": self.answer_result[
                "feedback"
            ],

            "concept_scores": self.answer_result[
                "concept_scores"
            ],

            # Existing overall score
            "overall_score": total,

            # Recommendations
            "recommendations": recommendations
        }