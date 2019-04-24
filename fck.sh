python src/main.py train \
    --use-bert \
    --model-path-base models/english_baseline \
    --bert-model "bert-base-multilingual-cased" --no-bert-do-lower-case \
    --learning-rate 0.00005 --num-layers 2 --batch-size 32 --eval-batch-size 16 --subbatch-max-tokens 500 \
    --predict-tags --train-path data/train.txt --dev-path data/22.auto.clean \
    --evalb-dir EVALB \
    --use-syntactic \
    --embed-layer 8 \
    --word-level "last"