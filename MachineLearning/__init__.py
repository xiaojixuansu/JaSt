'''
    Init file for the package MachineLearning.
'''

import sys
import os

currentPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, currentPath+'/src') #To add a directory to import modules from
sys.path.insert(0, currentPath+'/src/Dico_MapTokens-Int')
sys.path.insert(0, currentPath+'/JsDetection')
sys.path.insert(0, currentPath+'/src/Dico_MapNGrams-Int')
sys.path.insert(0, currentPath+'/src/DicoProduction')

from StaticAnalysisJs import mainS
import ConfFileProduction
import TokensProduction
import NGramsProduction
import NGramsAnalysis
import NGramsRepresentation
import PreprocessingJsData
import FilesForJsClustering

import DicoIntToNGramsSlimit
import DicoNGramsToIntSlimit
import DicoIntToNGramsEsprima
import DicoNGramsToIntEsprima
import DicoIntToNGramsEsprimaAst
import DicoNGramsToIntEsprimaAst
import DicoIntToNGramsEsprimaAstSimplified
import DicoNGramsToIntEsprimaAstSimplified

import DicoOfTokensSlimit
import DicoOfTokensEsprima
import DicoOfAstEsprima
import DicoOfAstEsprimaSimplified

import JsDetection
