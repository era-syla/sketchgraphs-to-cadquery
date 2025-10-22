import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, 0.317).lineTo(-0.0, 0.797).lineTo(0.42, 0.797).lineTo(0.42, 0.437).lineTo(0.84, 0.437).lineTo(0.84, 0.257).lineTo(0.9, 0.257).lineTo(0.9, 0.197).lineTo(1.2, 0.197).lineTo(1.2, -0.36757).lineTo(1.082, -0.35908).lineTo(1.082, -0.0015).lineTo(0.616, -0.0).lineTo(0.616, 0.317).lineTo(-0.0, 0.317).close()
solid=wp_sketch0.add(loop0).extrude(-0.028950522740794325)
