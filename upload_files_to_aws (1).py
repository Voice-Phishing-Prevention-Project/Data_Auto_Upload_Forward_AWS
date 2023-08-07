# -*- coding: utf-8 -*-

!pip install boto3

import boto3

# AWS 자격 증명 설정
aws_access_key_id = '',
aws_secret_access_key = ''

# AWS 클라이언트 생성
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

import boto3

def upload_file_to_s3(local_file_path, bucket_name, s3_file_path, aws_access_key_id, aws_secret_access_key):
    """
    로컬 파일을 S3 버킷에 업로드하는 함수
    :param local_file_path: 업로드할 로컬 파일의 경로
    :param bucket_name: 업로드할 S3 버킷의 이름
    :param s3_file_path: S3 버킷 내에서 파일이 저장될 경로 및 이름
    :param aws_access_key_id: AWS 액세스 키 ID
    :param aws_secret_access_key: AWS 비밀 액세스 키
    """
    try:
        s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        s3_client.upload_file(local_file_path, bucket_name, s3_file_path)
        print(f"파일이 성공적으로 S3 버킷에 업로드되었습니다. 버킷: '{bucket_name}', 경로: '{s3_file_path}'")
    except Exception as e:
        print(f"파일 업로드에 실패했습니다. 오류 메시지: {str(e)}")

# 업로드할 로컬 파일의 경로
local_file_path = "/content/test.txt.txt"

# S3 버킷의 이름
bucket_name = "giveittome"

# S3 버킷 내에서 파일이 저장될 경로 및 이름
s3_file_path = "hello/test.txt"

# AWS 자격 증명 설정
aws_access_key_id = ''
aws_secret_access_key = ''
ㅁ
# 파일을 S3 버킷에 업로드
upload_file_to_s3(local_file_path, bucket_name, s3_file_path, aws_access_key_id, aws_secret_access_key)
