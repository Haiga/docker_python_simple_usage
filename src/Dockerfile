FROM python:3
ADD my_script.py /
#ADD / /  possível copia tudo
RUN pip install numpy
RUN pip install matplotlib
RUN pip install sklearn

#RUN python my_script.py #É possível rodar assim também (mas o comando será executado na construção da imagem)

# Com o cmd o comando é executado no container
CMD ["python","-u", "./my_script.py"] #-u é para mostrar a saída do código python

