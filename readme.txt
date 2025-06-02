


docker run -itd --name my-csv-viewer --hostname my-csv-viewer -p 8092:8092 --network weixin-network my-csv-viewer 

docker build -t my-csv-viewer .      



 
http://127.0.0.1:8092/csv-render?dataUrl=http://cisdi.net.cn:9000/agent-development/housing.csv

