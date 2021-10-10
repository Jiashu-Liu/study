# dot -Tpdf trace.dot -o trace.pdf

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from src.train.train import training

g = GraphvizOutput(output_file=r'./trace.dot',output_type='dot')
with PyCallGraph(output=g):
    training()