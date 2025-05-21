


docker run -itd --name my-csv-viewer --hostname my-csv-viewer -p 8091:8091 --network weixin-network my-csv-viewer 

docker build -t my-csv-viewer .      


http://localhost:8091/echart-render?dataUrl=https://edu.stonybrook.uk/agent/echart-plot.json

 
http://127.0.0.1:8092/csv-render?dataUrl=http://cisdi.net.cn:9000/agent-development/housing.csv

