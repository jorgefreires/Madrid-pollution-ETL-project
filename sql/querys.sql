-- Media de cantidad de partículas < 10 um a las 9 de la mañana por estación y año ordenado por año

SELECT e.estacion, m.magnitud, u.unidad, d.ano, AVG(`9`) AS media
FROM datos_anteriores AS d
LEFT JOIN estaciones as e
ON d.estacion = e.estaciones_id
LEFT JOIN magnitudes as m
ON d.magnitud = m.magnitudes_id
LEFT JOIN unidades_medida as u
ON d.unidad_medida = u.unidades_id
WHERE m.magnitud = 'particulas < 10 um'
GROUP BY e.estacion, m.magnitud, u.unidad, ano
ORDER BY ano 

-- Se piden los valores que se acaban de añadir mediante el scrapping de los datos en tiempo real

SELECT e.estacion, m.magnitud, u.unidad, ano, mes, dia, hora, valor
FROM datos_nuevos AS d
LEFT JOIN estaciones as e
ON d.estacion = e.estaciones_id
LEFT JOIN magnitudes as m
ON d.magnitud = m.magnitudes_id
LEFT JOIN unidades_medida as u
ON d.unidad_medida = u.unidades_id