import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0133, -0.01915).lineTo(-0.0133, -0.01915).lineTo(-0.0133, 0.01915).lineTo(0.0133, 0.01915).lineTo(0.0133, -0.01915).close()
solid=wp_sketch0.add(loop0).extrude(0.0703808248814824)
