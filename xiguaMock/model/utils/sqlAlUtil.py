from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine


class sqlAlUtil:
    # 连接数据库，echo=True =>把所有的信息都打印出来
    connect = create_engine("mysql+pymysql://grampus:123456@10.7.2.15:3306/grampus_qa?charset=utf8", encoding='utf-8',
                            echo=False)
    # 生成ORM基类
    Base = declarative_base()
    # 创建表结构
    # Base.metadata.create_all(connect)
    # 创建与数据库的会话session class ,这里返回给session的是个class,不是实例
    session_class = sessionmaker(bind=connect)
    # 生成session实例
    session = session_class()
