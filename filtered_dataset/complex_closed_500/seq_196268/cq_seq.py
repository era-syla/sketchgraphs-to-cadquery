import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.69567, 0.90894).lineTo(-0.64567, 0.90894).lineTo(-0.64567, 0.00894).lineTo(-0.69567, 0.00894).lineTo(-0.69567, 0.90894).close()
solid=wp_sketch0.add(loop0).extrude(-0.7102861989662609)
