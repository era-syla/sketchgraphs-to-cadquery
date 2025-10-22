import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.06, -0.36726).lineTo(0.18208, -0.36726).lineTo(0.18208, 0.0).lineTo(0.06, 0.0).lineTo(0.06, -0.25).lineTo(0.06, -0.36726).close()
solid=wp_sketch0.add(loop0).extrude(-0.6223339163483441)
