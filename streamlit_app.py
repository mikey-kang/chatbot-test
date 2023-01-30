#!/usr/bin/env python
# coding: utf-8

import streamlit as st

def main():

	# Title
	st.title("수아 Version 1.0.0")
	st.subheader("")
	st.markdown("""
		AI 챗봇 수아의 1.0.0 Version입니다👩🏻‍⚕️
		"""
		"""
		수아와 대화를 하며, 위로와 공감을 받아보세요😊
	""")

	st.subheader("챗봇과 대화해보세요!")

	utterance = st.text_input("나: ", "오늘은 어떤 기분이신가요?")

	st.sidebar.subheader("Generation Settings")
	maxlen=st.sidebar.slider("max length of the sequence", 30, 60,value=50)
	numbeams=st.sidebar.slider("number of beams", 5,20, value=10)
	topk=st.sidebar.slider("top k sampling", 10, 50, value=20)
	ngramsize=st.sidebar.slider("Ngram size not to repeat", 1,4,value=2)
	temp=st.sidebar.slider("temperature: threshold probability of each token", 0.7, 0.95, value=0.85)
	sampling=st.sidebar.checkbox("do sampling", value=False)


	st.sidebar.subheader("(주)아몬디")
	st.sidebar.text("Copyright 2023. amondy Inc. All rights reserved.")

	if st.button("전송"):
# 		result = chat(utterance,maxlen,numbeams,sampling,topk,ngramsize,temp)
# 		st.text_area("챗봇: ", value=result)
		st.text_area("챗봇: ", value="성공")

	st.sidebar.subheader("개발자")
	st.sidebar.text("김은진, jyej3154@snu.ac.kr")
	st.sidebar.text("서울대학교 언어학과 석사과정")

	st.subheader("참조")
	st.markdown("kogpt2 기반 챗봇: https://github.com/haven-jeon/KoGPT2-chatbot")
	st.markdown("pytorch lightning: https://www.pytorchlightning.ai/")
	st.markdown("huggingface transformers: https://huggingface.co/")
	st.markdown("wellness dataset: https://aihub.or.kr/keti_data_board/language_intelligence")

if __name__ == '__main__':
	main()
