aws s3 sync --no-sign-request s3://smithsonian-open-access/metadata/edan/ ./data/
# aws s3 ls --no-sign-request s3://smithsonian-open-access/
# rclone mount si-open:smithsonian-open-access/ ./mount
# aws s3api list-objects --bucket smithsonian-open-access --prefix "media/chsdm/" --output json --query "sum(Contents[?contains(Key,'.jpg')].Size)" --no-sign-request
# aws s3api list-objects --bucket smithsonian-open-access --prefix "media/chsdm/" --output json --no-sign-request > si-media.json
# jq .Contents[].Key si-media.json | grep ".jpg" | sed 's/^"media\/chsdm\///' | sed 's/"$//' > si-media.txt
