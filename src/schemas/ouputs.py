from pydantic import Field

from src.core.base import BaseSchema


class OutputTopic(BaseSchema):
    """
    Schema for outputting a topic.
    """

    task: str = Field(
        title="Task",
        description="The task to be performed or required.",
        examples=[
            "Summarize the article",
            "Generate action items based on the summary",
            "Recommend movies for tonight",
        ],
    )
    result: str = Field(
        title="Result",
        description="The result of the task performed.",
        examples=[
            "The article discusses the impact of AI on society.",
            """
                1) Improve model accuracy; 
                2) Conduct user testing; 
                3) Analyze feedback.
            """,
            """
            1) Inception (2010); 
            2) The Matrix (1999); 
            3) Interstellar (2014).
            """,
        ],
    )
    num_messages: int = Field(
        title="Number of Messages",
        description="""
        The total number of messages exchanged in the conversation 
        by user and assistant
        """,
        examples=[5, 10, 15],
    )
