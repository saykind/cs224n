##! /bin/bash

# Pretrain the model
python src/run.py pretrain bilinear wiki.txt --writing_params_path bilinear.pretrain.params
        
# Finetune the model
python src/run.py finetune bilinear wiki.txt --reading_params_path bilinear.pretrain.params --writing_params_path bilinear.finetune.params --finetune_corpus_path birth_places_train.tsv
        
# Evaluate on the dev set; write to disk
python src/run.py evaluate bilinear wiki.txt --reading_params_path bilinear.finetune.params --eval_corpus_path birth_dev.tsv --outputs_path bilinear.pretrain.dev.predictions
        
# Evaluate on the test set; write to disk
python src/run.py evaluate bilinear wiki.txt  --reading_params_path bilinear.finetune.params --eval_corpus_path birth_test_inputs.tsv --outputs_path bilinear.pretrain.test.predictions
