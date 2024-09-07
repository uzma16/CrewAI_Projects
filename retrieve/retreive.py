import logging
import os
 
from autogen import config_list_from_json
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen import UserProxyAgent

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

config_list = config_list_from_json(
    env_or_file="OAI_CONFIG_LIST", 
    filter_dict={
        "model": [
            "gpt-4-1106-preview",
        ]
    }
)

assistant_id = None

llm_config = {
    "config_list": config_list,
    "assistant_id": assistant_id,
    "tools": [
            {
                "type": "retrieval"
            }
        ],
    "file_ids": ["file-7ohePVdw17LGjag6UREOxGNJ"]
}

gpt_assistant = GPTAssistantAgent(name="assistant",
                                instructions="You are adapt at summarizing the doc file",
                                llm_config=llm_config)

user_proxy = UserProxyAgent(name="user_proxy",
    code_execution_config=False,
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    human_input_mode="ALWAYS")

user_proxy.initiate_chat(gpt_assistant, message="I gave you a file.  Could you please describe it?")

gpt_assistant.delete_assistant()