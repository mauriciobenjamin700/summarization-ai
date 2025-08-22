from typing import Any, Callable, Optional

from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaLLM
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel

from src.core.settings import settings


class AIHandler:
    def __init__(self) -> None:
        self.__model = OllamaLLM(model=settings.AI_MODEL)

    def invoke(
        self, template: ChatPromptTemplate, params: dict[str, Any]
    ) -> str:
        """
        Generate a response from the AI model using the provided template
        and parameters.
        """
        prompt_input = template.format(**params)
        response = self.__model.invoke(prompt_input)
        return response

    def summarize(self) -> str:
        """
        Summarize the provided chat history.
        """
        return "Not implemented yet."

    def create_agent(
        self,
        tools: list[Callable[..., Any]],
        response_format: Optional[BaseModel] = None,
    ) -> CompiledStateGraph[Any]:
        return create_react_agent(
            ChatOllama(model=settings.AI_MODEL),
            tools=tools,
            response_format=response_format,
        )

    def execute_agent(
        self, agent: CompiledStateGraph[Any], messages: list[BaseMessage]
    ):
        messages_to_agent = [msg.model_dump() for msg in messages]
        return agent.invoke({"messages": messages_to_agent})

    def get_agent_structured_response(
        self, agent: CompiledStateGraph[Any], messages: list[BaseMessage]
    ) -> Optional[BaseModel]:
        return self.execute_agent(agent, messages)["structured_response"]
