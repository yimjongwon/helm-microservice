```bash
# chart를 압축해서 docs/ 폴더 안에 저장하기
helm package . -d docs/
# index.yaml 파일을 docs/ 폴더 안에 자동 생성하기
helm repo index docs --url https://yimjongwon.github.io/helm-microservice/

git add .
git commit -m "docs 폴더 구성함"
git push


```

###  page가 동작하도록 설정

### helm 저장소에 등록
```bash
# 현재 등록된 helm 저장소 목록 조회
helm repo ls
# helm chart의 위치를 helm 저장소로 등록하기
helm repo add msa https://yimjongwon.github.io/helm-microservice/
# 저장소에 있는 내용을 모두 받아올 수 있도록 동기화
helm repo update
# 저장소에 어떤 chart가 들어 있는지 검색
helm search repo msa

# install 해보기
helm install msa-release msa/msa-platform -n msa --create-namespace

helm ls -n msa
k get pod,svc -n msa

# 삭제
helm uninstall msa-release -n msa
k delete ns msa
```