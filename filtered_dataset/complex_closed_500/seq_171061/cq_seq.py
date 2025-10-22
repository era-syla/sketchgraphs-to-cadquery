import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04699, 0.0362).lineTo(0.04699, 0.0362).lineTo(0.04699, -0.0362).lineTo(-0.04699, -0.0362).lineTo(-0.04699, 0.0362).close()
solid=wp_sketch0.add(loop0).extrude(0.002679972782660554)
