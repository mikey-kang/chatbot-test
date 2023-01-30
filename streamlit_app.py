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

	utterance = st.text_input("나: ")

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
# 		st.text_area("수: ", value=result)
		st.text_area("수아: ", value="성공")

if __name__ == '__main__':
	main()
