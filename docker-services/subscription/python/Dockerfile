# FROM scratch
# ADD docker-services/shared/centos-8-x86_64.tar.xz /
#
# LABEL org.label-schema.schema-version="1.0" \
#     org.label-schema.name="CentOS Base Image" \
#     org.label-schema.vendor="CentOS" \
#     org.label-schema.license="GPLv2" \
#     org.label-schema.build-date="20200611"
#
# RUN yum -y update && \
# yum -y groupinstall "Development Tools" && \
# yum -y install openssl-devel bzip2-devel libffi-devel &&\
# yum -y install wget &&\
# yum -y install python3-devel mysql-devel &&\
# wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
#
# RUN tar xvf Python-3.8.3.tgz && rm -rf Python-3.8.3.tgz
#
# RUN cd Python-3.8*/ && \
# ./configure --enable-optimizations &&\
#  make altinstall
#
# COPY  requirements.txt /root/
# RUN pip3.8 install mysqlclient && pip3.8 install -r /root/requirements.txt && useradd centos
#
# ENV HOME=/home/centos
# USER centos
# COPY ./ /home/centos/
# WORKDIR /home/centos/
# #EXPOSE 8081
#
# #CMD ["python3.8", "app.py"]

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY . .


RUN python -m pip install --user --upgrade setuptools wheel
WORKDIR /usr/src/app/knocqueue/links
RUN python setup.py sdist bdist_wheel

WORKDIR /usr/src/app
RUN python -m pip install --no-cache-dir -v --find-links knocqueue/links/dist  -r requirements.txt
CMD [ "python", "./your-daemon-or-script.py" ]