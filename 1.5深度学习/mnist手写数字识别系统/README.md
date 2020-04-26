## mnist_flask

基于 TensorFlow2.0 （Keras） + Flask 的 Mnist 手写数字集识别系统

### 部署

- 安装依赖库文件

```shell
pip install -r requirements.txt	
```

### 运行

- 启动服务

```shell
python app.py
```

启动完成后，用浏览器访问：http://localhost:10170

- 本程序已包含训练好的模型 model.h5 , 如需自行训练，请运行：

```shell
python model/train.py
```

