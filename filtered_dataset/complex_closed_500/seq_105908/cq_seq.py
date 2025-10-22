import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.77411, 0.0177).lineTo(0.57911, 0.0177).lineTo(0.57911, 0.2477).lineTo(0.77411, 0.2477).lineTo(0.77411, 0.0177).close()
solid=wp_sketch0.add(loop0).extrude(0.5104081792694954)
