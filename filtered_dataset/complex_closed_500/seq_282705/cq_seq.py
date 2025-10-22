import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.106, 0.0551).lineTo(-0.087, 0.0551).lineTo(-0.087, -0.0551).lineTo(-0.106, -0.0551).lineTo(-0.106, 0.0551).close()
solid=wp_sketch0.add(loop0).extrude(0.07815549605624329)
