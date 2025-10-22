import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00822, 0.00032).lineTo(0.00684, 0.00032).lineTo(0.00684, -0.00032).lineTo(0.00822, -0.00032).lineTo(0.00822, 0.00032).close()
solid=wp_sketch0.add(loop0).extrude(0.0005902635156780743)
