import utils

eval_corpus_path = "birth_dev.tsv"

predictions = ["London"] * sum(1 for _ in open(eval_corpus_path, encoding='utf-8'))
total, correct = utils.evaluate_places(eval_corpus_path, predictions)

if total > 0:
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
else:
    print('no targets provided')
