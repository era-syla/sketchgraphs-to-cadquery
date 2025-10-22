import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02201, 0.02466).lineTo(0.03305, 0.01714).lineTo(0.0, -0.06509).lineTo(-0.04801, -0.06897).lineTo(-0.02201, 0.02466).close()
solid=wp_sketch0.add(loop0).extrude(-0.008650394848740781)
