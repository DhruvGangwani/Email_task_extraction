from flask import Flask, request
from nltk.tokenize import sent_tokenize
from check_email import get_emails
from preprocessing import preprocessing
from model_inference import bert_encode, create_model


app = Flask(__name__)

@app.route("/email_task_extract")
def compute():
	username = request.args.get("username")
	password = request.args.get("password")
	emails = get_emails(username, password)
	model_path = "checkpoint/my_checkpoint"
	email_result = list()

	for email in emails:
		email_body = email.get("body")
		body_sent = sent_tokenize(email_body)
		
		#preproceesing
		preprocessed_body_sent = [preprocessing(sentence) for sentence in body_sent]
		
		#bert encoding
		test_input_ids,test_attention_masks = bert_encode(preprocessed_body_sent, max_len=33)
		
		#model inference
		model = create_model(bert_model, max_len)
		model.load_weights(model_path)
		result = model.predict([test_input_ids,test_attention_masks])
		result = np.round(result).astype(int)

		for index, temp in enumaerate(result):
			if temp == 1:
				result = {"date": email.get("Date"), "from_email":email.get("From_email"), "subject": email.get("subject"), "task_text": body_sent[index]}
				email_result.append(result)
		return email_result



