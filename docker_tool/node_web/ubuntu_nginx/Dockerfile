FROM ubuntu:latest
# -y는 모두 수락 모두 예스 
RUN apt-get update && apt-get install -y -q nginx
# 같은 폴더 이니까 index.html그냥 쓰면 됨 
COPY index.html /usr/share/nginx/html/

CMD ["nginx", "-g", "daemon off;"]

#ENTRYPOINT ["node", "app.js"]