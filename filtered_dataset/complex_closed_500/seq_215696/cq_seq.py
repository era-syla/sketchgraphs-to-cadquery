import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0065, 0.00027).lineTo(0.00681, 0.0).lineTo(0.0065, -0.00026).lineTo(0.00618, 0.0).lineTo(0.0065, 0.00027).close()
solid=wp_sketch0.add(loop0).extrude(0.001667298223542921)
