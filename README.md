# FairyTale-Generator
This is a repo for the project of Advanced Project in Natural Language processing. This project contains a generator for creating fairy tales based on a fixed story structure, for example: 

_Long long ago, in a land far far away, there was a sleazy mistress called Charlie. The mistress really wanted to find the love of their life. Somewhere near, there was a bachelor that was inarticulate. The mistress felt truly sorry for the bachelor. The bachelor flashed its bedroom eyes at the mistress. They took the bachelor to its bed. The bachelor seemed a magnificent figure to them. The mistress became utterly besotted with them. Will the mistress and the bachelor be star-crossed lovers or will love prevail?_


## Content
This repo contains the following
* _Data_:
  * _Fairytales\_db > merged_clean.txt_: Fairy tales from the 19th - 20th century, concatenated into one text file as obtained from https://www.kaggle.com/cuddlefish/fairy-tales
  * _Veale\_db > *_: Datasheets containing story elements and templates as obtained from the Scealextric knowledge base.
  * _Own\_db > *_: Preprocessed and self-created datasets
* _src_:
  * _story\_maker.py_: To generate a story
  * _characters.py_: To extract commonly used fairy tale characters
  * _common\_actions.py_: To extract a list of the most common actions
  * _story_counter.py_: To count how many stories were included in the fairy tale dataset
  * _utils.py_: To extract a reduced list of Veale's script midpoints that end in actions for which a need was defined in our need dataset

## Install
To use the scripts, the following packages need to be installed:
* openpyxl
* pandas

## Use
To generate a story, run the _story\_maker.py_ file. A story will be generated based on a certain seed, which is printed before the story is printed. When the source code is not changed, this seed will always result in the same story being generated. 

## References
This project uses datasets from https://www.kaggle.com/cuddlefish/fairy-tales and https://github.com/prosecconetwork/Scealextric. For the Scealextric approach, we refer to the paper of Tony Veale:

Veale, T. (2016). A Rap on the Knuckles and a Twist in the Tale: From Tweeting Affective Metaphors to Generating Stories with a Moral. In Proceedings of the AAAI Spring Symposium on Ethical and Moral Considerations in Non-Human Agents.
