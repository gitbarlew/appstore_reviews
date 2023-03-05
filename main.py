import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello Liberty!",
        page_icon="👋",
    )

    st.write("# Welcome to Liberty Global App Analysis tool 👋")

    st.sidebar.success("Select an app version.")

    st.markdown(
        """
        Markdown
    """
    )


if __name__ == "__main__":
    run()
