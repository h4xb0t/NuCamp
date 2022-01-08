SELECT * FROM moma_artists LIMIT 50;


SELECT jsonb_pretty(info) AS formatted_info
FROM moma_artists LIMIT 50;


SELECT
info -> 'display_name' AS name,
info -> 'nationality' as nationality
FROM moma_artists
ORDER BY id
LIMIT 50;