# model trainigs results on the CONLL_03


## Round 1.
- No rnn and no reproject_embeddings, 10 training runs
- 1-2: Baseline, all without Gazetteer Embeddings, model 1 with Glove, model 2 without Glove
- 3-5: all with Gazetteer Embeddings, all without Glove, model 03 with partial and full matching, model 04 with only full model 05 with only partial matching
- 6-8: all with Gazetteer Embeddings, all with Glove, model 06 with partial and full matching, model 05 with only full model 08 with only partial matching

## Round 2.
- With rnn and with reproject_embeddings, 3 training runs
- 1-2: Baseline, all without Gazetteer Embeddings, model 1 with Glove, model 2 without Glove
- 3-5: all with Gazetteer Embeddings, all without Glove, model 03 with partial and full matching, model 04 with only full model 05 with only partial matching
- 6-8: all with Gazetteer Embeddings, all with Glove, model 06 with partial and full matching, model 05 with only full model 08 with only partial matching

## Round 3.
- With rnn and with reproject_embeddings, with use_all_gazetteers, 3 training runs
- No Baseline models
- 3-5: all with Gazetteer Embeddings, all without Glove, model 03 with partial and full matching, model 04 with only full model 05 with only partial matching
- 6-8: all with Gazetteer Embeddings, all with Glove, model 06 with partial and full matching, model 05 with only full model 08 with only partial matching

## Round 4.
- Same as Round 3 but with extended gazetteer collection
