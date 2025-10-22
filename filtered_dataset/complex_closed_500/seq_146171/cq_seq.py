import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(2.28162, 0.0).lineTo(2.28162, -0.25).lineTo(-0.11838, -0.25).lineTo(-0.11838, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.17888456824173746)
