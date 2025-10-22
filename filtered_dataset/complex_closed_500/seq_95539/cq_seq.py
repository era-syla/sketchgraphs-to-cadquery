import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.003, 0.003).lineTo(-0.003, 0.003).lineTo(-0.003, -0.003).lineTo(0.003, -0.003).lineTo(0.003, 0.003).close()
solid=wp_sketch0.add(loop0).extrude(-0.01058459920322213)
