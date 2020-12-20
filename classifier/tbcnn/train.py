"""Train the cnn model as  described in Lili Mou et al. (2015) 
https://arxiv.org/pdf/1409.5718.pdf"""

import os
import sys
import pickle
import tensorflow as tf
import numpy as np
import network as network
import sampling as sampling
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def train_model(logdir, infile, embedfile, checkpoint_every=10000):
    conv_feature=100
    learn_rate=0.1
    batch_size=2
    epochs=50
#     """Train a classifier to label ASTs"""
#def train_model(logdir, conv_feature=100, learn_rate=0.1, batch_size=2, epochs=50, checkpoint_every=10000):
    #"""Train a classifier to label ASTs"""

    with open(embedfile, 'rb') as fh:
        embeddings, embed_lookup = pickle.load(fh)
        num_feats = len(embeddings[0])


    with open(infile, 'rb') as fh:
        trees, _, labels = pickle.load(fh)

    # build the inputs and outputs of the network
    nodes_node, children_node, hidden_node = network.init_net(
        num_feats,
        conv_feature,
        len(labels)
    )

    out_node = network.out_layer(hidden_node)
    labels_node, loss_node = network.loss_layer(hidden_node, len(labels))

    optimizer = tf.train.GradientDescentOptimizer(learn_rate)
    train_step = optimizer.minimize(loss_node)

    tf.summary.scalar('loss', loss_node)

    ### init the graph
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    sess.run(tf.global_variables_initializer())

    with tf.name_scope('saver'):
        saver = tf.train.Saver()
        summaries = tf.summary.merge_all()
        writer = tf.summary.FileWriter(logdir, sess.graph)

    checkfile = os.path.join(logdir, 'cnn_tree.ckpt')

    num_batches = len(trees) // batch_size + (1 if len(trees) % batch_size != 0 else 0)
    for epoch in range(1, epochs + 1):
        max_step = 0
        for i, batch in enumerate(sampling.batch_samples(
                sampling.gen_samples(trees, labels, embeddings, embed_lookup), batch_size
        )):
            nodes, children, batch_labels = batch
            step = ((epoch - 1) * num_batches + i)
            max_step = max(step, max_step)
            if not nodes:
                continue  # don't try to train on an empty batch

            _, summary, err, out = sess.run(
                [train_step, summaries, loss_node, out_node],
                feed_dict={
                    nodes_node: nodes,
                    children_node: children,
                    labels_node: batch_labels
                }
            )
            if i % 200 == 0:
                print('Epoch:', epoch,
                      'Step:', step,
                      'Loss:', err,
                      'Max nodes:', len(nodes[0])
                      )
                sys.stdout.flush()

            if step % checkpoint_every == 0:
                # save state so we can resume later 
                writer.add_summary(summary, step)
                saver.save(sess, os.path.join(checkfile), step)

    saver.save(sess, os.path.join(checkfile), step)

    # compute the training accuracy
    correct_labels = []
    predictions = []
    print('Computing training accuracy...')
    for batch in sampling.batch_samples(
            sampling.gen_samples(trees, labels, embeddings, embed_lookup), 1
    ):
        nodes, children, batch_labels = batch
        output = sess.run([out_node],
                          feed_dict={
                              nodes_node: nodes,
                              children_node: children,
                          }
                          )
        correct_labels.append(np.argmax(batch_labels))
        predictions.append(np.argmax(output))

    target_names = list(labels)
    print('Accuracy:', accuracy_score(correct_labels, predictions))
    print(classification_report(correct_labels, predictions, target_names=target_names))
    print(confusion_matrix(correct_labels, predictions))
