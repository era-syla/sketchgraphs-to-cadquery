import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.9906, 0.3429).lineTo(0.0, 0.3429).lineTo(0.0, 0.04445).lineTo(0.9906, 0.04445).lineTo(0.9906, 0.3429).close()
solid=wp_sketch0.add(loop0).extrude(-2.593448436072864)
