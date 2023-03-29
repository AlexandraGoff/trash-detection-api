import argparse

import tensorflow as tf

print('tf.__version__', tf.__version__)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# TODO: add input/output shapes


def print_inputs(pb_filepath):
    with tf.gfile.GFile(pb_filepath, "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())

        with tf.Graph().as_default() as graph:
            tf.import_graph_def(graph_def, name='')

        input_list = []
        for op in graph.get_operations(): # tensorflow.python.framework.ops.Operation
            if op.type == "Placeholder":
                input_list.append(op.name)

        print('Inputs:', input_list)


def print_outputs(pb_filepath):
    with open(pb_filepath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

        name_list = []
        input_list = []
        for node in graph_def.node: # tensorflow.core.framework.node_def_pb2.NodeDef
            name_list.append(node.name)
            input_list.extend(node.input)

        outputs = set(name_list) - set(input_list)
        print('Outputs:', list(outputs))


if __name__ == '__main__':
    print_inputs('ssd_mobilenet_v2_taco_2018_03_29.pb')
    print_outputs('ssd_mobilenet_v2_taco_2018_03_29.pb')