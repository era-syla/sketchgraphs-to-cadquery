import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.018, 0.007).lineTo(-0.018, 0.007).lineTo(-0.018, -0.007).lineTo(0.018, -0.007).lineTo(0.018, 0.007).close()
solid=wp_sketch0.add(loop0).extrude(0.05025845408241807)
