import setuptools  # 导入setuptools打包工具

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="addcomments",
    version="1.1.0",
    author="jk",
    author_email="wan525589@qq.com",
    description="add database table column comments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j5255089/django_databse_column_comment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
