SELECT * FROM moma_works WHERE classification = 'Photograph';


SELECT height, width FROM moma_works
WHERE classification = 'Photograph' AND height > 0 AND width > 0;


SELECT
CEIL(width) + 2 AS frame_width,
CEIL(height) + 4 AS frame_height
FROM moma_works
WHERE classification = 'Photograph' AND width > 0 AND height > 0;



WITH frames AS (
    SELECT
    CEIL(width) + 2 AS frame_width,
    CEIL(height) + 4 AS frame_height
    FROM moma_works
    WHERE classification = 'Photograph' AND width > 0 AND height > 0
)
SELECT
frame_width,
frame_height,
frame_width * frame_height AS frame_area
FROM frames;