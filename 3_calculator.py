"""Simple Streamlit bootstrap for the multi-page Calculator app.

This module wires together the multi-page app helper and the
calculator page implementation. It keeps the top-level app
definition minimal so `streamlit run 3_calculator.py` starts the
application.
"""

import streamlit as st
from app_pages.multi_page import MultiPage

# Import the function that renders the calculator page body. The
# function should accept no arguments and render Streamlit components
# when called by the MultiPage framework.
from app_pages.page_calculator import calculator_body


# Create the MultiPage application instance. The app_name is used by
# the MultiPage helper to display a title/header in the UI.
app = MultiPage(app_name='Calculator App')


# Register pages with the MultiPage app. The first argument is the
# label that will appear in the sidebar/navigation; the second is the
# callable that renders the page. You can call `add_page` multiple
# times to register more pages.
app.add_page('Calculator', calculator_body)


# Start the Streamlit app. This will run the registered page's
# rendering function when the page is selected in the UI.
app.run()