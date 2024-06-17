# display_main_util.py

import streamlit as st

from configs.config_local import DEBUG

from utils.display_debug_util import display_debug
from utils.display_agent_util import display_agent_dropdown, display_agent_properties
from utils.display_project_util import display_project_dropdown, display_project_timestamps, display_project_properties
from utils.display_settings_util import display_settings
from utils.display_tool_util import (display_tool_dropdown, display_tool_properties)
from utils.display_workflow_util import display_workflow_dropdown, display_workflow_properties, display_workflow_timestamps


def display_main():
    if DEBUG:
        print("called display_main()")
    
    with open("styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    projectTab, workflowTab, agentTab, toolTab, settingsTab, debugTab = st.tabs(["Project", "Workflows", "Agents", "Tools", "Settings", "Debug"])

    with projectTab:
        project = st.session_state.current_project
        col1, col2 = st.columns(2)
        with col1:
            display_project_dropdown()
                
        with col2:
            if st.session_state.current_project is not None:
                display_project_timestamps(project)  

        display_project_properties(project)


    with workflowTab:
        workflow = st.session_state.current_workflow
        col1, col2 = st.columns(2)
        with col1:
            display_workflow_dropdown()
                        
        with col2:
            display_workflow_timestamps(workflow)

        display_workflow_properties(workflow)
        

    with agentTab:
        display_agent_dropdown()

        if st.session_state.current_agent is not None:
            display_agent_properties()

    with toolTab:
        display_tool_dropdown()
        display_tool_properties()
        
    with settingsTab:
        display_settings()

    with debugTab:
        display_debug()

def sidebar_begin():
    if DEBUG:
        print("sidebar_begin()")

    st.sidebar.write("<div class='title'>AutoGrok™ <br/> Universal AI Agents Made Easy. <br/> Eventually.</div><p/>", unsafe_allow_html=True)
    st.sidebar.write("(We're putting the 'mental' in 'experimental'.)")
    st.sidebar.write("No need to report what's broken, we know.")
    # display_project_dropdown()  
    # display_workflow_dropdown()
    