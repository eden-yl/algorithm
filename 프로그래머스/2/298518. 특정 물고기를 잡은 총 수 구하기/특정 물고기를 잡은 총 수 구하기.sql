-- 코드를 작성해주세요
SELECT  COUNT(I.ID) AS FISH_COUNT
FROM    FISH_INFO I INNER JOIN FISH_NAME_INFO N ON (I.FISH_TYPE=N.FISH_TYPE)
WHERE   N.FISH_NAME = 'BASS' OR N.FISH_NAME = 'SNAPPER'