# --------------------------------------------------
# AI INTERVIEW QUESTION BANK
# --------------------------------------------------

QUESTION_BANK = {

    "Software Engineer": [

        {
            "question": "What is object-oriented programming?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Objects and behavior",
                    "aliases": [
                        "programming based on objects",
                        "objects contain data and behavior",
                        "objects combine data and methods"
                    ]
                },
                {
                    "name": "Classes",
                    "aliases": [
                        "classes define objects",
                        "class is a blueprint for objects",
                        "objects are created from classes"
                    ]
                },
                {
                    "name": "OOP principles",
                    "aliases": [
                        "encapsulation inheritance polymorphism abstraction",
                        "four principles of object oriented programming",
                        "inheritance polymorphism encapsulation abstraction"
                    ]
                }
            ]
        },

        {
            "question": "What is the difference between an array and a linked list?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Memory layout",
                    "aliases": [
                        "array uses contiguous memory",
                        "array elements are stored next to each other",
                        "linked list nodes can be stored in different memory locations"
                    ]
                },
                {
                    "name": "Random access",
                    "aliases": [
                        "arrays provide fast random access",
                        "array supports constant time indexing",
                        "linked lists do not provide direct random access"
                    ]
                },
                {
                    "name": "Insertion and deletion",
                    "aliases": [
                        "linked lists allow efficient insertion and deletion",
                        "insertion is easier in linked lists",
                        "arrays may require shifting elements"
                    ]
                }
            ]
        },

        {
            "question": "What is a REST API?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Communication",
                    "aliases": [
                        "API allows applications to communicate",
                        "APIs enable communication between software systems",
                        "applications communicate through an API"
                    ]
                },
                {
                    "name": "HTTP methods",
                    "aliases": [
                        "uses HTTP methods",
                        "GET POST PUT DELETE",
                        "HTTP verbs such as GET POST PUT DELETE"
                    ]
                },
                {
                    "name": "Resources and endpoints",
                    "aliases": [
                        "resources are identified by URLs",
                        "API endpoints represent resources",
                        "resources are accessed through endpoints"
                    ]
                },
                {
                    "name": "Statelessness",
                    "aliases": [
                        "REST is stateless",
                        "server does not store client session state",
                        "each request contains the required information"
                    ]
                }
            ]
        },

        {
            "question": "What is time complexity?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Algorithm efficiency",
                    "aliases": [
                        "measures algorithm efficiency",
                        "describes how efficient an algorithm is",
                        "measures computational efficiency"
                    ]
                },
                {
                    "name": "Input size",
                    "aliases": [
                        "running time grows with input size",
                        "describes how performance changes as input increases",
                        "growth with respect to input size"
                    ]
                },
                {
                    "name": "Big O",
                    "aliases": [
                        "Big O notation",
                        "O notation describes complexity",
                        "complexities such as O(1) O(n) O(log n)"
                    ]
                }
            ]
        },

        {
            "question": "What is the difference between a stack and a queue?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Stack LIFO",
                    "aliases": [
                        "stack follows LIFO",
                        "last in first out",
                        "last element inserted is removed first"
                    ]
                },
                {
                    "name": "Queue FIFO",
                    "aliases": [
                        "queue follows FIFO",
                        "first in first out",
                        "first element inserted is removed first"
                    ]
                }
            ]
        }
    ],


    "AI Engineer": [

        {
            "question": "What is artificial intelligence?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Human intelligence tasks",
                    "aliases": [
                        "machines perform tasks requiring human intelligence",
                        "machines perform intelligent tasks",
                        "computers simulate human intelligence"
                    ]
                },
                {
                    "name": "AI capabilities",
                    "aliases": [
                        "learning reasoning perception decision making",
                        "machines can learn reason perceive and make decisions"
                    ]
                }
            ]
        },

        {
            "question": "What is the difference between AI and machine learning?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "AI is broader",
                    "aliases": [
                        "AI is the broader field",
                        "artificial intelligence is a larger field",
                        "machine learning is part of AI"
                    ]
                },
                {
                    "name": "ML learns from data",
                    "aliases": [
                        "machine learning learns patterns from data",
                        "ML learns from examples",
                        "machine learning uses data to learn"
                    ]
                }
            ]
        },

        {
            "question": "What is deep learning?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "ML subset",
                    "aliases": [
                        "deep learning is a subset of machine learning",
                        "deep learning is part of machine learning"
                    ]
                },
                {
                    "name": "Multiple neural network layers",
                    "aliases": [
                        "uses neural networks with multiple layers",
                        "deep neural networks have many layers",
                        "multiple layers of neural networks"
                    ]
                },
                {
                    "name": "Automatic representation learning",
                    "aliases": [
                        "automatically learns representations",
                        "learns features automatically from data",
                        "automatically extracts useful features"
                    ]
                }
            ]
        },

        {
            "question": "What is transfer learning?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Pretrained knowledge",
                    "aliases": [
                        "reuses knowledge from a pretrained model",
                        "uses a model already trained on another task",
                        "starts from pretrained weights"
                    ]
                },
                {
                    "name": "Target task adaptation",
                    "aliases": [
                        "knowledge is adapted to a target task",
                        "pretrained model is adapted to a new task",
                        "fine tune the model for another task"
                    ]
                },
                {
                    "name": "Benefits",
                    "aliases": [
                        "reduces training time",
                        "requires less training data",
                        "reduces data or computational requirements"
                    ]
                }
            ]
        },

        {
            "question": "What is overfitting in machine learning?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Training data memorization",
                    "aliases": [
                        "model learns training data too closely",
                        "model memorizes training examples",
                        "model fits the training data excessively",
                        "model learns noise in the training data"
                    ]
                },
                {
                    "name": "Poor unseen performance",
                    "aliases": [
                        "performs poorly on unseen data",
                        "performs badly on new data",
                        "fails on new examples",
                        "poor test performance"
                    ]
                },
                {
                    "name": "Poor generalization",
                    "aliases": [
                        "poor generalization",
                        "fails to generalize",
                        "does not generalize well",
                        "cannot generalize to new data"
                    ]
                },
                {
                    "name": "Prevention",
                    "aliases": [
                        "regularization reduces overfitting",
                        "cross validation helps prevent overfitting",
                        "more training data can reduce overfitting"
                    ]
                }
            ]
        }
    ],


    "Machine Learning Engineer": [

        {
            "question": "What is supervised learning?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Labeled data",
                    "aliases": [
                        "model learns from labeled data",
                        "training data contains labels",
                        "input output pairs are provided"
                    ]
                },
                {
                    "name": "Prediction",
                    "aliases": [
                        "used for prediction",
                        "learns to predict outputs",
                        "predicts labels for new data"
                    ]
                },
                {
                    "name": "Classification and regression",
                    "aliases": [
                        "classification and regression are examples",
                        "supervised learning includes classification and regression"
                    ]
                }
            ]
        },

        {
            "question": "What is unsupervised learning?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Unlabeled data",
                    "aliases": [
                        "model learns from unlabeled data",
                        "training data has no labels",
                        "data does not have predefined outputs"
                    ]
                },
                {
                    "name": "Pattern discovery",
                    "aliases": [
                        "finds patterns in data",
                        "discovers hidden structure",
                        "identifies patterns without labels"
                    ]
                },
                {
                    "name": "Clustering",
                    "aliases": [
                        "clustering is an example",
                        "groups similar data points",
                        "clustering algorithms"
                    ]
                }
            ]
        },

        {
            "question": "What is overfitting and how can you prevent it?",
            "difficulty": "Medium",
            "concepts": [
    {
        "name": "Training performance",
        "aliases": [
            "model performs well on training data",
            "model fits the training data very well"
        ],
        "evidence": [
            "training data",
            "training set",
            "performs well on training",
            "fits the training data",
            "high training accuracy"
        ]
    },

    {
        "name": "Unseen performance",
        "aliases": [
            "model performs poorly on unseen data",
            "model performs badly on new data"
        ],
        "evidence": [
            "unseen data",
            "new data",
            "new examples",
            "test data",
            "test set",
            "poor test performance"
        ]
    },

    {
        "name": "Generalization",
        "aliases": [
            "poor generalization",
            "fails to generalize",
            "does not generalize well"
        ],
        "evidence": [
            "generalize",
            "generalization",
            "fails to generalize",
            "does not generalize"
        ]
    },

    {
        "name": "Regularization",
        "aliases": [
            "regularization reduces overfitting",
            "use regularization"
        ],
        "evidence": [
            "regularization",
            "L1",
            "L2",
            "regularization penalty"
        ]
    },

    {
        "name": "Cross validation",
        "aliases": [
            "cross validation helps prevent overfitting",
            "use k fold cross validation"
        ],
        "evidence": [
            "cross validation",
            "cross-validation",
            "k fold",
            "k-fold",
            "validation folds"
        ]
    },

    {
        "name": "More data",
        "aliases": [
            "more training data can help",
            "increase the training dataset"
        ],
        "evidence": [
            "more data",
            "more training data",
            "larger dataset",
            "increase the dataset",
            "collect more data"
        ]
    }
]
        },

        {
            "question": "What is the difference between classification and regression?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Classification",
                    "aliases": [
                        "predicts discrete categories",
                        "predicts class labels",
                        "classification outputs categories"
                    ]
                },
                {
                    "name": "Regression",
                    "aliases": [
                        "predicts continuous numerical values",
                        "regression predicts numbers",
                        "regression outputs continuous values"
                    ]
                }
            ]
        },

        {
            "question": "What is gradient descent?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Optimization",
                    "aliases": [
                        "optimization algorithm",
                        "used to optimize model parameters",
                        "optimization method"
                    ]
                },
                {
                    "name": "Loss minimization",
                    "aliases": [
                        "minimizes the loss function",
                        "reduces the cost function",
                        "finds parameters that minimize error"
                    ]
                },
                {
                    "name": "Gradients",
                    "aliases": [
                        "uses gradients to determine update direction",
                        "gradient determines parameter update",
                        "parameters are updated using gradients"
                    ]
                },
                {
                    "name": "Learning rate",
                    "aliases": [
                        "learning rate controls step size",
                        "learning rate determines how much parameters change"
                    ]
                }
            ]
        },

        {
            "question": "What is cross validation?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Multiple data splits",
                    "aliases": [
                        "evaluates using multiple data splits",
                        "data is divided into multiple folds",
                        "uses different train validation splits"
                    ]
                },
                {
                    "name": "K fold",
                    "aliases": [
                        "k fold cross validation",
                        "data is divided into k folds"
                    ]
                },
                {
                    "name": "Generalization",
                    "aliases": [
                        "estimates generalization performance",
                        "evaluates how model performs on unseen data"
                    ]
                }
            ]
        }
    ],


    "Data Analyst": [

        {
            "question": "What is the difference between mean median and mode?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Mean",
                    "aliases": [
                        "mean is the arithmetic average",
                        "sum divided by number of values",
                        "average of the values"
                    ]
                },
                {
                    "name": "Median",
                    "aliases": [
                        "median is the middle value",
                        "middle value after sorting",
                        "median is the central value"
                    ]
                },
                {
                    "name": "Mode",
                    "aliases": [
                        "mode is the most frequent value",
                        "most common value",
                        "value occurring most often"
                    ]
                },
                {
                    "name": "Outliers",
                    "aliases": [
                        "median is less affected by outliers",
                        "mean is sensitive to outliers",
                        "median is more robust to extreme values"
                    ]
                }
            ]
        },

        {
            "question": "What is data cleaning?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Data quality",
                    "aliases": [
                        "improves data quality",
                        "makes data accurate and consistent",
                        "prepares reliable data"
                    ]
                },
                {
                    "name": "Missing values",
                    "aliases": [
                        "handles missing values",
                        "deals with missing data",
                        "fills or removes missing values"
                    ]
                },
                {
                    "name": "Duplicates",
                    "aliases": [
                        "removes duplicate records",
                        "handles duplicate data",
                        "identifies duplicate rows"
                    ]
                },
                {
                    "name": "Inconsistent data",
                    "aliases": [
                        "fixes inconsistent data",
                        "corrects incorrect values",
                        "handles inconsistent formats"
                    ]
                }
            ]
        },

        {
            "question": "What is an outlier?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Unusual observation",
                    "aliases": [
                        "observation significantly different from others",
                        "unusually high or low value",
                        "data point far from the rest"
                    ]
                },
                {
                    "name": "Causes",
                    "aliases": [
                        "may result from errors or unusual events",
                        "can be caused by measurement errors",
                        "may represent unusual behavior"
                    ]
                },
                {
                    "name": "Detection",
                    "aliases": [
                        "IQR can detect outliers",
                        "z score can identify outliers",
                        "box plots can identify outliers"
                    ]
                }
            ]
        },

        {
            "question": "What is the difference between correlation and causation?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Correlation",
                    "aliases": [
                        "correlation indicates association",
                        "variables are related",
                        "correlation measures relationship between variables"
                    ]
                },
                {
                    "name": "Causation",
                    "aliases": [
                        "causation means one variable causes another",
                        "one variable produces a change in another",
                        "cause and effect relationship"
                    ]
                },
                {
                    "name": "Correlation does not imply causation",
                    "aliases": [
                        "correlation does not mean causation",
                        "correlation does not prove cause and effect",
                        "association does not establish causality"
                    ]
                }
            ]
        },

        {
            "question": "What is SQL used for?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Database interaction",
                    "aliases": [
                        "SQL interacts with relational databases",
                        "SQL is used to work with databases",
                        "SQL manages relational database data"
                    ]
                },
                {
                    "name": "Data retrieval",
                    "aliases": [
                        "retrieves data",
                        "queries data from databases",
                        "SELECT retrieves records"
                    ]
                },
                {
                    "name": "Data modification",
                    "aliases": [
                        "inserts updates and deletes data",
                        "modifies database records",
                        "INSERT UPDATE DELETE"
                    ]
                },
                {
                    "name": "Data analysis operations",
                    "aliases": [
                        "filters groups and joins data",
                        "GROUP BY JOIN WHERE",
                        "SQL can filter group and join data"
                    ]
                }
            ]
        }
    ],


    "HR Interview": [

        {
            "question": "Tell me about yourself.",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Introduction",
                    "aliases": [
                        "professional introduction",
                        "academic or professional background",
                        "brief introduction about yourself"
                    ]
                },
                {
                    "name": "Relevant skills",
                    "aliases": [
                        "relevant skills",
                        "skills related to the job",
                        "technical or professional abilities"
                    ]
                },
                {
                    "name": "Achievements",
                    "aliases": [
                        "important achievements",
                        "academic or professional accomplishments",
                        "projects or achievements"
                    ]
                },
                {
                    "name": "Career goals",
                    "aliases": [
                        "career interests",
                        "career goals",
                        "professional aspirations"
                    ]
                }
            ]
        },

        {
            "question": "What are your strengths?",
            "difficulty": "Easy",
            "concepts": [
                {
                    "name": "Relevant strengths",
                    "aliases": [
                        "personal strengths relevant to the job",
                        "professional strengths",
                        "qualities that help at work"
                    ]
                },
                {
                    "name": "Evidence",
                    "aliases": [
                        "provides examples",
                        "supports strengths with evidence",
                        "gives examples of strengths"
                    ]
                }
            ]
        },

        {
            "question": "What is your biggest weakness?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Self awareness",
                    "aliases": [
                        "shows self awareness",
                        "recognizes an area for improvement",
                        "understands personal weaknesses"
                    ]
                },
                {
                    "name": "Improvement",
                    "aliases": [
                        "steps taken to improve",
                        "working on the weakness",
                        "actions taken to improve"
                    ]
                },
                {
                    "name": "Growth mindset",
                    "aliases": [
                        "demonstrates growth mindset",
                        "willingness to learn and improve",
                        "focuses on personal development"
                    ]
                }
            ]
        },

        {
            "question": "Why should we hire you?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Job relevance",
                    "aliases": [
                        "connects skills to job requirements",
                        "skills match the position",
                        "relevant qualifications"
                    ]
                },
                {
                    "name": "Value",
                    "aliases": [
                        "value candidate can provide",
                        "contribution to the organization",
                        "how candidate can help the company"
                    ]
                },
                {
                    "name": "Evidence",
                    "aliases": [
                        "relevant experience or achievements",
                        "examples of past accomplishments",
                        "demonstrates previous success"
                    ]
                }
            ]
        },

        {
            "question": "Where do you see yourself in five years?",
            "difficulty": "Medium",
            "concepts": [
                {
                    "name": "Career goals",
                    "aliases": [
                        "career goals",
                        "future professional plans",
                        "long term career aspirations"
                    ]
                },
                {
                    "name": "Professional growth",
                    "aliases": [
                        "professional growth",
                        "developing skills and responsibilities",
                        "career development"
                    ]
                },
                {
                    "name": "Learning",
                    "aliases": [
                        "willingness to learn",
                        "develop new skills",
                        "continuous learning"
                    ]
                }
            ]
        }
    ]
}


# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def get_questions(role):
    return QUESTION_BANK.get(role, [])


def get_question(role, index):
    questions = get_questions(role)

    if not questions:
        return None

    if index < 0 or index >= len(questions):
        return None

    return questions[index]


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    for role, questions in QUESTION_BANK.items():

        print("\n" + "=" * 60)
        print(role)
        print("=" * 60)

        for i, item in enumerate(questions, start=1):

            print(
                f"{i}. {item['question']}"
            )

            print(
                f"   Difficulty: {item['difficulty']}"
            )

            print(
                f"   Concepts: {len(item['concepts'])}"
            )