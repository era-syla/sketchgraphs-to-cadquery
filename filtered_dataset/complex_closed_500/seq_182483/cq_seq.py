import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01725, -0.0).lineTo(-0.02413, -0.0).lineTo(-0.02413, 0.01921).lineTo(-0.01725, 0.01921).lineTo(-0.01725, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.05748464654612858)
