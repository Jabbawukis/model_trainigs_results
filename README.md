# model trainigs results on the CONLL_03 data set
gazetteer-collection provided by: https://github.com/hltcoe/gazetteer-collection

GEMNET gazetteer provided by: https://code-mixed-ner.s3.amazonaws.com/readme.html

SHARED_MODEL_PARAMATERS (unless explicitly set otherwise):
- label_type=ner
- hidden_size=256
- use_crf=True
- learning_rate=0.1
- mini_batch_size=32
- max_epochs=150
- reproject_embeddings=True
- use_rnn=True

MODELS CONSTELLATIONS:
- 1-2: Baseline, all without Gazetteer Embeddings, model 01 with Glove, model 02 without Glove
- 3-5: all with Gazetteer Embeddings, all without Glove, model 03 with partial and full matching, model 04 with only full model 05 with only partial matching
- 6-8: all with Gazetteer Embeddings, all with Glove, model 06 with partial and full matching, model 07 with only full model 08 with only partial matching

## Round 1.
- No rnn and no reproject_embeddings!, 10 training runs, with gazetteer-collection

## Round 2.
- With rnn and with reproject_embeddings, 3 training runs, with gazetteer-collection

## Round 3.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 3 training runs, with gazetteer-collection
- No Baseline models

## Round 4. (3.5)
- Same as Round 3 but with extended gazetteer-collection (see directory readme)

## Round 8.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 3 training runs, only with GEMNET gazetteers
- No Baseline models

## Round 9.
- With rnn and with reproject_embeddings, without use_all_gazetteers (not necessary), 3 training runs, with count sensitive gazetteers provided by Susanna Rücker
- No Baseline models

## Round 10.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 3 training runs, with gazetteer-collection + GEMNET gazetteers + count sensitive gazetteers
- No Baseline models

## Round 12.
- With rnn and with reproject_embeddings, without use_all_gazetteers (not necessary), 3 training runs, with NON-count sensitive gazetteers provided by Susanna Rücker
- No Baseline models

## Round 13.
- With rnn and with reproject_embeddings, with use_all_gazetteers, with tokenize_gazetteer_entries, 3 training runs, with gazetteer-collection
- No Baseline models

## Round 15.
- With rnn and with reproject_embeddings, without use_all_gazetteers (not necessary), 3 training runs, with EXTENDED count sensitive gazetteers provided by Susanna Rücker
- No Baseline models

## Round 18.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 3 training runs, with gazetteer-collection + GEMNET gazetteers + EXTENDED count sensitive gazetteers
- No Baseline models

# model trainigs results on the WNUT_17 data set

## Round 5.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 6 training runs, with gazetteer-collection

## Round 11.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 6 training runs, with gazetteer-collection + GEMNET gazetteers + count sensitive 
- No Baseline models

## Round 14.
- With rnn and with reproject_embeddings, with use_all_gazetteers, with tokenize_gazetteer_entries, 6 training runs, with gazetteer-collection
- No Baseline models

## Round 16.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 6 training runs, with GEMNET gazetteers
- No Baseline models

## Round 17.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 6 training runs, with EXTENDED count sensitive gazetteers provided by Susanna Rücker
- No Baseline models

## Round 19.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 6 training runs, with gazetteer-collection + GEMNET gazetteers + EXTENDED count sensitive gazetteers
- No Baseline models

## Bonus Round
- Same as WNUT_17 round 05
- model 05 and model 06 from previous round with a manually added entities to the COMP gazetteers ("Mandalorian" and "The Mandalorian")

# model trainigs results on the NER_ENGLISH_STACKOVERFLOW data set

## Round 6.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 5 training runs, only with code_gazetteers

## Round 7.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 5 training runs, with gazetteer-collection + code_gazetteers
- No Baseline models
