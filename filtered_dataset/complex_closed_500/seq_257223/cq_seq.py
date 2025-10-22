import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.009, -0.56652).lineTo(1.309, -0.56652).lineTo(1.309, 0.33348).lineTo(1.009, 0.33348).lineTo(1.009, -0.56652).close()
solid=wp_sketch0.add(loop0).extrude(-0.20735428746899373)
