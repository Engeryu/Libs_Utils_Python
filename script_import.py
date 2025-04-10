# -*- coding: utf-8 -*-
# @Author: Engeryu
# @Date:   2024-10-13 23:24:18
# @Last Modified by:   Engeryu
# @Last Modified time: 2025-04-10 05:58:57
import os
os.environ['OMP_NUM_THREADS'] = '1'

# Bibliothèques générales
import pandas as pd, numpy as np, datetime as dt, time
from dimensions.table_Info import *
from dimensions.analyse_DF import *
from convert_Variables.convert import *
from convert_Variables.inplace import *
from filtering.df_Loop_Graph import *
from analysis.analysis_script import *
from models_Preparation.prepare_Df_Model import *
from models_Preparation.train_Evaluate_Model import *
from models_Preparation.evaluate_Model import *
from models_Results_comparisons.record_Results import *
from models_Results_comparisons.comparison_Models import *

from collections import Counter

from pandas.api.types import CategoricalDtype
from IPython.display import display
# Bibliothèques de visualisation
from plotly.subplots import make_subplots
import plotly.express as px, plotly.graph_objects as go, matplotlib.pyplot as plt
import networkx as nx
import plotly.figure_factory as ff
import plotly.io as pio
from dash import dash, dcc, html
from dash.dependencies import Input, Output
import seaborn as sns
# Bibliothèques mathématiques et statistiques
import statsmodels.api as sm, sympy as smp
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sympy import symbols, Eq, Sum, Function, MatrixSymbol, Derivative
from scipy import stats as st
from scipy.misc import derivative
from scipy.stats import pearsonr, spearmanr, chi2_contingency
# Bibliothèques Scikit-learn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as lR, Lasso as l1, Ridge as l2 ,SGDRegressor as sgdR
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsRegressor as knnR, KNeighborsClassifier as knnC
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor as rfR, GradientBoostingRegressor as gbR, RandomForestClassifier as rfC



















