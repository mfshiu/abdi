# Physiologically Inspired Framework for Complex System Integration



## Introduction
In this study, inspired by the physiological operation of the human body, an efficient and resilient software framework was developed to aid in the integration of mature AI technologies, allowing them to coordinate with one another to accomplish more advanced goals. A navigation system for the visually impaired was then developed to validate the framework, with promising experimental results. This framework can be applied to other types of AI systems.


## Class Diagram
The class diagram of the integration of agents and coordination. HolonicAgent represents the core, and HeadAgents and BodyAgents represent the collection of head agents and subagents, respectively. MQTT is the fundamental communication protocol for agents in the global circulation system, and MqttClient is a private member of HolonicAgent, which allows the agent to have built-in MQTT connection and reception capabilities.

All agents inherit from HolonicAgent to form a hierarchical structure, and they use the DDS to achieve neural message transmission depending on their specific behavior. Each super-agent is a DDS domain that publishes or subscribes to related topics with the required QoS, such as the DEADLINE policy to confirm the date of the data or the TRANSPORT_PRIORITY policy to define the transmission priority order, in order to achieve the purpose of a specific agent.

<img src="https://i.imgur.com/9vIa7JH.png" width="600"/>

*Class diagram of integration*


## Sequence Diagram
According to the sequence diagram depicted in below, the DDS and MQTT serve to transmit messages for the agents. Action 1 entails generating an independent process immediately after the root agent is initialized. Action 2 entails subscribing to or publishing relevant topics within the QoS constraints. Action 3 entails recursively calling all the subagents to initiate the action. The agent main action is performed in a separate process of Action 2 until it is notified of its termination. Finally, Action 4 entails generating a global broadcast with MQTT, with a system termination notification serving as an example in this study.

<img src="https://i.imgur.com/6lA3w1X.png" width="600"/>

*Sequence Diagram of Integration*
