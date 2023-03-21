import tensorflow as tf
from tensorflow import keras


def load_graph(frozen_graph_filename):
    with tf.io.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())

    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def, name="prefix")
    return graph


if __name__ == '__main__':
    graph = load_graph('ssd_mobilenet_v2_taco_2018_03_29.pb')
    for op in graph.get_operations():
        abc = graph.get_tensor_by_name(op.name + ":0")
        print(abc)