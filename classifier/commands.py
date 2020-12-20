"""File for defining commands for the classifier."""

import argparse
import logging

import tbcnn.train as tbcnn_train
import tbcnn.test as tbcnn_test

if __name__ == "__main__":
    """Commands to train and test classifiers."""
    parser = argparse.ArgumentParser(
        description="Train and test classifiers on datasets.""",
    )
    parser.add_argument(
        'action',
        type=str,
        help='train or test action',
    )
    parser.add_argument('--infile', type=str, help='Data file to sample from')
    parser.add_argument(
        '--embedfile', type=str, help='Learned vector embeddings from the vectorizer'
    )
    parser.add_argument("--learn_rate", type=float, help="Learning rate")
    parser.add_argument("--batch_size", type=int, help="Batch size")
    parser.add_argument("--conv_feature", type=int, help="Convolution output feature")
    parser.add_argument("--epoch", type=int, help="Epoch")

    args = parser.parse_args()

    if args.action.lower() == "train":
        logdir="classifier/logs/%d_%d_%.3f_%d" % (args.conv_feature, args.batch_size, args.learn_rate, args.epoch)
        tbcnn_train.train_model(logdir, args.infile, args.embedfile)
    elif args.action.lower() == "test":
        logdir = "classifier/logs/%d_%d_%.3f_%d" % (args.conv_feature, args.batch_size, args.learn_rate, args.epoch)
        tbcnn_test.test_model(logdir, args.infile, args.embedfile, args.conv_feature)

    # if args.action.lower() == "train":
    #     logdir = "classifier/logs/%d_%d_%.3f_%d" % (args.conv_feature, args.batch_size, args.learn_rate, args.epoch)
    #     tbcnn_train.train_model(logdir, args.infile, args.embedfile, args.conv_feature, args.learn_rate,
    #                             args.batch_size, args.epoch)
    # elif args.action.lower() == "test":
    #     logdir = "classifier/logs/%d_%d_%.3f_%d" % (args.conv_feature, args.batch_size, args.learn_rate, args.epoch)
    #     tbcnn_test.test_model(logdir, args.infile, args.embedfile, args.conv_feature)

