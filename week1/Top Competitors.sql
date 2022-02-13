select H.hacker_id, H.name
from Submissions as S
 inner join Challenges as C on S.challenge_id = C.challenge_id
 inner join Difficulty as D on C.difficulty_level = D.difficulty_level
 inner join Hackers as H on S.hacker_id = H.hacker_id
where S.score = D.score and C.difficulty_level = D.difficulty_level
group by H.hacker_id, H.name
having count (H.hacker_id) > 1
order by count(H.hacker_id) desc , H.hacker_id;
