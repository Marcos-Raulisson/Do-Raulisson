import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


# ========= Layout ========= #
layout = dbc.Col([
    html.H1("Financeiro", className="text-primary"),
    html.P("Por Marcos Raulisson", className="text-info"),
    html.Hr(),

    # Seção PERFIL ----------------------
    dbc.Button(id='botao_avatar')
])


# =========  Callbacks  =========== #
# Pop-up receita
