import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
from transformers import TFBertModel
bert_model = TFBertModel.from_pretrained('bert-base-uncased')


def bert_encode(data,maximum_length) :
  input_ids = []
  attention_masks = []
  
  
  for temp in data:
      encoded = tokenizer.encode_plus(
        
        temp,
        add_special_tokens=True,
        max_length=maximum_length,
        pad_to_max_length=True,
        
        return_attention_mask=True
        
      )
      # print(temp)
      input_ids.append(encoded['input_ids'])
      attention_masks.append(encoded['attention_mask'])
  return np.array(input_ids),np.array(attention_masks)





def create_model(bert_model, max_len):
  input_ids = tf.keras.Input(shape=(max_len,),dtype='int32')
  attention_masks = tf.keras.Input(shape=(max_len,),dtype='int32')
  
  output = bert_model([input_ids,attention_masks])
  output = output[1]
  # output = tf.keras.layers.Dense(16,activation='relu')(output)
  # output = tf.keras.layers.Dropout(0.2)(output)

  output = tf.keras.layers.Dense(1,activation='sigmoid')(output)
  model = tf.keras.models.Model(inputs = [input_ids,attention_masks],outputs = output)
  model.compile(Adam(lr=6e-6), loss='binary_crossentropy', metrics=['accuracy'])
  return model