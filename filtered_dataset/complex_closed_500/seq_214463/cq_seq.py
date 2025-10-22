import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0105, 0.015).lineTo(-0.0105, -0.005).lineTo(0.0105, -0.005).lineTo(0.0105, 0.0).lineTo(0.01494, -0.00119).lineTo(0.0105, 0.015).lineTo(0.0083, 0.015).lineTo(0.0083, -0.0038).lineTo(-0.0083, -0.0038).lineTo(-0.0083, 0.015).lineTo(-0.0105, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(-0.01162506327331676)
