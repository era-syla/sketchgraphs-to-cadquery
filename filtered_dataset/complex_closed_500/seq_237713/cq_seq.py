import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0381, 0.00412).lineTo(0.0381, 0.00493).lineTo(0.03849, 0.0056).lineTo(0.03865, 0.0056).lineTo(0.03905, 0.00493).lineTo(0.03905, 0.00412).lineTo(0.0381, 0.00412).close()
solid=wp_sketch0.add(loop0).extrude(-0.0008387093985496521)
